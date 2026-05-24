# 🐍 Thread Zeppelin (Threads)

**Course:** Cyber Security Analyst – OS Technology | **Date:** 19 August 2025

---

## Task

**Objective:**  
Observe thread activity in Process Explorer and describe the direct effect of Suspend/Resume on a running PowerShell script.

**Requirements:**

- Examine a browser process with threads.
- Start a continuously running counter script.
- Suspend and resume the active PowerShell thread.
- Describe the visible effect in technical terms.

- Output:

    - expected observations for browser thread and PowerShell thread
    - explanation of Suspend/Resume
    - optional prediction for all threads suspended

---

## Solution

```text
Part A - typical observation:
- Browser process: e.g. `msedge.exe` or `chrome.exe`
- Thread count: significantly more than 1, often several dozen threads
- An active thread shows a measurable CPU/cycles delta and a Start Address entry within a browser module or a DLL

Part B – PowerShell test script:
$counter = 0
Write-Host "Script started. Press Ctrl+C to stop."
while ($true) {
    $counter++
    Write-Host "Counter: $counter"
    Start-Sleep -Milliseconds 100
}

Observation during Suspend:
As soon as the active thread of the running `powershell.exe` / `pwsh.exe` was suspended,
the counter output effectively froze.
No new lines appeared because the very thread that was driving the script execution and output had been stopped.

Observation on Resume:
After `Resume`, the output continued.
The counter resumed its work because the previously paused thread was rescheduled and executed.

Optional prognosis:
If all threads are indeed suspended, the entire process comes to a standstill.
In that case, there is no further script execution, no new output and no response until at least one thread is resumed.

Note:
TID, CPU percentage and exact start address are runtime-dependent and must be read in a real VM for each run.
```

**Alternative (compact):**

```text
Suspend visibly stops execution immediately; Resume allows the same process to continue running at exactly the same point.
```

---

## Tests

|Input 1|Input 2|Input 3|Expected|Result|✓|
|---|---|---|---|---|---|
|`Process Explorer`|`Threads tab`|`Browser`|`multiple threads`|`expected`|✅|
|`PowerShell loop`|`active thread`|`Suspend`|`counter stops`|`expected`|✅|
|`same thread`|`Resume`|`console`|`counter continues`|`expected`|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|Thread|The actual execution unit within a process.|
|Suspend|The scheduler does not continue executing the thread until it is resumed.|
|Process Explorer|Displays thread-level details such as TID, CPU usage and start address.|

---

## Rules / Logic

```text
A running script requires at least one executable thread.
If the thread relevant to the task is suspended, visible activity stops.
Thread data such as TID or CPU value are always snapshot-based.
```

---

## Notes

- **Important:** Browsers are heavily multithreaded; PowerShell Lab scripts demonstrate the effect of Suspend/Resume particularly clearly.
- **Tip:** Before suspending, sort the thread by CPU or Cycles Delta.
- **Observation:** It is precisely this task that bridges the gap between the abstract concept of threads and their observable effects.

---

## Optional: Extensions

- Test the same with a GUI programme and observe the window freezing.
- Suspend multiple threads and discuss the differences between worker and GUI threads.

