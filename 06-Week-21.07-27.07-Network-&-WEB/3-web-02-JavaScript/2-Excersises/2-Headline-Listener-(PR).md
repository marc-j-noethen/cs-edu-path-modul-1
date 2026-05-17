# Headline Listener (JavaScript)

**Course:** Cyber Security Analyst – Web Technology | **Date:** 23 July 2025

---

## Task

**Objective:**  
Dynamically insert new headlines into the page by clicking a button.

**Requirements:**

- Create a button and a container.
- Set up a click event listener.
- Create new elements using JavaScript.
- Do not remove old headlines.

---

## Solution

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>CyberNews Tracker</title>
</head>
<body>
  <h1>CyberNews Tracker</h1>
  <button id="refreshButton">Refresh Headlines</button>
  <section id="headlinesContainer"></section>

  <script>
    const headlines = [
      "Breaking: Cyber Attack Hits Major Company!",
      "New Security Patch Released Today",
      "AI Tool Detects Malware Faster Than Ever",
      "Phishing Scam Targets Online Users"
    ];

    const descriptions = [
      "Experts are analysing the incident to prevent future breaches.",
      "Make sure to update your systems to stay safe.",
      "AI algorithms are now capable of spotting threats automatically.",
      "Users are advised to verify all emails before clicking links."
    ];

    const button = document.getElementById("refreshButton");
    const container = document.getElementById("headlinesContainer");
    const title = document.querySelector("h1");

    button.addEventListener("click", () => {
      const index = Math.floor(Math.random() * headlines.length);
      title.textContent = "CyberNews Tracker - Updated";

      const article = document.createElement("article");
      const h3 = document.createElement("h3");
      const p = document.createElement("p");

      h3.textContent = headlines[index];
      p.textContent = descriptions[index];

      article.appendChild(h3);
      article.appendChild(p);
      container.appendChild(article);
    });
  </script>
</body>
</html>
```

**Alternative (compact):**

```text
Button click -> random index -> create new DOM elements -> append to container.
```

---

## Tests

|Scenario|Expected|✓|
|---|---|---|
|One click|a new headline appears|✅|
|Five clicks|five entries remain visible|✅|
|Check title|`h1` is updated|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|Event Listener|Responds to user interaction.|
|DOM Creation|Elements are built dynamically using JS.|
|Append Child|Inserts new elements into the page.|

---

## Rules / Logic

```text
Interaction triggers logic.
New content is created, not just made visible.
Append instead of Replace retains old elements.
```

---

## Notes

- **Concept:** This is the bridge from static HTML to a dynamic UI.
- **Tip:** When clicks are repeated, make sure nothing is overwritten.

---

## Optional: Extensions

- Save a timestamp for each headline.
- Avoid duplicate headlines.


