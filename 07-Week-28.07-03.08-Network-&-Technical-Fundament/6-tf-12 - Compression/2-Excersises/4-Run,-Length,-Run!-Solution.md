# 🐍 Run, Length, Run! (Compression)

**Course:** Cyber Security Analyst - Network Technology | **Date:** 1 August 2025

---

## Task

**Objective:**  
Implement Run-Length Encoding in Python for encoding, decoding and simple validation.

**Requirements:**

- Implement `encode_rle(data)` and `decode_rle(encoded_data)`.
- Handle empty strings, single characters and non-repeating characters correctly.
- Handle invalid encodings cleanly.
- Output the required test cases.

- Output:

    - Complete Python code for RLE
    - Round-trip test `decode_rle(encode_rle(x)) == x`
    - Visible test outputs for the example strings

---

## Solution

```python
import re


def encode_rle(data: str) -> str:
    if not data:
        return ""

    parts = []
    count = 1

    for index in range(1, len(data)):
        if data[index] == data[index - 1]:
            count += 1
        else:
            parts.append(f"{count}{data[index - 1]}")
            count = 1

    parts.append(f"{count}{data[-1]}")
    return "".join(parts)


def decode_rle(encoded_data: str) -> str:
    if not encoded_data:
        return ""

    parts = re.findall(r"(\d+)(.)", encoded_data)
    if not parts or "".join(count + char for count, char in parts) != encoded_data:
        raise ValueError("Invalid RLE format")

    return "".join(int(count) * char for count, char in parts)


test_cases = [
    "AAAAABBCDDDDE",
    "XYZ",
    "A",
    "",
    "WWWWBBWWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW",
]

for original in test_cases:
    encoded = encode_rle(original)
    decoded = decode_rle(encoded)
    print(f"Original: {original!r}")
    print(f"Encoded : {encoded!r}")
    print(f"Decoded : {decoded!r}")
    print(f"Roundtrip OK: {decoded == original}")
    print("-" * 40)
```

**Alternative (compact):**

```text
RLE replaces repetitions with `count + character`; for mixed data, it is simple but not always efficient.
```

---

## Tests

|Input 1|Input 2|Input 3|Expected|Result|✓|
|---|---|---|---|---|---|
|`AAAAABBCDDDDE`|`encode`|`decode`|`5A2B1C4D1E`|`Roundtrip OK`|✅|
|`XYZ`|`no repetition`|`decode`|`1X1Y1Z`|`Roundtrip OK`|✅|
|`''`|`empty`|`decode`|`''`|`Roundtrip OK`|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|RLE|Lossless compression in which identical character sequences are stored using run lengths.|
|Round-Trip Test|An encoder is considered valid if decoding returns the original text.|
|Input Validation|Invalid formats must be detected, rather than silently producing incorrect data.|

---

## Rules / Logic

```text
Empty input must be valid.
Every RLE representation consists of a number followed by exactly one character.
The encoding is only valid if the entire string can be neatly split into pairs.
```

---

## Notes

- **Important:** Even non-repeating characters are explicitly prefixed with a `1` in this format.
- **Edge Case:** Multi-digit run lengths such as `12A` must be decoded correctly.
- **Tip:** Regular expressions are very useful for parsing the decoding format here.

---

## Optional: Extensions

- Extend decoding to include escape sequences or digits as payload data.
- Compare compression rates for various example strings.

