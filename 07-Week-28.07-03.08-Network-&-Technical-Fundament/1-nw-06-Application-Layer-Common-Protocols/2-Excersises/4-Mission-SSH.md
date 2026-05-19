# Mission SSH (SSH)

**Course:** Cyber Security Analyst – Network Technology | **Date:** 28 July 2025

---

## Task

**Objective:**  
Understand SSH algorithm negotiation and observe the effect of an outdated KEX algorithm.

**Requirements:**

- Analyse a normal connection to `test.rebex.net`.
- Force a second connection using only `diffie-hellman-group1-sha1`.
- Explain why it succeeded or failed.

---

## Solution

```text
Did the modified connection work?
Usually not.

Why?
The client then only offers `diffie-hellman-group1-sha1`.
If the server no longer accepts this old KEX algorithm, there is no common subset.
Without a common key exchange, the SSH handshake cannot be completed.

What does this tell us about SSH?
SSH is a negotiation protocol. Both sides must agree on compatible and secure algorithms.

Why is rejecting old algorithms important?
Old methods are cryptographically weak or obsolete.
Rejecting them reduces the risk of downgrade attacks and insecure connections.
```

**Alternative (compact):**

```text
No common KEX method -> no SSH connection.
```

---

## Tests

|Item|Expected|✓|
|---|---|---|
|Standard connection|Handshake successful|✅|
|Forced legacy algorithm|usually error/abort|✅|
|Security assessment|legacy KEX methods are deliberately rejected|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|KEX|Key Exchange selects the key exchange.|
|Negotiation|Client and server compare lists.|
|Hardening|Insecure legacy methods are disabled.|

---

## Rules / Logic

```text
SSH requires a common set of algorithms.
No match -> connection error.
Secure defaults are more important than backwards compatibility.
```

---

## Notes

- **Tip:** In Wireshark, `KEXINIT` packets are the key to this task.
- **Concept:** Security gains are often achieved by deliberately not supporting old technology.

---

## Optional: Extensions

- Also restrict `Ciphers` or `HostKeyAlgorithms` specifically.
- Examine SSH client defaults with `ssh -Q`.

