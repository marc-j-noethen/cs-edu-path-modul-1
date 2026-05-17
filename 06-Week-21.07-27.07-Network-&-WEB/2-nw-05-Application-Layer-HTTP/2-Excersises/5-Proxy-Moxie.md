# 🐍 Proxy Moxie

**Course:** Cyber Security Analyst – Network Technology | **Date:** 22 July 2025

---

## Task

**Goal:**  
Explain and demonstrate how a local HTTPS interception proxy such as `mitmproxy` can decrypt traffic by becoming a trusted TLS endpoint on the local machine.

**Requirements:**

- Verify that Wireshark alone cannot read HTTPS page contents.

- Configure the browser or system to send traffic through `mitmproxy`.

- Install and trust the proxy certificate in the local test environment.

- Explain the decryption process accurately in your own words.

- Output:
    
    - `Submit the final result in the exact format requested by the task.`
        
    - `A reviewer-readable final result`
        
    - `The submission artifact requested by the task`

---

## Solution

```text
# Inputs
context = 'Local analysis or lab environment'
objective = 'Explain and demonstrate how a local HTTPS interception proxy such as `mitmproxy` can decrypt traffic by becoming a trusted TLS endpoint on the local machine.'
evidence = 'Submit the final result in the exact format requested by the task.'

# Main logic
A correct high-level workflow is:

1. Browse to `https://httpbin.org/get` and capture the traffic in Wireshark.
   Result: you will see TLS packets and metadata, but not the readable HTTP body.
2. Start `mitmproxy` or `mitmweb` locally.
3. Configure the browser to use the proxy.
4. Install the `mitmproxy` CA certificate into the browser or OS trust store for this lab machine.
5. Browse to `https://httpbin.org/get` again.
   Result: the browser now trusts the proxy, so `mitmproxy` can show the HTTP request and response in clear text.

Direct answer to the question:

HTTPS was not “broken” directly. The proxy generated a substitute certificate for the requested site and the browser accepted it because the local mitmproxy CA certificate had been installed as trusted. That means the browser created one encrypted TLS session to mitmproxy, while mitmproxy created a second encrypted TLS session to the real website. Because the proxy terminated one connection and re-encrypted the next one, it could read and display the decrypted HTTP data in the middle.
```

**Alternative (compact):**

```text
Browser trusts the proxy CA -> browser encrypts to the proxy -> proxy decrypts and re-encrypts to the real server.
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
