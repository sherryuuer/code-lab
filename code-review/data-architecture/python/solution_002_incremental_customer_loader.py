"""
Solution Example: Incremental Customer Loader

This example focuses on safer incremental loading for a customer dimension.
It demonstrates credential handling, watermark management, schema validation,
PII-safe logging, staging load, and idempotent upsert.
"""

import os
from typing import Final

import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine


WAREHOUSE_URL: Final[str] = os.environ["WAREHOUSE_URL"]
INPUT_PATH: Final[str] = os.environ["CUSTOMER_EXPORT_PATH"]
JOB_NAME: Final[str] = "incremental_customer_loader"
REQUIRED_COLUMNS: Final[set[str]] = {
    "customer_id",
    "email",
    "first_name",
    "last_name",
    "phone",
    "country",
    "status",
    "updated_at",
}


class CustomerLoadError(Exception):
    pass


def get_engine() -> Engine:
    return create_engine(WAREHOUSE_URL)


def read_watermark(engine: Engine) -> pd.Timestamp:
    query = text(
        """
        select watermark_value
        from etl_control.watermarks
        where job_name = :job_name
        """
    )
    with engine.begin() as conn:
        value = conn.execute(query, {"job_name": JOB_NAME}).scalar_one_or_none()

    if value is None:
        return pd.Timestamp("2020-01-01 00:00:00", tz="UTC")

    return pd.to_datetime(value, utc=True)


def update_watermark(engine: Engine, watermark: pd.Timestamp) -> None:
    query = text(
        """
        insert into etl_control.watermarks (job_name, watermark_value, updated_at)
        values (:job_name, :watermark_value, now())
        on conflict (job_name)
        do update set
            watermark_value = excluded.watermark_value,
            updated_at = now()
        """
    )
    with engine.begin() as conn:
        conn.execute(
            query,
            {
                "job_name": JOB_NAME,
                "watermark_value": watermark.isoformat(),
            },
        )


def validate_schema(df: pd.DataFrame) -> None:
    missing_columns = REQUIRED_COLUMNS - set(df.columns)
    if missing_columns:
        raise CustomerLoadError(f"Missing required columns: {sorted(missing_columns)}")


def validate_data(df: pd.DataFrame) -> None:
    if df["customer_id"].isna().any():
        raise CustomerLoadError("customer_id contains null values")

    if df["updated_at"].isna().any():
        raise CustomerLoadError("updated_at contains invalid or null values")

    duplicated_ids = df["customer_id"].duplicated().sum()
    if duplicated_ids:
        raise CustomerLoadError(f"customer_id contains duplicates: {duplicated_ids}")


def read_customer_export(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    validate_schema(df)

    df["updated_at"] = pd.to_datetime(df["updated_at"], utc=True, errors="coerce")
    validate_data(df)

    return df


def transform_customers(df: pd.DataFrame, watermark: pd.Timestamp) -> pd.DataFrame:
    new_df = df[df["updated_at"] > watermark].copy()

    if new_df.empty:
        return new_df

    new_df["email"] = new_df["email"].str.lower().str.strip()
    new_df["full_name"] = (
        new_df["first_name"].fillna("").str.strip()
        + " "
        + new_df["last_name"].fillna("").str.strip()
    ).str.strip()
    new_df["is_active"] = new_df["status"].str.lower().ne("deleted")

    return new_df[
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


def load_staging_table(engine: Engine, df: pd.DataFrame) -> None:
    with engine.begin() as conn:
        conn.execute(text("truncate table staging.customer_updates"))

    df.to_sql(
        "customer_updates",
        engine,
        schema="staging",
        if_exists="append",
        index=False,
        method="multi",
        chunksize=1000,
    )


def merge_customer_dimension(engine: Engine) -> None:
    query = text(
        """
        insert into analytics.dim_customer (
            customer_id,
            email,
            full_name,
            phone,
            country,
            is_active,
            updated_at
        )
        select
            customer_id,
            email,
            full_name,
            phone,
            country,
            is_active,
            updated_at
        from staging.customer_updates
        on conflict (customer_id)
        do update set
            email = excluded.email,
            full_name = excluded.full_name,
            phone = excluded.phone,
            country = excluded.country,
            is_active = excluded.is_active,
            updated_at = excluded.updated_at
        where analytics.dim_customer.updated_at <= excluded.updated_at
        """
    )
    with engine.begin() as conn:
        conn.execute(query)


def load_customers() -> None:
    engine = get_engine()
    watermark = read_watermark(engine)

    source_df = read_customer_export(INPUT_PATH)
    customer_updates = transform_customers(source_df, watermark)

    if customer_updates.empty:
        print("No customer updates found")
        return

    print(f"Customer updates to load: {len(customer_updates)}")

    load_staging_table(engine, customer_updates)
    merge_customer_dimension(engine)

    new_watermark = customer_updates["updated_at"].max()
    update_watermark(engine, new_watermark)
    print(f"Customer load completed. New watermark: {new_watermark.isoformat()}")


if __name__ == "__main__":
    load_customers()
