为 BigQuery 中执行的各个步骤的 SQL 代码：

### 1. 创建一个数据表 `zdh_dev__dwh__samples.outest1`，插入三行数据
```sql
CREATE TABLE `zdh_dev__dwh__samples.outest1` (
    id INT64,
    name STRING,
    salary FLOAT64
);

INSERT INTO `zdh_dev__dwh__samples.outest1` (id, name, salary)
VALUES
    (1, 'Alice', 50000),
    (2, 'Bob', 60000),
    (3, 'Charlie', 70000);
```

### 2. 再创建一个和第一个表一样的表，表名为 `outest2`
```sql
CREATE TABLE `zdh_dev__dwh__samples.outest2` (
    id INT64,
    name STRING,
    salary FLOAT64
);

INSERT INTO `zdh_dev__dwh__samples.outest2` (id, name, salary)
VALUES
    (1, 'Alice', 50000),
    (2, 'Bob', 60000),
    (3, 'Charlie', 70000);
```

### 3. 针对 `outest1` 创建一个 View，只包含 `id` 和 `name`
```sql
CREATE VIEW `zdh_dev__dwh__samples.outest1_view` AS
SELECT id, name
FROM `zdh_dev__dwh__samples.outest1`;
```

### 4. 针对 `outest2` 创建一个 Materialized View，也只包含 `id` 和 `name`
```sql
CREATE MATERIALIZED VIEW `zdh_dev__dwh__samples.outest2_mview` AS
SELECT id, name
FROM `zdh_dev__dwh__samples.outest2`;
```

### 5. 对 `outest1` 进行 `ADD COLUMN` 操作，增加一个 `sex` 列，随意插入数据
```sql
ALTER TABLE `zdh_dev__dwh__samples.outest1`
ADD COLUMN sex STRING;

UPDATE `zdh_dev__dwh__samples.outest1`
SET sex = 'F'
WHERE id = 1;

UPDATE `zdh_dev__dwh__samples.outest1`
SET sex = 'M'
WHERE id = 2;

UPDATE `zdh_dev__dwh__samples.outest1`
SET sex = 'M'
WHERE id = 3;
```

### 6. 检查 View 是否损坏，进行 `SELECT` 操作
```sql
SELECT id, name
FROM `zdh_dev__dwh__samples.outest1_view`;
```

### 7. 对 `outest1` 进行 `DROP COLUMN` 操作，删除 `salary`
```sql
ALTER TABLE `zdh_dev__dwh__samples.outest1`
DROP COLUMN salary;
```

### 8. 检查 View 是否损坏，进行 `SELECT` 操作
```sql
SELECT id, name
FROM `zdh_dev__dwh__samples.outest1_view`;
```

### 9. 对 `outest2` 进行 `ADD COLUMN` 操作，增加一个 `sex` 列，随意插入数据
```sql
ALTER TABLE `zdh_dev__dwh__samples.outest2`
ADD COLUMN sex STRING;

UPDATE `zdh_dev__dwh__samples.outest2`
SET sex = 'F'
WHERE id = 1;

UPDATE `zdh_dev__dwh__samples.outest2`
SET sex = 'M'
WHERE id = 2;

UPDATE `zdh_dev__dwh__samples.outest2`
SET sex = 'M'
WHERE id = 3;
```

### 10. 检查 Materialized View 是否损坏，进行 `SELECT` 操作
```sql
SELECT id, name
FROM `zdh_dev__dwh__samples.outest2_mview`;
```

### 11. 对 `outest2` 进行 `DROP COLUMN` 操作，删除 `salary`
```sql
ALTER TABLE `zdh_dev__dwh__samples.outest2`
DROP COLUMN salary;
```

### 12. 检查 Materialized View 是否损坏，进行 `SELECT` 操作
```sql
SELECT id, name
FROM `zdh_dev__dwh__samples.outest2_mview`;
```
