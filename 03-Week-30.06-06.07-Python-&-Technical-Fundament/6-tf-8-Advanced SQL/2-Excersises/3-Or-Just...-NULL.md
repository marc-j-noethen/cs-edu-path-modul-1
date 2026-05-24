# 🗄️ SQL NULL Values (Database Queries)

**Course:** Cyber Security Analyst - Technical Fundamentals | **Date:** 4 July 2025

---

## Task

**Objective:**  
To deepen your understanding of how `NULL` values are represented in SQL and how they are correctly handled with `IS NULL` and `IS NOT NULL` in queries.

**Requirements:**

- Open SQLBolt Lesson 8: https://sqlbolt.com/lesson/select_queries_with_nulls
    
- Read the explanations and complete all query tasks
    
- Obtain the green ✓ tick for each task
    
- `NULL` cannot be compared using `=` or `!=` – always use `IS NULL` / `IS NOT NULL`
    
- Output:
    
    - `Rows where a column is NULL`
        
    - `Rows where a column is NOT NULL`
        
    - `Screenshot of the completed lesson (all ticks visible)`
        

---

## Solution

```sql
-- Query 1: Find all films without a director
SELECT title, director
FROM movies
WHERE director IS NULL;

-- Query 2: Find all films with a year
SELECT title, year
FROM movies
WHERE year IS NOT NULL;
```

**Alternative (compact):**

```sql
-- Combined condition: films without a director AND without a year
SELECT title
FROM movies
WHERE director IS NULL
  AND year IS NULL;
```

---

## Tests

|Input 1 (table)|Input 2 (column)|Input 3 (condition)|Expected|Result|✓|
|---|---|---|---|---|---|
|`movies`|`director`|`IS NULL`|`Rows without a director`|`Correct rows`|✅|
|`movies`|`year`|`IS NOT NULL`|`Rows with a year`|`Correct rows`|✅|
|`movies`|`director`|`IS NOT NULL`|`Rows with a director`|`Correct rows`|✅|
|`employees`|`building`|`IS NULL`|`Employees without an office`|`Correct rows`|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|`NULL`|Missing or unknown value – not a space, not 0, not an empty string|
|`IS NULL`|Checks whether a value is missing / not set|
|`IS NOT NULL`|Checks whether a value is present (not NULL)|
|`= NULL`|Never works – always returns FALSE, as NULL is not equal to anything|
|`WHERE` clause|`IS NULL` / `IS NOT NULL` are used here to filter out NULL values|
|Database design|NULL occurs when optional fields are left blank (e.g. missing data)|

---

## Rules / Logic

```
Rule 1:  NULL = NULL        → FALSE  (never TRUE!)
Rule 2:  NULL IS NULL       → TRUE
Rule 3:  NULL IS NOT NULL   → FALSE

Basic structure:
  SELECT columns
  FROM table
  WHERE column IS NULL;        -- finds missing entries

  SELECT columns
  FROM table
  WHERE column IS NOT NULL;    -- finds existing entries
```

---

## Notes

- **Concept:** NULL represents a missing or unknown value in a database cell
    
- **Syntax:** `IS NULL` and `IS NOT NULL` (never use `= NULL` or `!= NULL`)
    
- **Order is important:**
    
    1. Understand what NULL means (no value, not empty, not 0)
        
    2. Use `IS NULL` to search for missing entries
        
    3. Use `IS NOT NULL` to filter existing entries
        
- **Edge cases:**
    
    - `= NULL` never works – always use `IS NULL`
        
    - `COUNT(*)` counts all rows, `COUNT(column)` ignores NULL values
        
    - JOIN operations involving NULL columns can cause rows to ‘disappear’
        
- **Tip:** NULL is not a ‘value’ – it cannot be compared using either `=` or `!=`. Aggregate functions such as `AVG()` or `SUM()` automatically ignore NULL values.
    

---

## Optional: Extensions

- Use `COALESCE(column, 'default value')` to replace NULL with a fallback value
    
- Use `NULLIF(column, 0)` to treat certain values as NULL
    
- Error handling: ensure that NULL values are handled in applications
    
- User-friendliness: display NULL fields in the output as `'N/A'` or `'Unknown'`

