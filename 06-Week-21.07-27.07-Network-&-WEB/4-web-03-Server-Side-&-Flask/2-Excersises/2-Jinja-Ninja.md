# Jinja Ninja (Flask Templates)

**Course:** Cyber Security Analyst – Web Technology | **Date:** 24 July 2025

---

## Task

**Objective:**  
Render an HTML template using Flask and populate it with dynamic data.

**Requirements:**

- Create the route `/user/<username>`.
- Render `profile.html` with name, language and hobbies.
- Pass data from Python via `render_template`.

---

## Solution

```python
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/user/<username>")
def user_profile(username):
    language = "Python"
    hobbies = ["Reading", "Gaming", "Traveling"]
    return render_template(
        "profile.html",
        username=username,
        language=language,
        hobbies=hobbies,
    )


if __name__ == "__main__":
    app.run(debug=True)
```

```html
<!-- templates/profile.html -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>User Profile - {{ username }}</title>
</head>
<body>
  <h1>Welcome, {{ username }}!</h1>
  <p>Your favourite language is: {{ language }}.</p>
  <ul>
    {% for hobby in hobbies %}
      <li>{{ hobby }}</li>
    {% endfor %}
  </ul>
</body>
</html>
```

**Alternative (compact):**

```text
Jinja replaces placeholders such as `{{ username }}` at runtime.
```

---

## Tests

|Scenario|Expected|✓|
|---|---|---|
|`/user/Alice`|Title and greeting with `Alice`|✅|
|Language visible|`Python` appears in the paragraph|✅|
|List visible|3 hobbies are rendered|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|`render_template`|Renders HTML from the `templates` folder.|
|Jinja|Template engine with variables and loops.|
|Data flow|Python passes values to HTML.|

---

## Rules / Logic

```text
Route reads URL parameters.
View prepares data.
Template displays data.
```

---

## Notes

- **Tip:** Output lists using `{% for %}`.
- **Concept:** Template rendering separates logic from presentation.

---

## Optional: Extensions

- Introduce a layout file with shared navigation.
- Load preferred language from a database.


