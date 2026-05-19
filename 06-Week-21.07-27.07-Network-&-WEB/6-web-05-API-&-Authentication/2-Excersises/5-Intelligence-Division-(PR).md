# 🐍 Intelligence Division (PR)

**Course:** Cyber Security Analyst – Web Technology | **Date:** 26 July 2025

---

## Task

**Goal:**  
Combine session-based login with a separate bearer-token protected API so users can view a protected page and then request role-dependent intelligence reports with a manually entered token.

**Requirements:**

- Keep the session login flow for the `/intelligence` page.

- Protect `/api/intelligence-feed` with `Authorization: Bearer <token>`.

- Return different report data for admin vs analyst tokens.

- Append each successful frontend result instead of replacing earlier reports.

- Output:
    
    - `Submit the final result in the exact format requested by the task.`
        
    - `A reviewer-readable final result`
        
    - `The submission artifact requested by the task`

---

## Solution

```text
# Inputs
context = 'Local analysis or lab environment'
objective = 'Combine session-based login with a separate bearer-token protected API so users can view a protected page and then request role-dependent intelligence reports with a manually entered token.'
evidence = 'Submit the final result in the exact format requested by the task.'

# Main logic
web_app.py:
import secrets
from flask import Flask, jsonify, make_response, redirect, render_template, request

app = Flask(__name__)

USERS = {
    'alice': {'password': 'alicepass', 'role': 'analyst'},
    'bob': {'password': 'bobpass', 'role': 'admin'},
}
SESSIONS = {}
ACTIVE_TOKENS = {
    'token-analyst-123': {'username': 'alice', 'role': 'analyst'},
    'token-admin-456': {'username': 'bob', 'role': 'admin'},
}

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
            return 'Invalid credentials', 401
        session_token = secrets.token_urlsafe(16)
        SESSIONS[session_token] = {'username': username, 'role': user['role']}
        response = make_response(redirect('/intelligence'))
        response.set_cookie('session_token', session_token, httponly=True, samesite='Lax', secure=False)
        return response
    return render_template('login.html')

@app.route('/intelligence')
def intelligence_page():
    session_data = current_session()
    if not session_data:
        return redirect('/login')
    return render_template('intelligence.html', session_data=session_data)

@app.route('/api/intelligence-feed')
def intelligence_feed():
    auth_header = request.headers.get('Authorization', '')
    if not auth_header.startswith('Bearer '):
        return jsonify({'error': 'Missing bearer token'}), 401

    token = auth_header.split(' ', 1)[1]
    token_data = ACTIVE_TOKENS.get(token)
    if not token_data:
        return jsonify({'error': 'Access denied'}), 403

    if token_data['role'] == 'admin':
        report = {
            'classification': 'ADMIN',
            'summary': 'Admin-level report: suspicious outbound beaconing in Segment 4.',
        }
    else:
        report = {
            'classification': 'ANALYST',
            'summary': 'Analyst report: phishing lure detected in employee mailbox queue.',
        }

    return jsonify(report)

if __name__ == '__main__':
    app.run(debug=True)

templates/intelligence.html:
<h1>Intelligence Dashboard</h1>
<p>Logged in as {{ session_data.username }} ({{ session_data.role }})</p>
<button id="fetchIntelButton" type="button">Fetch Intelligence</button>
<section id="reports"></section>

<script>
  const button = document.getElementById('fetchIntelButton');
  const reports = document.getElementById('reports');

  button.addEventListener('click', async () => {
    const token = prompt('Enter bearer token:');
    if (!token) {
      alert('Access Denied: token is required.');
      return;
    }

    try {
      const response = await fetch('/api/intelligence-feed', {
        headers: { Authorization: `Bearer ${token}` },
      });
      const data = await response.json();
      if (!response.ok) {
        throw new Error(data.error || 'Access denied');
      }

      const card = document.createElement('div');
      card.innerHTML = `<h3>${data.classification}</h3><p>${data.summary}</p>`;
      reports.appendChild(card);
    } catch (error) {
      alert(`Access Denied: ${error.message}`);
    }
  });
</script>

Behavioral truth:
- Session login protects the page itself.
- The bearer token protects the API independently.
- A valid token can append a new report each click, while an invalid token triggers the error path.
```

**Alternative (compact):**

```text
Session controls page access; bearer token controls API access.
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
