# 🖥️ X Files - Matching filenames

**Course:** Cyber Security Analyst - Technical Fundament Basics | **Date:** 11 July 2025

---

## Task

**Objective:** Create a regular expression that matches only image files (.jpg, .png, .gif), capturing the filename and extension separately in capture groups. Temporary files (.tmp) and other file types should be ignored.

**Problem URL:** [https://regexone.com/problem/matching_filenames](https://regexone.com/problem/matching_filenames)

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
- `.bash_profile` - hidden file → skip
- `workspace.doc` - no image → skip
- `img0912.jpg` - image file → match
- `updated_img0912.png` - image file → match
- `documentation.html` - no image → skip
- `favicon.gif` - image file → match
- `img0912.jpg.tmp` - temporary file → skip
- `access.lock` - no image → skip

**Step 2:** Regex construction
```regex
^(\w+)\.(jpg|png|gif)$
```

**Explanation of components:**
- `^` - start of line
- `(\w+)` - **CAPTURE GROUP 1: alphanumeric characters (filename)**
- `\.` - literal dot (escaped)
- `(jpg|png|gif)` - **CAPTURE GROUP 2: one of the three image extensions**
- `$` - end of line

**Step 3:** Validation
Only image files are matched; temporary and other files are skipped.

---

## Results

| Test case | Result | Filename | Extension | Reason |
|-----------|----------|-----------|-----------|------------|
| .bash_profile | ✓ Skip | - | - | Starts with a dot (no filename before `.`) |
| workspace.doc | ✓ Skip | - | - | Incorrect extension |
| img0912.jpg | ✓ Match | img0912 | jpg | Valid image file |
| updated_img0912.png | ✓ Match | updated_img0912 | png | Valid image file |
| documentation.html | ✓ Skip | - | - | Incorrect extension |
| favicon.gif | ✓ Match | favicon | gif | Valid image file |
| img0912.jpg.tmp | ✓ Skip | - | - | Ends with .tmp, not an image extension |
| access.lock | ✓ Skip | - | - | Incorrect extension |

**Status:** ✓ Solution is correct!

---

## Notes

- **Learned:** 
  - `\.` matches a literal dot (not any character)
  - `(jpg|png|gif)` uses alternation (`|`) for multiple options
  - The `$` anchor is crucial for excluding `.tmp` files
  - `\w+` matches alphanumeric characters and underscores

- **Tip:** 
  - End-of-line anchor (`$`) prevents matching of files with additional extensions
  - For hidden files (starting with `.`), the filename is missing before the dot
