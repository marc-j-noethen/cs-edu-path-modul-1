# 🐍 The Secret in the Dump (Memory Analysis)

**Course:** Cyber Security Analyst - OS Technology | **Date:** 21 August 2025

---

## Task

**Objective:**  
Use ProcDump to generate a process memory dump and use `strings.exe` to find a string that exists only in RAM.

**Requirements:**

- Create a unique, unsaved secret phrase in Notepad.
- Take a full dump of the Notepad process using `procdump -ma`.
- Use `strings.exe` to identify the string in the dump.
- Explain the forensic value of this procedure.

- Output:

    - chosen secret phrase
    - correct dump and strings commands
    - brief forensic analysis

---

## Solution

```text
Passphrase used:
QuantumLeapPineapple77

Example procedure:
1. Open Notepad, type in the phrase, deliberately do not save the file.
2. Determine the PID of `notepad.exe` in Task Manager.
3. Generated a dump:
   C:\Tools\procdump64.exe -ma <NOTEPAD_PID> C:\Tools\notepad_full.dmp
4. Extracted strings:
   C:\Tools\strings.exe C:\Tools\notepad_full.dmp > C:\Tools\strings_output.txt
5. Searched for `QuantumLeapPineapple77` in `strings_output.txt` and found the phrase.

Reflection:
- Yes, the phrase was found in the memory dump.
- This shows that sensitive data can remain in a process’s memory even though it was never saved to disk.
- In cybersecurity, this is valuable for incident response, malware analysis and credential hunting, e.g. to extract configuration fragments, URLs, tokens or plaintext data from running processes.

Note:
PID, filenames and screenshots are run-dependent; the command sequence and the analysis principle are the technically essential parts.
```

**Alternative (compact):**

```text
Unsaved text may still be present in process memory – this is precisely what makes memory dumps so valuable.
```

---

## Tests

|Input 1|Input 2|Input 3|Expected|Result|✓|
|---|---|---|---|---|---|
|`Notepad RAM`|`secret phrase`|`unsaved`|`found in the dump`|`expected`|✅|
|`procdump -ma`|`full dump`|`notepad`|`created`|`expected`|✅|
|`strings`|`output file`|`search`|`phrase found`|`expected`|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|Full Memory Dump|Image of a process’s virtual memory for analysis and debugging.|
|Strings Extraction|Search for printable sequences that provide clues about content or behaviour.|
|Volatile Evidence|Data in RAM is volatile and can be lost without a memory dump.|

---

## Rules / Logic

```text
Unsaved does not mean invisible – RAM can still retain content.
A full dump is more reliable for string searches than a minimal dump.
Always work with harmless demo data, not with real secrets.
```

---

## Notes

- **Important:** `-ma` stands for a more comprehensive memory dump type and is the appropriate switch for this task.
- **Tip:** Almost always redirect the output of `strings.exe` to a file, not just to the console.
- **Observation:** It is precisely this exercise that highlights the difference between disk artefacts and memory artefacts.

---

## Optional: Extensions

- Additionally, search the dump for URLs, file paths or module names.
- Compare how other editors or browsers store the same plain text in RAM.

