# 🐍 Back to the Future 

**Course:** Cyber Security Analyst – OS Technology | **Date:** 08 August 2025

---

## Task

**Goal:**  
Explain what a VM snapshot preserves and what happens when the VM is restored to a snapshot taken before a later terminal session existed.

**Requirements:**

- Take a snapshot before opening a new terminal state.

- Create a visible change after the snapshot.

- Restore the earlier snapshot.

- Explain the observed rollback accurately.

- Output:
    
    - `Submit the final result in the exact format requested by the task.`
        
    - `A reviewer-readable final result`
        
    - `The submission artifact requested by the task`

---

## Solution

```text
# Inputs
context = 'Local analysis or lab environment'
objective = 'Explain what a VM snapshot preserves and what happens when the VM is restored to a snapshot taken before a later terminal session existed.'
evidence = 'Submit the final result in the exact format requested by the task.'

# Main logic
Direct answer:

After restoring the original snapshot, the terminal that was opened later should disappear or revert, because the VM returns to the saved earlier state. In other words, the changes made after the snapshot are rolled back.

Important truth detail:

If the snapshot included VM memory, restoring it returns the machine to that exact running state, including which windows were open at the time of the snapshot. If the snapshot did not include memory, the disk state still rolls back, but the VM may boot or resume differently. In both cases, the later terminal state is not preserved as the current live state after the restore.
```

**Alternative (compact):**

```text
A snapshot is a rollback point. Anything created after it should not survive a restore to the earlier state.
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
