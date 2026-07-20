/*
Template 008: Window Functions

Use case:
  Calculate customer transaction rank and running total.

Key ideas:
  - ROW_NUMBER for latest / rank
  - SUM OVER for running total
  - partition by business entity
*/

SELECT
  customer_id,
  transaction_id,
  transaction_time,
  amount,
  ROW_NUMBER() OVER (
    PARTITION BY customer_id
    ORDER BY transaction_time DESC
  ) AS latest_transaction_rank,
  SUM(amount) OVER (
    PARTITION BY customer_id
    ORDER BY transaction_time
    ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
  ) AS running_total_amount
FROM `project.dataset.transactions`
WHERE transaction_date BETWEEN DATE('2026-07-01') AND DATE('2026-07-20')
  AND customer_id IS NOT NULL
  AND amount IS NOT NULL;

