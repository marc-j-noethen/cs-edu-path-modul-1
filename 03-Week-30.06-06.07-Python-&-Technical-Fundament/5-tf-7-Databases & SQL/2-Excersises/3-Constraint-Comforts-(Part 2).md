# 🖥️ Constraint Comforts Part 2 - Advanced WHERE

**Course:** Cyber Security Analyst - Technical Foundation Basics | **Date:** 03 July 2025

---

## Task

**Objective:** Practise advanced constraints such as `LIKE`, `IN`, `AND`, `OR`.

**Link:** [SQLBolt Lesson 3](https://sqlbolt.com/lesson/select_queries_with_constraints_pt_2)

---

## Solution

### Task 1: Films with "Toy Story" in the title
```sql
SELECT * FROM movies WHERE title LIKE "Toy Story%";
```

### Task 2: Films by director John Lasseter
```sql
SELECT * FROM movies WHERE director = "John Lasseter";
```

### Task 3: Films NOT by John Lasseter
```sql
SELECT * FROM movies WHERE director != "John Lasseter";
```

### Task 4: Films with "WALL" in the title
```sql
SELECT * FROM movies WHERE title LIKE "%WALL%";
```

---

## Results

| Task | Status |
|------|--------|
| Task 1-4 | ✅ All checkmarks |

---

## Notes

- **`LIKE "text%"`:** Starts with "text"
- **`LIKE "%text"`:** Ends with "text"
- **`LIKE "%text%"`:** Contains "text"
- **`%`:** Wildcard for any characters (0 or more)
- **`_`:** Wildcard for exactly one character
- **String comparisons:** Use quotation marks `"` or `'`


