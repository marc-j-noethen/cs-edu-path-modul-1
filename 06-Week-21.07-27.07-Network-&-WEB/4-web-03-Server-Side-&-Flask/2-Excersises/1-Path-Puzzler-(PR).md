# Path Puzzler (Flask)

**Course:** Cyber Security Analyst – Web Technology | **Date:** 24 July 2025

---

## Task

**Objective:**  
Build a small Flask application with static and dynamic routes.

**Requirements:**

- Create routes `/`, `/status`, `/info`, `/greet/<name>` and `/calculate/add/<int:num1>/<int:num2>`.
- Return strings or calculated output.
- Make the app runnable locally.

---

## Solution

```python
from datetime import date
from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome to the Route Master Home Page!"


@app.route("/status")
def status():
    return "Application is running."


@app.route("/info")
def info():
    return f"Today's date is {date.today().isoformat()}"


@app.route("/greet/<name>")
def greet(name):
    return f"Hello, {name}!"


@app.route("/calculate/add/<int:num1>/<int:num2>")
def add(num1, num2):
    return f"The sum of {num1} and {num2} is {num1 + num2}."


if __name__ == "__main__":
    app.run(debug=True)
```

**Alternative (compact):**

```text
Static route = fixed path.
Dynamic route = path with placeholder, e.g. `<name>`.
```

---

## Tests

|Route|Expected|✓|
|---|---|---|
|`/`|Welcome message|✅|
|`/greet/Eliza`|`Hello, Eliza!`|✅|
|`/calculate/add/5/3`|`The sum of 5 and 3 is 8.`|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|Route|Links URL and Python function.|
|Dynamic parameter|Read from the URL and passed to the function.|
|Flask app|Lightweight web server for Python.|

---

## Rules / Logic

```text
URL -> Route -> View function -> Response.
`<int:...>` forces integer conversion.
Calculations can be performed directly in the view.
```

---

## Notes

- **Tip:** Always use appropriate type converters for numeric routes.
- **Concept:** This app is a good starting framework for future pages.

---

## Optional: Extensions

- Add a 404 error page.
- Use HTML templates instead of plain strings.

