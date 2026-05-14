# 🖥️ The Void Trimmer - Trimming whitespace

**Course:** Cyber Security Analyst - Technical Fundament Basics | **Date:** 11 July 2025

---

## Task

**Objective:** Create a regular expression that captures the text content of lines whilst removing (trimming) leading and trailing spaces/tabs.

**Problem URL:** [https://regexone.com/problem/trimming_whitespace](https://regexone.com/problem/trimming_whitespace)

---

## Solution

### Environment
```
Tool: RegexOne Web Interface
Browser: Chrome/Firefox
Regex Flavor: Standard
```

### Procedure

**Step 1:** Analysis of the test cases
- `\t\t\tThe quick brown fox...` - three tabs at the start
- `   jumps over the lazy dog.` - three spaces at the start

**Step 2:** First regex version (simple)
```regex
^\s*(.*)\s*$
```

**Problem:** `.*` is greedy and also matches trailing whitespace.

**Step 3:** Improved regex construction
```regex
^\s*(\S.*\S|\S)\s*$
```

**Alternative (simpler, but less precise):**
```regex
^\s*(.*?)\s*$
```

**Explanation of components (improved version):**
- `^` - start of line
- `\s*` - zero or more whitespace characters (not captured)
- `(\S.*\S|\S)` - **CAPTURE GROUP:**
  - `\S.*\S` - non-whitespace, then any characters, then non-whitespace
  - `|` - OR
  - `\S` - single non-whitespace character
- `\s*` - zero or more whitespace characters (not captured)
- `$` - end of line

**Step 4:** Validation
The text content is captured without leading/trailing whitespace.

---

## Results

| Test Case | Captured Content | Removed Whitespace |
|-----------|------------------|----------------------|
| `\t\t\tThe quick brown fox...` | `The quick brown fox...` | 3 tabs at the start |
| `   jumps over the lazy dog.` | `jumps over the lazy dog.` | 3 spaces at the start |

**Status:** ✓ Solution is correct!

---

## Notes

- **Learned:** 
  - `\s` matches any whitespace character (spaces, tabs, line breaks)
  - `\S` matches any non-whitespace character
  - `.*?` is non-greedy (minimal matching)
  - `\S.*\S` ensures that trailing whitespace is not captured
  - Alternative `|\S` handles single-character strings

- **Tip:** 
  - For true trimming: match from the first to the last non-whitespace character
  - `^\s*` and `\s*$` remove whitespace at the start and end of a line
  - Often easier in practice: use built-in `.trim()` functions

