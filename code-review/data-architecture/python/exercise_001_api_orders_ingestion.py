"""
Exercise 001: API Orders Ingestion

Scenario:
    This job is scheduled every hour. It extracts order records from an external
    API and writes them to a raw orders table in the data warehouse.

Review task:
    Review this code from a Data Architecture / Data Pipeline perspective.
    Focus on correctness, data quality, reliability, security, maintainability,
    and cost.

Expected output:
    List findings by severity and explain the impact and suggested fix.
"""

import json
import requests
import pandas as pd
from sqlalchemy import create_engine


API_URL = "https://external.example.com/api/orders"
API_KEY = "prod_123456789_secret_key"
WAREHOUSE_URL = "postgresql://analytics:password@warehouse.example.com:5432/dwh"


def fetch_orders(start_date, end_date):
    all_orders = []
    page = 1

    while True:
        response = requests.get(
            API_URL,
            params={
                "start_date": start_date,
                "end_date": end_date,
                "page": page,
                "limit": 1000,
                "api_key": API_KEY,
            },
        )

        if response.status_code != 200:
            print("API error:", response.text)
            break

        data = response.json()
        orders = data["orders"]
        all_orders.extend(orders)

        if len(orders) == 0:
            break

        page += 1

    return all_orders


def transform_orders(orders):
    df = pd.DataFrame(orders)

    df["order_date"] = pd.to_datetime(df["order_date"]).dt.date
    df["total_amount"] = df["quantity"] * df["unit_price"]
    df["customer_email"] = df["customer_email"].str.lower()

    return df[
        [
            "order_id",
            "customer_id",
            "customer_email",
            "order_date",
            "sku",
            "quantity",
            "unit_price",
            "total_amount",
            "status",
            "updated_at",
        ]
    ]


def write_to_warehouse(df):
    engine = create_engine(WAREHOUSE_URL)
    df.to_sql("raw_external_orders", engine, if_exists="append", index=False)


def main():
    start_date = "2026-06-01"
    end_date = "2026-06-26"

    orders = fetch_orders(start_date, end_date)
    print("Fetched orders:", len(orders))
    print(json.dumps(orders[:5], indent=2))

    df = transform_orders(orders)
    write_to_warehouse(df)

    print("Done")


if __name__ == "__main__":
    main()


"""
Review Answer Example:

このコードは、主に Bug / Correctness、API / Reliability、Security、
Data / Data Quality の4つの観点でレビューできます。

1. Bug / Correctness

まず、`while True` を使った pagination にリスクがあります。現在は
`orders` が空になったら終了しますが、API が同じ page を返し続ける場合や、
pagination metadata が壊れている場合、想定外に長く実行される可能性があります。
`has_more`、`next_page`、または最大 page 数を使って終了条件を明確にすべきです。

また、`status_code != 200` の場合に `break` している点も問題です。途中で
API error が発生しても、取得済みの partial data を後続処理に渡してしまう
可能性があります。ここは exception を投げて job を failed にする方が安全です。

2. API / Reliability

`requests.get()` に timeout が設定されていません。そのため、外部 API が
応答しない場合に job が止まり続ける可能性があります。

また、retry / backoff がないため、429、500、503 などの一時的なエラーに弱いです。
External API では rate limit や一時障害が起こり得るため、retry policy、
backoff、max retry count を設計すべきです。

3. Security

`API_KEY` と `WAREHOUSE_URL` に credential が hard-code されています。
これは repository に secret が残るリスクがあります。Secret Manager や
environment variable から取得する形に変更すべきです。

また、`print(json.dumps(orders[:5]))` で raw order data を log に出しています。
`customer_email` などの PII が含まれる可能性があるため、log には件数や job id
など必要最小限の情報だけを出すべきです。

4. Data / Data Quality

`if_exists="append"` で warehouse に書き込んでいるため、同じ期間を再実行すると
duplicate record が発生する可能性があります。`order_id` や `updated_at` を
使った deduplication、staging table、merge / upsert を検討すべきです。

また、`start_date` と `end_date` が hard-code されているため、毎時実行の job
としては不自然です。Watermark や execution window を使って、前回実行以降の
データを incremental load する設計にした方が良いです。

さらに、API response に対する schema validation や required column check が
ありません。`data["orders"]` や `df["customer_email"]` を前提にしているため、
schema drift が起きると job が壊れます。必須項目、型、NULL、重複、件数などの
Data Quality Check を追加すべきです。
"""
