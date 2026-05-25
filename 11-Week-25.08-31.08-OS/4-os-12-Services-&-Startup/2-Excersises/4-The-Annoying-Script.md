# 🐍 The Annoying Script (Safe Mode)

**Course:** Cyber Security Analyst - OS Technology | **Date:** 28 August 2025

---

## Task

**Objective:**  
Explain why Safe Mode is the correct way to remove a persistent startup entry.

**Requirements:**

- Identify the problem in Normal Mode.
- Identify Safe Mode as the solution and explain why.
- Outline the steps for entering, removing and returning to Normal Mode.
- Name two further useful use cases for Safe Mode.

- Output:

    - Clear Safe Mode strategy
    - Removal method via the Startup folder
    - Justification for why this particular boot mode helps

---

## Solution

```text
1. Why Normal Mode is problematic:
The script restarts with every login and opens disruptive command-line windows.
This makes normal operation so disruptive that deactivation via GUI tools or search is hardly possible anymore.

2. Suitable boot mode:
Safe Mode
Why does this help?
Safe Mode starts Windows with minimal drivers and services
and does not load most user-specific startup applications.
This keeps `PersistentlyAnnoyingScript.bat` out of the way.

3. Entering Safe Mode (one possible method):
- Open `msconfig`
- `Boot` tab
- Enable `Safe boot`
- Restart

4. Removal in Safe Mode:
- Open `shell:startup`
- Delete `PersistentlyAnnoyingScript.bat` from the Startup folder
  or move it to another location

5. Return to Normal Mode:
- Open `msconfig` again
- Disable `Safe boot` again
- Restart

6. Why was this effective?
Safe Mode prevents the disruptive user autostart from sabotaging its own removal.

7. Two further useful scenarios for Safe Mode:
- Driver issues following a faulty installation
- Troubleshooting malware or autorun issues when normal startup becomes unusable
```

**Alternative (compact):**

```text
Safe Mode is not a luxury here, but the method to prevent the troublemaker from starting up in the first place.
```

---

## Tests

|Input 1|Input 2|Input 3|Expected|Result|✓|
|---|---|---|---|---|---|
|`Normal Mode`|`startup script`|`desktop use`|`disruptive`|`expected`|✅|
|`Safe Mode`|`minimal startup`|`script`|`does not run`|`expected`|✅|
|`startup folder cleanup`|`back to normal`|`reboot`|`issue gone`|`expected`|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|Safe Mode|Diagnostic mode with minimal system startup.|
|Startup Folder|User-specific autostart folder for programmes/scripts at login.|
|Troubleshooting Isolation|The source of the error is removed by ensuring that disruptive components are not loaded in the first place.|

---

## Rules / Logic

```text
If the disruptive component prevents its own removal, the boot environment must be simplified.
Startup issues are often much easier to resolve in Safe Mode.
Deactivate Safe Mode again after successful repair.
```

---

## Notes

- **Important:** This task is intentionally an example of 'problem-solving via boot mode', not just via the command line.
- **Tip:** Alternatively, use `Shift + Restart` -> Troubleshoot -> Startup Settings.
- **Observation:** Safe Mode is particularly useful when the normal GUI interface is overloaded or frozen.

---

## Optional: Extensions

- Additionally, explain the difference between Safe Mode and Clean Boot.
- Compare the Startup folder, Run Keys and scheduled tasks as three different persistence locations.

