# 🖥️ Address Book - Matching email addresses

**Course:** Cyber Security Analyst - Technical Fundament Basics | **Date:** 11 July 2025

---

## Task

**Objective:** Create a regular expression that matches email addresses and extracts only the name part (before the @), without the plus sign (+).

**Problem URL:** [https://regexone.com/problem/matching_emails](https://regexone.com/problem/matching_emails)

---

## Solution

### Environment
```
Tool: RegexOne Web Interface
Browser: Chrome/Firefox
Regex Flavor: Standard
```

### Procedure

**Step 1:** Analysis of test cases
- `tom@hogwarts.com` - simple email
- `tom.riddle@hogwarts.com` - name with a full stop
- `tom.riddle+regexone@hogwarts.com` - with plus sign
- `tom@hogwarts.eu.com` - multi-component domain
- `potter@hogwarts.com` - simple email
- `harry@hogwarts.com` - simple email
- `hermione+regexone@hogwarts.com` - with plus sign

**Step 2:** Regex construction
```regex
^([\w.]+)\+?.*@[\w.]+$
```

**Explanation of components:**
- `^` - start of line
- `([\w.]+)` - **CAPTURE GROUP: alphanumeric characters or dots (email name)**
- `\+?` - optional plus sign (start of filtering)
- `.*` - any characters (filter text, not captured)
- `@` - literal @ symbol
- `[\w.]+` - alphanumeric characters or dots (domain)
- `$` - end of line

**Step 3:** Validation
All test cases are processed correctly; only the email name is captured.

---

## Results

| Test Case | Captured Name | Special Feature |
|-----------|---------------|--------------|
| tom@hogwarts.com | tom | Simple name |
| tom.riddle@hogwarts.com | tom.riddle | Name with a dot |
| tom.riddle+regexone@hogwarts.com | tom.riddle | Plus filter excluded |
| tom@hogwarts.eu.com | tom | Multi-domain |
| potter@hogwarts.com | potter | Simple name |
| harry@hogwarts.com | harry | Simple name |
| hermione+regexone@hogwarts.com | hermione | Plus filter excluded |

**Status:** ✓ Solution is correct!

---

## Notes

- **Learned:** 
  - `[\w.]+` matches alphanumeric characters (letters, numbers, underscore) and dots
  - `\+?.*` matches optional plus addressing, but does not capture it in the group
  - `[\w.]+` after `@` handles multi-component domains such as "hogwarts.eu.com"

- **Tip:** 
  - Plus addressing is a useful feature for filtering and tracking
  - `\w` is shorthand for `[a-zA-Z0-9_]`
  - Use standard libraries for production email validation

