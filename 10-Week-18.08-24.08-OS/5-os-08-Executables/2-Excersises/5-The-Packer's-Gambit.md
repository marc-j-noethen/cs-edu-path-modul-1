# 🐍 The Packer's Gambit (PE Overlay Analysis)

**Course:** Cyber Security Analyst - OS Technology | **Date:** 22 August 2025

---

## Task

**Objective:**  
Identify and explain an artificially enlarged EXE with an overlay as a suspicious PE artefact.

**Requirements:**

- Copy a clean EXE and append additional data to the end.
- Compare the total file size with the PE-defined sections.
- Explain the overlay as a red flag.
- Identify further packing/obfuscation indicators.

- Output:

    - Description of the overlay discrepancy
    - At least two further indicators of suspicious behaviour
    - Rationale for the overlay/packing

---

## Solution

```text
Key finding:
`suspicious_agent.exe` is significantly larger than the end of the last section described by the PE header.
There is therefore an overlay – additional data at the end of the file that does not belong to the officially described PE sections.

Why is this a red flag?
Such extra material may indicate appended payloads, configuration data, encrypted blocks, or a simple packer/dropper mechanism.
A cleanly compiled standard programme typically does not have a large, unexpected overlay block.

Further indicators I would look out for in CFF Explorer:
- Suspicious section names or atypical section permissions (e.g. `RWX` all at once)
- A very small import table despite an apparently complex programme
- An unusual entry point, e.g. directly within packed or implausibly named code
- High entropy in a section, which may indicate compressed or encrypted content

Why do malware authors use overlays or packing?
- To make static analysis more difficult
- To hide additional payloads or configurations
- To bypass simple signature/string-based detection
- To complicate reverse engineering

Note:
The exact byte sizes depend on the locally compiled `program_B.exe`.
The technically decisive answer is the verifiable difference between the actual file size and the PE-defined structure.
```

**Alternative (compact):**

```text
If the file is larger than what the PE structure indicates, an overlay is very likely present.
```

---

## Tests

|Input 1|Input 2|Input 3|Expected|Result|✓|
|---|---|---|---|---|---|
|`program_B.exe`|`copy`|`append data`|`size grows`|`yes`|✅|
|`PE sections`|`real file size`|`compare`|`overlay visible`|`yes`|✅|
|`analyst view`|`packed clues`|`multiple indicators`|`listed`|`yes`|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|Overlay|File data beyond the logical end of the programme as described by the PE.|
|Entropy|Measure of apparent random distribution, often an indication of compressed or encrypted data.|
|Entry Point Triage|The first code executed can reveal a great deal about loaders, packers and startup logic.|

---

## Rules / Logic

```text
Not every large EXE is malicious, but unexplained extra bytes are always worth investigating.
The PE header and actual file size should be considered together during an initial assessment.
It is often only when several small anomalies are considered together that a reliable picture emerges.
```

---

## Notes

- **Important:** This exercise trains detection based on structure, not behaviour.
- **Tip:** Always compare the last section end address against the actual file size.
- **Observation:** Overlays combined with unusual section flags are, in practice, a very strong indicator for analysts.

---

## Optional: Extensions

- Automatically detect overlay patterns using a YARA rule approach.
- Extract the appended bytes separately and analyse them using entropy or signature-based methods.

