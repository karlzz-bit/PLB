# SQL语句基础语法汇总

## 1. 数据查询

### SELECT 语句
用于从表中查询数据。
```sql
SELECT column1, column2, ...
FROM table_name
WHERE condition
GROUP BY column1, column2, ...
HAVING condition
ORDER BY column1, column2, ...;
```
- **SELECT**：指定要查询的列。  
- **FROM**：指定查询的表名。  
- **WHERE**：过滤记录。  
- **GROUP BY**：对结果进行分组。  
- **HAVING**：对分组后的结果进行过滤。  
- **ORDER BY**：对结果排序。

### DISTINCT 关键字
去除查询结果中的重复记录。
```sql
SELECT DISTINCT column1, column2, ...
FROM table_name;
```

---

## 2. 数据操作

### INSERT 语句
用于向表中插入数据。
```sql
INSERT INTO table_name (column1, column2, ...)
VALUES (value1, value2, ...);
```

### UPDATE 语句
用于更新表中现有记录。
```sql
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
```
*注意：建议在 UPDATE 语句中使用 WHERE 子句以避免更新所有记录。*

### DELETE 语句
用于删除表中的记录。
```sql
DELETE FROM table_name
WHERE condition;
```
*注意：同样建议加上 WHERE 子句以防止删除所有数据。*

---

## 3. 表结构定义

### CREATE TABLE 语句
用于创建新表。
```sql
CREATE TABLE table_name (
    column1 datatype [constraint],
    column2 datatype [constraint],
    ...
);
```
- **datatype**：数据类型（如 INT, VARCHAR, DATE 等）。  
- **constraint**：约束条件（如 PRIMARY KEY, NOT NULL, UNIQUE, CHECK, FOREIGN KEY）。

### ALTER TABLE 语句
用于修改现有表的结构。
```sql
ALTER TABLE table_name
ADD column_name datatype;
```
或
```sql
ALTER TABLE table_name
DROP COLUMN column_name;
```
*其他操作包括修改列数据类型、添加约束等。*

### DROP TABLE 语句
用于删除表及其数据。
```sql
DROP TABLE table_name;
```

---

## 4. 视图和索引

### 创建视图
用于保存复杂查询的结果集，便于后续调用。
```sql
CREATE VIEW view_name AS
SELECT column1, column2, ...
FROM table_name
WHERE condition;
```

### 创建索引
用于提高查询效率。
```sql
CREATE INDEX index_name ON table_name (column1, column2, ...);
```

---

## 5. 联结操作（JOIN）

### INNER JOIN
返回两个表中匹配的记录。
```sql
SELECT A.column1, B.column2, ...
FROM tableA A
INNER JOIN tableB B ON A.common_field = B.common_field;
```

### LEFT JOIN / LEFT OUTER JOIN
返回左表中的所有记录及右表中匹配的记录。
```sql
SELECT A.column1, B.column2, ...
FROM tableA A
LEFT JOIN tableB B ON A.common_field = B.common_field;
```

### RIGHT JOIN / RIGHT OUTER JOIN
返回右表中的所有记录及左表中匹配的记录。
```sql
SELECT A.column1, B.column2, ...
FROM tableA A
RIGHT JOIN tableB B ON A.common_field = B.common_field;
```

### FULL JOIN / FULL OUTER JOIN
返回两个表中的所有记录，当没有匹配时返回 NULL。
```sql
SELECT A.column1, B.column2, ...
FROM tableA A
FULL OUTER JOIN tableB B ON A.common_field = B.common_field;
```

---

## 6. 子查询

### 基本用法
在一个查询语句中嵌套另一个查询语句。
```sql
SELECT column1
FROM table_name
WHERE column2 IN (SELECT column2 FROM table_name2 WHERE condition);
```

---

## 7. 常用函数

### 聚合函数
- **COUNT()**：统计行数  
- **SUM()**：求和  
- **AVG()**：平均值  
- **MIN() / MAX()**：最小值/最大值
```sql
SELECT COUNT(column_name), AVG(column_name)
FROM table_name
WHERE condition;
```

### 字符串函数（示例：MySQL）
- **CONCAT()**：字符串连接  
- **SUBSTRING()**：提取子字符串  
- **LENGTH()**：获取字符串长度
```sql
SELECT CONCAT(first_name, ' ', last_name) AS full_name
FROM users;
```

### 日期函数（示例：MySQL）
- **NOW()**：当前时间  
- **DATE()**：提取日期部分
```sql
SELECT NOW(), DATE(created_at)
FROM orders;
```

---

## 8. 事务控制

### 开启事务
```sql
BEGIN TRANSACTION;
```
或
```sql
START TRANSACTION;
```

### 提交事务
```sql
COMMIT;
```

### 回滚事务
```sql
ROLLBACK;
```

---
根据具体的数据库管理系统（如 MySQL、PostgreSQL、SQL Server、Oracle 等），语法和函数可能会有所不同，使用前请查阅相应的官方文档。
# 官方文档地址

以下是主流数据库的官方文档地址列表：

- **MySQL**  
  [MySQL官方文档](https://dev.mysql.com/doc/)  
  提供了 MySQL 安装、配置、使用以及 SQL 语法等详细说明。 :contentReference[oaicite:0]{index=0}

- **PostgreSQL**  
  [PostgreSQL官方文档](https://www.postgresql.org/docs/)  
  全面覆盖了 PostgreSQL 的基础和高级功能。 :contentReference[oaicite:1]{index=1}

- **Microsoft SQL Server**  
  [SQL Server官方文档](https://docs.microsoft.com/zh-cn/sql/?view=sql-server-ver16)  
  包含 SQL Server 的安装、管理、开发及 SQL 查询等方面的信息。 :contentReference[oaicite:2]{index=2}

- **Oracle Database**  
  [Oracle官方文档](https://docs.oracle.com/en/database/)  
  提供了关于 Oracle 数据库使用、SQL 编程和性能优化的详细指南。 :contentReference[oaicite:3]{index=3}

> 注：SQL语言标准由 ISO/IEC 9075 定义，标准文本可通过官方渠道获取。
