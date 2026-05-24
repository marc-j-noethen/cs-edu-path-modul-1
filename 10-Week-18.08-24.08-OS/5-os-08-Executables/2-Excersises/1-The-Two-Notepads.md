# The Two Notepads (PE Basics)

**Course:** Cyber Security Analyst – OS Technology | **Date:** 22 August 2025

---

## Task

**Objective:**  
Read the basic data of a PE file.

**Requirements:**

- Open `notepad.exe` in the PE Tool.
- Note down Machine, TimeDateStamp, SizeOfImage and NumberOfSections.
- Document the values.

---

## Solution

```text
File:
C:\Windows\System32\notepad.exe

Values:
- Machine: x64
- TimeDateStamp: 0xa434753f
- SizeOfImage: 0x5a000
- NumberOfSections: 8
```

**Alternative (compact):**

```text
These fields describe the architecture, build timestamp, image size and structure scope.
```

---

## Tests

|Field|Expected|✓|
|---|---|---|
|Machine|Architecture detected|✅|
|TimeDateStamp|Hex value recorded|✅|
|Sections|Number present|✅|

---

## Explanation / Concepts

|Concept|Description|
|---| ---|
|Machine|Target architecture of the file.|
|TimeDateStamp|Build-related timestamp in the header.|
|SizeOfImage|Size of the mapped image in memory.|

---

## Rules / Logic

```text
PE headers provide quick insights into the platform and structure of an EXE.
```

---

## Notes

- **Tip:** Always document the file path as well.
- **Concept:** Such fields are often the first point of classification in malware and IR analyses.

---

## Optional: Extensions

- Compare `ping.exe` and `notepad.exe` directly.
- Check the timestamp against file version information.

