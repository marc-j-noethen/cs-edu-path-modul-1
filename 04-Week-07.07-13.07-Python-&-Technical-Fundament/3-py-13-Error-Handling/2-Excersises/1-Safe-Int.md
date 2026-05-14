# 🐍 Safe Integer Conversion

**Course:** Cyber Security Analyst - Python Basics | **Date:** 09 July 2025

---

## Task

**Objective:** Function for safely converting a string to an integer

**Requirements:**
- Function: `safe_int_convert(input_string)`
- Parameter: `input_string` (string)
- Return value: Integer (on success) or None (on error)
- Edge Cases: Non-numeric characters → None

---

## Solution

```python
def safe_int_convert(input_string):
    """Safely converts a string to an integer. Returns None on error."""
    try:
        return int(input_string)
    except ValueError:
        return None
```

---

## Tests

| Input | Expected | Result | ✓ |
|-------|----------|----------|---|
| `safe_int_convert("123")` | 123 | 123 | ✅ |
| `safe_int_convert("abc")` | None | None | ✅ |
| `safe_int_convert("12.5")` | None | None | ✅ |
| `safe_int_convert("-42")` | -42 | -42 | ✅ |

---

## Notes

- **Concept:** ValueError exception handling during type conversion
- **int():** Raises a ValueError if the string cannot be converted
- **Alternative:** Regex validation before conversion (more complex)


