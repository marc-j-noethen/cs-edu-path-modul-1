# 🐍 Get Specific Line from File

**Course:** Cyber Security Analyst - Python Basics | **Date:** 08 July 2025

---

## Task

**Objective:** Function to read a specific line from a file

**Requirements:**
- Function: `get_line(filename, line_number)`
- Parameters: `filename` (string), `line_number` (integer, 1-based)
- Return value: String (line content without whitespace) or None
- Edge cases: Invalid line number, file not found → None

---

## Solution

```python
def get_line(filename, line_number):
    """Reads a specific line (1-based) from a file. Returns None on error."""
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
            if line_number < 1 or line_number > len(lines):
                return None
            return lines[line_number - 1].strip()
    except FileNotFoundError:
        return None
```

---

## Tests

| Input | Expected | Result | ✓ |
|-------|--------- -|----------|---|
| `get_line("sample_data.txt", 2)` | "Line 2: Python Files" | Line 2: Python Files | ✅ |
| `get_line("sample_data.txt", 9)` | "Line 9: End of sample" | Line 9: End of sample | ✅ |
| `get_line("sample_data.txt", 0)` | None | None | ✅ |
| `get_line("sample_data.txt", 100)` | None | None | ✅ |
| `get_line("not_found.txt", 1)` | None | None | ✅ |

---

## Notes

- **Concept:** 1-based indexing (user-friendly) vs. 0-based Python lists
- **strip():** Removes leading/trailing whitespace and newlines
- **Validation:** Checking for a valid line number before accessing

