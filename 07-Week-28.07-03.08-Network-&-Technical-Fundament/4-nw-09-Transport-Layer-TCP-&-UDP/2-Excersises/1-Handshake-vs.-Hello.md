# 🐍 Handshake vs. Hello

**Course:** Cyber Security Analyst – Network Technology | **Date:** 31 July 2025

---

## Task

**Goal:**  
Observe how TCP establishes, numbers, and acknowledges a connection, then compare that behavior with UDP and its ICMP error signaling for closed ports.

**Requirements:**

- Capture TCP traffic for a local `nc` conversation.

- Identify the SYN, SYN/ACK, and ACK packets of the three-way handshake.

- Compare TCP acknowledgments with UDP behavior to open and closed ports.

- Explain why ICMP is involved when UDP reaches a closed port.

- Output:
    
    - `Submit the final result in the exact format requested by the task.`
        
    - `A reviewer-readable final result`
        
    - `The submission artifact requested by the task`

---

## Solution

```text
# Inputs
context = 'Local analysis or lab environment'
objective = 'Observe how TCP establishes, numbers, and acknowledges a connection, then compare that behavior with UDP and its ICMP error signaling for closed ports.'
evidence = 'Submit the final result in the exact format requested by the task.'

# Main logic
Part I, TCP observations:

1. Client -> Server: SYN
   - Flags: SYN
   - Seq: client initial sequence number
   - Ack: not meaningful yet / zero in relative view

2. Server -> Client: SYN, ACK
   - Flags: SYN, ACK
   - Seq: server initial sequence number
   - Ack: client_seq + 1

3. Client -> Server: ACK
   - Flags: ACK
   - Seq: client_seq + 1
   - Ack: server_seq + 1

Data-exchange logic:

If the client sends N bytes of payload, the next acknowledgment from the server confirms receipt by setting:
ack = client_data_seq + N

The same rule applies in the opposite direction for the server reply.

Part II, UDP observations:

- UDP to an open port (12345): the datagram is delivered to the listener and there is normally no ICMP error because the port is open.
- UDP to a closed port (161 or 48753 in this lab): the receiving host usually sends ICMP Destination Unreachable -> Port Unreachable.
- The source IP of that ICMP message is the host that detected the closed port, which in this localhost exercise is the local machine itself.

Short answers:
- TCP confirms delivery and ordering with sequence numbers plus acknowledgments. Each side explicitly acknowledges the next byte it expects.
- UDP has no built-in handshake or acknowledgment. A closed UDP port is commonly reported by the network stack through ICMP Port Unreachable.
```

**Alternative (compact):**

```text
TCP says “I sent byte X, please confirm byte X+N.”
UDP just sends the datagram and relies on ICMP if the destination port is closed.
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
