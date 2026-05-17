# Shmoogle (HTML, CSS, JS)

**Course:** Cyber Security Analyst – Web Technology | **Date:** 21 July 2025

---

## Task

**Objective:**  
Recreate a simple local Google-style interface, but using `Shmoogle` and displaying an alert when clicked.

**Requirements:**

- Build a local website.
- Change the branding to `Shmoogle`.
- The search button displays `alert("You got Shmoogled!")`.
- Make the screenshot and files available for download.

---

## Solution

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Shmoogle</title>
  <style>
    body { font-family: Arial, sans-serif; text-align: center; margin-top: 120px; }
    h1 { font-size: 72px; margin-bottom: 20px; }
    input { width: 420px; padding: 12px 16px; border: 1px solid #ccc; border-radius: 24px; }
    button { margin-top: 20px; padding: 10px 18px; border: 1px solid #ddd; border-radius: 6px; cursor: pointer; }
  </style>
</head>
<body>
  <h1>Shmoogle</h1>
  <input type="text" placeholder="Search Shmoogle...">
  <div>
    <button onclick="alert('You got Shmoogled!')">Shmoogle Search</button>
  </div>
</body>
</html>
```

**Alternative (compact):**

```text
A single HTML document with embedded CSS and a button alert is sufficient for the task.
```

---

## Tests

|Scenario|Expected|✓|
|---|---|---|
|Open page|`Shmoogle` visible|✅|
|Click search button|Alert with `You got Shmoogled!`|✅|
|Check layout|Search field and button centred|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|HTML Layout|Structure for title, input field and button.|
|CSS Styling|Gives the page the familiar search engine look.|
|JavaScript Alert|Simplest interactive response to a click.|

---

## Rules / Logic

```text
HTML describes the structure.
CSS shapes the appearance.
JavaScript responds to user actions.
```

---

## Notes

- **Concept:** Even with very little JS, a static page becomes interactive.
- **Tip:** A clean local replica is sufficient for submission; pixel-perfect accuracy is not required.

---

## Optional: Extensions

- Add more buttons and a footer similar to Google’s.
- Replace the alert with real search logic at a later stage.

