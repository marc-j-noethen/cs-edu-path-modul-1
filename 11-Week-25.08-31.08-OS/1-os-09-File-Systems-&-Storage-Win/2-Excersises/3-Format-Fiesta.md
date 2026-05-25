# Format Fiesta (NTFS / FAT32 / exFAT)

**Course:** Cyber Security Analyst – OS Technology | **Date:** 25 August 2025

---

## Task

**Objective:**  
Compare file systems and identify suitable use cases.

**Requirements:**

- Format NTFS, FAT32 and exFAT.
- Compare security features.
- Explain the 4 GB limit of FAT32.

---

## Solution

```text
1. Security differences:
- NTFS: has true Windows permissions (ACLs), Security tab, Ownership, Quotas, compression, etc.
- FAT32: no true NTFS ACLs, significantly fewer security features
- exFAT: likewise no NTFS-style ACLs as on a local NTFS system

2. FAT32’s 4 GB limit:
A single file must not exceed 4 GB.
This is a major problem for DVD/Blu-ray images, VM disk files, large videos or backups.

3. When is exFAT ideal?
For external drives or USB media intended for use across Windows, macOS and other systems,
when large files need to be stored and high compatibility is more important than NTFS-specific security features.

4. When is NTFS better?
If the external drive is mainly used on Windows and permissions management, stability,
journaling or large system-level workloads are important.
In that case, NTFS is superior to exFAT.
```

**Alternative (compact):**

```text
NTFS = Features and security.
exFAT = Compatibility for large files.
FAT32 = Old and severely limited.
```

---

## Tests

|File system|Expected|✓|
|---|---|---|
|NTFS|Security features available|✅|
|FAT32|4 GB limit|✅|
|exFAT|Platform-friendly for large files|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|ACLs|Fine-grained file permissions in Windows.|
|Journaling|Helps with consistency and recovery.|
|Compatibility|Important for removable media used across multiple systems.|

---

## Rules / Logic

```text
Choosing a file system is always a trade-off between security, size and compatibility.
```

---

## Notes

- **Tip:** For pure Windows workflows, NTFS is usually the preferred choice.
- **Concept:** The "best" file system depends on the intended use.

---

## Optional: Extensions

- Compare ReFS as an additional Windows file system.
- Run benchmarks with many small files versus a few large files.

