# 🖥️ Feeling Left Out?

**Course:** Cyber Security Analyst - Technical Fundament Basics | **Date:** 04 July 2025

---

## Task

**Objective:** Use `OUTER JOIN`s (specifically `LEFT JOIN`) to include data even if no match exists in the other table.

**Source:** [SQLBolt Lesson 7: OUTER JOINs](https://sqlbolt.com/lesson/select_queries_with_outer_joins)

---

## Solution

### Environment
```
Browser: Chrome / Firefox / Safari
Platform: SQLBolt (Online)
```

### Procedure

**Step 1:** Read the explanations on the page
- Understand how `LEFT JOIN`, `RIGHT JOIN` and `FULL JOIN` work
- Syntax: `SELECT ... FROM table1 LEFT JOIN table2 ON table1.id = table2.id`

**Step 2:** Solve the query tasks

**Task 1:** [Task description]
```sql
-- Insert query here
SELECT ...
FROM ...
LEFT JOIN ... ON ...;
```

**Task 2:** [Task description]
```sql
-- Insert query here
SELECT ...
FROM ...
LEFT JOIN ... ON ...;
```

**Task 3:** [Task description]
```sql
-- Insert query here
SELECT ...
FROM ...
LEFT JOIN ... ON ...;
```

*(Add further tasks as required)*

---

## Results

| Task | Status |
|---------|--------|
| Task 1 | ✓ |
| Task 2 | ✓ |
| Task 3 | ✓ |
| ... | ✓ |

---

## Submission

📸 **Screenshot:** SQLBolt Lesson 7 with all checkmarks (✓) visible

---

## Notes

- **Learned:** `LEFT JOIN` returns all rows from the left table, even if no match exists
- **Tip:** If there is no match, the columns of the right-hand table are filled with `NULL`
- **Difference from INNER JOIN:** `OUTER JOIN` retains rows without a match, whereas `INNER JOIN` does not
- **Important:** `LEFT JOIN` = `LEFT OUTER JOIN` (same meaning)

