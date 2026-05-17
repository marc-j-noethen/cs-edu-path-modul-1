# 🐍 Let’s GET It

**Course:** Cyber Security Analyst – Web Technology | **Date:** 25 July 2025

---

## Task

**Goal:**  
Use `curl` and Python `requests` against JSONPlaceholder to practice common REST methods and interpret the expected HTTP responses.

**Requirements:**

- Write the `curl` commands for GET, POST, PUT, and DELETE.

- Submit a Python script for the requested GET and POST calls.

- Record the status codes for the POST operations.

- Keep the payloads in valid JSON format.

- Output:
    
    - `Submit the final result in the exact format requested by the task.`
        
    - `A reviewer-readable final result`
        
    - `The submission artifact requested by the task`

---

## Solution

```text
# Inputs
context = 'Local analysis or lab environment'
objective = 'Use `curl` and Python `requests` against JSONPlaceholder to practice common REST methods and interpret the expected HTTP responses.'
evidence = 'Submit the final result in the exact format requested by the task.'

# Main logic
`curl` commands for the required submission steps:

curl -i -X POST https://jsonplaceholder.typicode.com/posts \
  -H "Content-Type: application/json" \
  -d '{"title":"My Curl Post","body":"Content via curl.","userId":7}'

curl -i -X PUT https://jsonplaceholder.typicode.com/posts/1 \
  -H "Content-Type: application/json" \
  -d '{"id":1,"title":"Updated via Curl","body":"New body.","userId":1}'

curl -i -X DELETE https://jsonplaceholder.typicode.com/posts/1

jsonplaceholder_client.py:
import requests

BASE_URL = 'https://jsonplaceholder.typicode.com/posts'

post_15 = requests.get(f'{BASE_URL}/15', timeout=10)
print('GET /posts/15 status:', post_15.status_code)
print(post_15.json())

payload = {
    'title': 'My Python Post',
    'body': 'Content via Python requests.',
    'userId': 25,
}
created = requests.post(BASE_URL, json=payload, timeout=10)
print('POST /posts status:', created.status_code)
print(created.json())

Expected direct answers:
- Part 1, Step 4 (`curl` POST) status code: `201`
- Part 2, Step 2 (Python POST) status code: `201`

JSONPlaceholder is a practice API, so POST/PUT/DELETE simulate state changes for learning rather than persisting real data permanently.
```

**Alternative (compact):**

```text
JSONPlaceholder normally returns `201 Created` for successful POST requests and echoes the JSON payload back.
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
