# Run Spot Run (Run Keys)

**Course:** Cyber Security Analyst – OS Technology | **Date:** 26 August 2025

---

## Task

**Objective:**  
Read autostart run keys and identify suspicious persistence.

**Requirements:**

- Examine HKLM-Run and HKCU-Run.
- Note down programme names.
- Evaluate the `sysupdater.exe` scenario.

---

## Solution

```text
HKLM\Software\Microsoft\Windows\CurrentVersion\Run
Programme names found on the current system:
- SecurityHealth
- RtkAudUService

HKCU\Software\Microsoft\Windows\CurrentVersion\Run
Program names found on the current system:
- OneDriveSetup

Why is `sysupdater.exe` located at `C:\Users\Public\Downloads\sysupdater.exe` suspicious?
- The name sounds generic and may simply be masquerading as legitimate update software.
- The location `Public\Downloads` is unusual for permanent system software and easily exploitable.
- An HKLM Run key ensures persistence on every login with a wide scope.

Immediate concern as an analyst:
Possible malware persistence or unwanted autostart code that establishes itself via an easily writable path.
```

**Alternative (compact):**

```text
Run keys are useful for software – and just as attractive to malware.
```

---

## Tests

|Item|Expected|✓|
|---|---|---|
|HKLM entries|found|✅|
|HKCU entries|found|✅|
|Suspect rating|plausibly justified|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|HKLM Run|Autostart for the system / all users.|
|HKCU Run|Autostart for the current user only.|
|Persistence|Code restarts after a reboot or login.|

---

## Rules / Logic

```text
Suspicious names + unusual path + autostart = high interest for IR.
```

---

## Notes

- **Tip:** Always evaluate the path and publisher together.
- **Concept:** An autostart entry alone proves nothing, but is a strong indicator.

---

## Optional: Extensions

- Compare the same entries with Autoruns.
- Check the digital signatures of the referenced files.


