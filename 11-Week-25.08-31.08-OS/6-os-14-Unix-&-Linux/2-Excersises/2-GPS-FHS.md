# 🐍 GPS FHS (Linux FHS)

**Course:** Cyber Security Analyst - OS Technology | **Date:** 30 August 2025

---

## Task

**Objective:**  
Identify key paths in the Linux Filesystem Hierarchy Standard for users, MOTD, programmes, APT and auth logs.

**Requirements:**

- Specify the user file, MOTD location, `nmap` path, `apt` configuration file and auth log.
- Provide the answer as a list of paths only.
- Use Ubuntu/Debian-specific locations correctly.
- Clearly distinguish between files and directories in your wording.

- Output:

    - five full paths
    - Ubuntu/Debian-compatible answer
    - clear reference to the FHS

---

## Solution

```text
1. List of all user accounts:
   /etc/passwd

2. Directory for Message of the Day:
   /etc/update-motd.d/

3. Path to the `nmap` executable:
   /usr/bin/nmap

4. Configuration file for `apt`:
   /etc/apt/apt.conf

5. Authentication log:
   /var/log/auth.log
```

**Alternative (compact):**

```text
FHS knowledge is often simply path knowledge: users in `/etc`, binaries in `/usr/bin`, logs in `/var/log`.
```

---

## Tests

|Input 1|Input 2|Input 3|Expected|Result|✓|
|---|---|---|---|---|---|
|`/etc/passwd`|`users`|`system file`|`correct`|`yes`|✅|
|`/usr/bin/nmap`|`binary`|`path`|`correct`|`yes`|✅|
|`/var/log/auth.log`|`auth log`|`Ubuntu`|`correct`|`yes`|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|FHS|Standardised Linux file system structure with typical roles per directory.|
|System Binary|Executable programmes are often located under `/usr/bin`.|
|Auth Log|Authentication events are typically logged in `/var/log/auth.log` on Debian/Ubuntu.|

---

## Rules / Logic

```text
Configuration files are typically located under `/etc`.
Variable logs belong in `/var/log`.
System-wide user and programme data follow clear FHS conventions.
```

---

## Notes

- **Important:** The MOTD question here specifically refers to the Ubuntu/Debian mechanism via `/etc/update-motd.d/`.
- **Tip:** On other distributions, individual log or MOTD paths may differ.
- **Observation:** This task is a quick reality check for basic Linux orientation.

---

## Optional: Extensions

- Additionally document `which nmap` and `dpkg -L nmap` as verification commands.
- Functionally compare `/etc/motd` with `/etc/update-motd.d/`.

