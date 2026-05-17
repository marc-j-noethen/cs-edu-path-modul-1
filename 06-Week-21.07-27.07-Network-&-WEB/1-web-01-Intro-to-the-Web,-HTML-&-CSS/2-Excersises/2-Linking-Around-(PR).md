# Linking Around (HTML & CSS)

**Course:** Cyber Security Analyst – Web Technology | **Date:** 21 July 2025

---

## Task

**Objective:**  
Add a simple navigation menu to the header of `index.html`.

**Requirements:**

- Use `nav` in the header.
- Create a `ul` with three `li` entries.
- Set placeholder links with `href="#"`.
- Retain the existing structure.

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
    <nav>
      <ul>
        <li><a href="#">Home</a></li>
        <li><a href="#">News</a></li>
        <li><a href="#">Contact</a></li>
      </ul>
    </nav>
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
Navigation consists of links that semantically belong in a `nav`.
```

---

## Tests

|Scenario|Expected|✓|
|---|---|---|
|Browser view|three navigation links visible|✅|
|HTML structure|`nav > ul > li > a` present|✅|
|Link target|Placeholder `#` set|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|Navigation|Helps users find page sections or subpages.|
|Unordered List|Typical basic pattern for menus.|
|Anchor Tag|Creates clickable links.|

---

## Rules / Logic

```text
Navigation belongs in semantically appropriate markup.
Links are often modelled as lists.
Placeholder targets are fine for early layout phases.
```

---

## Notes

- **Concept:** A clean structure makes it easier to apply CSS to horizontal menus later on.
- **Tip:** Build semantically correctly now; styling comes later.

---

## Optional: Extensions

- Highlight active links later using CSS.
- Connect actual subpages.

