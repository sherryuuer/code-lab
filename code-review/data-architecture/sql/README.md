# SQL Code Review Practice

DWH、Data Mart、Dashboard、Analytical Reporting で使われる SQL を Review する練習領域です。

## 主な Review 観点

Default framework:

```text
Data Quality
Security
Scalability
Reliability
Maintainability
Cost
```

- Source Table と Final Output の Grain が合っているか。
- JOIN によって Row Duplication が起きていないか。
- Filter が不足、または誤っていないか。
- Aggregation Level が正しいか。
- `COUNT(*)` と `COUNT(DISTINCT ...)` の使い分けが適切か。
- Metric Calculation における NULL Handling が正しいか。
- Timezone や Date Boundary の Bug がないか。
- Late Arriving Data を考慮しているか。
- Slowly Changing Dimension を考慮しているか。
- Partition Filter 不足により Full Table Scan になっていないか。
- 不要な `SELECT *` がないか。
- Window Function の使い方が正しいか。
- KPI 定義と SQL ロジックが一致しているか。
- Upstream System との Count / Sum Reconciliation があるか。

## 練習問題の例

- JOIN Duplication がある Revenue Aggregation SQL。
- Timezone Issue を含む Daily Active Users 集計。
- Late Update を含む Inventory Snapshot。
- PII 露出リスクがある Customer 360 Mart。
- Partition Pruning が効かない Dashboard Query。
- KPI Definition Change を伴う SQL Migration。

## Review 出力テンプレート

```md
## Read

-

## Evaluate

- Data Quality:
- Security:
- Scalability:
- Reliability:
- Maintainability:
- Cost:

## Open Questions

-

## Better Approach

-
```
