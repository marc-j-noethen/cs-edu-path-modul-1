# Hint Deception (HTML & CSS)

**Course:** Cyber Security Analyst – Web Technology | **Date:** 21 July 2025

---

## Task

**Objective:**  
Create a link that displays a misleading tooltip when hovered over and redirects to a different URL when clicked.

**Requirements:**

- Place a visible link.
- Display the tooltip using HTML/CSS only.
- Hovering displays a hint text.
- Clicking leads to a different URL.

---

## Solution

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Hint Deception</title>
  <style>
    .link-wrapper {
      position: relative;
      display: inline-block;
      margin: 80px;
    }

    .fake-tooltip {
      position: absolute;
      bottom: 125%;
      left: 0;
      background: #222;
      color: #fff;
      padding: 6px 10px;
      border-radius: 6px;
      font-size: 14px;
      white-space: nowrap;
      opacity: 0;
      pointer-events: none;
      transition: opacity 0.2s ease;
    }

    .link-wrapper:hover .fake-tooltip {
      opacity: 1;
    }
  </style>
</head>
<body>
  <div class="link-wrapper">
    <a href="https://www.example.com">Open secure portal</a>
    <span class="fake-tooltip">https://trusted.company-login.example</span>
  </div>
</body>
</html>
```

**Alternative (compact):**

```text
A CSS tooltip can look convincing, even though the real link points to a different destination.
```

---

## Tests

|Scenario|Expected|✓|
|---|---|---|
|Hover over link|Tooltip appears|✅|
|Click on link|Navigation to `https://www.example.com`|✅|
|Without JS|Tooltip works with CSS only|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|Tooltip via CSS|Additional information is displayed on hover.|
|Relative/Absolute positioning|Allows the tooltip to be placed close to the link.|
|Social engineering aspect|The displayed text and the actual destination may differ.|

---

## Rules / Logic

```text
The visible text is not automatically the actual destination.
Hover hints can mislead users.
CSS is sufficient to create misleading displays.
```

---

## Notes

- **Concept:** Technically simple, relevant to security.
- **Tip:** The exercise demonstrates why link targets should always be checked critically.

---

## Optional: Extensions

- Add an arrow to the tooltip using `::after`.
- Show how browser status bars can help.

