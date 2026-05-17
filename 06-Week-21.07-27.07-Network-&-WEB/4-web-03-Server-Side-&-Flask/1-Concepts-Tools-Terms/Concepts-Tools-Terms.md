## 📊 Summary based on the 80/20 principle

### What is server-side development?

Server-side code runs on a web server (not in the browser) and can access databases and server resources. It generates dynamic HTML content based on user requests.

### Flask Basics

**Flask** is a Python framework for web development. It is lightweight, flexible and easy to learn.

**Installation (Windows 11):**

```bash
pip install Flask
```

**Minimal Flask application:**

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
```

### The 3 core concepts:

1. **Routing** – URLs are mapped to Python functions using `@app.route('/path')`
2. **View Functions** – Functions that process requests and return responses
3. **Templates** – HTML files with placeholders `{{ variable }}` for dynamic content

### Request-Response Cycle:

1. Browser sends HTTP request to server
2. Flask finds matching route
3. View function is executed
4. Response (usually HTML) is sent back to browser
5. Browser renders the page

### Important parameters:

- `debug=True` - Automatic reloading + error display (for development only!)
- `host='0.0.0.0'` - Server accessible from anywhere on the network
- `port=5000` - Default port for Flask

**Practical tip:** With `render_template()`, you can populate HTML templates with dynamic data instead of writing HTML code directly in Python.

---

## Summary table

|Category|Content|Meaning|
|---|---|---|
|**Tools used**|Flask|Micro-web framework for Python for developing web applications|
||pip / pip3|Package manager for Python for installing libraries|
||Python|Programming language for server-side development|
||Jinja2|Template engine for dynamic HTML generation|
||Werkzeug|WSGI library (used internally by Flask)|
||Terminal / Command Prompt|Command-line tool for executing commands (Windows: CMD or PowerShell)|
|**Technical terms**|Client-side|Code executed in the user’s web browser (HTML, CSS, JavaScript)|
||Server-side|Code executed on a web server (e.g. Python with Flask)|
||HTTP Request|Request from the browser to the server|
||HTTP Response|Response from the server to the browser|
||Routing|Mapping of URLs to specific Python functions|
||View Function|Function that processes a route and returns a response|
||Decorator `@app.route()`)|Python syntax for defining routes|
||Template|HTML file with placeholders for dynamic content|
||Rendering|Process of converting a template into finished HTML|
||Debug Mode|Development mode with automatic reloading and error display|
||Port|Network endpoint for communication (default: 5000)|
||localhost / 127.0.0.1|Local IP address of your own computer|
|**Key terms**|Web framework|Collection of tools and libraries to simplify web development|
||Micro framework|Lean framework with a minimal core, but extensible|
||Request-response cycle|Process from request to response between browser and server|
||Dynamic Content|Content generated at runtime (e.g. personalised pages)|
||Extension|Additional module for extending Flask functionality|
||Development Server|Integrated test server for development (not for production)|
||Production Environment|Live environment for real users (no debug mode here!)|


