# The Enigma (Encryption)

**Course:** Cyber Security Analyst - Technical Fundamentals | **Date:** 15 July 2025

---

## Task

**Objective:**  
Apply frequency analysis to a monoalphabetic substitution cipher and use it to derive a decryption.

**Requirements:**

- Compare frequencies for the plaintext and ciphertext.
- Formulate initial guesses regarding the letters.
- Identify words and patterns.
- Reconstruct a large portion of the plaintext.

---

## Solution

```python
from collections import Counter

def calculate_frequencies(text_sample):
    letters = [c.upper() for c in text_sample if c.isalpha()]
    total = len(letters)
    counts = Counter(letters)
    return [(ch, round(count / total * 100, 2)) for ch, count in counts.most_common()]

ciphertext = """ Odie ie vbh gvhsx cvg… odp gvhsx vn odp psptohvc ycx odp egiotd, odp apybor vn odp aybx. Gp plieo giodvbo eqic tvsvh, giodvbo cyoivcysior, giodvbo hpsimivbe aiye… ycx rvb tyss be thificyse. Gp plzsvhp… ycx rvb tyss be thificyse. Gp eppq ynoph qcvgspxmp… ycx rvb tyss be thificyse. Gp plieo giodvbo rvbh syge — gp plieo aptybep rvb imcvhp vbhe."""

print(calculate_frequencies(ciphertext))
```

**Alternative (compact):**

```text
Decrypted plaintext:
This is our world now... the world of the electron and the switch, the beauty of the baud.
We exist without skin colour, without nationality, without religious bias... and you call us criminals.
We explore... and you call us criminals.
We seek after knowledge... and you call us criminals.
We exist without your laws – we exist because you ignore ours.
```

---

## Tests

|Input 1|Input 2|Input 3|Expected|Result|✓|
|---|---|---|---|---|---|
|Ciphertext|Frequency analysis|Top letters|most common symbols visible|P, V, O, I at the top|✅|
|Substitutions|manual fine-tuning|Word patterns|`the`, `and`, `you` recognisable|correct|✅|
|Complete reading|Plausibility test|English continuous text|Logical in content|yes|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|Frequency analysis|Compares letter frequencies with typical English.|
|Monoalphabetic substitution|Each letter is consistently replaced by exactly one other.|
|Pattern recognition|Short, common words and repetitions aid in matching.|

---

## Rules / Logic

```text
Common cipher letters are candidates for E, T, A, O, I, N.
Short recurring words help in guessing 'the', 'and', 'you', 'we'.
With each secure mapping, the rest of the text becomes easier to read.
```

---

## Notes

- **Concept:** The text is a well-known quote from the Hacker Manifesto.
- **Syntax:** `Counter` is sufficient for frequency calculation.
- **Order is important:**
    1. Collect frequencies
    2. Check candidates for E/T/A/O
    3. Validate word patterns
- **Edge Cases:**
    - Short texts produce noisy frequencies.
    - Individual letters are not enough; word patterns are more important.
    - Punctuation marks are retained and aid in reading the structure.
- **Tip:** Once `the`, `and` and `you` are identified, the task shifts from guessing to text reconstruction.

---

## Optional: Extensions

- Write a helper function for partial substitution.
- Maintain a mapping dictionary of reliable correspondences.
- Compare English reference frequencies with your own book text.

