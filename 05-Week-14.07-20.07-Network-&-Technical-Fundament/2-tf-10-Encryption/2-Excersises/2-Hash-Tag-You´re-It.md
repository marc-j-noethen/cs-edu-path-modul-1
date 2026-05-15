# Hash-Tag-You're-It (Encryption)

**Course:** Cyber Security Analyst - Technical Fundamentals | **Date:** 15 July 2025

---

## Task

**Objective:**  
Understand SHA-256 as an integrity check and see how sensitive hashes are to small changes.

**Requirements:**

- Select a stable VS Code file from the official SHA website.
- Note down the official SHA-256 hash.
- Calculate your own hash and compare it.
- Compare a modified copy.

---

## Solution

```text
Selected file:
VSCode-darwin-universal.dmg

Official SHA-256 hash:
d7f9e27f2211c91fb955a9747c48111d1b4bee02d5ba097c58a5ad647a8f191e

Download URL:
https://vscode.download.prss.microsoft.com/dbazure/download/stable/8b640eef5a6c6089c029249d48efa5c99adf7d51/VSCode-darwin-universal.dmg

Calculated hash of the original download:
d7f9e27f2211c91fb955a9747c48111d1b4bee02d5ba097c58a5ad647a8f191e

Comparison:
Yes, the hash of the original download matches the official hash.

Tampered Copy:
After `echo "some_change" >> VSCode-tampered.zip`, the hash is completely different.
It matches neither the official hash nor the hash of the original.
```

**Alternative (compact):**

```bash
shasum -a 256 VSCode-darwin-universal.dmg
shasum -a 256 VSCode-tampered.zip
```

---

## Tests

|Input 1|Input 2|Input 3|Expected|Result|✓|
|---|---|---|---|---|---|
|Original file|Official hash|SHA-256|Hash matches|Match|✅|
|Copy + minor change|Official hash|SHA-256|Hash differs|No match|✅|
|Original vs. tampered|File comparison via hash|SHA-256|Different values|Different|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|Hash function|Calculates a fixed fingerprint from any data.|
|Integrity|Same file -> same hash; minor change -> different hash.|
|Avalanche effect|Even minimal changes significantly alter the hash.|

---

## Rules / Logic

```text
If official hash == calculated hash, the file is very likely unchanged.
If even just 1 byte is changed, the hash changes significantly.
Hashes check integrity, not automatically the authenticity of the source.
```

---

## Notes

- **Concept:** Hashes are very well suited for integrity checking of downloads.
- **Syntax:** `shasum -a 256 <file>`.
- **Order is important:**
    1. Retrieve the official hash
    2. Download the file
    3. Calculate the hash locally
- **Edge cases:**
    - Comparing the wrong file.
    - Wrong hash algorithm selected.
    - Manipulation occurring during the download.
- **Tip:** Always check that the source, filename and hash algorithm match exactly.

---

## Optional: Extensions

- Compare SHA-1 and SHA-256.
- Check GPG signatures as an additional authenticity check.
- Recreate the same process locally using a small test file.

