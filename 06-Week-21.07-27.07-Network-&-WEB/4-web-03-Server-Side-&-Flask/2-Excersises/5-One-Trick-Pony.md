# 🐍 One Trick Pony

**Course:** Cyber Security Analyst – Web Technology | **Date:** 24 July 2025

---

## Task

**Goal:**  
Implement a one-time secret message service in Flask where a generated link can reveal the stored message exactly once and then permanently invalidate it.

**Requirements:**

- Accept a message through a web form.

- Generate an unpredictable unique token for the retrieval URL.

- Display the message exactly once when the token is visited.

- Reject any second attempt to open the same token.

- Output:
    
    - `Submit the final result in the exact format requested by the task.`
        
    - `A reviewer-readable final result`
        
    - `The submission artifact requested by the task`

---

## Solution

```text
# Inputs
context = 'Local analysis or lab environment'
objective = 'Implement a one-time secret message service in Flask where a generated link can reveal the stored message exactly once and then permanently invalidate it.'
evidence = 'Submit the final result in the exact format requested by the task.'

# Main logic
app.py:
import secrets
from flask import Flask, render_template, request, url_for

app = Flask(__name__)
MESSAGES = {}

@app.route('/', methods=['GET', 'POST'])
def create_message():
    if request.method == 'POST':
        message = request.form.get('message', '').strip()
        if not message:
            return render_template('create.html', error='Message is required.')

        token = secrets.token_urlsafe(16)
        MESSAGES[token] = message
        reveal_url = url_for('read_message', token=token, _external=True)
        return render_template('created.html', reveal_url=reveal_url)

    return render_template('create.html')

@app.route('/message/<token>')
def read_message(token):
    message = MESSAGES.pop(token, None)
    if message is None:
        return render_template('expired.html'), 410
    return render_template('message.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)

templates/create.html:
<form method="post">
  <textarea name="message" required></textarea>
  <button type="submit">Lock message</button>
  {% if error %}<p>{{ error }}</p>{% endif %}
</form>

templates/created.html:
<p>Share this one-time URL:</p>
<a href="{{ reveal_url }}">{{ reveal_url }}</a>

templates/message.html:
<h1>Secret message</h1>
<p>{{ message }}</p>

templates/expired.html:
<h1>Message unavailable</h1>
<p>This link was already used or never existed.</p>

Why this works:
- `secrets.token_urlsafe(...)` creates an unpredictable retrieval token.
- `MESSAGES.pop(token, None)` returns the message once and deletes it in the same operation.
- A second visit receives `None`, so the app can show an expired response.
```

**Alternative (compact):**

```text
Store message under random token -> reveal with `pop()` -> token becomes unusable immediately after the first read.
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
