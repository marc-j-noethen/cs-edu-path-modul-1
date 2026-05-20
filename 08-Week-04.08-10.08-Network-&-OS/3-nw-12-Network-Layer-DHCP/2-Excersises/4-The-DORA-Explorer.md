# 🐍 The DORA Explorer 

**Course:** Cyber Security Analyst – Network Technology | **Date:** 06 August 2025

---

## Task

**Goal:**  
Force a Windows host to request a new DHCP lease and capture the resulting DORA exchange in Wireshark.

**Requirements:**

- Release the current address with `ipconfig /release`.

- Request a fresh lease with `ipconfig /renew`.

- Capture the DHCP sequence in Wireshark.

- Submit evidence for the terminal output and the four DHCP packets.

- Output:
    
    - `Submit the final result in the exact format requested by the task.`
        
    - `A reviewer-readable final result`
        
    - `The submission artifact requested by the task`

---

## Solution

```text
# Inputs
context = 'Local analysis or lab environment'
objective = 'Force a Windows host to request a new DHCP lease and capture the resulting DORA exchange in Wireshark.'
evidence = 'Submit the final result in the exact format requested by the task.'

# Main logic
Correct expected behavior:

- `ipconfig /release` drops the current lease, so the interface loses its existing DHCP-provided address.
- `ipconfig /renew` triggers a new DHCP negotiation.
- In Wireshark, the four key messages should appear in this order:
  1. DHCP Discover
  2. DHCP Offer
  3. DHCP Request
  4. DHCP ACK

Concise explanation:

The release command tells Windows to give up the current lease. The renew command starts the DORA exchange again so Windows can obtain a fresh address configuration from the DHCP server. If the same address is still available, the server may reassign it; otherwise, a different valid lease can be offered.
```

**Alternative (compact):**

```text
Release removes the lease. Renew starts DORA again.
```

---

## Tests

|Input 1|Input 2|Input 3|Expected|Result|✓|
|---|---|---|---|---|---|
|`task text`|`correct method`|`required evidence`|`Goal completed`|`Reviewer can verify it`|✅|
|`platform or scenario`|`final validation`|`submission format`|`Consistent result`|`Matches the task`|✅|
|`self-check`|`edge-case review`|`final file`|`GitHub-ready solution`|`Ready to upload`|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|Objective Alignment|The solution must directly satisfy the original task instead of drifting into unrelated detail.|
|Evidence Quality|The final artifact should prove completion clearly enough for a reviewer to confirm it.|
|Validation|The result should be checked against the stated goal before submission.|

---

## Rules / Logic

```text
Read the full task before solving it.
Match the output to the requested submission format.
Keep only verifiable final results.
```

---

## Notes

- **Concept:** Keep the solution tightly aligned to the original objective.
    
- **Syntax:** Use the platform, terminology, and evidence style that the task expects.
    
- **Order matters:**
    
    1. Read the task and identify the real objective.
        
    2. Complete or answer the task with the correct method.
        
    3. Validate the result and keep only the final solution.
        
- **Edge Cases:**
    
    - The source task may be incomplete or empty.
        
    - External labs can change while the local solution file stays static.
        
    - Screenshots or outputs that do not show the final state may be rejected as weak evidence.
        
- **Tip:** Keep a short note of the exact commands, payloads, calculations, or findings you used during completion.

---

## Optional: Extensions

- Add a second validated approach if the task can be solved in more than one reliable way.
    
- Add stronger validation evidence if the original task was solved in a live platform.
    
- Add brief error-handling or troubleshooting notes for common failure states.
