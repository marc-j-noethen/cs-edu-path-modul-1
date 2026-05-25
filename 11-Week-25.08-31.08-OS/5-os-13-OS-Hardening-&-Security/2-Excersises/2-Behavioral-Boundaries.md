# 🐍 Behavioural Boundaries (Defender)

**Course:** Cyber Security Analyst - OS Technology | **Date:** 29 August 2025

---

## Task

**Objective:**  
Describe how Microsoft Defender responds to the harmless EICAR test signature.

**Requirements:**

- Write the EICAR string to a file.
- Observe Defender’s immediate reaction.
- Access Protection History and name the action.
- Classify the result as a safe test observation.

- Output:

    - expected Defender action
    - brief note on Protection History
    - Classification as a harmless test signature

---

## Solution

```text
Expected observation:
As soon as the exact EICAR string is saved,
Microsoft Defender immediately recognises the file as a test signature.

Typical result:
- The file is blocked, removed or moved to quarantine.
- A corresponding entry appears in `Windows Security -> Protection history`.
- The action visible there is typically `Quarantined` or `Removed`.

Technical classification:
EICAR is not genuine malware, but a secure industry-standard test string.
The response demonstrates that Defender’s detection and response chain functions without the need to use actual malware.
```

**Alternative (compact):**

```text
EICAR is the safety belt for AV tests: harmless, but deliberately detectable.
```

---

## Tests

|Input 1|Input 2|Input 3|Expected|Result|✓|
|---|---|---|---|---|---|
|`EICAR string`|`save file`|`Defender`|`detects`|`expected`|✅|
|`Protection history`|`entry visible`|`action`|`quarantine/remove`|`expected`|✅|
|`analysis`|`real malware?`|`EICAR`|`no`|`correct`|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|EICAR|Harmless test string that is treated as malware by AV products.|
|Protection History|Defender view for detected security events and actions taken.|
|Quarantine|File is isolated so that it can no longer be used normally.|

---

## Rules / Logic

```text
EICAR is used for testing purposes only, not for infection.
The key observation is the Defender reaction plus the Protection History entry.
With modern protection mechanisms, the file may disappear as soon as it is saved.
```

---

## Notes

- **Important:** No real malware is required – that is precisely the point of EICAR.
- **Tip:** If the file disappears immediately, check Protection History straight away.
- **Observation:** The exact wording of the notification may vary slightly depending on the Defender version.

---

## Optional: Extensions

- Conceptually compare the same behaviour with an excluded folder.
- Additionally classify the detected file as a test artefact using hashing and VirusTotal.

