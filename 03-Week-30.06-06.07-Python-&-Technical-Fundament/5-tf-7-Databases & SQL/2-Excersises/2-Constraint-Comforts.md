# 🖥️ Constraint Comforts - WHERE Clause

**Course:** Cyber Security Analyst - Technical Foundation Basics | **Date:** 03 July 2025

---

## Task

**Objective:** Practise using the `WHERE` clause with equality and numerical comparisons.

**Link:** [SQLBolt Lesson 2](https://sqlbolt.com/lesson/select_queries_with_constraints)

---

## Solution

### Task 1: Film with id 6
```sql
SELECT * FROM movies WHERE id = 6;
```

### Task 2: Films between 2000 and 2010
```sql
SELECT * FROM movies WHERE year BETWEEN 2000 AND 2010;
```

### Task 3: Films NOT between 2000 and 2010
```sql
SELECT * FROM movies WHERE year NOT BETWEEN 2000 AND 2010;
```

### Task 4: First 5 Pixar films
```sql
SELECT * FROM movies WHERE id <= 5;
```

---

## Results

| Task | Status |
|------|--------|
| Task 1-4 | ✅ All checkmarks |

---

## Notes

- **`WHERE column = value`:** Check for equality
- **`BETWEEN x AND y`:** Range (inclusive)
- **`NOT BETWEEN`:** Outside the range
- **Comparison operators:** `=`, `!=`, `<`, `>`, `<=`, `>=`
- **Numeric comparisons:** Without quotation marks


