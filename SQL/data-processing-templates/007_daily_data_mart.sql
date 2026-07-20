/*
Template 007: Daily Data Mart

Use case:
  Create or replace a dashboard-friendly daily summary table.

Key ideas:
  - pre-aggregate for BI
  - reduce dashboard query cost
  - centralize metric logic
*/

DECLARE target_date DATE DEFAULT DATE('2026-07-20');

CREATE OR REPLACE TABLE `project.dataset_mart.daily_revenue_by_region`
PARTITION BY transaction_date
CLUSTER BY region AS
SELECT
  transaction_date,
  COALESCE(region, 'UNKNOWN') AS region,
  COUNT(DISTINCT transaction_id) AS transaction_count,
  SUM(amount) AS total_revenue,
  SAFE_DIVIDE(SUM(amount), COUNT(DISTINCT transaction_id)) AS average_order_value
FROM `project.dataset.cleaned_transactions`
WHERE transaction_date = target_date
  AND status = 'SUCCESS'
GROUP BY
  transaction_date,
  region;

