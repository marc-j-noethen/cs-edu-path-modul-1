# 🐍 Check if a callable exists

**Course:** Cyber Security Analyst - Python Basics | **Date:** 7 July 2025

---

## Task

**Objective:** Check whether a module has a callable member (function/class)

**Requirements:**
- Function: `check_callable_exists(module_name_string, callable_name_string)`
- Return value: `True` if the callable exists and does not start with `_`, otherwise `False`
- Edge cases: Module cannot be imported → `False`, member is not callable → `False`

---

## Solution

```python
import importlib

def check_callable_exists(module_name_string, callable_name_string):
    """Checks whether the callable member exists in the module."""
    try:
        module = importlib.import_module(module_name_string)
        
        if not hasattr(module, callable_name_string):
            return False
        
        member = getattr(module, callable_name_string)
        
        if callable_name_string.startswith('_'):
            return False
        
        if callable(member):
            return True
        
        return False
    except ImportError:
        return False
```

---

## Tests

| Input | Expected | Result | ✓ |
|-------|----------|----------|---|
| `check_callable_exists("math", "sqrt")` | `True` | `True` | ✅ |
| `check_callable_exists("datetime", "date")` | `True` | `True` | ✅ |
| `check_callable_exists("math", "pi")` | `False` | `False` | ✅ |
| `check_callable_exists("nonexistent", "func")` | `False` | `False` | ✅ |

---

## Notes

- **Concept:** Dynamic import using `importlib`, checking with `callable()`
- **Alternative:** `__import__()` (less recommended)


