# POSTman (Flask Contact Form)

**Course:** Cyber Security Analyst – Web Technology | **Date:** 23 July 2025

---

## Task

**Objective:**  
Integrate a contact page with an HTML form into the existing Flask app and process POST data.

**Requirements:**

- Route `/contact` for GET.
- Route `/submit-message` for POST.
- Create `contact_form.html` and `confirmation.html`.
- Extend the navigation to include `Contact`.

---

## Solution

```python
# web_app.py
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/contact')
def contact():
    return render_template('contact_form.html')

@app.route('/submit-message', methods=['POST'])
def submit_message():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')
    return render_template('confirmation.html', name=name, email=email, message=message)
```

```html
<!-- contact_form.html -->
<form action="{{ url_for('submit_message') }}" method="POST">
  <label for="name">Name:</label>
  <input type="text" name="name" id="name" required>

  <label for="email">Email:</label>
  <input type="email" name="email" id="email" required>

  <label for="message">Message:</label>
  <textarea name="message" id="message" rows="5" required></textarea>

  <button type="submit">Send</button>
</form>
```

```html
<!-- confirmation.html -->
<h1>Thanks for reaching out, {{ name }}! Your message has been received.</h1>
<p>Email: {{ email }}</p>
<p>Message: {{ message }}</p>
```

**Alternative (compact):**

```text
GET displays the form, POST processes the data and renders a confirmation.
```

---

## Tests

|Scenario|Expected|✓|
|---|---|---|
|Call `/contact`|Form visible|✅|
|Submit form|Confirmation page appears|✅|
|Submit name|Name is displayed dynamically|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|GET|Retrieves the form page.|
|POST|Sends form data to the server.|
|Template Rendering|HTML is populated with dynamic values.|

---

## Rules / Logic

```text
Clearly separate the route for display and the route for processing.
Reference the form action via `url_for`.
Read user input via `request.form.get()`.
```

---

## Notes

- **Concept:** This is the first real request-response sequence involving user input.
- **Tip:** Validate and escape form data later when more logic is added.

---

## Optional: Extensions

- Use flash messages.
- Incorporate a layout template with shared navigation.

