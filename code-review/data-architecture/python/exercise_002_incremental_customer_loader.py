"""
Exercise 002: Incremental Customer Loader

Scenario:
    This job runs every night. It reads customer records from a CSV export
    stored in object storage and loads them into a customer dimension table.

Review task:
    Review this code from a Data Architecture / Data Pipeline perspective.
    Focus on Bug / Correctness, API / Reliability, Security, and
    Data / Data Quality.

Expected output:
    List findings by severity and explain the impact and suggested fix.
"""

import pandas as pd
from sqlalchemy import create_engine


WAREHOUSE_URL = "postgresql://analytics:password@warehouse.example.com:5432/dwh"
INPUT_PATH = "s3://company-data-exports/customers/latest/customers.csv"
WATERMARK_FILE = "/tmp/customer_watermark.txt"


def read_watermark():
    try:
        with open(WATERMARK_FILE, "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        return "2020-01-01 00:00:00"


def write_watermark(value):
    with open(WATERMARK_FILE, "w") as f:
        f.write(value)


def load_customers():
    watermark = read_watermark()
    print("Current watermark:", watermark)

    df = pd.read_csv(INPUT_PATH)
    df["updated_at"] = pd.to_datetime(df["updated_at"])

    new_df = df[df["updated_at"] > watermark]

    new_df["email"] = new_df["email"].str.lower()
    new_df["full_name"] = new_df["first_name"] + " " + new_df["last_name"]
    new_df["is_active"] = new_df["status"] != "deleted"

    print("Sample rows:")
    print(new_df.head(20).to_json(orient="records", indent=2))

    result_df = new_df[
        [
            "customer_id",
            "email",
            "full_name",
            "phone",
            "country",
            "is_active",
            "updated_at",
        ]
    ]

    engine = create_engine(WAREHOUSE_URL)
    result_df.to_sql("dim_customer", engine, if_exists="append", index=False)

    max_updated_at = str(new_df["updated_at"].max())
    write_watermark(max_updated_at)
    print("New watermark:", max_updated_at)


if __name__ == "__main__":
    load_customers()


"""
Review Answer Example:

このコードは、主に Security、Reliability、Data / Data Quality、
Idempotency の観点で問題があります。

1. Security

まず、`WAREHOUSE_URL` に username と password が hard-code されています。
Credential はコードに直接書かず、environment variable や Secret Manager から
取得するべきです。

また、customer data には `email`, `full_name`, `phone` などの PII が
含まれていますが、masking や access control を考慮していません。特に
`new_df.head(20)` をそのまま log に出力している点は危険です。Log 経由で
個人情報が漏洩する可能性があるため、件数や job id など必要最小限の情報だけを
出すべきです。

2. Reliability

`read_watermark()` が `/tmp/customer_watermark.txt` に依存している点が弱いです。
`/tmp` は永続化されない可能性があり、job 実行環境が変わると watermark が
失われます。Watermark は warehouse の metadata table や control table に
保存する方が安全です。

また、`write_watermark()` に try / except がなく、書き込み失敗時の扱いも
不明確です。Watermark の更新に失敗した場合、次回実行時に同じデータを再処理する
可能性があります。

3. Data / Data Quality

schema validation や required column check がありません。`updated_at`, `email`,
`customer_id` などの column が存在しない場合、job が途中で失敗します。また、
NULL、重複、型、日付 parse error に対する validation も必要です。

さらに、`df[df["updated_at"] > watermark]` では `watermark` が string のまま
使われているため、datetime として明示的に parse して比較する方が安全です。
`new_df` が空の場合、`new_df["updated_at"].max()` が `NaT` になり、watermark を
壊す可能性もあります。

4. Idempotency

`to_sql(..., if_exists="append")` のため、同じデータを再実行すると duplicate record
が発生する可能性があります。Customer dimension table では `customer_id` を key に
して staging table に一度ロードし、merge / upsert する設計にした方が idempotency を
保てます。
"""
