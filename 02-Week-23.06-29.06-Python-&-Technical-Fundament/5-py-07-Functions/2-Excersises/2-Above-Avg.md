# 🐍 Count Above Average

**Course:** Cyber Security Analyst - Python Basics | **Date:** 27 June 2025

---

## Task

**Objective:** Count the number of values in a list that are strictly greater than the average

**Requirements:**
- Function: `count_above_average(numbers)`
- Parameter: `numbers` (list of int/float)
- Return value: Integer (number of values > average)
- Calculation: Calculate the average, then count the values
- Edge cases: Empty list → return 0

---

## Solution

```python
def count_above_average(numbers):
    """
    Counts the number of numbers that are above the average.
    
    Args:
        numbers: List of numbers (int or float)
    
    Returns:
        Number of values strictly greater than the average (int)
    """
    # Edge case: Empty list
    if len(numbers) == 0:
        return 0
    
    # Calculate average
    average = sum(numbers) / len(numbers)
    
    # Count values above average
    count = 0
    for num in numbers:
        if num > average:
            count += 1
    
    return count
```

---

## Tests

| Input | Expected | Result | ✓ |
|-------|----------|----------|---|
| `count_above_average([1, 2, 3, 4, 5])` | `2` | `2` | ✅ |
| `count_above_average([10, 10, 10])` | `0` | `0` | ✅ |
| `count_above_average([])` | `0` | `0` | ✅ |
| `count_above_average([1, 100])` | `1` | `1` | ✅ |

---

## Notes

- **Concept:** `sum()`, `len()`, calculating the average, iteration
- **Important:** Strictly greater than (`>`) is not greater than or equal to (`>=`)
- **Alternative:** List comprehension: `return sum(1 for num in numbers if num > average)`
- **Example:** [1, 2, 3, 4, 5] → Ø = 3.0 → [4, 5] are > 3.0 → count = 2

