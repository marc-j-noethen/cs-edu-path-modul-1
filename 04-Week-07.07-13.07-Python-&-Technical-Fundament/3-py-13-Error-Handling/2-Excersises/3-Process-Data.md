# 🐍 Process Data List with Try-Except-Finally

**Course:** Cyber Security Analyst - Python Basics | **Date:** 9 July 2025

---

## Task

**Objective:** Function to calculate the sum of reciprocals with detailed error handling

**Requirements:**
- Function: `process_data_list(data)`
- Parameter: `data` (list with mixed data types)
- Return value: Float (sum of all successful reciprocals)
- Behaviour: Try-Except-Finally structure for each element
  - Try: Calculate 1.0/item and add to the sum
  - Except: Catch TypeError and ZeroDivisionError, output error message
  - Finally: Output "Finished processing item: {item}"
- Edge cases: Non-numeric values, division by zero

---

## Solution

```python
def process_data_list(data):
    """Calculates the sum of reciprocals using Try-Except-Finally error handling."""
    total = 0.0
    
    for item in data:
        try:
            reciprocal = 1.0 / item
            total += reciprocal
        except (TypeError, ZeroDivisionError) as e:
            print(f"Error processing {item}: {str(e)}")
        finally:
            print(f"Finished processing item: {item}")
    
    return total
```

---

## Tests

| Input | Expected | Result | ✓ |
|-------|----------|----------|---|
| `process_data_list([2, 4, 'abc', 0, 10])` | 0.85 (with error messages) | 0.85 | ✅ |
| `process_data_list([10, 0, -2, 5, 'skip'])` | -0.2 (with error output) | -0.2 | ✅ |
| `process_data_list([1, 1, 1, 1])` | 4.0 | 4.0 | ✅ |

---

## Notes

- **Concept:** Try-Except-Finally structure – Finally is ALWAYS executed
- **TypeError:** Occurs with 1.0 / 'string' (non-numeric value)
- **ZeroDivisionError:** Occurs with 1.0 / 0
- **str(e):** Extracts the error message from the exception object
- **Finally block:** Ideal for cleanup operations or logging
- **Calculation:** 1/2 + 1/4 + 1/10 = 0.5 + 0.25 + 0.1 = 0.85

