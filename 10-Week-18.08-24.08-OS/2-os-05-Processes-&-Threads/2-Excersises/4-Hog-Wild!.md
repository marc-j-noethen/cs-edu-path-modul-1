# 🐍 Hog Wild! (CPU vs I/O)

**Course:** Cyber Security Analyst – OS Technology | **Date:** 19 August 2025

---

## Task

**Objective:**  
Write CPU-bound and I/O-bound PowerShell scripts and explain the different process and thread states.

**Requirements:**

- Create a CPU-intensive script and an I/O-intensive script.
- Compare Task Manager and Process Explorer for both cases.
- Explain running vs. waiting behaviour.
- Clearly identify the link between script logic and resource consumption.

- Output:

    - cpu_hog.ps1
    - io_hog.ps1
    - Technical comparison of the observations

---

## Solution

```powershell
# cpu_hog.ps1
$endTime = (Get-Date).AddSeconds(20)
$value = 0
while ((Get-Date) -lt $endTime) {
    for ($i = 0; $i -lt 500000; $i++) {
        $value += [math]::Sqrt($i)
    }
}
Write-Host "CPU test finished: $value"

# io_hog.ps1
$path = "$env:TEMP\io_hog_test.bin"
$buffer = New-Object byte[] (1024 * 1024)
(New-Object System.Random).NextBytes($buffer)
$endTime = (Get-Date).AddSeconds (20)

while ((Get-Date) -lt $endTime) {
    [System.IO.File]::WriteAllBytes($path, $buffer)
    [void][System.IO.File]::ReadAllBytes($path)
}
Remove-Item $path -ErrorAction SilentlyContinue
Write-Host "I/O test finished."

Observations:
- CPU-bound:
  high CPU usage, main thread mostly `Running`, hardly any significant disk I/O.
- I/O-bound:
  significantly more read/write activity, threads frequently switch to `Wait`,
  as they wait for file system or I/O operations.

Technical context:
Computational load keeps the thread active on the CPU.
I/O load often blocks the thread briefly until the operating system has completed the file operation.
```

**Alternative (compact):**

```text
CPU-bound spends time on the CPU; I/O-bound spends a lot of time waiting for the file system.
```

---

## Tests

|Input 1|Input 2|Input 3|Expected|Result|✓|
|---|---|---|---|---|---|
|`cpu_hog`|`Task Manager`|`CPU`|`high`|`expected`|✅|
|`io_hog`|`Task Manager`|`I/O bytes`|`high`|`expected`|✅|
|`Process Explorer`|`thread state`|`compare`|`Running vs Wait`|`expected`|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|CPU-bound|The bottleneck is processing time, not I/O.|
|I/O-bound|The bottleneck lies in memory, file or device access.|
|Thread State|Threads switch between Running, Ready and Wait depending on resource requirements.|

---

## Rules / Logic

```text
Computational work directly increases CPU utilisation.
File accesses often cause wait states despite the overall task being active.
A process may appear 'busy' even though its main thread is frequently waiting for I/O.
```

---

## Notes

- **Important:** The exact percentages depend on the system and VM; the general behaviour is the key point.
- **Tip:** If necessary, first display the Disk/I/O columns in Task Manager.
- **Observation:** The learning objective is precisely to compare high CPU usage versus high wait time.

---

## Optional: Extensions

- Additionally, build a network-bound variant and compare it with I/O.
- Start several parallel workers and observe the thread distribution.

