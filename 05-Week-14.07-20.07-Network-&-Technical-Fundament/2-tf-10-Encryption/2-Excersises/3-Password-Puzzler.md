# Password Puzzler (Encryption)

**Course:** Cyber Security Analyst - Technical Fundamentals | **Date:** 15 July 2025

---

## Task

**Objective:**  
To find a very short lowercase string using brute force via SHA-256 and understand why hashing is not decryption.

**Requirements:**

- Write a Python script using `hashlib`.
- Systematically test combinations.
- Find the correct password.
- Explain technically why `sha256 decrypt` is inaccurate.

---

## Solution

```python
import hashlib
import itertools
import string

target_hash = "d74ff0ee8da3b9806b18c877dbf29bbde50b5bd8e4dad7a3a725000feb82e8f1"
letters = string.ascii_lowercase

for length in range(1, 6):
    for combo in itertools.product(letters, repeat=length):
        password = "".join(combo)
        if hashlib.sha256(password.encode()).hexdigest() == target_hash:
            print("Password found:", password)
            raise SystemExit
```

**Alternative (compact):**

```text
Password found: pass
```

---

## Tests

|Input 1|Input 2|Input 3|Expected|Result|✓|
|---|---|---|---|---|---|
|Hash value|lowercase a-z|Length 1-5|Match for correct password|`pass` found|✅|
|`pass`|SHA-256|Comparison|same hash|Match|✅|
|incorrect password|SHA-256|Comparison|different hash|no match|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|Brute Force|All possible candidates are systematically tried.|
|SHA-256|A cryptographic one-way hash function.|
|One-way function|The hash cannot be easily converted back into plaintext.|

---

## Rules / Logic

```text
Hashing is not encryption.
The plaintext cannot be found by reverse calculation, but only by guessing and comparing.
Short and simple passwords are particularly vulnerable to brute force attacks.
```

---

## Notes

- **Concept:** The password was weak, not SHA-256 broken.
- **Syntax:** `hashlib.sha256(text.encode()).hexdigest()`.
- **Order is important:**
    1. Generate candidate
    2. Calculate hash
    3. Compare hash
- **Edge cases:**
    - Maximum length too short.
    - Incorrect character set.
    - Forgot uppercase letters or special characters.
- **Tip:** For real passwords, salt and key stretching provide better protection against such simple attacks.

---

## Optional: Extensions

- Test `itertools.product` with a different alphabet.
- Compare bcrypt or Argon2 with SHA-256.
- Relate salt to attack difficulty.

