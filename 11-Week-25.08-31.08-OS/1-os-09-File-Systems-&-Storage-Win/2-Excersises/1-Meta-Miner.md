# Meta Miner (File Metadata)

**Course:** Cyber Security Analyst – OS Technology | **Date:** 25 August 2025

---

## Task

**Objective:**  
Compare file metadata in Explorer and CMD.

**Requirements:**

- Create a text, HTML and JPG file.
- Document size, timestamps and attributes.
- Describe the behaviour of `Read-only`.

---

## Solution

```text
Observation:
- Explorer conveniently displays file type, size, size on disk, creation and modification dates, as well as attributes.
- `dir /A` can also reveal hidden or system-related entries.
- `dir /Q` displays the owner.
- `dir /T:C`, `/T:A`, `/T:W` help to specifically check the creation, access or modification times.

What happens with `Read-only`?
Typically, the file cannot simply be overwritten.
Depending on the editor, either an error message or a `Save As` dialogue appears instead of saving directly.
```

**Alternative (compact):**

```text
Explorer is convenient, `dir` is faster for specific metadata views.
```

---

## Tests

|Item|Expected|✓|
|---|---|---|
|Explorer metadata|visible|✅|
|`dir /Q`|Owner visible|✅|
|Read-only test|Saving is difficult / blocked|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|Metadata|Data about files, not just their content.|
|Attributes|Controls such as write protection or visibility.|
|Timestamps|Important for operation and forensics.|

---

## Rules / Logic

```text
Files consist of content + metadata.
Good analysis considers both.
```

---

## Notes

- **Tip:** `dir /T:W` is often most useful for recently modified files.
- **Concept:** Ownership and timestamps are key forensic indicators.

---

## Optional: Extensions

- Record file hashes as well.
- Treat ADS (Alternate Data Streams) as an additional layer of metadata.

