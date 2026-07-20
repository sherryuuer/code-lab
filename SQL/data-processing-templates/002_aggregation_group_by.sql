/*
Template 002: Aggregation with GROUP BY

Use case:
  Calculate daily transaction metrics by region.

Key ideas:
  - define the grain clearly
  - aggregate after filtering valid records
  - use SAFE_DIVIDE for ratio metrics
*/

DECLARE target_date DATE DEFAULT DATE('2026-07-20');

WITH valid_transactions AS (
  SELECT
    transaction_id,
    customer_id,
    transaction_date,
    region,
    amount
  FROM `project.dataset.cleaned_transactions`
  WHERE transaction_date = target_date
    AND status = 'SUCCESS'
    AND amount IS NOT NULL
    AND amount >= 0
)

SELECT
  transaction_date,
  COALESCE(region, 'UNKNOWN') AS region,
  COUNT(DISTINCT transaction_id) AS transaction_count,
  SUM(amount) AS total_amount,
  SAFE_DIVIDE(SUM(amount), COUNT(DISTINCT transaction_id)) AS average_amount
FROM valid_transactions
GROUP BY
  transaction_date,
  region
ORDER BY
  transaction_date,
  region;

