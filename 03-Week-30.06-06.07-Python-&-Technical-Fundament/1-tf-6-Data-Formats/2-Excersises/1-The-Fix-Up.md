# 🖥️ The Fix-Up - Correcting JSON Syntax

**Course:** Cyber Security Analyst - Technical Fundament Basics | **Date:** 30 June 2025

---

## Task

**Objective:** Correct the syntax errors in the JSON snippet to make it valid.

---

## Solution

### Incorrect JSON (Original)

```json
{
  "username": 'alice',
  "userID": 101,
  "isActive": true,
  "interests": [hiking, reading],
  "last_login": 2023-10-26T10:00:00Z
```

### Corrected JSON

```json
{
  "username": "alice",
  "userID": 101,
  "isActive": true,
  "interests": ["hiking", "reading"],
  "last_login": "2023-10-26T10:00:00Z"
}
```

---

## Error analysis

| Line | Error | Correction |
|-------|--------|-----------|
| 2 | `'alice'` (single quotes) | `"alice"` (double quotes) |
| 3 | `"userID"- 101` (hyphen) | `"userID": 101` (colon) |
| 5 | `[hiking, reading,]` (no strings, trailing comma) | `["hiking", "reading"]` |
| 6 | Date without quotation marks | `"2023-10-26T10:00:00Z"` |
| 7 | Missing closing `}` | `}` added |

---

## Notes

- **JSON rule:** Always enclose strings in `"` (double quotes)
- **JSON rule:** Separate keys and values with `:` (colon)
- **JSON rule:** No trailing comma after the last array element
- **Validator:** jsonlint.com or VS Code JSON extension

