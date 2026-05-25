# 🐍 Rogue Runner (Service Forensics)

**Course:** Cyber Security Analyst - OS Technology | **Date:** 28 August 2025

---

## Task

**Objective:**  
Analyse a suspiciously configured Windows service persistence mechanism and remove it thoroughly.

**Requirements:**

- Technically evaluate `sc.exe qc` and `sc.exe query`.
- Assess the path, startup account, recovery behaviour and file artefacts.
- Formulate a secure removal sequence.
- Identify other possible persistence locations.

- Output:

    - Analysis of `SysUtilsSvc`
    - Clean removal sequence
    - Further persistence clues for emergency situations

---

## Solution

```text
Analysis of `sc.exe qc SysUtilsSvc`:
- `BINARY_PATH_NAME`: C:\ProgramData\SysUtils\SysUtils.exe
  This is suspicious because legitimate services are typically located under `C:\Windows\System32\...` or under a known vendor path.
- `SERVICE_START_NAME`: LocalSystem
  This grants the service very high privileges.
- `DISPLAY_NAME`: System Utility
  Sounds deliberately generic and designed to inspire trust.

Analysis of `sc.exe query SysUtilsSvc`:
- Depending on the timing, the service is often `RUNNING`, `START_PENDING`, `STOPPED` or changes state due to failed starts.
- As `SysUtils.exe` is empty or invalid, an immediate crash or error 193 (invalid Win32 programme) is plausible.
- Due to configured recovery/failure actions, the SCM attempts to restart the service.

Event Viewer:
Typical events would be 7000, 7009, 7031 or 7034.
They indicate that although the service starts or is supposed to start, it is not running properly and crashes again.

Why is this high-risk?
Autostart + LocalSystem + suspicious path + generic name + restart mechanism together constitute a strong persistence/abuse profile,
even if the current payload is empty or defective.

Robust removal:
1. sc.exe stop SysUtilsSvc
2. sc.exe failure SysUtilsSvc reset= 0 actions= ""
3. sc.exe config SysUtilsSvc start= disabled
4. sc.exe delete SysUtilsSvc
5. Check that no processes are still referencing `SysUtils.exe`
6. Delete file and directory:
   - C:\ProgramData\SysUtils\SysUtils.exe
   - C:\ProgramData\SysUtils\
7. Verification:
   - `sc.exe query SysUtilsSvc` -> Service no longer exists
   - Path no longer exists
   - Event Viewer / Services.msc confirms removal

Further persistence locations for a thorough investigation:
- Scheduled Tasks
- Run / RunOnce
- Startup folder
- WMI Event Consumers
- Browser / Explorer Extensions
```

**Alternative (compact):**

```text
The danger lies not only in the file’s content, but in the entire service configuration surrounding it.
```

---

## Tests

|Input 1|Input 2|Input 3|Expected|Result|✓|
|---|---|---|---|---|---|
|`ProgramData path`|`LocalSystem`|`auto start`|`red flags`|`yes`|✅|
|`failure actions`|`restart attempts`|`empty exe`|`service unstable`|`yes`|✅|
|`stop/disable/delete`|`file cleanup`|`verify`|`removed`|`yes`|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|Service Persistence|Windows services are a long-lived, privileged persistence mechanism.|
|Failure Actions|The SCM can automatically restart failed services.|
|Security Risk|Even without active malware, such a configuration poses a security risk.|

---

## Rules / Logic

```text
First neutralise the restart, then disable the service, then delete it.
Evaluate not only the service name, but also the path, account and recovery properties.
Removal is only verified once the service object and files are actually gone.
```

---

## Notes

- **Important:** An empty or defective payload does not mean it is harmless – the persistence structure remains relevant regardless.
- **Tip:** Use `services.msc` and `sc.exe` together; the GUI and CLI complement each other well.
- **Observation:** `ProgramData` plus a generic display name is a very typical camouflage approach.

---

## Optional: Extensions

- Additional: Document the hash, signature and PE metadata of `SysUtils.exe` if a genuine payload is present.
- Compare the same scenario using a Scheduled Task instead of a Service.

