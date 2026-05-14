# 🐍 FIFO Queue - First-In First-Out Data Structure

**Course:** Cyber Security Analyst - Python Basics | **Date:** 10 July 2025

---

## Task

**Objective:** To implement a FIFO (First-In, First-Out) queue data structure

**Requirements:**
- Class: `FIFOQueue`
- `__init__(self)`: Initialises an empty list `items`
- `enqueue(self, item)`: Adds an element to the end
- `dequeue(self)`: Removes and returns the first element
- `size(self)`: Returns the number of elements
- Edge Cases: `dequeue()` on an empty queue → None

---

## Solution

```python
class FIFOQueue:
    """Implements a FIFO (First-In, First-Out) queue."""
    
    def __init__(self):
        """Initialises an empty queue. """
        self.items = []
    
    def enqueue(self, item):
        """Adds an element to the end of the queue."""
        self.items.append(item)
    
    def dequeue(self):
        """Removes and returns the first element. None if the queue is empty."""
        if len(self.items) == 0:
            return None
        return self.items.pop(0)
    
    def size(self):
        """Returns the number of elements in the queue."""
        return len(self.items)
```

---

## Tests

| Input | Expected | Result | ✓ |
|-------|----------|----------|---|
| `q = FIFOQueue(); q.enqueue("apple"); q.enqueue("banana"); q.size()` | 2 | 2 | ✅ |
| `q.dequeue()` | "apple" | apple | ✅ |
| `q.size()` | 1 | 1 | ✅ |
| `q.dequeue()` | "banana" | banana | ✅ |
| `q.size()` | 0 | 0 | ✅ |
| `q.dequeue()` | None | None | ✅ |

---

## Notes

- **Concept:** Queue data structure (FIFO principle)
- **append():** Adds an element to the end of the list
- **pop(0):** Removes and returns the first element
- **Alternative:** `collections.deque` (more efficient for large queues)
- **Performance:** `pop(0)` is O(n), `deque.popleft()` is O(1)

