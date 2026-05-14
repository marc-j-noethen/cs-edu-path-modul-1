# 🖥️ UR.*L - Parsing URLs

**Course:** Cyber Security Analyst - Technical Fundament Basics | **Date:** 11 July 2025

---

## Task

**Objective:** Create a regular expression that parses URLs/URIs and extracts the protocol (scheme), hostname and port (optional) into separate capture groups.

**Problem URL:** [https://regexone.com/problem/parsing_and_extracting_data_from_a_url](https://regexone.com/problem/parsing_and_extracting_data_from_a_url)

---

## Solution

### Environment
```
Tool: RegexOne Web Interface
Browser: Chrome/Firefox
Regex Flavor: Standard
```

### Procedure

**Step 1:** Analysis of the URL structure
```
protocol://hostname:port/path
```

**Step 2:** Analysis of the test cases
- `ftp://file_server.com:21/top_secret/life_changing_plans.pdf`
- `https://regexone.com/lesson/introduction#section`
- `file://localhost:4040/zip_file`
- `https://s3cur3-server.com:9999/`
- `market://search/angry%20birds`

**Step 3:** Regex construction
```regex
^(\w+)://([\w\-\.]+):?(\d+)?
```

**Explanation of components:**
- `^` - start of line
- `(\w+)` - **CAPTURE GROUP 1: alphanumeric characters (protocol/scheme)**
- `://` - literal sequence "://"
- `([\w\-\.]+)` - **CAPTURE GROUP 2: alphanumeric characters, hyphens, dots (hostname)**
- `:?` - optional colon
- `(\d+)?` - **CAPTURE GROUP 3: optional digits (port)**

**Step 4:** Validation
All URLs are parsed correctly; protocol, hostname and port are extracted.

---

## Results

| Test case | Protocol | Hostname | Port | Special feature |
|-----------|----------|----------|------|---------- ----|
| `ftp://file_server.com:21/...` | ftp | file_server.com | 21 | With port |
| `https://regexone.com/...` | https | regexone.com | - | Without port |
| `file://localhost:4040/... ` | file | localhost | 4040 | Localhost with port |
| `https://s3cur3-server.com:9999/` | https | s3cur3-server.com | 9999 | Hostname with digits/hyphen |
| `market://search/...` | market | search | - | Custom protocol without port |

**Status:** ✓ Solution is correct!

---

## Notes

- **Learned:** 
  - `\w+` captures alphanumeric protocol names
  - `[\w\-\.]+` handles hostnames with hyphens and dots (e.g. "s3cur3-server.com")
  - `:?(\d+)?` makes both the colon and the port optional
  - The regex stops after the port, ignoring the path and query parameters
  - URIs have the format: `scheme://host:port/path`

- **Tip:** 
  - For production URL parsing: use standard libraries (e.g. `urllib.parse` in Python)
  - Do not escape hyphens in character classes, except at the start or end
  - Mark optional components with `?`
  - The port is always numeric, so use `\d+` instead of `\w+`

