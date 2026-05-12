# 🐍 Number Comparison

**Course:** Cyber Security Analyst - Python Basics | **Date:** 20 June 2025

---

## Task

**Objective:** Compare two integers and output the larger one.

**Requirements:**
- Prompt 1: `Enter the first integer:`
- Prompt 2: `Enter the second integer:`
- Output depending on the comparison:
  - `First number is larger.`
  - `Second number is larger.`
  - `The numbers are equal.`

---

## Solution

```python
first = int(input("Enter the first integer: "))
second = int(input("Enter the second integer: "))

if first > second:
    print("First number is larger.")
elif second > first:
    print("Second number is larger.")
else:
    print("The numbers are equal.")
```

**Alternative using variables:**
```python
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

if num1 > num2:
    result = "First number is larger."
elif num1 < num2:
    result = "Second number is larger."
else:
    result = "The numbers are equal."

print(result)
```

---

## Tests

| Input 1 | Input 2 | Expected | Result | ✓ |
|---------|-------- -|----------|----------|---|
| `10` | `5` | `First number is larger.` | `First number is larger.` | ✅ |
| `7` | `12` | `Second number is larger.` | `Second number is larger.` | ✅ |
| `8` | `8` | `The numbers are equal.` | `The numbers are equal.` | ✅ |
| `-5` | `-10` | `First number is larger.` | `First number is larger.` | ✅ |
| `0` | `0` | `The numbers are equal.` | `The numbers are equal.` | ✅ |

---

## Notes

- **Concept:** `if`, `elif`, `else` control structures
- **Comparison operators:**

| Operator | Meaning |
|----------|-----------|
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal to |
| `<=` | Less than or equal to |
| `==` | Equal to |
| `!=` | Not equal to |

- **Important:** `=` is assignment, `==` is comparison!
- **Indentation:** Code block after `:` must be indented (4 spaces)

