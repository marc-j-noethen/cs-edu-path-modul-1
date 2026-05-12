# 🐍 Multiline Print (Multi-line output)

**Course:** Cyber Security Analyst - Python Basics | **Date:** 16 June 2025

---

## Task

**Objective:** Output three lines of text using a single `print()` command.

**Requirements:**
- Only ONE `print()` command
- Output exactly:
  ```
  Line 1: Python is fun.
  Line 2: It is also powerful.
  Line 3: Let's learn more!
  ```

---

## Solution

```python
print("Line 1: Python is fun.\n" + "Line 2: It is also powerful.\n" + "Line 3: Let's learn more!")
```

**Alternative solutions:**
```python
# Using triple quotes (multi-line string) - recommended
print("""Line 1: Python is fun.
Line 2: It is also powerful.
Line 3: Let's learn more!""")

# Only with \n (without +)
print("Line 1: Python is fun.\nLine 2: It is also powerful.\nLine 3: Let's learn more!")

# With escape sequence for line break
print("Line 1: Python is fun.\n"
      "Line 2: It is also powerful.\n"
      "Line 3: Let's learn more!")
```

---

## Tests

| Input | Expected | Result | ✓ |
|-------|----------|----------|---|
| (none) | 3 lines as above | 3 lines as above | ✅ |

**Output:**
```
Line 1: Python is fun.
Line 2: It is also powerful.
Line 3: Let's learn more!
```

---

## Notes

- **Concept:** Escape sequences and multi-line strings
- **`\n`:** Newline (line break)
- **Triple quotes:** `"""` or `'''` for multi-line strings
- **Other escape sequences:**
  - `\t` = Tab
  - `\\` = Backslash
  - `\'` = Apostrophe
  - `\"` = Double quotation mark
- **Tip:** Triple quotes are more readable for longer texts


