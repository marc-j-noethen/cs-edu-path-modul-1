# Time Lord's Greeting (JavaScript)

**Course:** Cyber Security Analyst – Web Technology | **Date:** 23 July 2025

---

## Task

**Objective:**  
Display a time-dependent greeting in the console and update the `h1` element at the same time.

**Requirements:**

- Use `new Date().getHours()`.
- Set a different message depending on the time.
- Use `console.log()`.
- Update `h1` via DOM.

---

## Solution

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Dynamic Greeting</title>
</head>
<body>
  <h1>Welcome!</h1>

  <script>
    const hour = new Date().getHours();
    let message = "";

    if (hour < 12) {
      message = "Good Morning, Cyber Explorer!";
    } else if (hour < 18) {
      message = "Good Afternoon, Cyber Defender!";
    } else {
      message = "Good Evening, Night Watcher!";
    }

    console.log(message);
    document.querySelector("h1").textContent = message;
  </script>
</body>
</html>
```

**Alternative (compact):**

```text
Read time -> Select message -> Update console and DOM.
```

---

## Tests

|Scenario|Expected|✓|
|---|---|---|
|Before 12 noon|Morning message|✅|
|12 noon to 5 pm|Afternoon message|✅|
|From 6 pm|Evening message|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|Date API|Returns the current time from the browser.|
|Conditions|Selects the appropriate message depending on the state.|
|DOM Manipulation|Changes the visible content of the page.|

---

## Rules / Logic

```text
Time < 12 -> Morning
Time < 18 -> Afternoon
otherwise -> Evening
```

---

## Notes

- **Concept:** A script can handle logic, the console and the UI simultaneously.
- **Tip:** Placing the script at the end of the body simplifies DOM access.

---

## Optional: Extensions

- Update the greeting every minute.
- Customise colours according to the time of day.


