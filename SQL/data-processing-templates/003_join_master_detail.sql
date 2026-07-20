/*
Template 003: Join Master and Detail Tables

Use case:
  Enrich transactions with customer attributes.

Key ideas:
  - deduplicate master table before join
  - avoid join duplication
  - preserve transaction grain
*/

WITH customer_master AS (
  SELECT
    customer_id,
    ANY_VALUE(customer_name) AS customer_name,
    ANY_VALUE(region) AS region
  FROM `project.dataset.customers`
  WHERE customer_id IS NOT NULL
  GROUP BY
    customer_id
),

transactions AS (
  SELECT
    transaction_id,
    customer_id,
    transaction_date,
    amount,
    status
  FROM `project.dataset.transactions`
  WHERE transaction_date = DATE('2026-07-20')
)

SELECT
  t.transaction_id,
  t.customer_id,
  c.customer_name,
  COALESCE(c.region, 'UNKNOWN') AS region,
  t.transaction_date,
  t.amount,
  t.status
FROM transactions t
LEFT JOIN customer_master c
  ON t.customer_id = c.customer_id;

