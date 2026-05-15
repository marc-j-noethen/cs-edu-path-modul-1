# Caesar's Codebreaker (Encryption)

**Course:** Cyber Security Analyst - Technical Fundamentals | **Date:** 15 July 2025

---

## Task

**Objective:**  
Implement Caesar cipher encryption for letters and decrypt a given ciphertext using shift-and-search.

**Requirements:**

- Write `caesar_encrypt` and `caesar_decrypt`.
- Shift letters only.
- Preserve other characters.
- Find the correct shift for the given text.

---

## Solution

```python
def caesar_encrypt(text, shift):
    result = []
    for ch in text:
        if "A" <= ch <= "Z":
            result.append(chr((ord(ch) - ord("A") + shift) % 26 + ord("A")))
        elif "a" <= ch <= "z":
            result.append(chr((ord(ch) - ord("a") + shift) % 26 + ord("a")))
        else:
            result.append(ch)
    return "".join(result)


def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)


ciphertext = "Wh wg pshhsf hc qfsohs hvob hc zsofb! Qfsohwbu wg hvs sggsbqs ct zwts."

for shift in range(1, 26):
    candidate = caesar_decrypt(ciphertext, shift)
    if "better" in candidate.lower():
        print("Shift:", shift)
        print(candidate)
```

**Alternative (compact):**

```text
Shift = 14
Plaintext = It is better to create than to learn! Creating is the essence of life.
```

---

## Tests

|Input 1|Input 2|Input 3|Expected|Result|✓|
|---|---|---|---|---|---|
|`ABC`|Shift 3|Encrypt|`DEF`|correct|✅|
|`DEF`|Shift 3|Decrypt|`ABC`|correct|✅|
|given ciphertext|Shift 14|Decrypt|readable English sentence|correct|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|Caesar Cipher|Each letter is shifted by a fixed offset.|
|Modulo 26|Ensures wrap-around from Z back to A.|
|Brute Force on a small key space|25 possible shifts can be easily checked.|

---

## Rules / Logic

```text
letter_index = (original_index +/- shift) mod 26
Non-letters remain unchanged.
A small keyspace makes Caesar insecure.
```

---

## Notes

- **Concept:** Caesar is good for learning, but cryptographically very weak.
- **Syntax:** `ord()`, `chr()`, `% 26`.
- **Order is important:**
    1. Recognise letters
    2. Shift the index
    3. Reconstruct the character
- **Edge cases:**
    - Treat upper and lower case letters separately.
    - Preserve spaces.
    - Calculate negative shifts correctly using modulo.
- **Tip:** If a text looks like English, the correct shift is usually immediately obvious.

---

## Optional: Extensions

- Allow only uppercase letters, as in the problem statement.
- Output all 25 candidates in a table.
- Apply Vigenère as the next step.

