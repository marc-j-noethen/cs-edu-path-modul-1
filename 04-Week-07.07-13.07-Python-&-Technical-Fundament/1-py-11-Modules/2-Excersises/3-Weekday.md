# 🐍 Find Next Weekday

**Course:** Cyber Security Analyst - Python Basics | **Date:** 07 July 2025

---

## Task

**Objective:** Find the next occurrence of a specific weekday following a start date

**Requirements:**
- Function: `find_next_weekday(start_date_str, target_weekday_name)`
- Return value: Next date as a string in the format "YYYY-MM-DD"
- Edge cases: The date must be AFTER the start date

---

## Solution

```python
from datetime import datetime, timedelta

def find_next_weekday(start_date_str, target_weekday_name):
    """Finds the next occurrence of a weekday after the start date."""
    start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
    
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", 
                "Friday", "Saturday", "Sunday"]
    target_weekday = weekdays.index(target_weekday_name)
    
    days_ahead = (target_weekday - start_date.weekday()) % 7
    if days_ahead == 0:
        days_ahead = 7
    
    next_date = start_date + timedelta(days=days_ahead)
    return next_date.strftime("%Y-%m-%d")
```

---

## Tests

| Input | Expected | Result | ✓ |
|-------|----------|----------|---|
| `find_next_weekday("2024-04-30", "Friday")` | `2024-05-03` | `2024-05-03` | ✅ |
| `find_next_weekday("2024-04-30", "Tuesday")` | `2024-05-07` | `2024-05-07` | ✅ |
| `find_next_weekday("2024-04-30", "Wednesday")` | `2024-05-01` | `2024-05-01` | ✅ |

---

## Notes

- **Concept:** Modulo arithmetic for weekday calculation
- **Alternative:** Loop with daily increment (less efficient)


