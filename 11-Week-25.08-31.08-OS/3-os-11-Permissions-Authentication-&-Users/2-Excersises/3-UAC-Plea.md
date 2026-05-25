# 🐍 UAC Plea (UAC)

**Course:** Cyber Security Analyst - OS Technology | **Date:** 27 August 2025

---

## Task

**Objective:**  
Demonstrate how a PowerShell command using `RunAs` can trigger a UAC escalation and why a normal write attempt to `C:\Program Files` fails.

**Requirements:**

- Provide a command that triggers UAC and creates the file in `C:\Program Files`.
- Explain the behaviour in a non-elevated context.
- Explain the behaviour in an elevated context.
- Describe the practical significance of UAC for scripts.

- Output:

    - Specific PowerShell command
    - Result: standard vs. elevated
    - Brief security analysis

---

## Solution

```text
Command used:
Start-Process powershell.exe -Verb RunAs -ArgumentList "-Command New-Item -Path 'C:\Program Files\testfile.txt' -ItemType File -Force"

Standard PowerShell (non-elevated):
- A direct `New-Item` to `C:\Program Files` would fail with `Access denied`.
- The above `Start-Process ... -Verb RunAs`, however, triggers the UAC prompt because an elevated PowerShell process is deliberately started.

Elevated PowerShell:
- In the PowerShell window started as an administrator,
  `New-Item -Path 'C:\Program Files\testfile.txt' -ItemType File -Force`
  works successfully.

Analysis:
- `C:\Program Files` is protected; standard users are not permitted to write there freely.
- UAC separates standard and administrator tokens and requires a deliberate elevation for privileged actions.
- If a script always requires elevation for simple tasks in user folders, this is often an indication of unnecessarily privileged or poorly designed script logic.
```

**Alternative (compact):**

```text
The protected target path is the key: without elevation, the write attempt fails; with `RunAs`, UAC is explicitly triggered.
```

---

## Tests

|Input 1|Input 2|Input 3|Expected|Result|✓|
|---|---|---|---|---|---|
|`Program Files`|`normal shell`|`New-Item`|`Access denied`|`expected`|✅|
|`RunAs`|`UAC prompt`|`elevated shell`|`prompt appears`|`expected`|✅|
|`elevated shell`|`same file create`|`New-Item`|`success`|`expected`|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|UAC|Protects privileged actions through token separation and deliberate elevation.|
|Protected Path|Directories such as `Program Files` are deliberately restricted for standard contexts.|
|RunAs|PowerShell can specifically start a new process with elevation.|

---

## Rules / Logic

```text
Not every failed admin action automatically triggers a UAC prompt.
A UAC prompt appears when an elevated process is explicitly requested.
Good scripts only request elevation when the task genuinely requires it.
```

---

## Notes

- **Important:** A plain `New-Item` in a standard shell does not magically prompt for UAC, but simply fails.
- **Tip:** The task is best solved by deliberately using `-Verb RunAs`.
- **Observation:** UAC is not a bug, but the security boundary between standard and admin contexts.

---

## Optional: Extensions

- Compare the same behaviour with registry paths under HKLM.
- Rewrite a script so that only the part that genuinely requires privileges needs to run with elevated privileges.


