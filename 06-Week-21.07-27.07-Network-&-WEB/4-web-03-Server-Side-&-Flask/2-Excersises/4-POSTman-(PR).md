# Postman (Flask Form)

**Course:** Cyber Security Analyst – Web Technology | **Date:** 24 July 2025

---

## Task

**Objective:**  
Implement a contact page with a form and a confirmation page in Flask.

**Requirements:**

- GET route `/contact` for the form.
- POST route `/submit-message` for processing.
- Use templates `contact_form.html` and `confirmation.html`.

---

## Solution

```python
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/contact", methods=["GET"])
def contact():
    return render_template("contact_form.html")


@app.route("/submit-message", methods=["POST"])
def submit_message():
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")
    return render_template(
        "confirmation.html",
        name=name,
        email=email,
        message=message,
    )


if __name__ == "__main__":
    app.run(debug=True)
```

```html
<!-- templates/contact_form.html -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Contact</title>
</head>
<body>
  <h1>Contact</h1>
  <form action="{{ url_for('submit_message') }}" method="POST">
    <label for="name">Name:</label>
    <input type="text" id="name" name="name" required>

    <label for="email">Email:</label>
    <input type="email" id="email" name="email" required>

    <label for="message">Message:</label>
    <textarea id="message" name="message" rows="5" required></textarea>

    <button type="submit">Send</button>
  </form>
</body>
</html>
```

```html
<!-- templates/confirmation.html -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Confirmation</title>
</head>
<body>
  <h1>Thanks for reaching out, {{ name }}!</h1>
  <p>Your message has been received.</p>
  <p>Email: {{ email }}</p>
  <p>Message: {{ message }}</p>
</body>
</html>
```

**Alternative (compact):**

```text
GET displays form, POST processes data.
```

---

## Tests

|Scenario|Expected|✓|
|---|---|---|
|Call `/contact`|Form visible|✅|
|Submit form|Confirmation page appears|✅|
|Submit name|Name appears in the response|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|GET|Returns the form page.|
|POST|Sends form contents to the server.|
|`request.form`|Reads the transmitted form data.|

---

## Rules / Logic

```text
Form -> POST -> Server reads fields -> Template displays confirmation.
```

---

## Notes

- **Tip:** Always use `url_for(...)` for links and form actions.
- **Concept:** Form fields require clean `name` attributes.

---

## Optional: Extensions

- Save success message to a database.
- Add validation for empty or invalid inputs.


