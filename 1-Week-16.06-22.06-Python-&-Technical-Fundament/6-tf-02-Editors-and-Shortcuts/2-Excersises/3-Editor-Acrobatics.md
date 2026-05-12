# 🖥️ Editor Acrobatics (Text Manipulation)

**Course:** Cyber Security Analyst - Technical Foundation Basics | **Date:** 20 June 2025

---

## Task

**Objective:** Perform text transformations in Sublime Text on Windows 11 by using keyboard-driven editor commands.

---

## Solution

### Environment
```text
OS: Windows 11
Editor: Sublime Text
```

---

## Challenge A: Case Closed (UPPERCASE)

### Input text
```text
error: file not found
WARNING: disk space low
Info: user logged in successfully
ERROR: connection timed out
```

### Procedure

```text
1. Ctrl+A
2. Ctrl+Shift+P
3. Type: Convert Case: Upper Case
4. Enter
```

### Result
```text
ERROR: FILE NOT FOUND
WARNING: DISK SPACE LOW
INFO: USER LOGGED IN SUCCESSFULLY
ERROR: CONNECTION TIMED OUT
```

---

## Challenge B: Line Dance (Sort alphabetically)

### Source text
```text
Zulu
Alpha
Charlie
Bravo
Delta
```

### Procedure

```text
1. Ctrl+A
2. Ctrl+Shift+P
3. Type: Sort Lines
4. Enter
```

### Result
```text
Alpha
Bravo
Charlie
Delta
Zulu
```

---

## Challenge C: Column Extraction

### Input text
```text
ID001:UserA:Admin
ID002:UserB:Editor
ID003:UserC:Viewer
ID004:UserD:Admin
```

### Procedure

```text
1. Ctrl+H
2. Alt+R                     -> Enable Regex
3. Find:    ^[^:]+:([^:]+):[^:]+$
4. Replace: $1
5. Replace All
```

### Result
```text
UserA
UserB
UserC
UserD
```

---

## Results Summary

| Challenge | Main Action | Method |
|-----------|-------------|--------|
| A: UPPERCASE | Convert text to uppercase | Command Palette |
| B: Sort | Sort lines alphabetically | Command Palette |
| C: Columns | Extract middle field | Regex Find & Replace |

---

## Notes

- **Learned:** Case conversion, sorting, regex-based extraction.
- **Tip:** `Ctrl+Shift+P` is the safest keyboard-driven fallback when you do not remember an exact dedicated shortcut.
- **Important:** The results above are deterministic for the given inputs and use a Windows-friendly workflow.
