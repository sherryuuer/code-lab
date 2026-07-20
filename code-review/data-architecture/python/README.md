# Python Data Pipeline Code Review Practice

Data Ingestion、Transformation、API Integration、Validation、Scheduled Job で使われる Python Code を Review する練習領域です。

## 主な Review 観点

Review flow:

```text
1. Read: summarize the code.
2. Explain: explain why it may be implemented this way.
3. Evaluate: check data quality, security, scalability, reliability, maintainability, and cost.
4. Improve: propose code-level, architecture-level, and production-ready improvements.
```

- Error Handling が不足していないか。
- Write Process が Idempotent になっているか。
- Unsafe Overwrite / Append がないか。
- API Call に Retry / Backoff があるか。
- External Request に Timeout が設定されているか。
- Rate Limit への対応があるか。
- Large File を一括読み込みして Memory Issue を起こさないか。
- Timezone や Date Parsing の Bug がないか。
- Secret や Credential がハードコードされていないか。
- Logging と Observability が十分か。
- Data Quality Validation があるか。
- Schema Validation があるか。
- Reconciliation Check があるか。
- Extraction、Transformation、Loading の Responsibility が分離されているか。
- Edge Case に対するテストがあるか。

## 練習問題の例

- Pagination と Rate Limit に問題がある API Ingestion Job。
- Schema Drift に弱い CSV to Warehouse Loader。
- 重複と NULL 処理に問題がある Pandas Transformation。
- Watermark Logic が壊れている Incremental Load。
- Idempotent ではない Backfill Script。
- Incomplete Validation の Data Quality Checker。

## Review 出力テンプレート

```md
## Findings

- Severity:
- Location:
- Issue:
- Impact:
- Suggested Fix:

## Open Questions

- 

## Better Approach

- 
```
