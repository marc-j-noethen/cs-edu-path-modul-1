# 🐍 The Delegator (Parent and Child Processes)

**Course:** Cyber Security Analyst – OS Technology | **Date:** 19 August 2025

---

## Task

**Objective:**  
Launch a child process from PowerShell, wait for it to complete, and explain the parent/child relationship.

**Requirements:**

- Write a `worker_script.ps1` with a visible action and wait time.
- Write a `main_script.ps1` that starts the worker as a new PowerShell process.
- The parent must explicitly wait for the child process.
- Explain the effect of this wait on the process state and flow.

- Output:

    - Code for both scripts
    - Explanation of parent/child + wait
    - Typical wait state of the parent process

---

## Solution

```powershell
# worker_script.ps1
Start-Sleep -Seconds 5
"worker finished at $(Get-Date)" | Out-File -FilePath "$env:TEMP\worker_result.txt" -Encoding utf8
Write-Host "Worker completed."

# main_script.ps1
$worker = Start-Process powershell.exe `
    -ArgumentList "-ExecutionPolicy Bypass -File `"$PSScriptRoot\worker_script.ps1`"" `
    -PassThru

Write-Host "Started worker process with PID $($worker.Id). Waiting..."
$worker | Wait-Process
Write-Host "Worker is done. Parent continues."

Analysis:
- Parent and child processes can be clearly distinguished in Process Explorer using the tree view and the Command Line column.
- `Wait-Process`, or waiting for the process returned by `Start-Process -PassThru`, ensures that `main_script.ps1` only continues running once the worker has finished.
- Without this mechanism, the parent would terminate immediately or continue running straight away, even though the child is still active.
- Whilst waiting, the parent process is typically in a Wait/Waiting state because its main thread is blocked awaiting the end of the child process.
```

**Alternative (compact):**

```text
The parent starts the child and then intentionally blocks until the child is finished.
```

---

## Tests

|Input 1|Input 2|Input 3|Expected|Result|✓|
|---|---|---|---|---|---|
|`Start-Process`|`PassThru`|`Wait-Process`|`Parent waits`|`expected`|✅|
|`Process Explorer`|`tree view`|`command line`|`parent/child visible`|`expected`|✅|
|`worker_result.txt`|`after delay`|`parent resumes`|`order correct`|`yes`|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|Parent/Child|A process can create another process, which then becomes visible under it.|
|Wait-Process|PowerShell blocks until a specific process ends.|
|Command Line Evidence|The process arguments help to distinguish between `powershell.exe` processes with the same name.|

---

## Rules / Logic

```text
Without explicit waiting, the parent continues to run independently of the child.
`-PassThru` returns the process object that can be waited on later.
Process Explorer best displays parent/child relationships in the tree view alongside the command line.
```

---

## Notes

- **Important:** This task requires not only code, but also careful observation of the process tree.
- **Tip:** Make the worker action deliberately slow to allow sufficient time for observation.
- **Observation:** The wait state of the parent process is the direct OS-side expression of `Wait-Process`.

---

## Optional: Extensions

- Start multiple child processes and compare sequential vs. parallel waiting.
- Evaluate the return code of the child process.

