/*
Template 001: Basic Filtering and Validation

Use case:
  Select valid transaction records from a raw table.

Key ideas:
  - avoid SELECT *
  - validate required fields
  - filter invalid business values
  - use explicit date range or partition filter
*/

DECLARE target_date DATE DEFAULT DATE('2026-07-20');

SELECT
  transaction_id,
  customer_id,
  transaction_date,
  amount,
  currency,
  status,
  updated_at
FROM `project.dataset.raw_transactions`
WHERE transaction_date = target_date
  AND transaction_id IS NOT NULL
  AND customer_id IS NOT NULL
  AND amount IS NOT NULL
  AND amount > 0
  AND currency IN ('JPY', 'USD', 'EUR')
  AND status IN ('SUCCESS', 'FAILED', 'PENDING');

