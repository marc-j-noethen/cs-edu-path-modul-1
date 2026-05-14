# 🐍 Safe Division with Error Handling

**Course:** Cyber Security Analyst - Python Basics | **Date:** 09 July 2025

---

## Task

**Objective:** Function for safely dividing two string numbers with specific error messages

**Requirements:**
- Function: `safe_divide(numerator_str, denominator_str)`
- Parameters: Two strings (numerator, denominator)
- Return value: Float (on success), "Invalid number format" (on ValueError), "Cannot divide by zero" (on ZeroDivisionError)
- Edge cases: Invalid number formats, division by zero

---

## Solution

```python
def safe_divide(numerator_str, denominator_str):
    """Divides two strings as floats. Returns specific error messages."""
    try:
        numerator = float (numerator_str)
        denominator = float(denominator_str)
        try:
            return numerator / denominator
        except ZeroDivisionError:
            return "Cannot divide by zero"
    except ValueError:
        return "Invalid number format"
```

---

## Tests

| Input | Expected | Result | ✓ |
|-------|----------|----------|---|
| `safe_divide("10", "2")` | 5.0 | 5.0 | ✅ |
| `safe_divide("10", "0")` | "Cannot divide by zero" | Cannot divide by zero | ✅ |
| `safe_divide("abc", "2")` | "Invalid number format" | Invalid number format | ✅ |
| `safe_divide("10", "xyz")` | "Invalid number format" | Invalid number format | ✅ |
| `safe_divide("15", "3")` | 5.0 | 5.0 | ✅ |

---

## Notes

- **Concept:** Nested try-except blocks for different exception types
- **ValueError:** Occurs with float() if the string is not convertible
- **ZeroDivisionError:** Occurs when dividing by 0
- **Alternative:** try-except-else structure (division in the else block)

