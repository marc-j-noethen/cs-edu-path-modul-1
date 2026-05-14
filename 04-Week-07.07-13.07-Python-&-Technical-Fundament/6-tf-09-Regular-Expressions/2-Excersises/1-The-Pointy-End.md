# 🖥️ The Pointy End - Matching decimal numbers

**Course:** Cyber Security Analyst - Technical Foundation Basics | **Date:** 11 July 2025

---

## Task

**Objective:** Create a regular expression that correctly recognises various decimal number formats (positive/negative, with a comma, scientific notation), but does not match alphanumeric strings such as "720p".

**Problem URL:** [https://regexone.com/problem/matching_decimal_numbers](https://regexone.com/problem/matching_decimal_numbers)

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
- `3.14529` - positive decimal number
- `-255.34` - negative decimal number
- `128` - integer
- `1.9e10` - scientific notation
- `123,340.00` - number with thousands separator
- `720p` - should NOT be matched

**Step 2:** Regex construction
```regex
^-?\d+(,\d+)*(\.\d+)?(e\d+)?$
```

**Explanation of components:**
- `^` - start of line
- `-?` - optional minus sign
- `\d+` - one or more digits
- `(,\d+)*` - zero or more comma-separated groups of digits
- `(\.\d+)?` - optional decimal point with decimal places
- `(e\d+)?` - optional exponent
- `$` - end of line

**Step 3:** Validation
All test cases are processed correctly:
- ✓ Numbers are matched
- ✓ "720p" is skipped (due to `$` anchor)

---

## Results

| Test Case | Result | Reason |
|-----------|----------|------------|
| 3.14529 | ✓ Match | Positive decimal number |
| -255.34 | ✓ Match | Negative decimal number |
| 128 | ✓ Match | Integer |
| 1.9e10 | ✓ Match | Scientific notation |
| 123,340.00 | ✓ Match | With thousands separator |
| 720p | ✓ Skip | Does not end with a number (letter 'p') |

**Status:** ✓ Solution is correct!

---

## Notes

- **Learned:** 
  - `\.` matches a literal full stop (not any character like `.`)
  - The `$` anchor is crucial for excluding strings with subsequent letters
  - Optional groups with `?` allow flexibility with different number formats

- **Tip:** Always use the end-of-line anchor (`$`) for number formats to avoid unwanted partial matches

