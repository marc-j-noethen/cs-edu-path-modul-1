# 🐍 Sum Calculator (Adding two numbers)

**Course:** Cyber Security Analyst - Python Basics | **Date:** 17 June 2025

---

## Task

**Objective:** Read two numbers from the user and calculate their sum.

**Requirements:**
- Prompt 1: `Enter first number: `
- Prompt 2: `Enter second number: `
- Calculation: Sum of the two numbers
- Treat inputs as integers (`int`)

---

## Solution

```python
first_num = int(input("Enter first number: "))
second_num = int(input("Enter second number: "))
calc = first_num + second_num
print(calc)
```

**Alternative solutions:**
```python
# With f-string output
first_num = int(input("Enter first number: "))
second_num = int(input("Enter second number: "))
print(f"The sum is: {first_num + second_num}")

# Compact (not recommended for readability)
print(int(input("Enter first number: ")) + int(input("Enter second number: ")))
```

---

## Tests

| Input 1 | Input 2 | Expected | Result | ✓ |
|---------|---------|-- --------|----------|---|
| `5` | `3` | `8` | `8` | ✅ |
| `10` | `20` | `30` | `30` | ✅ |
| `-5` | `5` | `0` | `0` | ✅ |
| `0` | `0` | `0` | `0` | ✅ |

---

## Notes

- **Concept:** Type conversion with `int()` and arithmetic operations
- **Important:** Without `int()`, `"5" + "3"` would equal `"53"` (string concatenation!)
- **Arithmetic operators:**
  - `+` Addition
  - `-` Subtraction
  - `*` Multiplication
  - `/` Division (result: float)
  - `//` Integer division
  - `%` Modulo (remainder)
  - `**` Exponentiation

