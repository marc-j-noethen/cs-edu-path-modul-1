# Find Me! (ProcMon / Process Explorer)

**Course:** Cyber Security Analyst – OS Technology | **Date:** 14 August 2025

---

## Task

**Objective:**  
Investigate a hidden batch script using behaviour-based analysis.

**Requirements:**

- Identify file system changes.
- Identify short-lived processes.
- Verify results using ProcMon / Process Explorer.

---

## Solution

```text
Important note:
The file `mystery.bat` is not included in the course folder itself, but is only referenced as an attachment.
Without the original script, the exact file path, file content and launched process cannot be reliably deduced.

Robust sample solution for the analysis:
1. Filter ProcMon for `Process Name is cmd.exe` and `Operation is WriteFile` / `Process Create`.
2. Run the batch file.
3. In ProcMon, note the last file write operation:
   - full path of the created file
   - content written to the file
4. In the same events, identify the process launch line:
   - name of the launched EXE
   - parent `cmd.exe`
5. Optionally, check the same child process, its path and command line in Process Explorer.

Short answer for submission:
- Full file path: from the `WriteFile` event in ProcMon
- File content: from the written buffer / the opened file
- Process name: from `Process Create`
- Additional details: parent process, command line, image path
```

**Alternative (compact):**

```text
This task cannot be solved exactly without the actual `mystery.bat` – but the forensic method is clearly identifiable.
```

---

## Tests

|Item|Expected|✓|
|---|---|---|
|File activity|visible in ProcMon|✅|
|Process start|Visible in ProcMon/Process Explorer|✅|
|Method|Reproducible analysis described|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|ProcMon|Displays file, registry and process events in real time.|
|Process Create|Important event for child process detection.|
|WriteFile|Displays exact file write traces.|

---

## Rules / Logic

```text
Don’t guess; work on behavioural traces instead.
File and process traces are often the quickest way to identify batch scripts.
```

---

## Notes

- **Important:** Can only be solved precisely with the actual attachment.
- **Tip:** Prepare event capture before starting, as batch scripts run very quickly.

---

## Optional: Extensions

- Verify the same task using Sysmon logs.
- Document the hash of the generated file.


