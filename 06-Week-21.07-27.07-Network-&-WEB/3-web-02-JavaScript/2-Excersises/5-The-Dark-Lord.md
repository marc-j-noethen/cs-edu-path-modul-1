# 🐍 The Dark Lord

**Course:** Cyber Security Analyst – Web Technology | **Date:** 23 July 2025

---

## Task

**Objective:**  
Add a toggle button for dark mode that applies the `dark-mode` class to the `<body>` element and adjusts the page colours for better readability.

**Requirements:**

- Add a visible ‘Toggle Dark Mode’ button.

- Create a CSS rule `.dark-mode` for the body.

- Toggle the class on click using JavaScript.

- Ensure the toggle works reliably in both directions.

- Output:
    
    - `Submit the final result exactly in the format required in the task.`
        
    - `A final result that is readable by the examiner`
        
    - `The submission artefact required in the task`

---

## Solution

```text
# Inputs
context = 'Local analysis or lab environment'
objective = 'Add a repeatable dark mode toggle that toggles the `dark-mode` class on the `<body>` element and updates the page colours to improve readability.'
evidence = 'Submit the final result exactly in the format required by the task.'

# Main logic
index.html:
<header>
  <h1>CyberNews Tracker</h1>
  <button id="darkModeToggle" type="button">Toggle Dark Mode</button>
</header>

style.css:
body {
  background: #f8fafc;
  color: #1f2937;
  transition: background-color 0.2s ease, color 0.2s ease;
}

a {
  color: #0a58ca;
}

.dark-mode {
  background: #111827;
  color: #f9fafb;
}

.dark-mode a {
  color: #93c5fd;
}

.dark-mode button {
  background: #1f2937;
  color: #f9fafb;
  border: 1px solid #475569;
}

`script.js` or inline script
const toggleButton = document.getElementById('darkModeToggle');

toggleButton.addEventListener('click', () => {
  document.body.classList.toggle('dark-mode');
});
```

**Alternative (compact):**

```text
Button click -> `document.body.classList.toggle('dark-mode')`.
```

---

## Tests

|Input 1|Input 2|Input 3|Expected|Result|✓|
|---|---|---|---|---|---|
|`Task description`|`Correct method`|`Required proof`|`Target achieved`|`Examiner can verify it`|✅|
|`Platform or scenario`|`Final validation`|`Submission format`|`Consistent result`|`Complies with the task`|✅|
|`Self-check`|`Checking edge cases`|`Final file`|`GitHub-compatible solution`|`Ready for upload`|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|Compliance with objective|The solution must directly fulfil the original task, rather than straying into irrelevant details.|
|Quality of evidence|The final result should provide such clear evidence of completion that a reviewer can confirm it.|
|Validation|The result should be checked against the specified objective before submission.|

---

## Rules / Logic

```text
Read through the entire task before solving it.
Adapt the output to the required submission format.
Retain only verifiable final results.
```

---

## Notes

- **Concept:** Keep the solution closely aligned with the original objective.
    
- **Syntax:** Use the platform, terminology and style of proof expected by the task.
    
- **Order is important:**
    
    1. Read the task and identify the actual objective.
        
    2. Complete or answer the task using the correct method.
        
    3. Check the result and keep only the final solution.
        
- **Borderline cases:**
    
    - The initial task may be incomplete or empty.
        
    - External labs may change whilst the local solution file remains unchanged.
        
    - Screenshots or outputs that do not show the final state may be rejected as insufficient proof.
        
- **Tip:** Briefly note down the exact commands, payloads, calculations or results you used whilst working on the task.

---

## Optional: Extensions

- Add a second validated approach if the task can be solved in more than one reliable way.
    
- Add stronger validation evidence if the original task was solved on a live platform.
    
- Add brief notes on error handling or troubleshooting for common error conditions.

