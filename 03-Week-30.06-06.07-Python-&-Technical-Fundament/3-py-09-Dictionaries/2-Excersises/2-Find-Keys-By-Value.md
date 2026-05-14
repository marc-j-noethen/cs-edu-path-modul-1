# 🐍 Find Keys By Value - Search for keys by value

**Course:** Cyber Security Analyst - Python Basics | **Date:** 2 July 2025

---

## Task

**Objective:** Find all keys in a dictionary that have a specific value.

**Requirements:**
- Function: `find_keys_by_value(data_dict, value_to_find)`
- Return value: Sorted list of keys
- Edge cases: No match → empty list `[]`

---

## Solution

```python
def find_keys_by_value(data_dict, value_to_find):
    """Finds all keys with a specific value, returns a sorted list."""
    keys = []
    for key, value in data_dict.items():
        if value == value_to_find:
            keys.append(key)
    return sorted(keys)
```

**Alternative (List Comprehension):**
```python
def find_keys_by_value(data_dict, value_to_find):
    return sorted([k for k, v in data_dict.items() if v == value_to_find])
```

---

## Tests

| Input | Expected | Result | ✓ |
|-------|--------- -|----------|---|
| `({"apple": 5, "banana": 2, "cherry": 5, "date": 1}, 5)` | `['apple', 'cherry']` | `['apple', 'cherry']` | ✅ |
| `({"apple": 5, "banana": 2, "cherry": 5, "date": 1}, 10)` | `[]` | `[]` | ✅ |
| `({}, 5)` | `[]` | `[]` | ✅ |

---

## Notes

- **Concept:** Dictionary iteration using `.items()`
- **`sorted()`:** Returns a new sorted list
- **List Comprehension:** `[k for k, v in dict.items() if condition]`


