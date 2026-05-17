# 🐍 Socket To 'Em

**Course:** Cyber Security Analyst – Network Technology | **Date:** 22 July 2025

---

## Task

**Goal:**  
Reproduce the earlier browser form submission as a manually crafted raw HTTP POST request sent through `ncat`, then compare it with the browser-generated traffic in Wireshark.

**Requirements:**

- Use the same endpoint and form body as Exercise 2.

- Include a valid request line, `Host`, `Content-Type`, and `Content-Length` headers.

- Send the request over plain HTTP so the request stays readable.

- Compare the manual request against the browser request in Wireshark.

- Output:
    
    - `Submit the final result in the exact format requested by the task.`
        
    - `A reviewer-readable final result`
        
    - `The submission artifact requested by the task`

---

## Solution

```text
# Inputs
context = 'Local analysis or lab environment'
objective = 'Reproduce the earlier browser form submission as a manually crafted raw HTTP POST request sent through `ncat`, then compare it with the browser-generated traffic in Wireshark.'
evidence = 'Submit the final result in the exact format requested by the task.'

# Main logic
Example request, based on the body used in `Formidable POST`:

        ```text
        POST /forms/post HTTP/1.1
        Host: httpbin.org
        Content-Type: application/x-www-form-urlencoded
        Content-Length: 102
        Connection: close

        custname=Alice&custtel=123456&custemail=alice%40example.com&size=medium&delivery=13%3A00&comments=Test
        ```

        One workable way to send it with `ncat` is:

        ```bash
        printf 'POST /forms/post HTTP/1.1

Host: httpbin.org

Content-Type: application/x-www-form-urlencoded

Content-Length: 102

Connection: close

custname=Alice&custtel=123456&custemail=alice%%40example.com&size=medium&delivery=13%%3A00&comments=Test' | ncat httpbin.org 80
        ```

        What should match the browser request:
        - Method: `POST`
        - Path: `/forms/post`
        - Header: `Content-Type: application/x-www-form-urlencoded`
        - Body format: `key=value&key=value...`

        What may differ slightly:
        - `User-Agent`
        - header ordering
        - optional headers such as `Accept` or `Accept-Encoding`

        The important truth is that HTTP/1.1 requires a correct `Content-Length` for a manual body, and every line must end with CRLF (`\r\n`).
```

**Alternative (compact):**

```text
Same endpoint + same body + correct Content-Length = browser-like POST request.
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
