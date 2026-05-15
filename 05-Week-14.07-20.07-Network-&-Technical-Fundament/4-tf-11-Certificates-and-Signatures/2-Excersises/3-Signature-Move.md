# Signature Move (Certificates & Signatures)

**Course:** Cyber Security Analyst - Technical Fundamentals | **Date:** 17 July 2025

---

## Task

**Objective:**  
Digitally sign a file and verify how signatures ensure integrity and authenticity.

**Requirements:**

- Generate an RSA key pair.
- Sign a file.
- Successfully verify the signature against the original file.
- Cause the signature to fail when using a modified file.

---

## Solution

```bash
# generate private key
openssl genrsa -out signature_private_key.pem 2048

# Extract public key
openssl rsa -in signature_private_key.pem -pubout -out signature_public_key.pem

# Sign file
openssl dgst -sha256 -sign signature_private_key.pem -out message.sig my_secret_message.txt

# Validate
openssl dgst -sha256 -verify signature_public_key.pem -signature message.sig my_secret_message.txt

# Create a tampered file
cp my_secret_message.txt tampered_message.txt
echo "changed" >> tampered_message.txt

# verification failure
openssl dgst -sha256 -verify signature_public_key.pem -signature message.sig tampered_message.txt
```

**Alternative (compact):**

```text
Original file -> Verification OK
Tampered file -> Verification Failure
```

---

## Tests

|Input 1|Input 2|Input 3|Expected|Result|✓|
|---|---|---|---|---|---|
|Original file|`message.sig`|Public Key|Verification OK|correct|✅|
|Altered file|`message.sig`|Public Key|Verification Failure|Correct|✅|
|Incorrect Public Key|Signature verification|Original file|Error|As expected|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|Digital signature|Proves that data originates from the owner of the private key and is unaltered.|
|Private/Public Key|Private key signs, public key verifies.|
|Integrity + Authenticity|Signatures verify integrity and sender association, not confidentiality.|

---

## Rules / Logic

```text
Signing is performed using the private key.
Verification is performed using the public key.
Even minor file changes invalidate the signature.
```

---

## Notes

- **Concept:** This is not file encryption, but rather a verification of the file.
- **Syntax:** `openssl dgst -sha256 -sign ...` and `-verify ...`.
- **Order is important:**
    1. Generate key pair
    2. Sign file
    3. Verify signature
- **Edge cases:**
    - Incorrect public key.
    - Different hash algorithm.
    - Manipulation of the file or the signature file.
- **Tip:** A valid signature does not automatically mean that the content is confidential.

---

## Optional: Extensions

- Test other hash algorithms.
- Explain PEM formats.
- Compare signed files with GPG.

