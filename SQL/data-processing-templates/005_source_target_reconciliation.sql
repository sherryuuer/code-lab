/*
Template 005: Source vs Target Reconciliation

Use case:
  Validate migration result between source and target datasets.

Key ideas:
  - compare counts
  - find missing / extra IDs
  - detect amount mismatches
*/

WITH source_records AS (
  SELECT
    record_id,
    amount
  FROM `project.dataset.source_table`
  WHERE record_id IS NOT NULL
    AND amount IS NOT NULL
),

target_records AS (
  SELECT
    record_id,
    amount
  FROM `project.dataset.target_table`
  WHERE record_id IS NOT NULL
    AND amount IS NOT NULL
),

reconciliation AS (
  SELECT
    COALESCE(s.record_id, t.record_id) AS record_id,
    s.amount AS source_amount,
    t.amount AS target_amount,
    CASE
      WHEN s.record_id IS NULL THEN 'EXTRA_IN_TARGET'
      WHEN t.record_id IS NULL THEN 'MISSING_IN_TARGET'
      WHEN s.amount != t.amount THEN 'AMOUNT_MISMATCH'
      ELSE 'MATCHED'
    END AS reconciliation_status
  FROM source_records s
  FULL OUTER JOIN target_records t
    ON s.record_id = t.record_id
)

SELECT
  reconciliation_status,
  COUNT(*) AS record_count
FROM reconciliation
GROUP BY
  reconciliation_status
ORDER BY
  reconciliation_status;

