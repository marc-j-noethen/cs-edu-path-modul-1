# 🐍 Countdown

**Course:** Cyber Security Analyst - Python Basics | **Date:** 26 June 2025

---

## Task

**Objective:** Countdown from an entered number to 1, followed by a "Liftoff!" message

**Requirements:**
- Input: Positive integer (user input)
- Prompt: `"Enter countdown start number: "`
- Output: Numbers from n to 1 (each number on a new line)
- Final output: `"Liftoff!"` after the loop
- Edge cases: Assumption that the user enters a positive integer

---

## Solution

```python
# User input
n = int(input("Enter countdown start number: "))

# Countdown loop
for i in range(n, 0, -1):
    print(i)

# Liftoff message
print("Liftoff!")
```

---

## Tests

| Input | Expected | Result | ✓ |
|-------|----------|----------|---|
| `3` | `Enter countdown start number: 3`<br>`3`<br>`2`<br>`1`<br>`Liftoff!` | `3`<br>`2`<br>`1`<br>`Liftoff!` | ✅ |
| `5` | `5`<br>`4`<br>`3`<br>`2`<br>`1`<br>`Liftoff!` | Correct | ✅ |
| `1` | `1`<br>`Liftoff!` | `1`<br>`Liftoff!` | ✅ |

---

## Notes

- **Concept:** `for` loop with `range()` and a negative step
- **range():** `range(n, 0, -1)` counts from n to 1 (backwards)
- **Important:** Second parameter `0` means "up to but not including 0"
- **Alternative:** `while` loop with decrement

