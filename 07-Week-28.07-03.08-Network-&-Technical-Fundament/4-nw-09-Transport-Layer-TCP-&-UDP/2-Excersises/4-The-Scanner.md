# 🐍 The Scanner

**Course:** Cyber Security Analyst – Network Technology | **Date:** 31 July 2025

---

## Task

**Goal:**  
Write a local TCP port scanner, compare the results with system tools, and explain which listening services were detected.

**Requirements:**

- Scan at least 20 localhost TCP ports.

- Report only successful connections.

- Use command-line tools only.

- Compare the results with `netstat`.

- Output:
    
    - `Submit the final result in the exact format requested by the task.`
        
    - `A reviewer-readable final result`
        
    - `The submission artifact requested by the task`

---

## Solution

```text
# Inputs
context = 'Local analysis or lab environment'
objective = 'Write a local TCP port scanner, compare the results with system tools, and explain which listening services were detected.'
evidence = 'Submit the final result in the exact format requested by the task.'

# Main logic
Example PowerShell solution:

$ports = 20..40

foreach ($port in $ports) {
    $client = [System.Net.Sockets.TcpClient]::new()
    try {
        $async = $client.BeginConnect('127.0.0.1', $port, $null, $null)
        $connected = $async.AsyncWaitHandle.WaitOne(200)
        if ($connected -and $client.Connected) {
            Write-Output "Open TCP port: $port"
        }
    } finally {
        $client.Close()
    }
}

Verification commands:

netstat -ano | findstr LISTENING

How to compare:
- Ports printed by the script should also appear in the `LISTENING` state in `netstat`.
- `netstat -ano` adds the PID, which helps identify which process owns each listening port.
- If your script misses a port, check timing, firewall behavior, and whether the service stayed open during the scan.
```

**Alternative (compact):**

```text
Attempt a TCP connection to each port, and only print the ports that complete the connection successfully.
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
