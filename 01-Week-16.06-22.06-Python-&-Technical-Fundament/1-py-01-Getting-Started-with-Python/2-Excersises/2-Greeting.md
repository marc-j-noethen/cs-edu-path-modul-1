# 🐍 Welcome (user-entered data)

**Course:** Cybersecurity Analyst – Python Basics | **Date:** 16 June 2025

---

## Task

**Objective:** Ask the user for their name and display a personalised greeting.

**Requirements:**
- Prompt: `Enter your name: ` (with a space at the end)
- Output: `Hello, [Name]! Welcome to the world of Python.`
- Use: the `input()` and `print()` functions

---

## Solution

```python
save_name = input("Enter your name: ")
print(f"Hello, {save_name}! Welcome to Python.")
```

**Alternative solutions:**
```python
# Using string concatenation
name = input("Enter your name: ")
print("Hello, " + name + "! Welcome to Python.")

# Using a comma separator (note: extra spaces)
name = input("Enter your name: ")
print("Hello,", name + "! Welcome to Python.")
```

---

## Tests

| Input | Expected | Result | ✓ |
|-------|----------|----------|---|
| `Max` | `Hello, Max! Welcome to Python.` | `Hello, Max! Welcome to Python.` | ✅ |
| `Anna` | `Hello, Anna! Welcome to Python.` | `Hello, Anna! Welcome to Python.` | ✅ |
| `` (empty) | `Hello, ! Welcome to Python.` | `Hello, ! Welcome to Python.` | ✅ |

---

## Notes

- **Concept:** `input()` always returns a string
- **Important:** Note the spaces in the prompt (`"Enter your name: "`)
- **String f-formatting:** The best method for formatting strings
- **Tip:** `input()` waits for input + Enter



