# 🐍 Sum Calculator

**Course:** Cyber Security Analyst - Python Basics | **Date:** 26 June 2025

---

## Task

**Objective:** Calculate the sum of all integers from 1 to n using a loop

**Requirements:**
- Input: Positive integer `n` (user input)
- Prompt: `"Enter a positive integer: "`
- Calculation: Sum of 1 + 2 + 3 + ... + n
- Output: `"The sum is: [result]"`
- Edge Cases: Assumption that the user enters a positive integer

---

## Solution

```python
# User input
n = int(input("Enter a positive integer: "))

# Calculate the sum using a loop
total = 0
for i in range(1, n + 1):
    total += i

# Output
print(f"The sum is: {total}")
```

---

## Tests

| Input | Expected | Result | ✓ |
|-------|----------|----------|---|
| `5` | `Enter a positive integer: 5`<br>`The sum is: 15` | `The sum is: 15` | ✅ |
| `10` | `The sum is: 55` | `The sum is: 55` | ✅ |
| `1` | `The sum is: 1` | `The sum is: 1` | ✅ |

---

## Notes

- **Concept:** `for` loop with `range()`, accumulator variable
- **range():** `range(1, n + 1)` generates numbers from 1 to n (inclusive)
- **Alternative:** Gaussian sum formula `n * (n + 1) // 2` (without a loop)


