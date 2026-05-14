# 🐍 Find Key-Value in File

**Course:** Cyber Security Analyst - Python Basics | **Date:** 08 July 2025

---

## Task

**Objective:** Function to search for and extract an integer value from a key-value file

**Requirements:**
- Function: `find_value(filename, key)`
- Parameters: `filename` (string), `key` (string)
- Format: Lines in the format `key,value` (comma-separated)
- Return value: Integer (first value found) or None
- Edge cases: Key not found, file does not exist, conversion failed → None

---

## Solution

```python
def find_value(filename, key):
    """Searches for a key in a file and returns the corresponding integer value."""
    try:
        with open(filename, 'r') as f:
            for line in f:
                line = line.strip()
                if line.startswith(key + ','):
                    try:
                        value_part = line.split(',', 1)[1]
                        return int(value_part)
                    except (ValueError, IndexError):
                        return None
        return None
    except FileNotFoundError:
        return None
```

---

## Tests

| Input | Expected | Result | ✓ |
|-------|----------|----------|---|
| `find_value("sample_data.txt", "timeout")` | 120 | 120 | ✅ |
| `find_value("sample_data.txt", "max_users")` | 50 | 50 | ✅ |
| `find_value("sample_data.txt", "not_found")` | None | None | ✅ |
| `find_value("not_found.txt", "key")` | None | None | ✅ |

---

## Notes

- **Concept:** String parsing with `startswith()` and `split()`
- **split(',', 1):** Splits only at the first comma (if the value contains further commas)
- **Nested try/except:** Handles both FileNotFoundError and ValueError/IndexError
- **First match:** Function stops at the first match

