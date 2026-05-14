# 🖥️ Resource Watcher - Task Manager

**Course:** Cyber Security Analyst - Technical Fundament Basics | **Date:** 23 June 2025

---

## Task

**Objective:** Monitor and correctly interpret CPU, memory and storage usage in Windows 11.

**Task description:**
- Part 1: Generate and monitor CPU load
- Part 2: Monitor memory pressure caused by multiple browser tabs
- Part 3: Track storage activity when copying large files

---

## Solution

### Environment
```text
OS: Windows 11
Apps: Task Manager, PowerShell, web browser, File Explorer
```

### Procedure

**Part 1: CPU Load Observation**

**Step 1:** Preparation
- Open Task Manager with `Ctrl+Shift+Esc`
- Switch to the `Performance` or `Processes` tab

**Step 2:** Generate CPU load
```powershell
Start-Process powershell -ArgumentList '-NoProfile','-Command','while ($true) { [math]::Sqrt(12345) > $null }' -PassThru
```
**Effect:** Starts a separate PowerShell process that continuously generates computational load.

**Step 3:** Observation
- Look for high CPU usage in Task Manager
- The additional PowerShell process should be clearly visible
- **Important note:** On multi-core systems, a fully utilised core does not automatically mean 100% total CPU

**Step 4:** Clean up
```powershell
Get-Process powershell | Sort-Object StartTime -Descending | Select-Object -First 1 | Stop-Process
```

---

**Part 2: Memory Load Observation**

**Step 1:** Record baseline
- Task Manager -> `Performance` -> `Memory`
- Note down the initial values

**Step 2:** Generate memory load
- Open the browser
- Load 20 to 30 or more tabs

**Step 3:** Observation
- The browser’s RAM usage increases
- Overall free memory decreases
- Under heavy load, Windows may start to cache more or swap out

**Step 4:** Clean up
- Close any unnecessary tabs

---

**Part 3: Disk Activity Observation**

**Step 1:** Create a large test file
```powershell
Set-Location $HOME
fsutil file createnew large_test_file.bin 1073741824
```
**Note:** This creates a file 1 GB in size.

**Step 2:** Start the copy process
```powershell
Copy-Item large_test_file.bin large_test_file_copy.bin
```

**Step 3:** Observation
- Task Manager -> `Performance` -> Disk
- Observe read/write activity during the copy process

**Step 4:** Clean up
```powershell
Remove-Item large_test_file.bin, large_test_file_copy.bin
```

---

## Results

**Part 1 - CPU:**
- A single computationally intensive process can place a heavy load on a core.

**Part 2 - Memory:**
- Many browser tabs significantly increase RAM usage.

**Part 3 - Disk:**
- Large copy operations generate noticeable disk I/O.

---

## Notes

- **Learnt:** Task Manager is the key Windows 11 tool for this type of resource monitoring.
- **Important:** Specific percentage values always depend on your own system and must not be made up.
- **Tip:** For finer details, you can also use `resmon` (Resource Monitor) later on.

