# 🐍 Cross-Platform Translator (PowerShell to Bash)

**Course:** Cyber Security Analyst - OS Technology | **Date:** 30 August 2025

---

## Task

**Objective:**  
Convert several typical PowerShell one-liners into usable Bash/Linux equivalents.

**Requirements:**

- Map file searches, process listings, service statuses, listeners and web content.
- Combine Bash tools such as `find`, `awk`, `ps`, `systemctl`, `ss` and `curl` effectively.
- Identify the boundaries between the object-oriented and text-based worlds.
- Make the one-liners ready for immediate use.

- Output:

    - five Bash equivalents
    - brief reflection on objects vs. text streams
    - useful Ubuntu-compatible commands

---

## Solution

```bash
# 1. File System Query
find /var/log -type f -name "*.log" -printf "%p,%s,%TY-%Tm-%Td %TH:%TM:%TS\n" > ~/linux_logs.csv

# 2. Process Information
ps -eo pid,pcpu,comm --sort=-pcpu | awk '$2 > 0.5 {print}' | head -n 4

# 3. Service Status
systemctl show cron --property=Id,Description,ActiveState,UnitFileState

# 4. Network Listeners
python3 -m http.server 8888 >/dev/null 2>&1 &
ss -ltnp | awk 'NR==1 || /LISTEN/ {print}' | sort -k4,4n | head -n 10

# 5. Web Content Check
curl -s http://info.cern.ch/hypertext/WWW/TheProject.html | grep -qi "World Wide Web" && echo true || echo false

Reflection:
PowerShell works natively with objects and properties, whereas Bash mostly works with text streams.
This is why Bash often requires more `awk`/`grep`/`cut` logic, whilst PowerShell offers many properties that can be selected directly.
```

**Alternative (compact):**

```text
PowerShell filters properties, Bash shapes text streams – this is precisely where the biggest difference in translation arises.
```

---

## Tests

|Input 1|Input 2|Input 3|Expected|Result|✓|
|---|---|---|---|---|---|
|`find + printf`|`csv file`|`~/linux_logs.csv`|`created`|`expected`|✅|
|`ps + awk`|`cpu filter`|`top entries`|`works`|`expected`|✅|
|`curl + grep`|`World Wide Web`|`boolean`|`works`|`expected`|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|Object Pipeline|PowerShell passes structured objects between cmdlets.|
|Text Pipeline|Bash pipelines mainly process text and require parsers such as `awk` or `grep`.|
|Command Composition|Linux one-liners rely on small, combinable specialised tools.|

---

## Rules / Logic

```text
In Bash, required columns often need to be explicitly extracted and sorted.
Not every PowerShell property access has an equally convenient Bash equivalent.
With Linux commands, the text form of the output is part of the actual solution logic.
```

---

## Notes

- **Important:** For `OwningProcess` with network listeners, `ss -p` or `lsof` are the closest Linux equivalents.
- **Tip:** With `ps`, `head -n 4` produces the desired format due to the header and 3 processes.
- **Observation:** It is precisely this task that makes the difference between 'object-based' and 'text-based' very tangible.

---

## Optional: Extensions

- Convert the one-liners into small Bash functions.
- Build the same mapping for `Get-ChildItem`, `Select-String` and `Get-WinEvent`.

