# 🐍 Rectangle Area (Type Conversion)

**Course:** Cyber Security Analyst - Python Basics | **Date:** 16 June 2025

---

## Task

**Objective:** Calculate the area of a rectangle based on user input.

**Requirements:**
- Prompt 1: `Enter length:`
- Prompt 2: `Enter width:`
- Calculation: `Area = Length × Width`
- Output: `The area is: [Area]`
- Important: Use `int()` for type conversion

---

## Solution

```python
length = int(input("Enter length: "))
width = int(input("Enter width: "))
area = length * width
print("The area is:", area)
```

**Alternative solutions:**
```python
# Using f-strings
length = int(input("Enter length: "))
width = int(input("Enter width: "))
print(f"The area is: {length * width}")

# Using float for decimal numbers
length = float(input("Enter length: "))
width = float(input("Enter width: "))
area = length * width
print("The area is:", area)

# With separate conversion
length_str = input("Enter length: ")
width_str = input("Enter width: ")
length = int(length_str)
width = int(width_str)
area = length * width
print("The area is:", area)
```

---

## Tests

| Length | Width | Expected | Result | ✓ |
|--------|-------|----------|----------|---|
| `5` | `4` | `The area is: 20` | `The area is: 20` | ✅ |
| `10` | `10` | `The area is: 100` | `The area is: 100` | ✅ |
| `7` | `3` | `The area is: 21` | `The area is: 21` | ✅ |

---

## Notes

- **Concept:** Type conversion (Type Casting)
- **Important:** `input()` ALWAYS returns a string!
- **`int()`:** Converts a string to an integer
- **`float()`:** Converts a string to a floating-point number
- **Error without `int()`:** `"5" * "4"` → TypeError!
- **String multiplication:** `"5" * 4` → `"5555"` (repetition)

**Type conversion functions:**

| Function | Description | Example |
|----------|--------------|----------|
| `int()` | String → Integer | `int("42")` → `42` |
| `float()` | String → Decimal | `float("3.14")` → `3.14` |
| `str()` | Number → String | `str(42)` → `"42"` |

