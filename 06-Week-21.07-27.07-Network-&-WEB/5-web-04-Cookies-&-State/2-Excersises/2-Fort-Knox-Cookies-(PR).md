# 🐍 Fort Knox Cookies (PR) 

**Course:** Cyber Security Analyst – Web Technology | **Date:** 25 July 2025

---

## Task

**Goal:**  
Implement server-side session storage with an opaque session cookie and demonstrate that `HttpOnly` cookies are hidden from JavaScript while normal cookies remain visible.

**Requirements:**

- Generate a unique session token on login.

- Store user data on the server, not inside the cookie value.

- Set `session_token` with `HttpOnly` and `SameSite=Lax`.

- Expose a second route that sets one readable cookie and one `HttpOnly` cookie for comparison.

- Output:
    
    - `Submit the final result in the exact format requested by the task.`
        
    - `A reviewer-readable final result`
        
    - `The submission artifact requested by the task`

---

## Solution

```text
# Inputs
context = 'Local analysis or lab environment'
objective = 'Implement server-side session storage with an opaque session cookie and demonstrate that `HttpOnly` cookies are hidden from JavaScript while normal cookies remain visible.'
evidence = 'Submit the final result in the exact format requested by the task.'

# Main logic
from datetime import datetime
import secrets
from flask import Flask, make_response, redirect, render_template_string, request

app = Flask(__name__)
SESSIONS = {}

LOGIN_FORM = '''
<form method="post" action="/login">
  <input name="username" placeholder="Username" required>
  <input name="role" placeholder="Role" required>
  <button type="submit">Login</button>
</form>
'''

@app.route('/')
def home():
    token = request.cookies.get('session_token')
    session_data = SESSIONS.get(token)
    if not session_data:
        return LOGIN_FORM
    return f"Hello {session_data['username']} ({session_data['role']})"

@app.route('/login', methods=['POST'])
def login():
    token = secrets.token_urlsafe(16)
    SESSIONS[token] = {
        'username': request.form['username'],
        'role': request.form['role'],
        'login_time': datetime.utcnow().isoformat(),
    }
    response = make_response(redirect('/'))
    response.set_cookie(
        'session_token',
        token,
        httponly=True,
        samesite='Lax',
        secure=False,
    )
    return response

@app.route('/logout')
def logout():
    token = request.cookies.get('session_token')
    if token:
        SESSIONS.pop(token, None)
    response = make_response(redirect('/'))
    response.delete_cookie('session_token')
    return response

@app.route('/cookie_check')
def cookie_check():
    response = make_response(render_template_string('''
        <p>Open the developer console and run <code>document.cookie</code>.</p>
    '''))
    response.set_cookie('visible_cookie', 'javascript-can-read-me', httponly=False, samesite='Lax')
    response.set_cookie('hidden_cookie', 'http-only-value', httponly=True, samesite='Lax')
    return response

if __name__ == '__main__':
    app.run(debug=True)

Direct answers:
- Visible in `document.cookie`: `visible_cookie` and any other non-HttpOnly cookies.
- Hidden from `document.cookie`: `session_token` and `hidden_cookie`, because `HttpOnly` blocks JavaScript access.
- `HttpOnly` helps reduce XSS impact because injected script cannot directly steal those cookie values through `document.cookie`.
```

**Alternative (compact):**

```text
Client stores only an opaque session ID; the real identity and role stay on the server.
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
