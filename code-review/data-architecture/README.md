# Data Architecture Code Review Lab

この領域は、Data Architecture の観点で Code Review を練習するための場所です。

目的は、コードをゼロから書くことではありません。SQL や Python の Data Processing Code を読み、Risk を見つけ、Improvement を明確に説明できるようにすることです。

## Review の流れ

1. Business Purpose と Expected Output を理解する。
2. Data Source、Grain、Key、Time Range を確認する。
3. Correctness を確認する：JOIN、Filter、Aggregation、NULL、Duplicate、Timezone。
4. Data Quality を確認する：Validation、Reconciliation、Late Arriving Data、Error Handling。
5. Performance を確認する：Scan Size、Partitioning、Clustering、Pushdown、Batching、Memory Usage。
6. Reliability を確認する：Retry、Idempotency、Backfill、Observability、Alert。
7. Security と Governance を確認する：PII、Access Control、Masking、Logging、Lineage。
8. Findings を Severity 別に整理し、具体的な Fix を提示する。

## 練習フォーマット

各練習問題は、以下の形式で管理します。

- `prompt.md`: Scenario、Code、Review Task。
- `review-notes.md`: 自分の Findings。
- `answer.md`: Expected Findings と Better Implementation Ideas。

## Review 観点

- Correctness
- Data Quality
- Performance
- Reliability
- Security
- Maintainability
- Governance
- Cost

## サブフォルダ

- `sql/`: Analytics、DWH、Data Mart、Reporting Logic 向けの SQL Review 練習。
- `python/`: Ingestion、Transformation、API Integration、Pipeline Job 向けの Python Review 練習。
