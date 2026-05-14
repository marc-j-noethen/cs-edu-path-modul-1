# 🐍 Count Word Frequency - Counting word frequency

**Course:** Cyber Security Analyst - Python Basics | **Date:** 2 July 2025

---

## Task

**Objective:** Count how many times each word appears in a text (case-insensitive).

**Requirements:**
- Function: `count_word_frequency(text)`
- Return value: Dictionary `{word: count}`
- Edge cases: Ignore case

---

## Solution

```python
def count_word_frequency(text):
    """Counts word frequencies in a text (case-insensitive)."""
    frequency = {}
    words = text.lower().split()
    
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    
    return frequency
```

**Alternative (shorter):**
```python
def count_word_frequency(text):
    frequency = {}
    for word in text.lower().split():
        frequency[word] = frequency.get(word, 0) + 1
    return frequency
```

---

## Tests

| Input | Expected | Result | ✓ |
|-------|----------|----------|---|
| `"This is a test sentence this test is simple"` | `{'this': 2, 'is': 2, 'a': 1, 'test': 2, 'sentence': 1, 'simple': 1}` | ✓ | ✅ |
| `""` | `{}` | `{}` | ✅ |
| `"Hello"` | `{'hello': 1}` | `{'hello': 1}` | ✅ |

---

## Notes

- **Concept:** Dictionary as a counter, `str.lower()`, `str.split()`
- **`.get(key, default)`:** Returns `default` if the key does not exist
- **Alternative:** `collections.Counter(text.lower().split())`

