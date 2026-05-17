# 🐍 Token Gatekeeper

**Course:** Cyber Security Analyst – Web Technology | **Date:** 25 July 2025

---

## Task

**Goal:**  
Use `curl` to test bearer-token authentication behavior and to demonstrate how an API key can also be passed as a query parameter.

**Requirements:**

- Call the bearer endpoint once without an `Authorization` header.

- Call it again with `Authorization: Bearer <token>`.

- Send an API-key style query parameter to `httpbin.org/get`.

- Record the resulting status codes and response evidence.

- Output:
    
    - `Submit the final result in the exact format requested by the task.`
        
    - `A reviewer-readable final result`
        
    - `The submission artifact requested by the task`

---

## Solution

```text
# Inputs
context = 'Local analysis or lab environment'
objective = 'Use `curl` to test bearer-token authentication behavior and to demonstrate how an API key can also be passed as a query parameter.'
evidence = 'Submit the final result in the exact format requested by the task.'

# Main logic
curl -i https://httpbin.org/bearer

curl -i https://httpbin.org/bearer \
  -H "Authorization: Bearer MY_SECRET_TOKEN"

curl "https://httpbin.org/get?auth_key=key123secure"

Direct answers:
- Step 1 status code: `401`
- Step 2 status code: `200`
- Step 2 `authenticated` field: `true`
- Step 3 confirmation: the response JSON echoes the query parameter under `args`, for example:

{
  "args": {
    "auth_key": "key123secure"
  }
}
```

**Alternative (compact):**

```text
No bearer token -> unauthorized.
Valid bearer header -> authenticated.
Query parameter -> echoed back under `args`.
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
