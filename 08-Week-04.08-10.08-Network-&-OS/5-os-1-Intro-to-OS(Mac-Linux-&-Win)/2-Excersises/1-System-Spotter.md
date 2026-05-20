# System Spotter (Windows 11 Introduction)

**Course:** Cyber Security Analyst – OS Technology | **Date:** 08 August 2025

---

## Task

**Objective:**  
Locate and correctly interpret key OS and hardware data in Windows 11.

**Requirements:**

- Note down the Windows edition, version and build.
- Identify the CPU, RAM and system drive.
- Check the Windows Update status and BitLocker or device encryption.

---

## Solution

```text
This task is device-dependent.
The technically correct model answer consists of exactly these points:
- Windows edition: <e.g. Windows 11 Pro>
- Version / Build: <e.g. 23H2 / Build ...>
- Processor: <actual CPU name>
- Installed RAM: <e.g. 16 GB>
- System drive: <e.g. Drive C: / SSD model>
- Windows Update: <up to date / updates available>
- BitLocker or device encryption: <enabled / disabled / not available>

This is what your submission should look like:
`Windows 11 Pro, Version ..., Intel/AMD CPU ..., 16 GB RAM, Drive C:, System up to date, BitLocker enabled.`
```

**Alternative (compact):**

```text
`Settings -> System -> About` provides identity and hardware details,
`Windows Update` and `Privacy & Security` provide the security status.
```

---

## Tests

|Item|Expected|✓|
|---|---|---|
|Edition + Version|Found|✅|
|Hardware data|Found|✅|
|Update/Encryption|Status documented|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|System profile|Basic data about the operating system and hardware.|
|BitLocker / Device encryption|Full drive encryption under Windows.|
|Windows Update|Central status for patch level and security.|

---

## Rules / Logic

```text
System identity = Windows version + hardware + memory + system drive.
Security status = patch level + encryption.
```

---

## Notes

- **Important:** The specific values vary depending on the device.
- **Tip:** For actual reporting, always use the live values from your own Windows 11 system.

---

## Optional: Extensions

- Document the serial number and model ID.
- Check storage usage under `Settings -> System -> Storage`.

