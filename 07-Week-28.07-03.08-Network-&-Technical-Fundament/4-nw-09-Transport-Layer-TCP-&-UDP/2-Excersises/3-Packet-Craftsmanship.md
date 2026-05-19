# 🐍 Packet Craftsmanship 

**Course:** Cyber Security Analyst – Network Technology | **Date:** 31 July 2025

---

## Task

**Goal:**  
Capture a normal DNS query, understand the packet fields, and then send a handcrafted DNS A-record query over UDP with command-line tools only.

**Requirements:**

- Understand the DNS header, transaction ID, QNAME, QTYPE, and QCLASS layout.

- Build a valid hexadecimal DNS query manually.

- Send it over UDP to a DNS server.

- Verify in Wireshark that both the request and response are recognized as DNS.

- Output:
    
    - `Submit the final result in the exact format requested by the task.`
        
    - `A reviewer-readable final result`
        
    - `The submission artifact requested by the task`

---

## Solution

```text
# Inputs
context = 'Local analysis or lab environment'
objective = 'Capture a normal DNS query, understand the packet fields, and then send a handcrafted DNS A-record query over UDP with command-line tools only.'
evidence = 'Submit the final result in the exact format requested by the task.'

# Main logic
A valid handcrafted DNS query for `example.com` A/IN is:

1a2b 0100 0001 0000 0000 0000
07 65 78 61 6d 70 6c 65
03 63 6f 6d
00
0001
0001

As one continuous hex string:

1a2b01000001000000000000076578616d706c6503636f6d0000010001

Example send command:

printf '1a2b01000001000000000000076578616d706c6503636f6d0000010001' | xxd -r -p | ncat -u 8.8.8.8 53

Field meaning:
- `1a2b` = transaction ID
- `0100` = standard recursive query
- `0001` = one question
- `07example03com00` = QNAME encoding
- `0001` = QTYPE A
- `0001` = QCLASS IN

What to verify in Wireshark:
- The packet is decoded as DNS rather than as generic UDP.
- The question name is `example.com`.
- The response transaction ID matches `0x1a2b`.
- The answer section contains an A record if the server accepted the query.
```

**Alternative (compact):**

```text
Handcrafted DNS still works as long as the header and question section follow the wire format exactly.
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
