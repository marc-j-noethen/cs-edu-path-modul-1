# Hide n Seek (Autoruns)

**Course:** Cyber Security Analyst – OS Technology | **Date:** 28 August 2025

---

## Task

**Objective:**  
Assess the security implications of Autoruns categories.

**Requirements:**

- Select a non-Microsoft autostart entry.
- Document the category, publisher and image path.
- Explain the advantages and disadvantages for malware persistence.

---

## Solution

```text
Sample answer:
- Entry: e.g. `OneDrive` or a third-party updater
- Autoruns tab: `Logon`
- Publisher: depending on the entry, e.g. Microsoft Corporation or third-party provider
- Image Path: full path to the referenced EXE

Typical permissions and start time for `Logon`:
- usually user-level
- starts when the user logs in

Advantages and disadvantages from an attacker’s perspective:
Advantages:
- easy to set up
- starts reliably on every login
- often appears less conspicuous than a new service

Disadvantages:
- only runs after user login
- usually has lower privileges than a system service
- easier to detect using tools such as Autoruns or Task Manager

Comparison with `Services`:
- Services can start earlier and with higher privileges,
  but are often also very visible persistence locations for defenders.
```

**Alternative (compact):**

```text
The persistence category determines privileges, camouflage and start time.
```

---

## Tests

|Item|Expected|✓|
|---|---|---|
|Tab identified|Yes|✅|
|Publisher/Path evaluated|Yes|✅|
|Persistence analysis|Advantages and disadvantages identified|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|Autoruns|Collects many persistence locations in a single tool.|
|Logon Item|Starts with the user session.|
|Service|Often starts earlier and with higher privileges.|

---

## Rules / Logic

```text
Persistence is never just `whether`, but also `when` and `with what privileges`.
```

---

## Notes

- **Important:** The specific non-Microsoft entry is system-dependent.
- **Tip:** Always evaluate the path and publisher together.

---

## Optional: Extensions

- Evaluate Scheduled Tasks as an alternative category.
- Cross-reference Autoruns entries against Run keys from the Registry.


