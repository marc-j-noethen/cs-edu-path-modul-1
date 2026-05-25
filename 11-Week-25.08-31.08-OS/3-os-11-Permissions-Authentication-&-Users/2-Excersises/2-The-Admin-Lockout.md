# The Admin Lockout (Ownership & ACL Recovery)

**Course:** Cyber Security Analyst – OS Technology | **Date:** 27 August 2025

---

## Task

**Objective:**  
To understand how an administrator regains control despite the `Everyone Deny Full Control` setting.

**Requirements:**

- Describe the locked-out behaviour.
- Specify the steps to regain control.
- Cleanly remove the `Deny` entry.

---

## Solution

```text
1. Typical initial behaviour:
- File cannot be opened
- File cannot be deleted
- Changing permissions fails or is blocked

2. Correct sequence for recovery:
3. Open Properties -> Security -> Advanced
4. Change the file owner to `Administrators` or the current administrator
5. Apply changes and, if necessary, reopen the window
6. Then remove or neutralise the problematic ACE `Everyone - Deny Full Control`
7. Explicitly grant `Full Control` to the administrator or the administrators group
8. Now open, edit or delete the file

Why does this work?
Ownership and permissions are related, but not identical.
By taking ownership, the administrator regains the ability to manage ACLs
in order to remove the blocking `Deny` entry.
```

**Alternative (compact):**

```text
First ownership, then ACL repair.
```

---

## Tests

|Item|Expected|✓|
|---|---|---|
|Initial state|Admin still blocked|✅|
|Ownership change|Control restored|✅|
|Deny removed|File can be deleted|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|Ownership|Determines who is permitted to reset permissions.|
|ACL|List of Allow/Deny entries.|
|Deny|Can effectively lock out even administrators until ownership/ACL is corrected.|

---

## Rules / Logic

```text
No file control without ACL control.
Ownership is often the first lever for recovery.
```

---

## Notes

- **Tip:** Reload the window after changing ownership.
- **Concept:** Administrative rights do not automatically mean that every ACL is immediately ignored.

---

## Optional: Extensions

- Test the same with a folder instead of a file.
- Examine inheritance and explicit ACEs separately.

