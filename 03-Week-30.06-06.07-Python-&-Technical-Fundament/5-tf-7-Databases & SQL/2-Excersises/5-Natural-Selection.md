# 🖥️ Natural Selection - SELECT Review

**Course:** Cyber Security Analyst - Technical Fundament Basics | **Date:** 03 July 2025

---

## Task

**Objective:** Apply all SELECT concepts covered so far in a review task.

**Link:** [SQLBolt SELECT Review](https://sqlbolt.com/lesson/select_queries_review)

---

## Solution

### Task 1: Cities in North America
```sql
SELECT city, population 
FROM north_american_cities 
WHERE country = "Canada";
```

### Task 2: US cities sorted by latitude
```sql
SELECT * 
FROM north_american_cities 
WHERE country = "United States" 
ORDER BY latitude DESC;
```

### Task 3: Cities west of Chicago
```sql
SELECT city 
FROM north_american_cities 
WHERE longitude < -87.629798 
ORDER BY longitude;
```

### Task 4: Two largest cities in Mexico
```sql
SELECT city 
FROM north_american_cities 
WHERE country = "Mexico" 
ORDER BY population DESC 
LIMIT 2;
```

### Task 5: Third and fourth largest US cities
```sql
SELECT city 
FROM north_american_cities 
WHERE country = "United States" 
ORDER BY population DESC 
LIMIT 2 OFFSET 2;
```

---

## Results

| Task | Status |
|------|--------|
| Task 1-5 | ✅ All checkmarks |

---

## Notes

- **Combined queries:** WHERE + ORDER BY + LIMIT + OFFSET
- **Geographical data:** Longitude (East/West), Latitude (North/South)
- **Negative longitude:** West of Greenwich
- **Query order:** SELECT → FROM → WHERE → ORDER BY → LIMIT → OFFSET

