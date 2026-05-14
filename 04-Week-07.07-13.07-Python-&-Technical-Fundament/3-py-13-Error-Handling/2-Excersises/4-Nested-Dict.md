# 🐍 Get Value from Nested Dictionary

**Course:** Cyber Security Analyst - Python Basics | **Date:** 09 July 2025

---

## Task

**Objective:** Function for securely accessing values in nested dictionaries

**Requirements:**
- Function: `get_value_from_nested_dict(data_dict, keys)`
- Parameters: `data_dict` (dictionary), `keys` (list of keys)
- Return value: Value (on success), "Key not found: {key}" (KeyError), "Invalid path: Not a dictionary at key {key}" (TypeError)
- Behaviour: Sequential access through nested dictionaries
- Edge cases: Missing key, access to non-dictionary value

---

## Solution

```python
def get_value_from_nested_dict(data_dict, keys):
    """Safely accesses nested dictionary values."""
    current = data_dict
    
    for key in keys:
        try:
            # Check if current is a dictionary
            if not isinstance(current, dict):
                return f"Invalid path: Not a dictionary at key {key}"
            current = current[key]
        except KeyError:
            return f"Key not found: {repr(key)}"
    
    return current
```

---

## Tests

| Input | Expected | Result | ✓ |
|-------|----------|----------|---|
| `get_value_from_nested_dict({'a': {'b': {'c': 100}}}, ['a', 'b', 'c'])` | 100 | 100 | ✅ |
| `get_value_from_nested_dict({'a': {'b': {'c': 100}}}, ['a', 'x', 'c'])` | "Key not found: 'x'" | Key not found: 'x' | ✅ |
| `get_value_from_nested_dict({'a': 1}, ['a', 'b'])` | "Invalid path: Not a dictionary" | Invalid path: Not a dictionary at key b | ✅ |
| `get_value_from_nested_dict({'x': {'y': 'value'}}, ['x', 'y'])` | "value" | value | ✅ |

---

## Notes

- **Concept:** KeyError and TypeError handling for dictionary access
- **isinstance():** Checks whether an object is of type dict before accessing a key
- **repr(key):** Returns a string representation with quotation marks (e.g. 'x')
- **KeyError:** Occurs if the key does not exist in the dictionary
- **Sequential Access:** Iterates through the list of keys and accesses deeper levels step by step
- **Alternative:** Recursive implementation possible
