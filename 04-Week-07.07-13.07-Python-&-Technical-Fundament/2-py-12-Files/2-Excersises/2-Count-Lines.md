# 🐍 Count Lines in File

**Course:** Cyber Security Analyst - Python Basics | **Date:** 08 July 2025

---

## Task

**Objective:** Function to count the lines in a file

**Requirements:**
- Function: `count_lines(filename)`
- Parameter: `filename` (string)
- Return value: Integer (number of lines)
- Edge cases: File not found → 0

---

## Solution

```python
def count_lines(filename):
    """Counts lines in a file. Returns 0 on error."""
    try:
        with open(filename, 'r') as f:
            return sum(1 for _ in f)
    except FileNotFoundError:
        return 0
```

---

## Tests

| Input | Expected | Result | ✓ |
|-------|----------|----------|---|
| `count_lines("sample_data.txt")` | 9 | 9 | ✅ |
| `count_lines("not_found.txt")` | 0 | 0 | ✅ |

---

## Notes

- **Concept:** Exception handling with `try/except` for FileNotFoundError
- **Alternative:** `len(f.readlines())` (requires more memory)
- **Efficient:** Generator expression `sum(1 for _ in f)` counts without keeping the entire list in memory

