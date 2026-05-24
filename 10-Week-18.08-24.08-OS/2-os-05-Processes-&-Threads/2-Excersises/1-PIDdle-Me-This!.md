# PIDdle Me This! (Processes)

**Course:** Cyber Security Analyst – OS Technology | **Date:** 19 August 2025

---

## Task

**Objective:**  
Compare PIDs across multiple tools and understand the value of more detailed process information.

**Requirements:**

- Locate Notepad and PowerShell in Task Manager.
- Verify the Notepad PID using `Get-Process`.
- Explain the additional details from Process Explorer.

---

## Solution

```text
Sample answer:
- The PID of `notepad.exe` in Task Manager and in `Get-Process notepad` must match.
- The PID of PowerShell is session-dependent and is also visible in Task Manager.

Additional information that Process Explorer displays much more clearly:
- Full image path: shows the actual path from which the EXE was loaded.
- Command line: shows start parameters and any potentially malicious calls.
- Further possible details: Parent Process, DLLs, Handles, Signature, User Context.

Why is this important?
A process name alone can be misleading. An attacker might name a file `notepad.exe`, for example,
but the full path or a suspicious command line will reveal that it does not originate from `C:\Windows\System32\`.
```

**Alternative (compact):**

```text
The name is just the surface – the path and command line reveal the truth.
```

---

## Tests

|Item|Expected|✓|
|---|---|---|
|PID match|Task Manager and `Get-Process` match|✅|
|Level of detail|Process Explorer shows more context|✅|
|Security benefit|Path/command line help with suspicion|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|PID|Unique process ID at runtime.|
|Image Path|Full location of the EXE.|
|Command Line|Shows how the process was started.|

---

## Rules / Logic

```text
Same PID = same process.
More context = better forensic assessment.
```

---

## Notes

- **Important:** Exact PIDs are always runtime-dependent.
- **Tip:** In case of doubt, check the path, parent and command line first.

---

## Optional: Extensions

- View threads and open handles as well.
- Check the signature status of the process.

