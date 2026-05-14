# 🐍 Write Lines to File

**Course:** Cyber Security Analyst - Python Basics | **Date:** 08 July 2025

---

## Task

**Objective:** Function to write multiple lines to a new file

**Requirements:**
- Function: `write_lines(filename, lines)`
- Parameters: `filename` (string), `lines` (list of strings)
- Return value: None (creates a file)
- Edge cases: Each line from the list is written to a new line

---

## Solution

```python
def write_lines(filename, lines):
    """Writes a list of strings to a file, each string on a new line."""
    with open(filename, 'w') as f:
        for line in lines:
            f.write(line + '\n')
```

---

## Tests

| Input | Expected | Result | ✓ |
|-------|----------|----------|---|
| `write_lines("output1.txt", ["First line", "Second line", "Third"])` | File with 3 lines | First line<br>Second line<br>Third | ✅ |

---

## Notes

- **Concept:** File writing with `open()` in write mode
- **Alternative:** `f.write('\n'.join(lines) + '\n')` (more compact)
- **Important:** Add a newline (`\n`) manually, as `write()` does not do this automatically


