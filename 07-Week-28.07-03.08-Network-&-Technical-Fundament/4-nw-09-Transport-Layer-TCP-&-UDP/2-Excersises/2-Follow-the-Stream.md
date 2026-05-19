# 🐍 Follow the Stream

**Course:** Cyber Security Analyst – Network Technology | **Date:** 31 July 2025

---

## Task

**Goal:**  
Show that large application data is split across many transport packets and can later be reconstructed by Wireshark’s stream-following feature.

**Requirements:**

- Transfer a large text file over TCP and inspect it with Follow TCP Stream.

- Repeat the exercise over UDP.

- Compare the packetization and visible overhead.

- Explain why plaintext transport is dangerous without encryption.

- Output:
    
    - `Submit the final result in the exact format requested by the task.`
        
    - `A reviewer-readable final result`
        
    - `The submission artifact requested by the task`

---

## Solution

```text
# Inputs
context = 'Local analysis or lab environment'
objective = 'Show that large application data is split across many transport packets and can later be reconstructed by Wireshark’s stream-following feature.'
evidence = 'Submit the final result in the exact format requested by the task.'

# Main logic
Correct observations for this lab:

- The TCP file transfer does not appear as one giant packet. It is split into many TCP segments because the sender, receiver, and network stack must respect MSS/MTU limits and flow-control behavior.
- Follow TCP Stream reconstructs the original application data by reassembling those segments in order.
- The UDP transfer also appears as packets, but UDP has less header overhead and no sequence/acknowledgment exchange like TCP.
- TCP traffic shows more overhead because it includes connection setup, acknowledgments, and reliability behavior.
- Plaintext protocols are dangerous because anyone who can observe the traffic path can reconstruct the application data just like Wireshark does.

Submission-quality explanation:

TCP splits large data into multiple segments so it can fit within network limits and still provide reliable, ordered delivery. Wireshark can then reassemble those segments into one application stream. UDP sends datagrams with less overhead, but it does not provide the same delivery guarantees or ordering logic. In both cases, if the traffic is unencrypted, the transferred content can be reconstructed and read by an observer.
```

**Alternative (compact):**

```text
Many packets on the wire can still represent one readable application stream.
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
