# 🐍 Firewall Houdini

**Course:** Cyber Security Analyst – Network Technology | **Date:** 07 August 2025

---

## Task

**Goal:**  
Block direct HTTP access from Windows to Kali with the Windows firewall, then bypass that direct-path block by carrying the HTTP traffic through an SSH local-forward tunnel instead.

**Requirements:**

- Create an outbound Windows firewall rule that blocks direct TCP access to Kali’s HTTP port.

- Verify the direct browser/curl path fails.

- Create an SSH local port forward to Kali’s HTTP service.

- Explain why the tunnel still works despite the direct HTTP block.

- Output:
    
    - `Submit the final result in the exact format requested by the task.`
        
    - `A reviewer-readable final result`
        
    - `The submission artifact requested by the task`

---

## Solution

```text
# Inputs
context = 'Local analysis or lab environment'
objective = 'Block direct HTTP access from Windows to Kali with the Windows firewall, then bypass that direct-path block by carrying the HTTP traffic through an SSH local-forward tunnel instead.'
evidence = 'Submit the final result in the exact format requested by the task.'

# Main logic
Example Windows firewall rule:

New-NetFirewallRule -DisplayName "Block Kali HTTP" -Direction Outbound -Protocol TCP -RemoteAddress 192.168.56.20 -RemotePort 8000 -Action Block

Example remote HTTP service:

python3 -m http.server 8000

SSH local forward from Windows:

ssh -L 9999:127.0.0.1:8000 your_username@192.168.56.20

Direct explanation:

The firewall rule blocks direct outbound TCP connections from Windows to Kali on port 8000. The SSH tunnel does not use that blocked path. Instead, Windows opens an SSH connection to Kali on port 22, and the browser connects only to `localhost:9999` on Windows. SSH then carries the HTTP traffic inside the already-established SSH session and delivers it to `127.0.0.1:8000` on Kali.
```

**Alternative (compact):**

```text
Blocked path: Windows -> Kali:8000
Working path: Windows -> SSH on Kali:22 -> forwarded locally on Kali to 8000
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
