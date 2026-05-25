# 🐍 Command Cover-up 2 (Registry via CLI)

**Course:** Cyber Security Analyst - OS Technology | **Date:** 26 August 2025

---

## Task

**Objective:**  
Modify MRU entries in the registry without using `regedit` or GUI editors.

**Requirements:**

- List alternative methods for registry manipulation.
- Remove or modify RunMRU values without a GUI.
- Describe the solution as a CLI/script-based method.
- Briefly mention that other artefacts may still remain.

- Output:

    - at least one working CLI method
    - specific registry commands
    - forensic classification

---

## Solution

```text
Possible methods without `regedit`:
1. `reg.exe`
2. PowerShell (`Get-ItemProperty`, `Set-ItemProperty`, `Remove-ItemProperty`)
3. WMI / script libraries

Practical CLI solution using `reg.exe`:
reg query "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU"
reg delete "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU" /v a /f
reg delete "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU" /v b /f
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU" /v MRUList /t REG_SZ /d "" /f

PowerShell version:
Remove-ItemProperty -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU" -Name a -ErrorAction SilentlyContinue
Remove-ItemProperty -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU" -Name b -ErrorAction SilentlyContinue
Set-ItemProperty -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU" -Name MRUList -Value ""

Conclusion:
Even without a GUI editor, the registry can be fully modified.
However, hiding the RunMRU list does not automatically remove other artefacts such as UserAssist, Prefetch or Amcache.
```

**Alternative (compact):**

```text
No `regedit` does not mean 'no registry access' – `reg.exe` and PowerShell are perfectly sufficient.
```

---

## Tests

|Input 1|Input 2|Input 3|Expected|Result|✓|
|---|---|---|---|---|---|
|`reg query`|`RunMRU`|`list values`|`visible`|`yes`|✅|
|`reg delete`|`value names`|`cleanup`|`works`|`yes`|✅|
|`PowerShell`|`Remove-ItemProperty`|`same result`|`works`|`yes`|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|reg.exe|CLI tool for registry queries and modifications.|
|RunMRU|List of commands recently executed via `Win+R`.|
|Artifact Persistence|A deleted artifact does not mean that all traces have disappeared.|

---

## Rules / Logic

```text
Registry changes do not require a GUI editor.
CLI tools are often even faster and scriptable.
Forensic analysis must always consider multiple artefacts together.
```

---

## Notes

- **Important:** Query first, then specifically change or delete values.
- **Tip:** Export the original state before making changes, e.g. with `reg export`.
- **Observation:** Locked GUI editors in particular are often an indication of alternative administrative methods in exercises.

---

## Optional: Extensions

- Run through the same process for other registry artefacts such as `TypedPaths` or `RecentDocs`.
- Automatically save a before-and-after diff of the values.

