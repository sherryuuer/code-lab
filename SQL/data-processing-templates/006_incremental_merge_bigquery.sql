/*
Template 006: Incremental MERGE in BigQuery

Use case:
  Apply incremental customer updates to a target dimension table.

Key ideas:
  - use MERGE for upsert
  - match by business key
  - update only when source is newer
*/

MERGE `project.dataset.dim_customer` AS target
USING (
  SELECT
    customer_id,
    customer_name,
    region,
    status,
    updated_at
  FROM `project.dataset.stg_customer_updates`
  WHERE customer_id IS NOT NULL
    AND updated_at IS NOT NULL
) AS source
ON target.customer_id = source.customer_id
WHEN MATCHED AND source.updated_at > target.updated_at THEN
  UPDATE SET
    customer_name = source.customer_name,
    region = source.region,
    status = source.status,
    updated_at = source.updated_at
WHEN NOT MATCHED THEN
  INSERT (
    customer_id,
    customer_name,
    region,
    status,
    updated_at
  )
  VALUES (
    source.customer_id,
    source.customer_name,
    source.region,
    source.status,
    source.updated_at
  );

