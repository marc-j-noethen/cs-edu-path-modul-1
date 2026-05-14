# 📊 Advanced SQL — 80/20 Learning Summary

## 1. The most important concept: JOINs

Relational databases distribute data across multiple tables. **JOINs** connect these tables based on a shared column.

### INNER JOIN — only matches in both tables

```sql
SELECT e.name, d.dept_name
FROM Employees e
INNER JOIN Departments d ON e.dept_id = d.dept_id;
```

### LEFT JOIN — all rows from the left table, even without a match

```sql
SELECT e.name, d.dept_name
FROM Employees e
LEFT JOIN Departments d ON e.dept_id = d.dept_id;
-- Employees without a department → dept_name = NULL
```

|JOIN type|Behaviour|
|---|---|
|`INNER JOIN`|Only rows with a match in **both** tables (intersection ∩)|
|`LEFT JOIN`|All rows from the left table + matches from the right|
|`RIGHT JOIN`|All rows from the right table + matches from the left|
|`FULL OUTER JOIN`|All rows from both tables|

---

## 2. Core process: Aggregation with GROUP BY

Aggregate functions reduce many rows to a single summary value. Combined with `GROUP BY`, this is calculated per group.

```sql
SELECT dept_id,
       COUNT(*) AS number_of_employees,
       AVG(salary) AS average_salary
FROM Employees
WHERE dept_id IS NOT NULL      -- filters BEFORE grouping
GROUP BY dept_id
HAVING COUNT(*) > 1            -- filters AFTER grouping
ORDER BY number_of_employees DESC;
```

|Function|What it does|
|---|---|
|`COUNT(*)`|Counts all rows|
|`COUNT(col)`|Counts rows where `col` ≠ NULL|
|`SUM(col)`|Sum of all values|
|`AVG(col)`|Average|
|`MIN(col)` / `MAX(col)`|Smallest / largest value|

---

## 3. Order of execution of a query

This is how you write it — this is how the database executes it:

|Step|Clause|What happens|
|---|---|---|
|1|`FROM / JOIN`|Determine source tables & how they are combined|
|2|`WHERE`|Filter individual rows (before grouping!)|
|3|`GROUP BY`|Group rows by shared values|
|4|`HAVING`|Filter groups (aggregate functions allowed!)|
|5|`SELECT`|Calculate columns & expressions|
|6|`ORDER BY`|Sort the final result|
|7|`LIMIT / OFFSET`|Restrict the result set|

> **Key rule:** `WHERE` cannot use aggregate functions — aggregation has not happened yet at that point. That's what `HAVING` is for.

---

## 4. Key concepts with code examples

### Handling NULL correctly

```sql
-- WRONG: NULL = NULL evaluates to UNKNOWN, not TRUE
WHERE dept_id = NULL

-- CORRECT:
WHERE dept_id IS NULL
WHERE dept_id IS NOT NULL
```

### Calculated columns with expressions

```sql
SELECT item_name,
       price,
       price * 1.19 AS price_incl_tax
FROM Products;
```

### JOIN + GROUP BY combined

```sql
SELECT d.dept_name, COUNT(*) AS num_employees
FROM Employees e
INNER JOIN Departments d ON e.dept_id = d.dept_id
GROUP BY d.dept_name
ORDER BY num_employees DESC;
```

---

## ✅ Quick-start checklist

- ☐ I know the difference between INNER JOIN and LEFT JOIN
- ☐ I know that NULL is checked with `IS NULL` / `IS NOT NULL`
- ☐ I can apply aggregate functions (COUNT, SUM, AVG)
- ☐ I understand: `WHERE` filters rows, `HAVING` filters groups
- ☐ I can explain the logical order of execution of a query
- ☐ I can name calculated columns using `AS`
- ☐ I can combine JOIN and GROUP BY in a single query

---

## Table 1: Tools / clauses used

|Tool / Clause|Meaning|
|---|---|
|`INNER JOIN`|Connects tables — only rows with a match in both|
|`LEFT JOIN`|All rows from the left table, missing right-side values → NULL|
|`GROUP BY`|Groups rows with the same value for aggregation|
|`HAVING`|Filters groups based on an aggregate condition|
|`IS NULL`|Checks for a missing value (not `= NULL`!)|
|`AS`|Alias — gives columns or expressions a custom name|

## Table 2: Technical terms

|Term|Meaning|
|---|---|
|Join condition|The condition in the ON clause that defines how two tables are linked|
|Aggregate function|Calculates a single value across multiple rows (e.g. COUNT, SUM)|
|NULL|Missing / unknown value — not zero, not an empty string|
|Alias|Temporary name for a column or table within a query|
|Foreign key|Column that references the primary key of another table (e.g. dept_id)|
|Derived column|Calculated column that does not exist in the table (e.g. price * 1.19)|

## Table 3: Key vocabulary

|Vocabulary|Meaning|
|---|---|
|Redundancy|Storing the same information more than once|
|Join condition|The linking condition between two tables|
|Aggregate|To summarise / a summarised value|
|Overlapping area|Intersection (Venn diagram analogy for INNER JOIN)|
|Integer division|Whole-number division — 5/2 = 2, not 2.5|
|Derived information|Information calculated from existing columns|

---

**Key takeaway:** JOINs bring tables together, GROUP BY + aggregate functions summarise them — and the order of execution determines when you filter with `WHERE` versus `HAVING`.