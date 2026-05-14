# 🖥️ Dial M for Match – Matching phone numbers

**Course:** Cyber Security Analyst – Technical Foundation Basics | **Date:** 11 July 2025

---

## Task

**Objective:** Create a regular expression that recognises different telephone number formats and captures the area code in a capture group.

**Problem URL:** [https://regexone.com/problem/matching_phone_numbers](https://regexone.com/problem/matching_phone_numbers)

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
- `415-555-1234` - with hyphens
- `650-555-2345` - with hyphens
- `(416)555-3456` - area code in brackets
- `202 555 4567` - with spaces
- `4035555678` - without separators
- `1 416 555 9292` - with country code

**Step 2:** Regex construction
```regex
^1?\s*\(?(\d{3})\)?[\s-]?\d{3}[\s-]?\d{4}$
```

**Explanation of components:* *
- `^` - start of line
- `1?` - optional country code "1"
- `\s*` - zero or more spaces
- `\(?` - optional opening parenthesis
- `(\d{3})` - **CAPTURE GROUP: exactly 3 digits (country code)**
- `\)?` - optional closing parenthesis
- `[\s-]?` - optional space or hyphen
- `\d{3}` - exactly 3 digits (exchange)
- `[\s-]?` - optional space or hyphen
- `\d{4}` - exactly 4 digits (extension number)
- `$` - end of line

**Step 3:** Validation
All test cases are processed correctly and the area code is captured.

---

## Results

| Test Case | Captured Area Code | Format |
|-----------|------------------ -|--------|
| 415-555-1234 | 415 | With hyphens |
| 650-555-2345 | 650 | With hyphens |
| (416)555-3456 | 416 | Area code in brackets |
| 202 555 4567 | 202 | With spaces |
| 4035555678 | 403 | Without separators |
| 1 416 555 9292 | 416 | With country code |

**Status:** ✓ Solution is correct!

---

## Notes

- **Learned:** 
  - `\(` and `\)` match literal brackets (escaped, as `()` are metacharacters)
  - `[\s-]?` allows for flexible separators (space, hyphen or nothing)
  - Capture groups `()` extract specific parts of the match

- **Tip:** Take different formatting styles into account for telephone numbers (brackets, hyphens, spaces)


