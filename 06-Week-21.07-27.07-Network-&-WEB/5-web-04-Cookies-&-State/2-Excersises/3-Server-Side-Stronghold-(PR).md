# 🐍 Server-Side Stronghold (PR) 

**Course:** Cyber Security Analyst – Web Technology | **Date:** 25 July 2025

---

## Task

**Goal:**  
Extend the session-based Flask app with role-based authorization so only server-stored session data decides whether a user may view user or admin dashboards.

**Requirements:**

- Authenticate against a hardcoded user dictionary.

- Create a session token after successful login.

- Allow all logged-in users to access the user dashboard.

- Restrict the admin dashboard to users whose server-side session role is `admin`.

- Output:
    
    - `Submit the final result in the exact format requested by the task.`
        
    - `A reviewer-readable final result`
        
    - `The submission artifact requested by the task`

---

## Solution

```text
# Inputs
context = 'Local analysis or lab environment'
objective = 'Extend the session-based Flask app with role-based authorization so only server-stored session data decides whether a user may view user or admin dashboards.'
evidence = 'Submit the final result in the exact format requested by the task.'

# Main logic
import secrets
from flask import Flask, abort, make_response, redirect, render_template_string, request

app = Flask(__name__)

USERS = {
    'alice': {'password': 'alicepass', 'role': 'user'},
    'bob': {'password': 'bobpass', 'role': 'admin'},
}
SESSIONS = {}

def current_session():
    token = request.cookies.get('session_token')
    return SESSIONS.get(token)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username', '')
        password = request.form.get('password', '')
        user = USERS.get(username)
        if not user or user['password'] != password:
            return render_template_string('<p>Invalid credentials.</p>' + LOGIN_TEMPLATE), 401

        token = secrets.token_urlsafe(16)
        SESSIONS[token] = {'username': username, 'role': user['role']}
        response = make_response(redirect('/dashboard'))
        response.set_cookie('session_token', token, httponly=True, samesite='Lax', secure=False)
        return response

    return render_template_string(LOGIN_TEMPLATE)

@app.route('/logout')
def logout():
    token = request.cookies.get('session_token')
    if token:
        SESSIONS.pop(token, None)
    response = make_response(redirect('/login'))
    response.delete_cookie('session_token')
    return response

@app.route('/dashboard')
def dashboard():
    session_data = current_session()
    if not session_data:
        return redirect('/login')
    return render_template_string(
        '<h1>User Dashboard</h1><p>{{ username }} ({{ role }})</p>{% if role == "admin" %}<a href="/admin">Admin Dashboard</a>{% endif %}',
        username=session_data['username'],
        role=session_data['role'],
    )

@app.route('/admin')
def admin_dashboard():
    session_data = current_session()
    if not session_data:
        return redirect('/login')
    if session_data['role'] != 'admin':
        abort(403)
    return '<h1>Admin Dashboard</h1><p>Restricted content</p>'

LOGIN_TEMPLATE = '''
<form method="post">
  <input name="username" placeholder="Username" required>
  <input name="password" type="password" placeholder="Password" required>
  <button type="submit">Login</button>
</form>
'''

if __name__ == '__main__':
    app.run(debug=True)

Conceptual answer:

Server-side role storage is safer because the browser only holds an opaque session identifier. If role information lived directly in a client-side cookie, a user could modify that cookie and try to turn `user` into `admin`. When the server owns the session state, the browser cannot grant itself extra privileges by editing local data.
```

**Alternative (compact):**

```text
Authorization must trust the server-side session, not the browser’s editable storage.
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
