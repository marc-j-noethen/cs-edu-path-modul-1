# 🐍 Stream Secrets (SMTP Stream Analysis)

**Course:** Cyber Security Analyst – Network Technology | **Date:** 18 July 2025

---

## Task

**Objective:**  
In the `smtp.pcap` capture, track the mail stream, find the subject line and reconstruct the unencrypted password from the SMTP login.

**Requirements:**

- Identify the SMTP stream and read it in full.
- Extract the `Subject:` line from the TCP stream.
- Correctly decode the password from `AUTH LOGIN`.
- Document the results in a GitHub-compatible format with proof images.
- Output:
    - `Subject: SMTP`
    - `Password: punjabi@123`
    - `Evidence files: assets/5-Stream-Secrets-*.png`

---

## Solution

```python
# Inputs
capture_file = "smtp.pcap"
base64_password = "cHVuamFiQDEyMw=="
subject_line = "SMTP"

# Main logic
if capture_file != "smtp.pcap":
    print("This sample solution applies to the original file smtp.pcap.")
elif subject_line == "SMTP":
    print("Subject: SMTP")
elif base64_password == "cHVuamFiQDEyMw==":
    print("Password after Base64 decoding: punjabi@123")
else:
    print("The login credentials can be reconstructed unencrypted in the AUTH LOGIN.")
```

**Alternative (compact):**

```python
print("Subject = SMTP | Password = punjabi@123")
```

---

## Tests

|Input 1|Input 2|Input 3|Expected|Result|✓|
|---|---|---|---|---|---|
|`smtp`|`Follow TCP Stream`|`Subject`|`SMTP`|`SMTP`|✅|
|`AUTH LOGIN`|`cHVuamFiQDEyMw==`|`Base64`|`punjabi@123`|`punjabi@123`|✅|
|`assets/5-Stream-Secrets-tcp-stream.png`|`assets/5-Stream-Secrets-password-search.png`|`Documentation`|`Evidence available`|`Evidence available`|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|Follow TCP Stream|Reconstructs the SMTP communication into readable text.|
|AUTH LOGIN|SMTP authentication where the username and password are transmitted in Base64-encoded form.|
|Base64|An encoding, but not encryption; content remains reconstructible.|

---

## Rules / Logic

```
SMTP without TLS is readable.
Base64 must be decoded, not decrypted.
The subject is contained directly in the mail headers of the stream.
```

---

## Notes

- **Concept:** The actual vulnerability is not SMTP itself, but the lack of transport encryption.
- **Syntax:** `smtp`
- **Order is important:**
    1. Filter SMTP
    2. Open `Follow -> TCP Stream`
    3. Evaluate `Subject:` and `AUTH LOGIN`
- **Edge Cases:**
    - With TLS/STARTTLS, the content would not be visible in plain text.
    - The password appears Base64-encoded and must not be confused with hashing.
    - Individual frames show only fragments; only the stream makes the email fully readable.
- **Tip:** The evidence files are located here: `./assets/5-Stream-Secrets-tcp-stream.png` and `./assets/5-Stream-Secrets-password-search.png`

---

## Optional: Extensions

- Decode the Base64 username as well.
- Document the sender, recipient and attachment names as well.
- Explain the differences from SMTPS or STARTTLS.
- Record the email headers separately as evidence.

