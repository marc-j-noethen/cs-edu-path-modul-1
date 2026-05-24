# CSI cmdlet (PowerShell)

**Course:** Cyber Security Analyst – OS Technology | **Date:** 18 August 2025

---

## Task

**Objective:**  
Find cmdlets using Search and Help.

**Requirements:**

- Identify the cmdlet for date/time.
- Identify the cmdlet for file contents.
- Find the parameter for the first N lines.

---

## Solution

```text
1. Cmdlet for current date and time:
- Get-Date

2. Cmdlet for file contents:
- Get-Content

3. Parameter for the first N lines:
- -TotalCount
  (Alias: -First / -Head according to Help)
```

**Alternative (compact):**

```text
Verb-Noun helps with the search: `Get-Date`, `Get-Content`.
```

---

## Tests

|Question|Answer|✓|
|---|---|---|
|Date/Time|`Get-Date`|✅|
|File content|`Get-Content`|✅|
|First N lines|`-TotalCount`|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|Get-Command|Finds suitable cmdlets.|
|Get-Help|Displays documentation and parameters.|
|Verb-Noun|Naming convention for PowerShell cmdlets.|

---

## Rules / Logic

```text
Search -> Read help -> Select appropriate parameter.
```

---

## Notes

- **Tip:** `Get-Help Get-Content -Parameter TotalCount` is often quicker than reading the full help.
- **Concept:** Good cmdlet names are almost self-explanatory.

---

## Optional: Extensions

- Check `Get-Help Get-Date -Examples`.
- Use `Get-Command *content*` to search for other suitable cmdlets.


