# Root of All Trust (Certificates & Signatures)

**Course:** Cyber Security Analyst - Technical Fundamentals | **Date:** 17 July 2025

---

## Task

**Objective:**  
Identify the certificate chain of a genuine TLS site and understand the role of the intermediate certificate.

**Requirements:**

- Note down the certificate chain for `sha256.badssl.com`.
- Document the subject and issuer for each level.
- Explain the role of the intermediate certificate.
- Logically organise the chain of trust.

---

## Solution

```text
Website examined:
https://sha256.badssl.com/

Chain:
1. Leaf / Server Certificate
   Subject: CN=*.badssl.com
   Issuer: CN=R13, O=Let's Encrypt, C=US

2. Intermediate Certificate
   Subject: CN=R13, O=Let's Encrypt, C=US
   Issuer: CN=ISRG Root X1, O=Internet Security Research Group, C=US

3. Root Certificate
   Subject: CN=ISRG Root X1, O=Internet Security Research Group, C=US
   Issuer : CN=ISRG Root X1, O=Internet Security Research Group, C=US
```

**Alternative (compact):**

```text
Leaf -> Intermediate -> Root
*.badssl.com -> R13 -> ISRG Root X1
```

---

## Tests

|Scenario|Expected|Result|✓|
|---|---|---|---|
|Check leaf|Wildcard for badssl.com|`CN=*.badssl.com`|✅|
|Check Intermediate|Let's Encrypt R13|Found|✅|
|Check Root|ISRG Root X1|Found|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|Leaf|The actual server certificate for the hostname.|
|Intermediate|Connects the Leaf and Root so that the Root does not have to sign directly.|
|Root CA|Trust anchor located in the system’s trust store.|

---

## Rules / Logic

```text
Root certificates rarely sign Leaf certificates directly.
Intermediates limit risk and simplify management.
The client trusts the chain if every signature can be verified back to a known root.
```

---

## Notes

- **Concept:** Intermediates protect the root because its keys need to be used less frequently.
- **Syntax:** Read the subject and issuer separately for each certificate.
- **Order is important:**
    1. Identify the server certificate
    2. Trace the issuer
    3. Find the root as the trust anchor
- **Edge cases:**
    - Cross-signing.
    - Multiple intermediates.
    - Local trust store influences the view.
- **Tip:** The chain makes more sense when read from the leaf upwards rather than from the root downwards.

---

## Optional: Extensions

- Explain the difference between a self-signed root and a server-side chain.
- Check further test pages at `badssl.com`.
- Read up on OCSP stapling as an additional topic.

