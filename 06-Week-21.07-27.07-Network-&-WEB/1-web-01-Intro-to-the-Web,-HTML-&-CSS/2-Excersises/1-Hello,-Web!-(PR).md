# Hello, Web! (HTML & CSS)

**Course:** Cyber Security Analyst – Web Technology | **Date:** 21 July 2025

---

## Task

**Objective:**  
Build the basic framework for `CyberNews Tracker` as a clean HTML page.

**Requirements:**

- Create a folder named `cybernews_tracker`.
- Create `index.html`.
- Use standard HTML structure.
- Use `header`, `main` and `footer` semantically.

---

## Solution

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>CyberNews Tracker</title>
</head>
<body>
  <header>
    <h1>CyberNews Tracker</h1>
  </header>

  <main>
    <p>Latest cybersecurity updates will appear here soon.</p>
  </main>

  <footer>
    <p>&copy; 2025 CyberNews Tracker</p>
  </footer>
</body>
</html>
```

**Alternative (compact):**

```text
Header = Title, Main = Content, Footer = Closing.
```

---

## Tests

|Scenario|Expected|✓|
|---|---|---|
|Open file in browser|Title and placeholder visible|✅|
|Check page title|Browser tab shows `CyberNews Tracker`|✅|
|Check structure|Semantic tags present|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|DOCTYPE|Enables the browser’s standard mode.|
|Semantic tags|`header`, `main`, `footer` make the structure clearer.|
|HTML skeleton|The foundation for later CSS and JS extensions.|

---

## Rules / Logic

```text
Every HTML page needs a clear basic framework.
Semantics first, styling later.
The main area contains the actual page content.
```

---

## Notes

- **Concept:** A small, clean structure now saves on reworking later.
- **Tip:** Structure first, then navigation, then styling.

---

## Optional: Extensions

- Link to CSS file.
- Replace placeholder with card layout later.

