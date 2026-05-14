# 🐍 Rename Files with Word Match

**Course:** Cyber Security Analyst - Python Basics | **Date:** 08 July 2025

---

## Task

**Objective:** Function to rename .txt files that contain a specific word

**Requirements:**
- Function: `rename_files_with_word(word)`
- Parameter: `word` (string)
- Behaviour: Searches for all .txt files in the current directory
- Matching: Whole word (case-insensitive), not part of another word
- Renaming: `file.txt` → `file_FOUND.txt`
- Edge cases: Skip unreadable files, process only regular files

---

## Solution

```python
import os
import re

def rename_files_with_word(word):
    """Renames .txt files that contain the searched word (in full)."""
    # Pattern for whole-word match (case-insensitive)
    pattern = re.compile(r'\b' + re.escape(word) + r'\b', re.IGNORECASE)
    
    for filename in os.listdir():
        # Check if it is a regular .txt file (case-insensitive)
        if not os.path.isfile(filename):
            continue
        if not filename.lower().endswith('.txt'):
            continue
        
        # Attempt to read file and search for word
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read()
                if pattern.search(content):
                    # Create new filename
                    name_without_ext = filename[:-4]
                    new_filename = name_without_ext + '_FOUND.txt'
                    os.rename(filename, new_filename)
        except (OSError, UnicodeDecodeError):
            # Skip unreadable files
            continue
```

---

## Tests

| Input | Expected | Result | ✓ |
|-------|----------|----------|---|
| `rename_files_with_word("scatter")` → `os.listdir()` | `['notes.txt', 'scatter_FOUND.txt']` | ['notes.txt', 'scatter_FOUND.txt'] | ✅ |
| `rename_files_with_word("quick")` → `os.listdir()` | `['notes_FOUND.txt', 'scatter.txt']` | ['notes_FOUND.txt', 'scatter.txt'] | ✅ |

---

## Notes

- **Concept:** Regex for whole-word matching using `\b` (word boundary)
- **re.escape():** Escapes special characters in the search term
- **re.IGNORECASE:** Case-insensitive search
- **Exception Handling:** OSError (file access) and UnicodeDecodeError (not a UTF-8 file)
- **os.path.isfile():** Filters out directories and symbolic links
- **String Slicing:** `filename[:-4]` removes the last 4 characters (.txt)

