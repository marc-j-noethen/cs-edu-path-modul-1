# Key Keeper's Quest (Encryption)

**Course:** Cyber Security Analyst - Technical Fundamentals | **Date:** 15 July 2025

---

## Task

**Objective:**  
Understand AES encryption and decryption using a passphrase, and see why the key is crucial.

**Requirements:**

- Decrypt the given ciphertext using the correct passphrase.
- Encrypt your own text.
- Decrypt using the wrong key and observe the behaviour.
- Briefly explain the result.

---

## Solution

```text
Part 1 - Decrypted plaintext:
This is a secret message.

Part 2 - Example ciphertext:
U2FsdGVkX18xMjM0NTY3OG8JPKDthjOgXdiJqDxx2w0cwB9IlJhK/KPO5sTCu4XZ

Part 3 - Incorrect key:
Using the incorrect key does not produce any meaningful plaintext.
Typically, this results in either unreadable gibberish or a padding/decryption error.
```

**Alternative (compact):**

```text
Correct key -> readable plaintext
Incorrect key -> error or invalid plaintext
```

---

## Tests

|Input 1|Input 2|Input 3|Expected|Result|✓|
|---|---|---|---|---|---|
|Ciphertext from Part 1|`SecretKey123456!`|AES-Decrypt|`This is a secret message.`|correctly decrypted|✅|
|`Encryption is fun and useful!`|`MyCyberKey!1234`|AES-Encrypt|valid ciphertext|ciphertext generated|✅|
|Ciphertext from Part 2|`MyCyberKey@1234`|AES-Decrypt|Error or garbage|no valid plaintext|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|Symmetric encryption|The same secret is used for both encryption and decryption.|
|Passphrase / Key|Without the correct key, the plaintext cannot be meaningfully recovered.|
|Salt / IV|Ensures that the same text does not always produce the same ciphertext.|

---

## Rules / Logic

```text
Correct passphrase + correct algorithm = correct decryption.
Incorrect passphrase = invalid result.
Due to the salt and IV, the ciphertext can be different for each encryption.
```

---

## Notes

- **Concept:** AES protects confidentiality, not automatically integrity.
- **Syntax:** Use an online tool with AES-256-CBC and a passphrase.
- **Order is important:**
    1. Enter ciphertext
    2. Set passphrase
    3. Decrypt or encrypt
- **Edge cases:**
    - A different salt produces different ciphertext.
    - An incorrect mode also results in unusable output.
    - In everyday use, the passphrase and key are not always the same.
- **Tip:** If a tool always generates new ciphertext for the same message, this is normal and usually a good sign.

---

## Optional: Extensions

- Compare AES-GCM with CBC.
- Note the difference between passphrase, key and IV.
- Re-encrypt your own message using a different salt.

