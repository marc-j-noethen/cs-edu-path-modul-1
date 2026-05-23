# 🐍 The Lone Bit (Error Detection)

**Course:** Cyber Security Analyst - Network Technology | **Date:** 15 August 2025

---

## Task

**Objective:**  
Use exactly one additional bit to check a 7-bit payload for single-bit errors and explain the limitations of the method.

**Requirements:**

- Design an 8-bit scheme with exactly one parity bit.
- Write a Python function for error detection.
- Test several valid and manipulated examples.
- Explain why the method cannot localise the faulty bit nor reliably detect two bit errors.

- Output:

    - Description of the method
    - Python script for the check
    - Clear statement regarding the limitations

---

## Solution

```python
def detect_single_bit_error(received_8bit_sequence_str: str) -> bool:
    if len(received_8bit_sequence_str) != 8 or any(bit not in "01" for bit in received_8bit_sequence_str):
        raise ValueError("Expected exactly 8 bits as a string.")

    ones = received_8bit_sequence_str.count("1")
    return ones % 2 != 0


test_sequences = {
    "10110010": "No Error Detected",
    "01100110": "No Error Detected",
    "00110010": "Error Detected",
    "11110010": "Error Detected",
    "10100010": "Error Detected",
    "00100010": "No Error Detected",
}

for seq, expected in test_sequences.items():
    result = "Error Detected" if detect_single_bit_error(seq) else "No Error Detected"
    print(f"Sequence {seq}: {result} (expected: {expected})")

# Procedure description:
# Even parity is used here.
# Sender: sets the 8th bit so that the total number of 1-bits is even.
# Receiver: checks whether the total number of 1-bits is still even.
# If it is odd, an error has been detected.
```

**Alternative (compact):**

```text
Even Parity detects every single bit flip, but does not indicate which bit is affected.
```

---

## Tests

|Input 1|Input 2|Input 3|Expected|Result|✓|
|---|---|---|---|---|---|
|`10110010`|`even parity`|`original`|`no error`|`correct`|✅|
|`00110010`|`1 bit flipped`|`parity flips`|`error`|`correct`|✅|
|`00100010`|`2 bits flipped`|`parity remains even`|`cannot be reliably detected`|`correct`|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|Even Parity|The check bit is set so that the total number of ones remains even.|
|Error Detection|The method detects deviations but does not correct them.|
|Limitation|An even number of flipped bits may remain undetected.|

---

## Rules / Logic

```text
Parity reliably detects any odd number of bit errors.
Parity does not localise the error.
Exactly two bit errors may remain undetected if the overall parity remains the same.
```

---

## Notes

- **Important:** Returning `True` here means: error detected.
- **Observation:** Two bit flips are the classic counterexample to a pure parity check.
- **Tip:** For true error correction, you need, for example, Hamming codes rather than just parity.

---

## Optional: Extensions

- Implement odd parity as a variant.
- Compare the same example with a Hamming code.

