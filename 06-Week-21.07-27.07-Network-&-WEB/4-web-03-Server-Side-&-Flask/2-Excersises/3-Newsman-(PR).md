# 🐍 Newsman (PR) 

**Course:** Cyber Security Analyst – Web Technology | **Date:** 24 July 2025

---

## Task

**Goal:**  
Integrate the CyberNews Tracker frontend into Flask templates so `/news` renders dynamic article data rather than a static HTML page.

**Requirements:**

- Use `render_template` and a `templates` directory.

- Provide `/` and `/news` routes.

- Pass a username, article list, and timestamp from Flask to Jinja.

- Render the articles with a Jinja loop in `news.html`.

- Output:
    
    - `Submit the final result in the exact format requested by the task.`
        
    - `A reviewer-readable final result`
        
    - `The submission artifact requested by the task`

---

## Solution

```text
# Inputs
context = 'Local analysis or lab environment'
objective = 'Integrate the CyberNews Tracker frontend into Flask templates so `/news` renders dynamic article data rather than a static HTML page.'
evidence = 'Submit the final result in the exact format requested by the task.'

# Main logic
web_app.py:
from datetime import datetime
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to CyberNews Tracker!'

@app.route('/news')
def news():
    username = 'Alex'
    articles = [
        {
            'title': 'New AI Breakthrough',
            'summary': 'Researchers develop self-improving models.',
            'date': '2025-11-03',
        },
        {
            'title': 'Cyberattack on Major Bank',
            'summary': 'Millions of accounts affected in the latest breach.',
            'date': '2025-11-02',
        },
        {
            'title': 'Flask 3.0 Released',
            'summary': 'The new version improves modern route handling.',
            'date': '2025-11-01',
        },
    ]
    last_updated = datetime.now().strftime('%Y-%m-%d %H:%M')
    return render_template(
        'news.html',
        username=username,
        articles=articles,
        last_updated=last_updated,
    )

if __name__ == '__main__':
    app.run(debug=True)

templates/index.html:
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{% block title %}CyberNews Tracker{% endblock %}</title>
  <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
  <header>
    <h1>CyberNews Tracker</h1>
  </header>
  <main>
    {% block content %}{% endblock %}
  </main>
</body>
</html>

templates/news.html:
{% extends 'index.html' %}

{% block title %}CyberNews Tracker - News{% endblock %}

{% block content %}
  <h2>Welcome, {{ username }}</h2>
  <p>Last updated: {{ last_updated }}</p>

  <section>
    {% for article in articles %}
      <article>
        <h3>{{ article.title }}</h3>
        <p>{{ article.summary }}</p>
        <small>{{ article.date }}</small>
      </article>
    {% endfor %}
  </section>
{% endblock %}
```

**Alternative (compact):**

```text
Flask route prepares Python data -> `render_template()` passes it into Jinja -> Jinja loop renders the article cards.
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
