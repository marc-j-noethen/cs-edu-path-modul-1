# 🐍 Analyse File Path

**Course:** Cyber Security Analyst - Python Basics | **Date:** 7 July 2025

---

## Task

**Objective:** Extract the directory, filename and file extension from a file path

**Requirements:**
- Function: `analyze_path(file_path_string)`
- Return value: Dictionary containing 'directory', 'filename', 'extension'
- Edge cases: No directory → '.', No extension → ''

---

## Solution

```python
import os

def analyze_path(file_path_string):
    """Analyses file path and extracts components."""
    directory = os.path.dirname(file_path_string)
    filename = os.path.basename(file_path_string)
    extension = os.path.splitext(file_path_string)[1]
    
    if directory == '':
        directory = '.'
    
    return {
        'directory': directory,
        'filename': filename,
        'extension': extension
    }
```

---

## Tests

| Input | Expected | Result | ✓ |
|-------|----------|----------|---|
| `analyze_path("/home/user/documents/report.txt")` | `{'directory': '/ home/user/documents', 'filename': 'report.txt', 'extension': '.txt'}` | `{'directory': '/home/user/documents', 'filename': 'report.txt', 'extension': '.txt'}` | ✅ |
| `analyze_path("myfile.zip")` | `{'directory': '.', 'filename': 'myfile.zip', 'extension': '.zip'}` | `{'directory': '.', 'filename': 'myfile.zip', 'extension': '.zip'}` | ✅ |
| `analyze_path("noextension")` | `{'directory': '.', 'filename': 'noextension', 'extension': ''}` | `{'directory': '.', 'filename': 'noextension', 'extension': ''}` | ✅ |

---

## Notes

- **Concept:** Use of the `os.path` module for path manipulation
- **Alternative:** `pathlib.Path` (a more modern approach from Python 3.4 onwards)


