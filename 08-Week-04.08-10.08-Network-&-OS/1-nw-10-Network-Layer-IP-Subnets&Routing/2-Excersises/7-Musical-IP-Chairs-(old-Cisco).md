# 🐍 Musical IP Chairs (old Cisco)

**Course:** Cyber Security Analyst – Network Technology | **Date:** 04 August 2025

---

## Task

**Goal:**  
Compare dynamic NAT without overload to PAT with overload, show why the three-address public pool is exhausted, and explain how port translation lets more clients share the same pool.

**Requirements:**

- Define the private ACL and the NAT pool.

- Configure dynamic NAT without overload first.

- Observe what happens when more clients need translations than the pool can provide.

- Convert the same pool to PAT and explain why the additional clients now work.

- Output:
    
    - `Submit the final result in the exact format requested by the task.`
        
    - `A reviewer-readable final result`
        
    - `The submission artifact requested by the task`

---

## Solution

```text
# Inputs
context = 'Local analysis or lab environment'
objective = 'Compare dynamic NAT without overload to PAT with overload, show why the three-address public pool is exhausted, and explain how port translation lets more clients share the same pool.'
evidence = 'Submit the final result in the exact format requested by the task.'

# Main logic
Dynamic NAT without overload:

access-list 10 permit 192.168.50.0 0.0.0.255
ip nat pool INNOVATECH_POOL 203.0.113.41 203.0.113.43 netmask 255.255.255.0
ip nat inside source list 10 pool INNOVATECH_POOL

Expected behavior:

- PC1, PC2, and PC3 can each consume one address from the three-IP pool.
- PC4 and PC5 fail while those three translations remain active because no unused public IP remains in the pool.
- `show ip nat statistics` or `show ip nat translations` will show the pool fully allocated and new translations failing.

PAT with the same pool:

no ip nat inside source list 10 pool INNOVATECH_POOL
ip nat inside source list 10 pool INNOVATECH_POOL overload

Direct answers:

- With overload enabled, all five PCs can reach the server because the router can now reuse each public IP for multiple sessions by separating them with transport identifiers.
- If the ISP had provided only one public IP in the pool and overload was enabled, the router could still NAT a very large number of simultaneous unique sessions by using different source ports.
- The primary limiting factor is the available transport/port space per translated IP, plus device resources such as NAT table memory.
```

**Alternative (compact):**

```text
Dynamic NAT without overload is limited by pool size. PAT stretches the same pool by distinguishing sessions with ports.
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
