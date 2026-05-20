# 🐍 Another One 

**Course:** Cyber Security Analyst – OS Technology | **Date:** 08 August 2025

---

## Task

**Goal:**  
Install a Windows VM that can be reused throughout the training program and document the minimum configuration choices that make the installation successful.

**Requirements:**

- Create a new VM entry in the hypervisor.

- Attach a Windows installation ISO.

- Allocate enough CPU, RAM, and disk for a usable training VM.

- Complete the installation until the Windows desktop/home screen is reachable.

- Output:
    
    - `Submit the final result in the exact format requested by the task.`
        
    - `A reviewer-readable final result`
        
    - `The submission artifact requested by the task`

---

## Solution

```text
# Inputs
context = 'Local analysis or lab environment'
objective = 'Install a Windows VM that can be reused throughout the training program and document the minimum configuration choices that make the installation successful.'
evidence = 'Submit the final result in the exact format requested by the task.'

# Main logic
Truthful solution pattern:

1. Create a new virtual machine in VMware.
2. Select the Windows ISO as the installation media.
3. Choose a sensible baseline such as:
   - 2 vCPUs
   - 4 GB RAM or more
   - 50+ GB virtual disk
4. Complete the Windows installer.
5. Boot to the Windows desktop/home screen.
6. Install VMware Tools if the lab workflow expects smoother display, clipboard, or driver support.

Final verification checklist:
- Windows reaches the desktop successfully.
- The VM can be powered off and on again.
- Keyboard, mouse, display, and network adapter behave normally.

Important truth note:
- Because this is a real installation task, the screenshot must come from the actual VM you built. A generic stock screenshot is not a truthful substitute.
```

**Alternative (compact):**

```text
New VM -> attach Windows ISO -> install -> confirm you can reach the Windows desktop.
```

---

## Tests

|Input 1|Input 2|Input 3|Expected|Result|✓|
|---|---|---|---|---|---|
|`task text`|`correct method`|`required evidence`|`Goal completed`|`Reviewer can verify it`|✅|
|`platform or scenario`|`final validation`|`submission format`|`Consistent result`|`Matches the task`|✅|
|`self-check`|`edge-case review`|`final file`|`GitHub-ready solution`|`Ready to upload`|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|Objective Alignment|The solution must directly satisfy the original task instead of drifting into unrelated detail.|
|Evidence Quality|The final artifact should prove completion clearly enough for a reviewer to confirm it.|
|Validation|The result should be checked against the stated goal before submission.|

---

## Rules / Logic

```text
Read the full task before solving it.
Match the output to the requested submission format.
Keep only verifiable final results.
```

---

## Notes

- **Concept:** Keep the solution tightly aligned to the original objective.
    
- **Syntax:** Use the platform, terminology, and evidence style that the task expects.
    
- **Order matters:**
    
    1. Read the task and identify the real objective.
        
    2. Complete or answer the task with the correct method.
        
    3. Validate the result and keep only the final solution.
        
- **Edge Cases:**
    
    - The source task may be incomplete or empty.
        
    - External labs can change while the local solution file stays static.
        
    - Screenshots or outputs that do not show the final state may be rejected as weak evidence.
        
- **Tip:** Keep a short note of the exact commands, payloads, calculations, or findings you used during completion.

---

## Optional: Extensions

- Add a second validated approach if the task can be solved in more than one reliable way.
    
- Add stronger validation evidence if the original task was solved in a live platform.
    
- Add brief error-handling or troubleshooting notes for common failure states.
