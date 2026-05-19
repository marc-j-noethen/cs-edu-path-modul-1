# 🐍 The Mysterious Package (Compression)

**Course:** Cyber Security Analyst - Network Technology | **Date:** 1 August 2025

---

## Task

**Objective:**  
Identify the file type of the attachment and extract the hidden message – provided the existing attachment allows this without data loss.

**Requirements:**

- Do not open the file blindly; determine the type first.
- Evaluate clues from magic bytes and embedded names.
- Recognise nested compression layers.
- Deliver the hidden message or provide clear evidence of damage to the attachment.

- Output:

    - recognised outer file type
    - recognised inner layer indication
    - honest statement regarding the final payload of this repository attachment

---

## Solution

```text
Analysis of the existing attachment:
- The file begins with `50 4B 03 04` and is therefore clearly recognisable as a ZIP-like container.
- The name `layer3` also appears in the content, strongly suggesting the presence of at least one further inner compression layer.
- However, the attachment in the current repository is text-corrupted: several NUL and structure bytes have already been altered into spaces or text artefacts during saving/transfer.

What can therefore be stated with certainty:
1. `mystery_package.txt` was not created as a normal text file.
2. It is a ZIP container with at least one further embedded layer (`layer3`).
3. The current repository attachment can no longer be extracted losslessly to reveal the final message, as the binary structure is already damaged.

Technically correct submission:
- File type identified: ZIP container
- Internal note: embedded additional layer / gzip-like layer named `layer3`
- Final hidden message: can no longer be 100% reconstructed from this text-damaged copy

If the original, unmodified binary file is available:
- Rename to `.zip`
- unzip
- run `file` on the contents
- continue unpacking each additional layer until plain text is reached
```

**Alternative (compact):**

```text
The task is intended as a layering exercise; however, the file in the repository is already textually corrupted and therefore can no longer be reproduced down to the final payload.
```

---

## Tests

|Input 1|Input 2|Input 3|Expected|Result|✓|
|---|---|---|---|---|---|
|`PK0304`|`File header`|`Container`|`ZIP detected`|`yes`|✅|
|`layer3`|`Internal name`|`Multiple layers`|`Indication clear`|`yes`|✅|
|`Existing attachment`|`Binary integrity`|`End payload`|`Not lossless`|`Confirmed`|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|Magic Bytes|File signatures allow type determination even without a matching extension.|
|Layered Compression|Archives or streams can be nested multiple times within one another.|
|Evidence Integrity|If a binary file has already been damaged textually, any further analysis is only of limited reliability.|

---

## Rules / Logic

```text
For unknown files, always check the type and integrity first.
A corrupted binary must not be presented as a fully reconstructable source.
Proper forensic work separates reliably established facts from residual assumptions that can no longer be verified.
```

---

## Notes

- **Important:** This particular task is not a technical problem, but an artefact problem relating to the stored copy of the attachment.
- **Observation:** `PK\x03\x04` and `layer3` are sufficiently unique to identify the intended workflow.
- **Tip:** With the unaltered original file, the final message would be reproducible by unpacking layer by layer.

---

## Optional: Extensions

- Download the original file from the learning platform again as a genuine binary and repeat the workflow.
- Then automate the layer order as a small Bash or Python script.

