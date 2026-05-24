# 🗄️ Queries with Aggregates Pt. 1 (Database Queries)

**Course:** Cyber Security Analyst - Technical Fundamentals | **Date:** 4 July 2025

---

## Task

**Objective:**  
Use basic aggregate functions such as `COUNT`, `SUM`, `AVG`, `MIN` and `MAX` to summarise data across multiple rows.

**Requirements:**

- Open SQLBolt Lesson 10: https://sqlbolt.com/lesson/select_queries_with_aggregates
    
- Read the explanations and complete all query tasks
    
- Obtain the green ✓ tick for each task
    
- Use aggregate functions correctly in the `SELECT` clause and name them using `AS`
    
- Output:
    
    - `Number of rows / entries (COUNT)`
        
    - `Sum, average, minimum or maximum of a column`
        
    - `Screenshot of the completed lesson (all ticks visible)`
        

---

## Solution

```sql
-- Query 1: Total number of employees
SELECT COUNT(*) AS total_employees
FROM employees;

-- Query 2: Average salary of all employees
SELECT AVG(salary) AS average_salary
FROM employees;

-- Query 3: Highest and lowest salary
SELECT MAX(salary) AS highest_salary,
       MIN(salary) AS lowest_salary
FROM employees;

-- Query 4: Total salary of all employees (sum)
SELECT SUM(salary) AS total_salary_cost
FROM employees;
```

**Alternative (compact):**

```sql
-- All aggregate functions in a single query
SELECT COUNT(*)      AS total_employees,
       AVG(salary)   AS avg_salary,
       SUM(salary)   AS total_salary,
       MIN(salary)   AS min_salary,
       MAX(salary)   AS max_salary
FROM employees;
```

---

## Tests

|Input 1 (table)|Input 2 (column)|Input 3 (function)|Expected|Result|✓|
|---| ---|---|---|---|---|
|`employees`|`*`|`COUNT(*)`|`Number of rows`|`Correct number`|✅|
|`employees`|`salary`|`AVG(salary)`|`Average salary`|`Correct number`|✅|
|`employees`|`salary`|`MAX(salary)`|`Highest salary`|`Correct number`|✅|
|`employees`|`salary`|`SUM(salary)`|`Total salary`|`Correct number`|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|`COUNT(*)`|Counts all rows, including NULL values|
|`COUNT(column)`|Counts only rows where the column is **not** NULL|
|`SUM(column)`|Adds up all values in a column|
|`AVG(column)`|Calculates the average of all values (NULL is ignored)|
|`MIN(column)`|Returns the smallest value in a column|
|`MAX(column)`|Returns the largest value in a column|

---

## Rules / Logic

```
Basic structure:
  SELECT AGGREGATE_FUNCTION(column) AS alias_name
  FROM table;

The 5 aggregate functions:
  COUNT(*)          → Number of all rows (including NULL)
  COUNT(column)     → Number of rows without NULL in this column
  SUM(column)       → Sum of all values
  AVG(Column)       → Average of all values (NULLs ignored)
  MIN(Column)       → Smallest value
  MAX(Column)       → Largest value

Important:
  NULL values are ignored by SUM, AVG, MIN, MAX
  COUNT(*) vs COUNT(Column) → Note the difference with NULL!
```

---

## Notes

- **Concept:** Aggregate functions summarise multiple rows into a single result value
    
- **Syntax:** `SELECT COUNT(*) AS total FROM table;`
    
- **Order is important:**
    
    1. Select the desired aggregate function (`COUNT`, `SUM`, `AVG`, `MIN`, `MAX`)
        
    2. Specify the relevant column (or `*` for `COUNT`)
        
    3. Assign a meaningful alias using `AS`
        
- **Edge cases:**
    
    - `COUNT(*)` counts all rows, `COUNT(column)` skips NULL values
        
    - `AVG` ignores NULL – this can skew the average
        
    - `MIN` / `MAX` also work with text (alphabetical sorting)
        
- **Tip:** Aggregate functions always return **exactly one row** – they reduce all rows to a single result value.
    

---

## Optional: Extensions

- Use `GROUP BY` to calculate aggregate functions per group (e.g. average salary per department)
    
- Validation: Use `COUNT(DISTINCT column)` to count only unique values
    
- Error handling: Avoid division by 0 when using `COUNT` in your own expressions
    
- Usability: Use `ROUND(AVG(salary), 2)` for neatly rounded average values

