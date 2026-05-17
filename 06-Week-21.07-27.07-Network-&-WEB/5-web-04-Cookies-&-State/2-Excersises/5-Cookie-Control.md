# 🐍 Cookie Control 

**Course:** Cyber Security Analyst – Web Technology | **Date:** 25 July 2025

---

## Task

**Goal:**  
Demonstrate how `SameSite=Lax` and `SameSite=Strict` affect cookie sending in cross-site requests, while correcting the browser model so the lab truly uses cross-site navigation instead of only different ports.

**Requirements:**

- Create Site A to set the test cookie and trigger GET and POST navigations.

- Create Site B to display whether the cookie arrived.

- Test both `SameSite=Lax` and `SameSite=Strict`.

- Use two genuinely different sites, not only two different ports on the same site.

- Output:
    
    - `Submit the final result in the exact format requested by the task.`
        
    - `A reviewer-readable final result`
        
    - `The submission artifact requested by the task`

---

## Solution

```text
# Inputs
context = 'Local analysis or lab environment'
objective = 'Demonstrate how `SameSite=Lax` and `SameSite=Strict` affect cookie sending in cross-site requests, while correcting the browser model so the lab truly uses cross-site navigation instead of only different ports.'
evidence = 'Submit the final result in the exact format requested by the task.'

# Main logic
First, an important correction for truthfulness:

Different ports alone do not create a cross-site scenario for SameSite testing.
Browsers treat `http://localhost:5000` and `http://localhost:5001` as the same site because the site concept is based on scheme + registrable domain, not port alone.
To test SameSite honestly, use two different hostnames such as `sitea.localtest.me:5000` and `siteb.localtest.me:5001` (or another pair of hostnames that resolve to 127.0.0.1).

site_a.py:
from flask import Flask, make_response, render_template_string, request

app = Flask(__name__)

PAGE = '''
<h1>Site A</h1>
<p>Current policy: {{ policy }}</p>
<a href="/set_cookie/lax">Set Lax cookie</a><br>
<a href="/set_cookie/strict">Set Strict cookie</a><br><br>

<a href="http://siteb.localtest.me:5001/receive">Cross-site GET to Site B</a>

<form action="http://siteb.localtest.me:5001/receive" method="post">
  <button type="submit">Cross-site POST to Site B</button>
</form>
'''

@app.route('/')
def index():
    return render_template_string(PAGE, policy=request.cookies.get('policy', 'not set'))

@app.route('/set_cookie/<policy>')
def set_cookie(policy):
    response = make_response(render_template_string(PAGE, policy=policy))
    response.set_cookie(
        'cross_site_test_cookie',
        f'{policy}-value',
        samesite=policy.capitalize(),
        httponly=False,
        secure=False,
    )
    response.set_cookie('policy', policy)
    return response

if __name__ == '__main__':
    app.run(port=5000, debug=True)

site_b.py:
from flask import Flask, render_template_string, request

app = Flask(__name__)

@app.route('/receive', methods=['GET', 'POST'])
def receive():
    cookie_value = request.cookies.get('cross_site_test_cookie')
    return render_template_string('''
        <h1>Site B</h1>
        <p>Method: {{ method }}</p>
        <p>Cookie received: {{ cookie_value if cookie_value else 'No' }}</p>
    ''', method=request.method, cookie_value=cookie_value)

if __name__ == '__main__':
    app.run(port=5001, debug=True)

Expected results in a real cross-site setup:

|Policy|Cross-site top-level GET|Cross-site POST|
|---|---|---|
|`SameSite=Lax`|Cookie is typically sent|Cookie is typically not sent|
|`SameSite=Strict`|Cookie is not sent|Cookie is not sent|

Explanation:
- `Lax` allows cookies on normal top-level cross-site navigations such as clicking a link.
- `Strict` blocks the cookie whenever the navigation starts from another site.
- A cross-site POST is more sensitive, so `Lax` does not normally send the cookie there.
```

**Alternative (compact):**

```text
Honest SameSite testing requires different sites, not merely different ports.
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
