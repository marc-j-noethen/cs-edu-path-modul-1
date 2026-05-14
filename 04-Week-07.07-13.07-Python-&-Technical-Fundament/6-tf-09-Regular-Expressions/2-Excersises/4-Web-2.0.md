# 🖥️ Web 2.0 - Matching HTML tags

**Course:** Cyber Security Analyst - Technical Fundament Basics | **Date:** 11 July 2025

---

## Task

**Objective:** Create a regular expression that matches HTML tags and captures the tag name in a capture group, including handling attributes and nested tags.

**Problem URL:** [https://regexone.com/problem/matching_html](https://regexone.com/problem/matching_html)

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
- `<a>This is a link</a>` - simple anchor tag
- `<a href='https://regexone.com'>Link</a>` - with attribute
- `<div class='test_style'>Test</div>` - div with class attribute
- `<div>Hello <span>world</span></div>` - nested tags

**Step 2:** Regex construction
```regex
^<(\w+).*?>.*?</\1>$
```

**Explanation of components:**
- `^` - start of line
- `<` - literal opening angle bracket
- `(\w+)` - **CAPTURE GROUP: alphanumeric characters (tag name)**
- `.*? ` - any characters, non-greedy (attributes)
- `>` - literal closing angle bracket
- `.*?` - any characters, non-greedy (content between tags)
- `</` - literal opening closing tag sequence
- `\1` - backreference to the first capture group (same tag name)
- `>` - literal closing angle bracket
- `$` - end of line

**Step 3:** Validation
All test cases are processed correctly; tag names are captured.

---

## Results

| Test Case | Captured Tag | Special Feature |
|-----------|--------------|--------------|
| `<a>This is a link</a>` | a | Simple tag |
| `<a href='https://regexone.com'>Link</a>` | a | With attribute |
| `<div class='test_style'>Test</div>` | div | With class attribute |
| `<div>Hello <span>world</span></div>` | div | Outer tag (nested) |

**Status:** ✓ Solution is correct!

---

## Notes

- **Learned:** 
  - `(\w+)` captures the opening tag name
  - `.*?` is non-greedy and matches minimally (important for nested tags)
  - `\1` is a backreference that ensures the closing tag matches the opening tag
  - Non-greedy `.*?` prevents overly long matching across multiple tags

- **Tip:** 
  - For production-grade HTML parsing, specialised parsers such as Beautiful Soup should be used
  - Regex is suitable for simple editor operations or well-formed HTML
  - Non-greedy quantifiers (`*?`) are essential for nested content


