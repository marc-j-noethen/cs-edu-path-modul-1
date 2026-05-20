# 🐍 Corporate Network Detective Workx

**Course:** Cyber Security Analyst – Network Technology | **Date:** 06 August 2025

---

## Task

**Goal:**  
Use local operating-system networking tools to document DHCP lease information, identify the default gateway, and explain how ARP visibility can reveal potential security concerns.

**Requirements:**

- Read the current address, gateway, DHCP server, and lease details from the chosen OS.

- Inspect the routing table and ARP/neighbor table.

- Answer the gateway and host-count questions correctly.

- Explain why unknown MAC addresses can be a warning sign.

- Output:
    
    - `Submit the final result in the exact format requested by the task.`
        
    - `A reviewer-readable final result`
        
    - `The submission artifact requested by the task`

---

## Solution

```text
# Inputs
context = 'Local analysis or lab environment'
objective = 'Use local operating-system networking tools to document DHCP lease information, identify the default gateway, and explain how ARP visibility can reveal potential security concerns.'
evidence = 'Submit the final result in the exact format requested by the task.'

# Main logic
Truthful solution pattern:

Q1. Default gateway
- Determine it from the default route entry in `route print`, `route get default`, or `ip route`.
- The correct answer format is: “My default gateway is <gateway-IP>, determined from the default route in the routing table.”

Q2. Possible host addresses
- Use the subnet mask / prefix length from the active interface.
- Formula: usable hosts = 2^(32 - prefix_length) - 2
- Example: `/24` -> 2^(32-24) - 2 = 254 usable hosts

Q3. Security concern
- Many unknown MAC addresses in the ARP table can mean you are sharing a large broadcast domain with many systems you do not recognize.
- In a corporate environment, that can indicate unmanaged devices, rogue systems, or simply a need for better inventory and segmentation.

What not to do:
- Do not invent your own gateway IP or lease timestamps.
- Do not assume `/24`; calculate the host count from the real subnet mask shown on your system.
```

**Alternative (compact):**

```text
Gateway = read the default route.
Host count = `2^(32-prefix) - 2`.
Unknown ARP neighbors can indicate unmanaged or suspicious devices.
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
