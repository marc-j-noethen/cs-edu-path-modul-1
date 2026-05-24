# Heir Apparent (Parent / Child)

**Course:** Cyber Security Analyst – OS Technology | **Date:** 19 August 2025

---

## Task

**Objective:**  
Understand parent-child relationships and the inheritance of environment variables.

**Requirements:**

- Write a script with your own environment variable.
- Start `notepad.exe` as a child process.
- Verify the variable in the child environment.

---

## Solution

```powershell
# process_launcher.ps1
$env:CYBER_LAB_TOKEN = "ParentValue-42"
Start-Process notepad.exe
Start-Sleep -Seconds 30
```

```text
How does Process Explorer display the relationship?
The child process is displayed indented under its parent process in the tree view.

Was the variable present in `notepad.exe`?
Yes – a child process normally inherits the environment variables of the parent process at start-up,
provided it is launched via that process.
Example value: `CYBER_LAB_TOKEN=ParentValue-42`

Why is this useful?
Legitimate: configuration values, paths, feature flags.
Risk: Secret or sensitive values could also be inadvertently passed on to processes
that have network access or are less trustworthy.
```

**Alternative (compact):**

```text
Children often inherit more context than you might think.
```

---

## Tests

|Item|Expected|✓|
|---|---|---|
|Tree view|PowerShell -> notepad visible|✅|
|Variable|Present in `notepad.exe`|✅|
|Assessment|Benefit and risk identified|✅|

---

## Explanation / Concepts

|Concept|Description|
|Parent Process|Process that starts another.|
|Child Process|Newly started process with inherited context.|
|Environment Inheritance|Inheritance of variables at process start.|

---

## Rules / Logic

```text
Inherited variables are copied at start-up.
Subsequent changes in the parent do not retroactively update the child.
```

---

## Notes

- **Tip:** Set the variable in the parent before `Start-Process`.
- **Concept:** Child processes are functionally useful but sensitive from a security perspective.

---

## Optional: Extensions

- Test with `cmd.exe` or `python.exe` instead of Notepad.
- Start multiple nested child processes.

