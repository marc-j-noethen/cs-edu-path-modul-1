# 🐍 Subnet Sculptor

**Course:** Cyber Security Analyst – Network Technology | **Date:** 04 August 2025

---

## Task

**Goal:**  
Calculate the first two `/18` subnets inside `172.16.0.0/16`, assign working host and router addresses, and explain why the router can move traffic between the two subnets.

**Requirements:**

- Compute network, host range, and broadcast for the first two `/18` subnets.

- Explain the borrowed bits and resulting subnet/host counts.

- Choose valid IP assignments for both PCs and both router interfaces.

- Provide the IOS interface commands and routing explanation.

- Output:
    
    - `Submit the final result in the exact format requested by the task.`
        
    - `A reviewer-readable final result`
        
    - `The submission artifact requested by the task`

---

## Solution

```text
# Inputs
context = 'Local analysis or lab environment'
objective = 'Calculate the first two `/18` subnets inside `172.16.0.0/16`, assign working host and router addresses, and explain why the router can move traffic between the two subnets.'
evidence = 'Submit the final result in the exact format requested by the task.'

# Main logic
Subnet calculations:

Parent network: 172.16.0.0/16
New mask:       /18
Borrowed bits:  2

Total subnets created from the /16: 2^2 = 4
Hosts per /18 subnet: 2^(32-18) - 2 = 16382

Subnet 1
- Network:   172.16.0.0/18
- Usable:    172.16.0.1 - 172.16.63.254
- Broadcast: 172.16.63.255

Subnet 2
- Network:   172.16.64.0/18
- Usable:    172.16.64.1 - 172.16.127.254
- Broadcast: 172.16.127.255

Valid device assignments:

PC1:        172.16.0.10 /18   gateway 172.16.0.1
Router G0/0 172.16.0.1  /18

PC2:        172.16.64.10 /18  gateway 172.16.64.1
Router G0/1 172.16.64.1  /18

Example router commands:

interface GigabitEthernet0/0
 ip address 172.16.0.1 255.255.192.0
 no shutdown

interface GigabitEthernet0/1
 ip address 172.16.64.1 255.255.192.0
 no shutdown

Direct answers:
- Question 1: Borrowing 2 bits from the host portion changes `/16` to `/18`, which creates 4 smaller subnets while reducing hosts per subnet from 65534 to 16382.
- Question 2: Successful pings show that each host has the correct address, mask, and default gateway, and that the router is forwarding traffic between two different Layer 3 networks.
- Question 3: Cisco router interfaces are administratively down by default, so `no shutdown` is required before they can pass traffic.
```

**Alternative (compact):**

```text
`/16 -> /18` means 2 borrowed bits, 4 total subnets, and 16382 usable hosts per subnet.
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
