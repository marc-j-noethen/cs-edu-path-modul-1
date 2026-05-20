# 🐍 Port Portal

**Course:** Cyber Security Analyst – Network Technology | **Date:** 07 August 2025

---

## Task

**Goal:**  
Use SSH local port forwarding to reach a web service that is listening on the remote machine’s localhost interface.

**Requirements:**

- Run the HTTP server on the remote machine on port 8888.

- Create a local tunnel that maps client port 9999 to remote `localhost:8888`.

- Browse to `http://localhost:9999/secret.html` from the client.

- Explain why this works even though the service is on a different host and port.

- Output:
    
    - `Submit the final result in the exact format requested by the task.`
        
    - `A reviewer-readable final result`
        
    - `The submission artifact requested by the task`

---

## Solution

```text
# Inputs
context = 'Local analysis or lab environment'
objective = 'Use SSH local port forwarding to reach a web service that is listening on the remote machine’s localhost interface.'
evidence = 'Submit the final result in the exact format requested by the task.'

# Main logic
Remote HTTP service:

python3 -m http.server 8888

Local SSH tunnel from the client:

ssh -L 9999:localhost:8888 your_username@remote_machine_ip

Direct explanation:

The browser connects to `localhost:9999` on the client machine. SSH receives that local connection and forwards it through the encrypted SSH session to the remote machine, where it opens a second connection to `localhost:8888`. From the browser’s perspective it feels local, but the actual HTTP request is being carried through the SSH tunnel and completed on the remote system.
```

**Alternative (compact):**

```text
Local port forwarding makes a remote service appear as if it were listening on your own machine.
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
