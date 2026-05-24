# Section Secrets (PE Sections)

**Course:** Cyber Security Analyst – OS Technology | **Date:** 22 August 2025

---

## Task

**Objective:**  
Read the section permissions of a PE file and interpret them from a security perspective.

**Requirements:**

- Select an EXE file.
- Compare `.text` and `.data`.
- Explain the security implications of writable code sections.

---

## Solution

```text
Selected file:
C:\Windows\System32\charmap.exe

Observed properties:
- .text: 0x60000020  -> executable + readable (typical code section)
- .data: 0xc0000040  -> readable + writable (typical data section)

Food for thought 1:
Why should `.text` not be writable?
Because that is where the executable machine code resides. If this memory area were writable at runtime,
an error or an attacker could directly modify the program code.

Dangerous consequences of a writable code section:
- Injection or overwriting of instructions in memory
- Bypassing control flow and protection mechanisms
- Facilitation of exploits and self-modifying malicious code

In short:
Code should be executable and readable, data should be readable and writable – but not both at the same time for the same sensitive area.
```

**Alternative (compact):**

```text
`.text` may run, `.data` may change. It is precisely this separation that is a fundamental principle of memory security.
```

---

## Tests

|Section|Expected|✓|
|---|---|---|
|`.text`|execute/read|✅|
|`.data`|read/write|✅|
|Security rationale|clearly presented|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|Section Characteristics|Permissions and type of a PE section.|
|W^X Principle|An area should not be both writable and executable at the same time.|
|Code Injection|Abuse of writable/executable memory areas.|

---

## Rules / Logic

```text
Code = execute/read.
Data = read/write.
Writable code is a security issue.
```

---

## Notes

- **Tip:** `.rdata` is often read-only and contains constants.
- **Concept:** Memory permissions are a core component of modern exploit defence.

---

## Optional: Extensions

- Trace your own compiled Hello World EXE in a hex editor.
- Compare `PointerToRawData` with actual file regions.

