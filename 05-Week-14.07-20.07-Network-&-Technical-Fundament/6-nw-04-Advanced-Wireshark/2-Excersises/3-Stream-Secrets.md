# 🐍 Stream Secrets (Advanced Wireshark)

**Course:** Cyber Security Analyst - Network Technology | **Date:** 19 July 2025

---

## Task

**Objective:**  
Extract the SMTP TCP stream and the authentication data from `smtp.pcap`.

**Requirements:**

- Open `smtp.pcap` and filter for SMTP.
- Trace the TCP stream containing the email content.
- Identify the subject line in the reassembled stream.
- Find the password information in the SMTP login.

- Output:

    - Email subject line
    - User password from the SMTP login
    - Brief note on how both were found

---

## Solution

```text
Result from `smtp.pcap`:
- Subject: SMTP
- Password: punjab@123

How it was found:
1. Set the display filter to `smtp`.
2. Open the SMTP TCP stream via `Follow -> TCP Stream`.
3. The reassembled email text reads:
   Subject: SMTP
4. The Base64 values appear in the AUTH-LOGIN sequence:
   - `VXNlcm5hbWU6` -> `Username:`
   - `UGFzc3dvcmQ6` -> `Password:`
   - `cHVuamFiQDEyMw==` -> `punjab@123`

Additional observation:
The username is also directly visible and decodes to `gurpartap@patriots.in`,
but the task only asked for the password.
```

**Alternative (compact):**

```text
The subject is clearly visible in the SMTP stream; the password is only slightly hidden as Base64 in the AUTH-LOGIN dialogue.
```

---

## Tests

|Input 1|Input 2|Input 3|Expected|Result|✓|
|---|---|---|---|---|---|
|`Filter smtp`|`Follow TCP Stream`|`Mail text`|`Subject visible`|`SMTP`|✅|
|`AUTH LOGIN`|`Base64`|`Password prompt`|`Password decodable`|`punjab@123`|✅|
|`334 Username`|`334 Password`|`Responses`|`Login flow matches`|`correct`|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|TCP Stream Reassembly|Wireshark reassembles the application payload across multiple packets.|
|SMTP AUTH LOGIN|Login procedure in which the username and password are typically transmitted in Base64-encoded form.|
|Base64|An encoding, not encryption – therefore easily decodable.|

---

## Rules / Logic

```text
Unencrypted SMTP reveals email content and login credentials.
Base64 must never be confused with true encryption.
In login flows, always look for challenge/response and encoded payloads.
```

---

## Notes

- **Important:** The password was sought from the packet contents, not from the stream name.
- **Observation:** The email itself was unencrypted enough to allow the subject and headers to be read directly.
- **Tip:** In Wireshark, using `Find Packet` to search for `UGFzc3dvcmQ6` or `AUTH LOGIN` provides immediate results.

---

## Optional: Extensions

- Reconstruct the complete SMTP dialogue, including MAIL FROM, RCPT TO and DATA.
- Compare how the same process would differ under STARTTLS.

