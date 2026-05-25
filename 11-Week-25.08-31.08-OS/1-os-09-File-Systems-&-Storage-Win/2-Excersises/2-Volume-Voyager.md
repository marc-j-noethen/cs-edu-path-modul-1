# Volume Voyager (Partitions)

**Course:** Cyber Security Analyst – OS Technology | **Date:** 25 August 2025

---

## Task

**Objective:**  
Classify partitions and file systems within storage device management.

**Requirements:**

- Read storage device 0.
- Count the partitions.
- Explain the C: file system and letterless partitions.

---

## Solution

```text
Sample answer for a typical modern Windows installation:
- Number of partitions on data carrier 0: usually 3 to 4
- File system of C:: NTFS
- Partitions without drive letters: often EFI system partition, MSR and/or recovery partition

What are these partitions used for?
- EFI system partition: contains boot files for system startup
- Recovery partition: contains recovery environment for repair/reset
- MSR (if present): reserved area for Windows management on GPT storage devices
```

**Alternative (compact):**

```text
Not every important partition needs a drive letter.
```

---

## Tests

|Item|Expected|✓|
|---|---|---|
|C:-Volume|NTFS|✅|
|Partitions without letters|System/recovery purpose plausible|✅|
|Graphical representation|Storage device management explains structure|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|NTFS|Standard file system for Windows system volumes.|
|EFI|Boot environment for UEFI systems.|
|Recovery|Assists with repair and recovery.|

---

## Rules / Logic

```text
System boot, operating system and recovery are often deliberately separated.
```

---

## Notes

- **Important:** The exact number of partitions depends on the VM and installation.
- **Tip:** Roles are often easier to read in the graphical view than in tables.

---

## Optional: Extensions

- Compare GPT and MBR directly.
- Verify partition labels using `diskpart`.


