# 🖥️ Filter Fanatic - ORDER BY, LIMIT, OFFSET

**Course:** Cyber Security Analyst - Technical Foundation Basics | **Date:** 03 July 2025

---

## Task

**Objective:** Filter and sort results using `ORDER BY`, `LIMIT`, `OFFSET`.

**Link:** [SQLBolt Lesson 4](https://sqlbolt.com/lesson/filtering_sorting_query_results)

---

## Solution

### Task 1: Directors (without duplicates, alphabetical)
```sql
SELECT DISTINCT director FROM movies ORDER BY director;
```

### Task 2: Last 4 films (by year)
```sql
SELECT * FROM movies ORDER BY year DESC LIMIT 4;
```

### Task 3: First 5 films (alphabetically by title)
```sql
SELECT * FROM movies ORDER BY title LIMIT 5;
```

### Task 4: Next 5 films (alphabetically, following the first 5)
```sql
SELECT * FROM movies ORDER BY title LIMIT 5 OFFSET 5;
```

---

## Results

| Task | Status |
|------|--------|
| Task 1-4 | ✅ All checkmarks |

---

## Notes

- **`ORDER BY column`:** Sort in ascending order (ASC, default)
- **`ORDER BY column DESC`:** Sort in descending order
- **`LIMIT n`:** Return only n results
- **`OFFSET n`:** Skip the first n results
- **`DISTINCT`:** Remove duplicates
- **Order:** SELECT → FROM → WHERE → ORDER BY → LIMIT → OFFSET

