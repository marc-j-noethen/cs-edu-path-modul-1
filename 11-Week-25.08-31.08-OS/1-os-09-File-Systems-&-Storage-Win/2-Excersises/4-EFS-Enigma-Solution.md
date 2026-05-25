# 🐍 EFS Enigma (EFS)

**Course:** Cyber Security Analyst - OS Technology | **Date:** 25 August 2025

---

## Task

**Objective:**  
Explain how EFS works on a file- and user-specific basis and why another user cannot read the file.

**Requirements:**

- Identify visual changes to an EFS file.
- Confirm access by the admin who encrypted the file.
- Explain why a second user’s access attempt failed.
- Clearly explain the EFS key principle tied to the user.

- Output:

    - visible change in Explorer
    - result for Admin vs. TempUserEFS
    - clear explanation of EFS

---

## Solution

```text
Sample result:
1. Visual indication:
   In Windows Explorer, an EFS-encrypted file typically appears green.

2. Admin access:
   Yes, the user who encrypted the file can still open and read it as normal.

3. Access by `TempUserEFS`:
   The second user cannot open the file in any meaningful way.
   The typical result is `Access is denied` or a message stating that no permission / no matching key is available.

4. Why?
   EFS does not simply encrypt ‘the file in general’, but ties access to the certificate or security context of the user who encrypted it.
   Without the correct private key, another local user cannot decrypt the same content transparently.
```

**Alternative (compact):**

```text
EFS protects files on a user-specific basis – the same file remains readable to the owner, but is effectively locked for others.
```

---

## Tests

|Input 1|Input 2|Input 3|Expected|Result|✓|
|---|---|---|---|---|---|
|`encrypted file`|`Explorer`|`colour`|`green`|`typical`|✅|
|`admin user`|`open file`|`same account`|`success`|`expected`|✅|
|`TempUserEFS`|`open file`|`other account`|`fail`|`expected`|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|EFS|Windows file encryption at the file system level for individual user contexts.|
|User Certificate|EFS uses key-bound user certificates for transparent access.|
|Transparent Decryption|The owner often does not notice the decryption when opening the file, but other users certainly do.|

---

## Rules / Logic

```text
EFS does not replace file permissions, but supplements them with cryptographic protection.
Without the correct private key, the content remains unreadable.
The Explorer colour is an indication, but not the actual proof of security.
```

---

## Notes

- **Important:** In practice, EFS keys should be backed up; loss of the key risks data loss.
- **Tip:** The task primarily aims to illustrate the principle of ‘same system, different user, no access’.
- **Observation:** It is precisely this difference that makes EFS interesting for endpoint protection.

---

## Optional: Extensions

- Compare EFS with BitLocker conceptually.
- Research the Recovery Agent approach for enterprise environments.

