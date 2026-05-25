# Policy Power Up (Local Security Policy)

**Course:** Cyber Security Analyst – OS Technology | **Date:** 29 August 2025

---

## Task

**Objective:**  
Strengthen password and account lockout policies and understand their effects.

**Requirements:**

- Set minimum length to 12.
- Enable complexity.
- Configure password history and account lockout.

---

## Solution

```text
Configured policies:
- Minimum length: 12 characters
- Complexity: enabled
- Password history: 5
- Account lockout after: 3 failed attempts
- Lockout duration: 15 minutes

Observation regarding the password `pass`:
The password is rejected because it is both too short and does not meet the complexity requirements.

Consequence of repeated failed logins:
After 3 incorrect login attempts, the account is locked for 15 minutes.
This significantly hinders brute-force or password-guessing attacks.
```

**Alternative (compact):**

```text
Strong policies make weak passwords and blind guessing more costly.
```

---

## Tests

|Item|Expected|✓|
|---|---|---|
|Weak password|Rejected|✅|
|Strong password|Accepted|✅|
|3 failed attempts|Lockout active|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|Password Complexity|Enforces more robust passwords.|
|Password History|Prevents immediate reuse of old passwords.|
|Account Lockout|Limits repeated failed attempts.|

---

## Rules / Logic

```text
Length + Complexity + Lockout Logic = better basic protection against standard attacks.
```

---

## Notes

- **Tip:** Overly strict policies without good processes can create a helpdesk burden.
- **Concept:** Hardening is always a balancing act between security and usability.

---

## Optional: Extensions

- Further fine-tune password age and lockout periods.
- Roll out policies later via Group Policy.


