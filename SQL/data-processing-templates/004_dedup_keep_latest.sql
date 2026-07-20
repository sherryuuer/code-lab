/*
Template 004: Deduplicate and Keep Latest Record

Use case:
  Keep the latest customer status record by customer_id.

Key ideas:
  - use ROW_NUMBER
  - partition by business key
  - order by updated_at descending
*/

WITH ranked_records AS (
  SELECT
    customer_id,
    status,
    updated_at,
    ROW_NUMBER() OVER (
      PARTITION BY customer_id
      ORDER BY updated_at DESC
    ) AS row_num
  FROM `project.dataset.customer_status_history`
  WHERE customer_id IS NOT NULL
    AND updated_at IS NOT NULL
)

SELECT
  customer_id,
  status,
  updated_at
FROM ranked_records
WHERE row_num = 1;

