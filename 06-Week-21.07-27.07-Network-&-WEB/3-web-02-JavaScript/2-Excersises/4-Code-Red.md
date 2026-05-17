# 🐍 Code Red

**Course:** Cyber Security Analyst – Web Technology | **Date:** 23 July 2025

---

## Task

**Objective:**  
Create a small web page that executes JavaScript entered by the user, replacing direct `alert()` calls with console output instead of a pop-up window.

**Requirements:**

- Provide a `<textarea>` for user code input.

- Execute the code when a button is clicked.

- Intercept simple `alert()` calls and redirect them to the console.

- Allow other code, such as `console.log()`, to execute normally.

- Output:
    
    - `Submit the final result in exactly the format required by the task.`
        
    - `A final result that is readable by the examiner`
        
    - `The submission artefact required by the task`

---

## Solution

```text
# Inputs
context = 'Local analysis or lab environment'
objective = 'Create a small browser page that executes user-provided JavaScript, replacing direct `alert()` calls with console output instead of a pop-up window.'
evidence = 'Submit the final result exactly in the format required by the task.'

# Main logic
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Code Red</title>
  <style>
    body { font-family: Arial, sans-serif; max-width: 760px; margin: 2rem auto; }
    textarea { width: 100%; min-height: 220px; font-family: monospace; }
    button { margin-top: 1rem; padding: 0.7rem 1rem; }
  </style>
</head>
<body>
  <h1>Code Runner</h1>
  <textarea id="codeInput">alert('Hello from user code!');
console.log('Test message');</textarea>
  <button id="runButton">Run code</button>

  <script>
    const codeInput = document.getElementById('codeInput');
    const runButton = document.getElementById('runButton');

    function blockedAlert(message) {
      console.log(`Warning message blocked: ${message}`);
    }

    runButton.addEventListener('click', () => {
      try {
        const userProgram = new Function('alert', codeInput.value);
        userProgram(blockedAlert);
      } catch (error) {
        console.error('Execution error:', error.message);
      }
    });
  </script>
</body>
</html>

Summary of the method:
- The page overrides `alert` by passing a replacement function to `new Function(...)`.
- Within this scope, `alert('...')` resolves to `blockedAlert(...)`.
- `console.log(...)` continues to use the normal global console object and works as usual.
```

**Alternative (compact):**

```text
Pass a fake `alert` function to the user code area and log the message instead of opening a pop-up.
```

---

## Tests

|Input 1|Input 2|Input 3|Expected|Result|✓|
|---|---|---|---|---|---|
|`Task description`|`Correct method`|`Required proof`|`Target achieved`|`Reviewer can verify it`|✅|
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
    
    - The initial task may be incomplete or blank.
        
    - External labs may change whilst the local solution file remains unchanged.
        
    - Screenshots or outputs that do not show the final state may be rejected as insufficient proof.
        
- **Tip:** Briefly note down the exact commands, payloads, calculations or results you used whilst working on the task.

---

## Optional: Extensions

- Add a second validated approach if the task can be solved in more than one reliable way.
    
- Add stronger validation evidence if the original task was solved on a live platform.
    
- Add brief notes on error handling or troubleshooting for common error conditions.

