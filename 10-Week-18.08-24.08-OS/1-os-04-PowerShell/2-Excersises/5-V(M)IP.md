# 🐍 V(M)IP (PowerShell System Report)

**Course:** Cyber Security Analyst – OS Technology | **Date:** 18 August 2025

---

## Task

**Objective:**  
Use PowerShell to generate a brief system report covering the OS version, drives and uptime.

**Requirements:**

- Automatically retrieve OS information, fixed disks and uptime.
- Convert free storage to GB.
- Format the uptime in a readable format in days, hours and minutes.
- Provide the complete file `system_snapshot.ps1`.

- Output:

    - Complete PowerShell script
    - readable system output with labels
    - calculated uptime instead of raw timestamp

---

## Solution

```powershell
$os = Get-CimInstance Win32_OperatingSystem
$disks = Get-CimInstance Win32_LogicalDisk | Where-Object { $_.DriveType -eq 3 }
$uptime = (Get-Date) - $os.LastBootUpTime

Write-Host "OS Information:"
Write-Host "Caption: $($os.Caption)"
Write-Host "Version: $($os.Version)"
Write-Host ""

Write-Host "Disk Information:"
foreach ($disk in $disks) {
    $freeGb = [math]::Round($disk.FreeSpace / 1GB, 2)
    Write-Host "DeviceID: $($disk.DeviceID), VolumeName: $($disk.VolumeName), FreeSpace (GB): $freeGb"
}
Write-Host ""

Write-Host "System Uptime:"
Write-Host ("Uptime: {0} days, {1} hours, {2} minutes" -f $uptime.Days, $uptime.Hours, $uptime.Minutes)
```

**Alternative (compact):**

```text
A useful mini-report needs only three things: OS, disks and correctly formatted uptime.
```

---

## Tests

|Input 1|Input 2|Input 3|Expected|Result|✓|
|---|---|---|---|---|---|
|`Win32_OperatingSystem`|`Caption+Version`|`output`|`visible`|`yes`|✅|
|`Win32_LogicalDisk`|`DriveType 3`|`GB conversion`|`correct`|`yes`|✅|
|`LastBootUpTime`|`TimeSpan`|`days/hours/minutes`|`readable`|`yes`|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|CIM|Modern, user-friendly query interface for system information in PowerShell.|
|DriveType 3|Identifies local / fixed drives.|
|TimeSpan|Object for displaying and formatting time differences.|

---

## Rules / Logic

```text
System information should be retrieved via structured sources such as CIM.
Byte values must be converted to GB for human readability.
Uptime is the difference between the current time and `LastBootUpTime`.
```

---

## Notes

- **Important:** Windows VMs may display the caption text as Windows 10 despite running Windows 11 – this is normal here.
- **Tip:** `Get-CimInstance` is cleaner for this task than the older WMI alias cmdlets.
- **Observation:** A little formatting instantly turns raw data into a report.

---

## Optional: Extensions

- Include RAM information and computer name in the report.
- Save the report as a text or CSV file.

