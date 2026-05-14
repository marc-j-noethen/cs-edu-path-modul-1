# 🐍 Circle Properties Calculator

**Course:** Cyber Security Analyst - Python Basics | **Date:** 7 July 2025

---

## Task

**Objective:** Calculate the properties of a circle (diameter, circumference, area) based on its radius

**Requirements:**
- Function: `calculate_circle_properties(radius)`
- Parameter: Non-negative number (radius)
- Return value: Tuple containing (diameter, circumference, area)
- Edge cases: Use of `math.pi` for precise calculations

---

## Solution

```python
import math

def calculate_circle_properties(radius):
    """Calculates the diameter, circumference and area of a circle."""
    diameter = 2 * radius
    circumference = 2 * math.pi * radius
    area = math.pi * radius ** 2
    
    return (diameter, circumference, area)
```

---

## Tests

| Input | Expected | Result | ✓ |
|-------|----------|----------|---|
| `calculate_circle_properties(10)` | ` (20.0, 62.83185307179586, 314.1592653589793)` | `(20.0, 62.83185307179586, 314.1592653589793)` | ✅ |
| `calculate_circle_properties(5)` | `(10.0, 31.41592653589793, 78.53981633974483)` | `(10.0, 31.41592653589793, 78.53981633974483)` | ✅ |
| `calculate_circle_properties(0)` | `(0, 0.0, 0.0)` | `(0, 0.0, 0.0)` | ✅ |

---

## Notes

- **Concept:** Use of `math.pi` for precise calculations
- **Formulas:** Diameter = 2r, circumference = 2πr, area = πr²
- **Alternative:** `math.tau` (= 2π) for circumference


