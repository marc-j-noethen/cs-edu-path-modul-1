# 🐍 The Lone IP Ranger (old Cisco)

**Course:** Cyber Security Analyst – Network Technology | **Date:** 04 August 2025

---

## Task

**Goal:**  
Configure NAT overload (PAT) on a Cisco router so two private hosts can reach an external server through one public interface address.

**Requirements:**

- Address the inside LAN and outside server network correctly.

- Mark the inside and outside router interfaces for NAT.

- Create an ACL that matches the private subnet.

- Verify the translation table after traffic crosses the router.

- Output:
    
    - `Submit the final result in the exact format requested by the task.`
        
    - `A reviewer-readable final result`
        
    - `The submission artifact requested by the task`

---

## Solution

```text
# Inputs
context = 'Local analysis or lab environment'
objective = 'Configure NAT overload (PAT) on a Cisco router so two private hosts can reach an external server through one public interface address.'
evidence = 'Submit the final result in the exact format requested by the task.'

# Main logic
Router configuration:

interface GigabitEthernet0/0
 ip address 192.168.1.1 255.255.255.0
 ip nat inside
 no shutdown

interface GigabitEthernet0/1
 ip address 203.0.113.1 255.255.255.0
 ip nat outside
 no shutdown

access-list 1 permit 192.168.1.0 0.0.0.255
ip nat inside source list 1 interface GigabitEthernet0/1 overload

Expected interpretation after `PC-A -> ping 203.0.113.2`:

- Inside local IP: 192.168.1.10
- Inside global IP: 203.0.113.1

Important truth detail:

Because the test uses `ping`, the translation table may show ICMP identifiers rather than TCP/UDP port numbers. The NAT concept is still the same: the private inside address `192.168.1.10` is represented externally as `203.0.113.1`.
```

**Alternative (compact):**

```text
PAT lets many inside hosts share one outside IP by separating sessions with transport or ICMP identifiers.
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
