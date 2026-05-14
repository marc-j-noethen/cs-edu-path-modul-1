# 🐍 Invert Dictionary - Reverse a dictionary

**Course:** Cyber Security Analyst - Python Basics | **Date:** 02 July 2025

---

## Task

**Objective:** Reverse a dictionary: values become keys, and keys become lists of values.

**Requirements:**
- Function: `invert_dictionary(d)`
- Return value: New dictionary `{old_value: [old_keys]}`
- Edge cases: Skip mutable values (lists, dictionaries)

---

## Solution

```python
def is_hashable(obj):
    """Checks whether an object is hashable (immutable)."""
    try:
        hash(obj)
        if isinstance(obj, tuple):
            return all(is_hashable(el) for el in obj)
        return True
    except TypeError:
        return False

def invert_dictionary(d):
    """Inverts the dictionary. Mutable values are skipped."""
    inverted = {}
    
    for key, value in d.items():
        # Only hashable (immutable) values as new keys
        if not is_hashable(value):
            continue
        
        if value not in inverted:
            inverted[value] = []
        inverted[value].append(key)
    
    return inverted
```

**Alternative (using .setdefault()):**
```python
def invert_dictionary(d):
    inverted = {}
    for key, value in d.items():
        if is_hashable(value):
            inverted.setdefault(value, []).append(key)
    return inverted
```

---

## Tests

| Input | Expected | ✓ |
|----- --|----------|---|
| `{"a": 1, "b": 2, "c": 1, "d": [3,4], "e": 2}` | `{1: ['a', 'c'], 2: ['b', 'e']}` | ✅ |
| `{}` | `{}` | ✅ |
| `{"x": (1, 2)}` | `{(1, 2): ['x']}` | ✅ |

---

## Notes

- **Hashable:** Strings, integers, floats, booleans, tuples (with hashable elements)
- **Non-hashable:** Lists, Dicts, Sets → cannot be dict keys
- **`hash()`:** Raises `TypeError` for non-hashable objects
- **Multiple keys → same value:** Are collected in a list

