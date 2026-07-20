/*
Template 009: Partition and Clustering Friendly Query

Use case:
  Query a large BigQuery table efficiently.

Key ideas:
  - filter partition column directly
  - avoid functions on partition column
  - select only needed columns
  - use clustered columns in filters or joins when possible
*/

DECLARE start_date DATE DEFAULT DATE('2026-07-01');
DECLARE end_date DATE DEFAULT DATE('2026-07-20');

SELECT
  transaction_id,
  customer_id,
  transaction_date,
  amount,
  status
FROM `project.dataset.transactions`
WHERE transaction_date >= start_date
  AND transaction_date <= end_date
  AND customer_id = 'c123'
  AND status = 'SUCCESS';

/*
Avoid:

WHERE DATE(transaction_time) = CURRENT_DATE()
SELECT *

Prefer:

WHERE transaction_date = @target_date
SELECT only needed columns
*/

