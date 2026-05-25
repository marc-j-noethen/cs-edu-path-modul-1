# 🐍 The Registered Watchdog (Registry Monitoring)

**Course:** Cyber Security Analyst - OS Technology | **Date:** 26 August 2025

---

## Task

**Objective:**  
Write a Python script that monitors suspicious registry keys for new, removed or modified values by comparing snapshots.

**Requirements:**

- Select security-relevant keys.
- Detect and log changes to values.
- Output the timestamp and type of change.
- Provide a brief explanation of how it works.

- Output:

    - Complete Python script
    - Monitoring for multiple relevant keys
    - Readable console entries when changes occur

---

## Solution

```python
import time
from datetime import datetime
import winreg

WATCH_KEYS = [
    (winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run"),
    (winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\RunOnce"),
]


def snapshot_values(root, subkey):
    result = {}
    try:
        with winreg.OpenKey(root, subkey) as key:
            index = 0
            while True:
                try:
                    name, value, value_type = winreg.EnumValue(key, index)
                    result[name] = (value, value_type)
                    index += 1
                except OSError:
                    break
    except FileNotFoundError:
        pass
    return result


def diff(old, new):
    events = []
    for name in new.keys() - old.keys():
        events.append(("ADDED", name, None, new[name][0]))
    for name in old.keys() - new.keys():
        events.append(("REMOVED", name, old[name][0], None))
    for name in old.keys() & new.keys():
        if old[name] != new[name]:
            events.append(("CHANGED", name, old[name][0], new[name][0]))
    return events


baselines = {(root, subkey): snapshot_values(root, subkey) for root, subkey in WATCH_KEYS}
print("Watching registry keys. Press Ctrl+C to stop.")

while True:
    for root, subkey in WATCH_KEYS:
        current = snapshot_values(root, subkey)
        changes = diff(baselines[(root, subkey)], current)
        for change_type, name, old_value, new_value in changes:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"[{timestamp}] {change_type} in {subkey}: {name} | old={old_value!r} | new={new_value!r}")
        baselines[(root, subkey)] = current
    time.sleep(2)

Explanation:
The script takes a starting snapshot of each target key.
It then compares the current state with the last known state every two seconds
and reports new, removed or modified value entries with a timestamp.
```

**Alternative (compact):**

```text
Polling is entirely sufficient for this task: take a snapshot, compare, log differences.
```

---

## Tests

|Input 1|Input 2|Input 3|Expected|Result|✓|
|---|---|---|---|---|---|
|`Run key`|`new value`|`snapshot diff`|`ADDED`|`expected`|✅|
|`Run key`|`edited value`|`snapshot diff`|`CHANGED`|`expected`|✅|
|`Run key`|`deleted value`|`snapshot diff`|`REMOVED`|`expected`|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|Registry Snapshot|Snapshot of all value names and data for a registry key.|
|Persistence Keys|Keys related to autostart, such as `Run` and `RunOnce`, are of particular interest for security monitoring.|
|Polling|Periodic comparison is often sufficient if no kernel- or API-based real-time hook is required.|

---

## Rules / Logic

```text
Monitoring begins with a known initial state.
Added/Changed/Removed events are particularly relevant to security.
Monitoring should focus specifically on keys of forensic interest.
```

---

## Notes

- **Important:** For this task, a clean snapshot diff is usually more robust and simpler than complex API hooks.
- **Tip:** Other keys of interest include services, shell extensions or startup paths.
- **Observation:** `Run` and `RunOnce` are ideal for initial persistence tests.

---

## Optional: Extensions

- Additionally write logs to a file.
- Extend the key list to include `Policies`, `Services` or `Explorer` artefacts.
