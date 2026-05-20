# 🐍 Mystery of Missing Addresses 

**Course:** Cyber Security Analyst – Network Technology | **Date:** 06 August 2025

---

## Task

**Goal:**  
Capture a full DORA exchange in Wireshark, identify the DHCP lease details, and explain what happens when the server does not answer.

**Requirements:**

- Capture Discover, Offer, Request, and Acknowledge packets.

- Record the offered IP, gateway, DNS servers, and lease time.

- Note the MAC address visible in the DHCP exchange.

- Answer the conceptual question about no-response behavior.

- Output:
    
    - `Submit the final result in the exact format requested by the task.`
        
    - `A reviewer-readable final result`
        
    - `The submission artifact requested by the task`

---

## Solution

```text
# Inputs
context = 'Local analysis or lab environment'
objective = 'Capture a full DORA exchange in Wireshark, identify the DHCP lease details, and explain what happens when the server does not answer.'
evidence = 'Submit the final result in the exact format requested by the task.'

# Main logic
Truthful answer structure:

1. DHCP Discover  -> client broadcasts because it does not yet have a valid address
2. DHCP Offer     -> server proposes an IP, subnet mask, gateway, DNS, and lease time
3. DHCP Request   -> client asks to use the offered configuration
4. DHCP ACK       -> server confirms the lease

What to extract from the capture:
- Offered IP address: use the `yiaddr` / offered-address field from the Offer or ACK
- Lease time: read DHCP option 51
- Default gateway: read DHCP option 3
- DNS servers: read DHCP option 6
- Your device MAC address: read the client hardware address field

Direct conceptual answer:

If the DHCP server does not answer a Discover message, the client typically retries the discovery process after a delay. Depending on the operating system, it may eventually leave the interface without a usable address or assign itself a link-local/APIPA-style address such as `169.254.0.0/16` so it can at least communicate locally.

Important truth note:
- The exact offered IP and lease time are environment-specific and must be copied from your actual capture, not invented in advance.
```

**Alternative (compact):**

```text
DORA = Discover, Offer, Request, Acknowledge. The exact lease values must come from the captured packets.
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
