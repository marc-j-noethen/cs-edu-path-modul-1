# Mission SMTP (SMTP)

**Course:** Cyber Security Analyst – Network Technology | **Date:** 28 July 2025

---

## Task

**Objective:**  
Open an SMTP session using `smtplib`, analyse the `EHLO` message and understand `STARTTLS`.

**Requirements:**

- Establish a connection to `smtp.googlemail.com:587`.
- Send `EHLO` and output the features.
- Recognise and explain `STARTTLS`.

---

## Solution

```python
import smtplib

server = smtplib.SMTP("smtp.googlemail.com", 587, timeout=10)
server.ehlo()

for key, value in server.esmtp_features.items():
    print(f"{key}: {value}")

print("STARTTLS supported:", "starttls" in server.esmtp_features)
server.quit()
```

```text
Purpose of STARTTLS:
STARTTLS upgrades an existing plaintext SMTP connection to a TLS-protected connection.
On port 587, this is crucial because although submission often begins in plain text,
login credentials and further SMTP commands must be encrypted thereafter.

What happens immediately afterwards?
The client sends `STARTTLS`, the server responds, for example, with `220 Ready to start TLS`,
after which the TLS handshake begins immediately. Only after a successful TLS setup is `EHLO` sent again.
```

**Alternative (compact):**

```text
STARTTLS = Upgrade from plaintext SMTP to encrypted SMTP.
```

---

## Tests

|Item|Expected|✓|
|---|---|---|
|EHLO possible|Feature list visible|✅|
|STARTTLS detected|`starttls` present|✅|
|After STARTTLS|TLS handshake starts|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|EHLO|Queries server capabilities.|
|ESMTP Features|Extensions such as `STARTTLS`, `SIZE`, `AUTH`.|
|TLS Upgrade|Secures the session retrospectively.|

---

## Rules / Logic

```text
587 = Submission port.
EHLO shows what the server is capable of.
STARTTLS successful -> immediate TLS handshake.
```

---

## Notes

- **Tip:** Always send `EHLO` again after STARTTLS.
- **Concept:** Without TLS, login credentials and content could be intercepted.

---

## Optional: Extensions

- Test `AUTH` only after TLS.
- Compare SMTPS on port 465 with Submission on 587.

