# 🐍 Notepad Nuisance (PowerShell)

**Course:** Cyber Security Analyst – OS Technology | **Date:** 18 August 2025

---

## Task

**Objective:**  
Write a short PowerShell script that checks whether `notepad.exe` is running and responds appropriately.

**Requirements:**

- Use `Get-Process` and `Where-Object`.
- Check for running processes using `ProcessName -eq 'notepad'`.
- If a match is found, output an alert message; otherwise, output a ‘all clear’ message.
- Submit the script as a complete submission.

- Output:

    - Full contents of `check_notepad.ps1`
    - Appropriate response for running / not running
    - Clean use of simple built-in PowerShell tools

---

## Solution

```powershell
$notepadProcess = Get-Process | Where-Object { $_.ProcessName -eq 'notepad' }

if ($null -ne $notepadProcess) {
    Write-Host "ALERT: Notepad is running! Evict immediately!"
}
else {
    Write-Host "All quiet on the Notepad front. Carry on."
}
```

**Alternative (compact):**

```text
If `Get-Process` returns a Notepad hit, an alert is triggered – otherwise, all is quiet.
```

---

## Tests

|Input 1|Input 2|Input 3|Expected|Result|✓|
|---|---|---|---|---|---|
|`Notepad closed`|`script run`|`process query`|`quiet message`|`expected`|✅|
|`Notepad open`|`script run`|`process query`|`alert message`|`expected`|✅|
|`Where-Object`|`ProcessName`|`notepad`|`correct filtering`|`yes`|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|Get-Process|Returns running processes as objects.|
|Where-Object|Filters objects based on properties and conditions.|
|$null Check|An empty result is clearly identified in PowerShell via `$null`.|

---

## Rules / Logic

```text
PowerShell works with objects rather than just text.
The process check must be performed via `ProcessName`, not via the window title.
The `if` branch directly determines the output.
```

---

## Notes

- **Important:** `notepad.exe` appears in `ProcessName` only as `notepad` without `.exe`.
- **Tip:** The script can also be written more concisely using `Get-Process -Name notepad -ErrorAction SilentlyContinue`.
- **Observation:** This task specifically trains the PowerShell object-oriented approach rather than text grepping.

---

## Optional: Extensions

- Addition: Output the number of processes.
- Check multiple target processes via an array.

