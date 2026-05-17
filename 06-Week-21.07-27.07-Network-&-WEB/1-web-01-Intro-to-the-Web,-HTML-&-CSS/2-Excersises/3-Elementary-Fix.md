# Elementary Fix (HTML & CSS)

**Course:** Cyber Security Analyst – Web Technology | **Date:** 21 July 2025

---

## Task

**Objective:**  
Correct the faulty CSS file so that the menu is displayed horizontally and neatly.

**Requirements:**

- Modify only `menu_style.css`.
- Remove bullets.
- Arrange menu items horizontally.
- Style the hover and active states correctly.

---

## Solution

```css
.main-navigation ul {
  list-style: none;
  margin: 0;
  padding: 0;
}

.main-navigation li {
  display: inline-block;
  margin-right: 5px;
}

.main-navigation a {
  display: block;
  padding: 10px 15px;
  background-color: #dddddd;
  color: #333333;
  text-decoration: none;
}

.main-navigation a:hover,
.main-navigation .active-item a {
  background-color: #333333;
  color: #ffffff;
}
```

**Alternative (compact):**

```text
The core errors were: `list-style`, typos in `margin`, `display`, colour contrast and `text-decoration`.
```

---

## Tests

|Scenario|Expected|✓|
|---|---|---|
|Menu view|Items side by side|✅|
|List style|No bullets visible|✅|
|Hover/Active|Dark background, white text|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|`inline-block`|Allows horizontal menu items with box model.|
|`display: block` on links|Makes padding and click area usable in a meaningful way.|
|Hover/Active State|Feedback for interaction and current menu item.|

---

## Rules / Logic

```text
List menus usually require `list-style: none`.
Block links are more clickable than inline links.
Good contrast makes menus more readable.
```

---

## Notes

- **Concept:** Small CSS errors often have a big impact on the display.
- **Tip:** First layout, then colours, then check hover states.

---

## Optional: Extensions

- Use Flexbox instead of `inline-block`.
- Add focus styles for keyboard navigation.
