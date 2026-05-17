# The Bakery (Cookies & State)

**Course:** Cyber Security Analyst – Web Technology | **Date:** 25 July 2025

---

## Task

**Objective:**  
Build a Flask app that demonstrates session cookies, persistent cookies and the deletion of cookies.

**Requirements:**

- Set `visit_count` as a session cookie.
- Set `last_visit_time` as a persistent cookie.
- Be able to display and delete both cookies.

---

## Solution

```python
import datetime
from flask import Flask, make_response, request

app = Flask(__name__)


@app.route("/")
def home():
    visit_count = request.cookies.get("visit_count", "Not set")
    last_visit_time = request.cookies.get("last_visit_time", "Not set")
    return f"""
    <h1>Cookie Baker</h1>
    <p>visit_count: {visit_count}</p>
    <p>last_visit_time: {last_visit_time}</p>
    <a href='/set_session'>Set session cookie</a><br>
    <a href='/set_persistent'>Set persistent cookie</a><br>
    <a href='/clear_all'>Clear cookies</a>
    """


@app.route("/set_session")
def set_session():
    current = int(request.cookies.get("visit_count", 0))
    new_count = current + 1
    resp = make_response(f"Session cookie updated: {new_count}")
    resp.set_cookie("visit_count", str(new_count))
    return resp


@app.route("/set_persistent")
def set_persistent():
    now = datetime.datetime.now().isoformat()
    resp = make_response(f"Persistent cookie updated: {now}")
    resp.set_cookie("last_visit_time", now, max_age=60)
    return resp


@app.route("/clear_all")
def clear_all():
    resp = make_response("Cookies cleared")
    resp.delete_cookie("visit_count")
    resp.delete_cookie("last_visit_time")
    return resp


if __name__ == "__main__":
    app.run(debug=True)
```

**Alternative (compact):**

```text
Session cookie = without `max_age`/`expires`.
Persistent cookie = with `max_age` or `expires`.
```

---

## Tests

|Route|Expected|✓|
|---|---|---|
|`/set_session`|Counter increments|✅|
|`/set_persistent`|Timestamp with expiry time set|✅|
|`/clear_all`|Both cookies deleted|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|Session cookie|Exists only for the browser session.|
|Persistent cookie|Remains across browser restarts.|
|`delete_cookie`|Effectively sets the cookie to expired.|

---

## Rules / Logic

```text
No lifetime -> Session.
With `max_age=60` -> persistent for at least 60 seconds.
Cookie values can be read via `request.cookies.get(...)`.
```

---

## Notes

- **Tip:** Developer tools display `Session` or `Expires/Max-Age` directly.
- **Concept:** Cookies are stored on the client side; the app reads and updates them.

---

## Optional: Extensions

- Set the HttpOnly and Secure attributes.
- Validate cookie values on the server side.


