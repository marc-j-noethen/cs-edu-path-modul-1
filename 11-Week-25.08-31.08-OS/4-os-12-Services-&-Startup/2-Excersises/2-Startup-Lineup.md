# Startup Lineup (Startup Apps)

**Course:** Cyber Security Analyst – OS Technology | **Date:** 28 August 2025

---

## Task

**Objective:**  
Evaluate startup entries and question their necessity.

**Requirements:**

- Identify non-Microsoft startup items.
- Research one.
- Classify non-Microsoft services in `msconfig`.

---

## Solution

```text
Sample evaluation for a typical non-Microsoft entry such as Dropbox:
- Name: Dropbox
- Publisher: Dropbox, Inc.
- Startup Impact: often Medium or High
- Purpose: File synchronisation, tray app, background synchronisation
- Necessary at system startup?
  Not essential for every VM session.
  Useful for immediate synchronisation, but often dispensable for a learning or test VM.

Regarding `msconfig`:
After hiding all Microsoft services, typically only third-party software services remain,
e.g. audio drivers, VPN software, cloud sync, launchers or updaters.
This list shows how much additional software starts up permanently with the system.
```

**Alternative (compact):**

```text
Not everything that starts automatically is actually necessary.
```

---

## Tests

|Item|Expected|✓|
|---|---|---|
|Non-Microsoft item|identified|✅|
|Purpose researched|briefly explained|✅|
|Necessity assessed|justified|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|Startup Impact|General impact on boot time and load.|
|Autostart|Convenient, but often overused.|
|Third-party services|Increase attack surface and complexity.|

---

## Rules / Logic

```text
Every autostart entry should justify a clear benefit.
```

---

## Notes

- **Important:** Specific startup apps depend on the installed software.
- **Tip:** Use persistent autostarts sparingly in VMs.

---

## Optional: Extensions

- Compare Task Manager and Autoruns directly.
- Measure startup time before and after deactivation.

