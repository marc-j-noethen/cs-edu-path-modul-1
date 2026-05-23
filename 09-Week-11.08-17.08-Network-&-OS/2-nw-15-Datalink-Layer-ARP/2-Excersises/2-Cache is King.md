# Cache is King (ARP Cache)

**Course:** Cyber Security Analyst – Network Technology | **Date:** 12 August 2025

---

## Task

**Objective:**  
Demonstrate that existing ARP entries render new broadcast requests unnecessary.

**Requirements:**

- Test with a dynamic cache entry.
- Then test with a static entry.
- Explain the difference.

---

## Solution

```text
Step 4:
- Normally, no new ARP request is visible.
- Reason: The dynamic ARP cache already contains the mapping for the gateway.

Step 8:
- No new ARP request visible here either.
- Reason: The static ARP entry provides the mapping directly and overrides the need for a broadcast resolution.

Conclusion:
In both cases, ARP is suppressed, but for different reasons:
- firstly due to a valid dynamic cache entry,
- subsequently due to a manually entered static mapping.
```

**Alternative (compact):**

```text
If the MAC is already known, there is no need to query it.
```

---

## Tests

|Scenario|New ARP request?|✓|
|---|---|---|
|Dynamic cache present|No|✅|
|Static entry present|No|✅|
|Explanation|Mechanism correctly named|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|Dynamic cache|Automatically learned, temporary ARP mapping.|
|Static entry|Manually set fixed mapping.|
|Broadcast avoidance|Saves traffic and time.|

---

## Rules / Logic

```text
Known IP->MAC mapping = no new ARP broadcast required.
```

---

## Notes

- **Tip:** Remove the static entry again after the test.
- **Concept:** Caching is purely a question of efficiency and load.

---

## Optional: Extensions

- Monitor the expiry time of dynamic entries.
- Test incorrect static entries as a source of error.


