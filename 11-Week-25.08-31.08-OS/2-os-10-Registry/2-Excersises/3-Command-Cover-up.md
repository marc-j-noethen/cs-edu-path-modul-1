# Command Cover-up (RunMRU)

**Course:** Cyber Security Analyst – OS Technology | **Date:** 26 August 2025

---

## Task

**Objective:**  
To understand how MRU traces can be deleted and what other artefacts remain.

**Requirements:**

- Manipulate `RunMRU`.
- Check visibility in the Run dialogue.
- Name another forensic artefact.

---

## Solution

```text
1. Could the commands disappear from the drop-down list?
Yes.
To do this, the letter values (`a`, `b`, `c` ...) in the key
`HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU`
must normally be deleted and the value `MRUList` removed or adjusted accordingly.

2. Further artefact:
Another very useful artefact is `UserAssist` under
`HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\UserAssist\{GUID}\Count`

Forensic relevance:
`UserAssist` stores records of executed programmes per user context.
Even if `RunMRU` has been deleted, `UserAssist` can still show that a programme was launched.
Other possible artefacts include Prefetch, Amcache or ShimCache.
```

**Alternative (compact):**

```text
Deleting one trace does not mean deleting all traces.
```

---

## Tests

|Item|Expected|✓|
|---|---|---|
|RunMRU values|deleted / adjusted|✅|
|Dropdown|Entries disappear|✅|
|Additional artefact|correctly named|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|RunMRU|List of recently executed `Win+R` commands.|
|UserAssist|User-related execution traces in the registry.|
|Artifact triangulation|Using multiple sources for the same action.|

---

## Rules / Logic

```text
A single artifact is rarely the whole truth.
Forensics relies on multiple, overlapping traces.
```

---

## Notes

- **Tip:** Always consider Prefetch and Amcache as well.
- **Concept:** Attackers usually only delete the most obvious artefacts.

---

## Optional: Extensions

- Compare Prefetch for `notepad.exe` or `calc.exe`.
- Also examine `RecentApps` or Jump Lists.


