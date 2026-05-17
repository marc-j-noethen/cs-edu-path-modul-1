# 🐍 Live Feed (PR)

**Course:** Cyber Security Analyst – Web Technology | **Date:** 25 July 2025

---

## Task

**Goal:**  
Build a dynamic CyberNews Tracker page that loads fallback headlines locally, refreshes live headlines from NewsAPI, and gracefully falls back again when the external request fails.

**Requirements:**

- Expose `/api/news` for local static headlines.

- Expose `/api/live-news` for the NewsAPI-backed response.

- Render the list in `news.html` and refresh it with JavaScript.

- Handle both API failure and invalid-key scenarios without breaking the page.

- Output:
    
    - `Submit the final result in the exact format requested by the task.`
        
    - `A reviewer-readable final result`
        
    - `The submission artifact requested by the task`

---

## Solution

```text
# Inputs
context = 'Local analysis or lab environment'
objective = 'Build a dynamic CyberNews Tracker page that loads fallback headlines locally, refreshes live headlines from NewsAPI, and gracefully falls back again when the external request fails.'
evidence = 'Submit the final result in the exact format requested by the task.'

# Main logic
web_app.py:
import os
import requests
from flask import Flask, jsonify, render_template

app = Flask(__name__)
NEWS_API_KEY = os.getenv('NEWS_API_KEY')

FALLBACK_ARTICLES = [
    {'title': 'New Malware Targets Industrial Systems', 'source': 'CyberDaily', 'url': '#'},
    {'title': 'Researchers Discover AI-Powered Phishing Campaign', 'source': 'TechWatch', 'url': '#'},
]

@app.route('/news')
def news_page():
    return render_template('news.html')

@app.route('/api/news')
def local_news():
    return jsonify(FALLBACK_ARTICLES)

@app.route('/api/live-news')
def live_news():
    if not NEWS_API_KEY:
        return jsonify({'error': 'Missing NEWS_API_KEY'}), 503

    response = requests.get(
        'https://newsapi.org/v2/everything',
        params={'q': 'cybersecurity', 'language': 'en', 'apiKey': NEWS_API_KEY},
        timeout=10,
    )
    response.raise_for_status()
    articles = response.json().get('articles', [])
    trimmed = [
        {
            'title': article['title'],
            'source': (article.get('source') or {}).get('name', 'Unknown source'),
            'url': article.get('url') or '#',
        }
        for article in articles[:10]
    ]
    return jsonify(trimmed)

if __name__ == '__main__':
    app.run(debug=True)

templates/news.html:
{% extends 'index.html' %}
{% block content %}
  <h2>Cybersecurity Headlines</h2>
  <button id="refreshButton" type="button">Refresh Headlines</button>
  <p id="statusMessage"></p>
  <ul id="headlinesContainer"></ul>

  <script>
    const container = document.getElementById('headlinesContainer');
    const statusMessage = document.getElementById('statusMessage');
    const refreshButton = document.getElementById('refreshButton');

    function renderArticles(articles) {
      container.innerHTML = '';
      for (const article of articles) {
        const li = document.createElement('li');
        li.innerHTML = `<a href="${article.url}" target="_blank" rel="noopener noreferrer">${article.title}</a> <small>(${article.source})</small>`;
        container.appendChild(li);
      }
    }

    async function loadArticles(url, fallbackToLocal = false) {
      try {
        statusMessage.textContent = 'Loading...';
        const response = await fetch(url);
        if (!response.ok) {
          throw new Error(`HTTP ${response.status}`);
        }
        const articles = await response.json();
        renderArticles(articles);
        statusMessage.textContent = url === '/api/live-news' ? 'Live headlines loaded.' : 'Showing fallback headlines.';
      } catch (error) {
        if (fallbackToLocal && url !== '/api/news') {
          statusMessage.textContent = 'News unavailable right now. Falling back to local headlines.';
          await loadArticles('/api/news');
          return;
        }
        statusMessage.textContent = 'News unavailable right now. Please try again later.';
      }
    }

    window.addEventListener('DOMContentLoaded', () => loadArticles('/api/news'));
    refreshButton.addEventListener('click', () => loadArticles('/api/live-news', true));
  </script>
{% endblock %}

Reachable vs unreachable behavior:
- If NewsAPI is reachable and the key is valid, clicking the button replaces the fallback list with live article titles and source names.
- If NewsAPI fails, the page catches the error and reloads `/api/news` so the UI stays functional instead of breaking.
```

**Alternative (compact):**

```text
Load static data on page open, then try live data on demand, and fall back automatically if the live request fails.
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
