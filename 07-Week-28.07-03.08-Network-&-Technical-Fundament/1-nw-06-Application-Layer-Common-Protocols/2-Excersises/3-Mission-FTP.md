# Mission FTP (FTP)

**Course:** Cyber Security Analyst – Network Technology | **Date:** 28 July 2025

---

## Task

**Objective:**  
Identify the FTP control channel, data channel and typical commands.

**Requirements:**

- Start a local FTP server.
- Observe `ls`, `get`, `put` and `quit`.
- Explain the control and data connections.

---

## Solution

```text
Typical control commands observed:
- USER
- PASS
- SYST
- TYPE I
- PASV or EPSV
- LIST
- RETR
- STOR
- QUIT

TYPE command:
`TYPE` specifies how data is interpreted, e.g. ASCII or Binary/Image (`I`).
This is important to ensure that text files and binary files are transferred correctly.

Why the separate data channel causes problems for firewalls:
FTP uses a fixed control channel and additionally dynamically negotiated ports for data.
Firewalls and NAT must recognise and allow these additional data ports.
This is significantly more complicated than protocols such as SSH/SFTP, which handle everything via a single connection.
```

**Alternative (compact):**

```text
FTP = control channel + data channel.
It is precisely this separation that makes it more cumbersome to operate.
```

---

## Tests

|Item|Expected|✓|
|---|---|---|
|Control channel|Commands visible in plain text|✅|
|Data channel|File contents visible|✅|
|TYPE understood|ASCII/Binary is controlled|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|Control channel|Port 21 for commands and responses.|
|Data channel|Separate port for directories and file contents.|
|Passive Mode|Server specifies a port to which the client connects.|

---

## Rules / Logic

```text
Commands go via the control channel.
File contents go via the data channel.
Multiple channels = increased firewall complexity.
```

---

## Notes

- **Tip:** `TYPE I` is the standard for binary files.
- **Concept:** Old protocols illustrate very well why modern designs are easier to secure.

---

## Optional: Extensions

- Compare active and passive FTP modes.
- Repeat the same scenario with SFTP.

