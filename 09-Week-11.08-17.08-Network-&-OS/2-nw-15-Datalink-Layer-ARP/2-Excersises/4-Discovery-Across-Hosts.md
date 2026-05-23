# 🐍 Discovery Across Hosts

**Course:** Cyber Security Analyst – Network Technology | **Date:** 12 August 2025

---

## Task

**Goal:**  
Observe normal ARP resolution and caching between two separate machines on the same Layer 2 segment, then compare the behavior with a static ARP entry.

**Requirements:**

- Clear ARP caches on both systems before the first ping.

- Capture ARP on both machines while they ping each other.

- Record the Ethernet source/destination MAC addresses and ARP target IPs.

- Explain why later pings often suppress new ARP broadcasts.

- Output:
    
    - `Submit the final result in the exact format requested by the task.`
        
    - `A reviewer-readable final result`
        
    - `The submission artifact requested by the task`

---

## Solution

```text
# Inputs
context = 'Local analysis or lab environment'
objective = 'Observe normal ARP resolution and caching between two separate machines on the same Layer 2 segment, then compare the behavior with a static ARP entry.'
evidence = 'Submit the final result in the exact format requested by the task.'

# Main logic
Expected first-ping behavior from HostA to HostB:

ARP request
- Ethernet source MAC: HostA_MAC
- Ethernet destination MAC: ff:ff:ff:ff:ff:ff
- ARP sender IP/MAC: HostA_IP / HostA_MAC
- ARP target IP: HostB_IP

ARP reply
- Ethernet source MAC: HostB_MAC
- Ethernet destination MAC: HostA_MAC
- ARP sender IP/MAC: HostB_IP / HostB_MAC
- ARP target IP: HostA_IP

Expected later behavior:

- A second ping from HostA to HostB usually does not trigger another ARP request if the dynamic ARP cache entry is still valid.
- The same is true in the opposite direction from HostB to HostA once the mapping has been learned.
- If HostA has a static ARP entry for HostB, ARP resolution is suppressed because HostA already has a fixed IP-to-MAC mapping.

Concise explanation:

ARP is needed only when the sender does not already know the destination MAC address for a local IP. Dynamic caching and static ARP entries both remove the need for repeated broadcast requests, although static entries do so permanently until removed.
```

**Alternative (compact):**

```text
First ping learns the MAC with broadcast ARP. Later pings often skip ARP because the mapping is cached.
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
