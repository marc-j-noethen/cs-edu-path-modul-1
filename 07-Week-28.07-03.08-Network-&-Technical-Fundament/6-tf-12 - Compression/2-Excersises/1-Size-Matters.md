# Size Matters (Compression)

**Course:** Cyber Security Analyst – Network Technology | **Date:** 1 August 2025

---

## Task

**Objective:**  
Compare file sizes before and after compression.

**Requirements:**

- Create a text file.
- Generate a `.gz` file.
- Create an uncompressed `tar` archive.

---

## Solution

```text
Sample measurements:
- novel_excerpt.txt: 5761 bytes
- novel_excerpt.txt.gz: 140 bytes
- my_files.tar: 20480 bytes
```

**Alternative (compact):**

```text
Repetitive text compresses significantly.
An uncompressed TAR archive merely archives; it does not compress.
```

---

## Tests

|File|Expected|✓|
|---|---|---|
|Original|larger than `.gz`|✅|
|`.gz`|significantly smaller|✅|
|`.tar`|contains both files, but is not compressed|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|gzip|Compresses a single file.|
|tar|Archives multiple files into a single container.|
|Redundancy|Repetitive patterns compress well.|

---

## Rules / Logic

```text
Compression saves space if there is sufficient redundancy.
TAR = Packaging.
GZIP = Reducing size.
```

---

## Notes

- **Important:** The exact values depend on the text selected.
- **Tip:** For text, gzip often yields significantly better results than for already compressed formats such as JPG.

---

## Optional: Extensions

- Compare `tar.gz` with plain `tar`.
- Test a text file against an image file.
