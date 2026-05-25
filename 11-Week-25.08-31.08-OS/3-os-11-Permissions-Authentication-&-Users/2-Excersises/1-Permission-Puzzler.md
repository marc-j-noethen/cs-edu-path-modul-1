# Permission Puzzler (NTFS Permissions)

**Course:** Cyber Security Analyst – OS Technology | **Date:** 27 August 2025

---

## Task

**Objective:**  
Deduce effective permissions from group memberships and `Allow`/`Deny`.

**Requirements:**

- `ReadSquad` allows read access.
- `WriteBlockers` denies write access.
- Assess effective access for `TempUser01`.

---

## Solution

```text
1. Can `TempUser01` read files?
Yes.
Membership of `ReadSquad` allows `Read & Execute`, `List folder contents` and `Read`.

2. Can `TempUser01` create a new file in `C:\PuzzleFolder`?
No.
This would require write permission. This is explicitly denied via `WriteBlockers`.
A `Deny` overrides the missing or conflicting `Allow` in this case.

3. Can `TempUser01` delete files?
No, not in practice.
No delete permission has been granted, and the existing permissions are limited to reading.
Without `Delete` or `Delete subfolders and files`, deletion is not permitted.
```

**Alternative (compact):**

```text
Read yes, Write no, Delete no.
```

---

## Tests

|Action|Expected|✓|
|---|---|---|
|Read file|allowed|✅|
|Create file|denied|✅|
|Delete file|denied|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|Allow|Grants a permission.|
|Deny|Explicit denial with high priority.|
|Effective permissions|Result of all groups and ACEs combined.|

---

## Rules / Logic

```text
An explicit `Deny` for writing blocks write operations.
Unassigned delete permissions are also denied.
```

---

## Notes

- **Tip:** With NTFS, never look at just one entry, but at the whole picture.
- **Concept:** Effective rights are a bit of a logic puzzle.

---

## Optional: Extensions

- Repeat the same task with inherited rights.
- Check `Effective Access` in the advanced security settings.

