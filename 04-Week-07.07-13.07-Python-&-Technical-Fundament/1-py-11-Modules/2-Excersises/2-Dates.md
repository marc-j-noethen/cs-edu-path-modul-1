# 🐍 Days Between Dates

**Course:** Cyber Security Analyst - Python Basics | **Date:** 7 July 2025

---

## Task

**Objective:** Calculate the absolute difference in days between two date values

**Requirements:**
- Function: `days_between_dates(date_str1, date_str2)`
- Return value: Non-negative integer (difference in days)
- Edge cases: Invalid date format → `None`

---

## Solution

```python
from datetime import datetime

def days_between_dates(date_str1, date_str2):
    """Calculates the absolute difference in days between two dates."""
    try:
        date1 = datetime.strptime(date_str1, "%Y-%m-%d")
        date2 = datetime.strptime(date_str2, "%Y-%m-%d")
        difference = abs((date2 - date1).days)
        return difference
    except ValueError:
        return None
```

---

## Tests

| Input | Expected | Result | ✓ |
|-------|----------|----------|---|
| `days_between_dates("2024-01-01", "2024-01-11")` | `10` | `10` | ✅ |
| `days_between_dates("2024-01-11", "2024-01-01")` | `10` | `10` | ✅ |
| `days_between_dates("2024-13-01", "2024-01-01")` | `None` | `None` | ✅ |

---

## Notes

- **Concept:** Exception handling with `try/except` for invalid date values
- **Alternative:** `datetime.fromisoformat()` (from Python 3.7)


