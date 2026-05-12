# 🐍 The Answer (Simple Calculation)

**Course:** Cyber Security Analyst - Python Basics | **Date:** 16 June 2025

---

## Task

**Objective:** Calculate `6 * 7` and display the result as formatted text.

**Requirements:**
- Calculate: `6 * 7`
- Output: `The answer is: 42`
- Use: `print()` function

---

## Solution

```python
answer = 6 * 7
print(f"The answer is: {answer}")
```

**Alternative solutions:**
```python
# With comma separator
answer = 6 * 7
print("The answer is:", answer)

# Direct calculation
print(f"The answer is: {6 * 7}")
```

---

## Tests

| Input | Expected | Result | ✓ |
|-------|----------|----------|---|
| (none) | `The answer is: 42` | `The answer is: 42` | ✅ |

---

## Notes

- **Concept:** Variable assignment and f-strings
- **f-string:** `f"Text {variable}"` inserts the variable value
- **Alternative:** `print("Text", var)` automatically inserts spaces
- **Tip:** f-strings are the most modern method (Python 3.6+)

