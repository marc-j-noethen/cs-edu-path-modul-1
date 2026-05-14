# 🖥️ Log 'Dis - Parsing log files

**Course:** Cyber Security Analyst - Technical Foundation Basics | **Date:** 11 July 2025

---

## Task

**Objective:** Create a regular expression that extracts method names, file names and line numbers from Android adb stack traces.

**Problem URL:** [https://regexone.com/problem/extracting_log_data](https://regexone.com/problem/extracting_log_data)

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
- `W/dalvikvm( 1553): threadid=1: uncaught exception` → skip
- `E/( 1553): FATAL EXCEPTION: main` → skip
- `E/( 1553): java.lang.StringIndexOutOfBoundsException` → skip
- `E/( 1553):   at widget.List.makeView(ListView.java:1727)` → capture
- `E/( 1553):   at widget.List.fillDown(ListView.java:652)` → capture
- `E/( 1553):   at widget.List.fillFrom(ListView.java:709)` → capture

**Format:** `at package.class.methodname(filename:linenumber)`

**Step 2:** Regex construction
```regex
^\w/.*at\s+[\w.]+\.(\w+)\((\w+\.java):(\d+)\)$
```

**Explanation of components:**
- `^` - start of line
- `\w/` - log level (E/, W/, etc.)
- `.*` - any characters (process ID and whitespace)
- `at\s+` - literal "at" followed by whitespace
- `[\w.]+\.` - package and class name (not captured)
- `(\w+)` - **CAPTURE GROUP 1: method name**
- `\(` - literal opening bracket
- `(\w+\.java)` - **CAPTURE GROUP 2: File name**
- `:` - literal colon
- `(\d+)` - **CAPTURE GROUP 3: Line number**
- `\)` - literal closing parenthesis
- `$` - end of line

**Step 3:** Validation
Only relevant stack trace lines are matched and the three pieces of information extracted.

---

## Results

| Test case | Result | Method | Filename | Line |
|-----------|----------|--------|----------|------|
| `W/dalvikvm( 1553): threadid=1: uncaught exception` | ✓ Skip | - | - | - |
| `E/( 1553): FATAL EXCEPTION: main` | ✓ Skip | - | - | - |
| `E/( 1553): java.lang.StringIndexOutOfBoundsException` | ✓ Skip | - | - | - |
| `E/( 1553):   at widget.List.makeView(ListView.java:1727)` | ✓ Match | makeView | ListView.java | 1727 |
| `E/( 1553):   at widget.List.fillDown(ListView.java:652)` | ✓ Match | fillDown | ListView.java | 652 |
| `E/( 1553):   at widget.List.fillFrom(ListView.java:709)` | ✓ Match | fillFrom | ListView.java | 709 |

**Status:** ✓ Solution is correct!

---

## Notes

- **Learned:** 
  - `[\w.]+\.` matches package/class path (e.g. "widget.List.")
  - `\(` and `\)` match literal parentheses (escaped)
  - `\w+\.java` specifically matches Java filenames
  - `\d+` captures numeric line numbers
  - Lines without "at" and stack trace format are not matched

- **Tip:** 
  - When parsing logs: identify the exact format of the relevant lines
  - Use multiple capture groups for structured data extraction
  - Match package/class paths with `[\w.]+`

