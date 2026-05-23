# 🐍 Book Class - Simple class with attributes

**Course:** Cyber Security Analyst - Python Basics | **Date:** 10 July 2025

---

## Task

**Objective:** Create a simple class to represent a book with a title and author

**Requirements:**
- Class: `Book`
- `__init__(self, title, author)`: Initialises attributes
- `get_details(self)`: Returns formatted book details
- Return value: String in the format "Title: [title], Author: [author]"
- Edge cases: No specific edge cases

---

## Solution

```python
class Book:
    """Represents a book with a title and author."""
    
    def __init__(self, title, author):
        """Initialises a book with a title and author."""
        self.title = title
        self.author = author
    
    def get_details(self):
        """Returns the book details as a formatted string."""
        return f"Title: {self.title}, Author: {self.author}"
```

---

## Tests

| Input | Expected | Result | ✓ |
|-------|----------|--------|---|
| `Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams").get_details()` | "Title: The Hitchhiker's Guide to the Galaxy, Author: Douglas Adams" | Title: The Hitchhiker's Guide to the Galaxy, Author: Douglas Adams | ✅ |
| `Book("1984", "George Orwell").get_details()` | "Title: 1984, Author: George Orwell" | Title: 1984, Author: George Orwell | ✅ |

---

## Notes

- **Concept:** Basic class structure with `__init__` constructor
- **self:** Reference to the instance itself
- **Attributes:** `self.title` and `self.author` store instance-specific data
- **f-string:** Modern string formatting in Python

