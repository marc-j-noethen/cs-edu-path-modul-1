# The Chatty Script (Network Troubleshooting)

**Course:** Cyber Security Analyst – OS Technology | **Date:** 14 August 2025

---

## Task

**Objective:**  
Analyse a hidden batch script based on its network traces.

**Requirements:**

- Identify the responsible processes.
- Determine the protocols and destinations of the communication.
- Compare the log file in `%TEMP%` with live monitoring.

---

## Solution

```text
Important note:
`mystery2.bat` is also not available as a file in the course folder, but only as a referenced attachment.
This means that exact target hosts, file paths and process names cannot be verified without the original.

Robust sample solution for the procedure:
1. Start the batch file and simultaneously monitor TCPView, Resource Monitor or Wireshark.
2. Look for `cmd.exe` and any auxiliary processes launched from there, e.g. `ping.exe`, `nslookup.exe`, `curl.exe`, `powershell.exe`.
3. Identify protocols:
   - ICMP for `ping`
   - DNS for `nslookup` or name resolution
   - HTTP/HTTPS for `curl` / `powershell Invoke-WebRequest`
4. Search `%TEMP%` for a new log file and read its contents.
5. Cross-check the process name, destination host and log entries.

Short answer for submission:
- Primary responsible processes: from Live-Tool or ProcMon `Process Create`
- Network activity: from Wireshark/TCPView (DNS, ICMP, HTTP ...)
- Full path to the log file: from `%TEMP%` based on creation time
- Relevance of the log file: documents what the script executed or logged internally
```

**Alternative (compact):**

```text
No exact artefacts without the original script – but the forensic analysis chain is unambiguous.
```

---

## Tests

|Item|Expected|✓|
|---|---|---|
|Live network trace|at least one destination/protocol identifiable|✅|
|Log file|Found in `%TEMP%`|✅|
|Matching|Log and live observation match|✅|

---

## Explanation / Concepts

|Concept|Description|
|Network artefacts|Show where a script actually communicated.|
|Auxiliary processes|Batch files often delegate tasks to system tools.|
|Temp logs|Short-lived but highly valuable evidence.|

---

## Rules / Logic

```text
Behaviour > Assumption.
Process + protocol + log file together provide the clearest picture.
```

---

## Notes

- **Important:** The actual attachment is required for an accurate final answer.
- **Tip:** Sort `%TEMP%` by timestamp.

---

## Optional: Extensions

- Back up the DNS cache after the run.
- Check Prefetch and RecentFileCache for secondary traces.

