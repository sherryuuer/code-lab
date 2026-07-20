/*
Template 010: Data Quality Checks

Use case:
  Run basic validation checks for a transaction table.

Key ideas:
  - null checks
  - duplicate checks
  - invalid value checks
  - row count summary
*/

DECLARE target_date DATE DEFAULT DATE('2026-07-20');

WITH base AS (
  SELECT
    transaction_id,
    customer_id,
    amount,
    currency,
    status,
    transaction_date
  FROM `project.dataset.transactions`
  WHERE transaction_date = target_date
),

checks AS (
  SELECT
    COUNT(*) AS total_rows,
    COUNTIF(transaction_id IS NULL) AS null_transaction_id_count,
    COUNTIF(customer_id IS NULL) AS null_customer_id_count,
    COUNTIF(amount IS NULL) AS null_amount_count,
    COUNTIF(amount < 0) AS negative_amount_count,
    COUNTIF(currency NOT IN ('JPY', 'USD', 'EUR')) AS invalid_currency_count,
    COUNTIF(status NOT IN ('SUCCESS', 'FAILED', 'PENDING')) AS invalid_status_count,
    COUNT(DISTINCT transaction_id) AS distinct_transaction_id_count
  FROM base
)

SELECT
  *,
  total_rows - distinct_transaction_id_count AS duplicate_transaction_id_count
FROM checks;

