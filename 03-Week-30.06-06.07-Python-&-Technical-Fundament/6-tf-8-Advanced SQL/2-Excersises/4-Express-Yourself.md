# 🗄️ Queries with Expressions (Database Queries)

**Course:** Cyber Security Analyst - Technical Fundamentals | **Date:** 4 July 2025

---

## Task

**Objective:**  
Use expressions (such as arithmetic operations) directly in `SELECT` statements to calculate new values from existing data.

**Requirements:**

- Open SQLBolt Lesson 9: https://sqlbolt.com/lesson/select_queries_with_expressions
    
- Read the explanations and complete all query tasks
    
- Obtain the green ✓ tick for each task
    
- Use arithmetic expressions (`+`, `-`, `*`, `/`, `%`) directly in `SELECT`
    
- Output:
    
    - `Calculated columns directly in the query (e.g. price * quantity)`
        
    - `Renamed columns using AS (alias)`
        
    - `Screenshot of the completed lesson (all ticks visible)`
        

---

## Solution

```sql
-- Query 1: Title and duration in hours (stored in minutes)
SELECT title, (length_minutes / 60.0) AS length_hours
FROM movies;

-- Query 2: Annual turnover for each employee (salary * 1.1 = +10% bonus)
SELECT name, (salary * 1.1) AS salary_with_bonus
FROM employees;

-- Query 3: All films with calculated duration and alias
SELECT title,
       (length_minutes / 60) AS hours,
       (length_minutes % 60) AS remaining_minutes
FROM movies;
```

**Alternative (compact):**

```sql
-- Combining multiple expressions and aliases in a single query
SELECT title,
       year,
       (length_minutes / 60.0) AS duration_hours
FROM movies
WHERE year >= 2000;
```

---

## Tests

|Input 1 (table)|Input 2 (column)|Input 3 (expression)|Expected|Result|✓|
|---|---|---|---|---|---|
|`movies`|`length_minutes`|`/ 60.0`|`Duration in hours`|`Correct values`|✅|
|`employees`|`salary`|`* 1.1`|`Salary with 10% bonus`|`Correct values`|✅|
|`movies`|`length_minutes`|`% 60`|`Remaining minutes`|`Correct values`|✅|
|`movies`|`year`|`AS alias`|`Column renamed`|`Correct output`|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|`Expression`|Calculation directly in `SELECT`, e.g. `price * quantity`|
|`AS`|Alias – gives a calculated column a readable name|
|`+` `-` `*` `/`|Basic arithmetic operations, applicable directly to column values|
|`%`|Modulo – returns the remainder of a division|
|`Integer vs. Float`|`10 / 3 = 3` (Integer), `10 / 3.0 = 3.333` (Float) – note the type!|
|`Column name`|Without `AS`, the calculated column is given an automatic, unreadable name|

---

## Rules / Logic

```
Basic structure with expression:
  SELECT expression AS alias_name
  FROM table;

Arithmetic operators:
  +   Addition
  -   Subtraction
  *   Multiplication
  /   Division (integer or float – depending on the data type!)
  %   Modulo (remainder of division)

Examples:
  price * quantity        → Total price
  salary * 1.1            → Salary + 10% bonus
  length_minutes / 60.0   → Duration in hours (Float!)
  length_minutes % 60     → Remaining minutes
```

---

## Notes

- **Concept:** Expressions in `SELECT` calculate new values without altering the original data
    
- **Syntax:** `SELECT column * number AS alias_name FROM table;`
    
- **Order is important:**
    
    1. Define the expression in the `SELECT` (e.g. `salary * 1.1`)
        
    2. Assign a meaningful alias using `AS` (e.g. `AS salary_with_bonus`)
        
    3. Optional: Add `WHERE`, `ORDER BY`, etc.
        
- **Edge cases:**
    
    - Integer division truncates decimal places – use `/ 60.0` instead of `/ 60` if necessary
        
    - `AS` is optional, but without an alias the column name becomes unreadable (e.g. `(salary * 1.1)`)
        
    - Expressions can also be used in `WHERE` and `ORDER BY`
        
- **Tip:** Expressions **never** alter the stored data in the table – they only calculate temporary values for the query output.
    

---

## Optional: Extensions

- Combine expressions with `ROUND(value, decimal places)`, e.g. `ROUND(salary * 1.1, 2)`
    
- Validation: Ensure that division by `0` does not occur (`WHERE count != 0`)
    
- Error handling: Use `CASE WHEN` expressions for conditional calculations
    
- Usability: Always assign meaningful alias names using `AS`

