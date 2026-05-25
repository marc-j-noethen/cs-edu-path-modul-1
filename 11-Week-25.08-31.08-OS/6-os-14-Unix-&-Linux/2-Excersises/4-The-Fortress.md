# 🐍 The Fortress (SSH Log Analysis)

**Course:** Cyber Security Analyst - OS Technology | **Date:** 30 August 2025

---

## Task

**Objective:**  
Identify SSH login attempts in Linux logs and, optionally, use a Bash script to check for repeated failed attempts from the same IP address.

**Requirements:**

- Locate failed and successful SSH logins in the auth logs.
- List suitable `grep`/`journalctl` commands.
- Write a Bash script to detect repeated failed attempts from the same IP address.
- Clearly explain the alerting mechanism.

- Output:

    - Example commands for log analysis
    - Complete `detect_ssh_bruteforce.sh`
    - Brief explanation of the detection approach

---

## Solution

```bash
# Relevant search commands
grep "Failed password" /var/log/auth.log
grep "Invalid user" /var/log/auth.log
grep "Accepted password" /var/log/auth.log

# Example of a journald-based view
journalctl -u ssh --since "1 hour ago"

# ~/bin/detect_ssh_bruteforce.sh
#!/usr/bin/env bash
set -euo pipefail

LOG_FILE="/var/log/auth.log"
THRESHOLD=3
WINDOW_LINES=1000

tail -n "$WINDOW_LINES" "$LOG_FILE"               | grep "Failed password"               | awk '{for (i=1; i<=NF; i++) if ($i=="from") print $(i+1)}'               | sort               | uniq -c               | awk -v threshold="$THRESHOLD" '$1 >= threshold {print "ALERT: Potential SSH brute-force from IP: " $2 " - " $1 " failed attempts detected."}'

Explanation:
The script examines the last 1000 lines of the auth log,
filters out failed SSH password attempts,
extracts the source IP following the word `from`,
counts hits per IP
and reports any address exceeding a configurable threshold.
```

**Alternative (compact):**

```text
Many `Failed password` entries from the same IP in quick succession are a very useful early indicator of a brute-force attack.
```

---

## Tests

|Input 1|Input 2|Input 3|Expected|Result|✓|
|---|---|---|---|---|---|
|`grep Failed password`|`auth.log`|`SSH failures`|`findable`|`yes`|✅|
|`same IP repeated`|`tail window`|`count`|`threshold alert`|`yes`|✅|
|`Accepted password`|`auth.log`|`success case`|`findable`|`yes`|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|Auth Log|Central source for SSH authentication events on Debian/Ubuntu systems.|
|Threshold Detection|Multiple identical failed attempts exceeding a threshold trigger an alert.|
|Source IP Extraction|The source address is the most important single indicator for correlation and response.|

---

## Rules / Logic

```text
First identify the log source, then filter for the specific SSH strings.
Not every single failed login attempt is an attack – it is the accumulation that triggers the alarm.
A successful SSH login should be included in the analysis as a control case.
```

---

## Notes

- **Important:** On Ubuntu, `/var/log/auth.log` is usually the direct source; on other distributions, `journalctl` may be the primary source.
- **Tip:** For real-world testing, generate several rapid failed attempts from the same IP address to trigger the script.
- **Observation:** Simple `grep`/`awk` pipelines are often sufficient for a robust first-pass detector.

---

## Optional: Extensions

- Include timestamps in the analysis and use a true time window rather than just a line window.
- Optionally prepare `ufw` or `iptables` block commands upon an alarm (defensive and controlled only).

