# Service Please (PowerShell)

**Course:** Cyber Security Analyst – OS Technology | **Date:** 18 August 2025

---

## Task

**Objective:**  
Filter services and store the result in a variable.

**Requirements:**

- Find only `Stopped` services whose names begin with `T`.
- Store the result in `$targetServices`.
- Display the count.

---

## Solution

```powershell
Get-Service | Where-Object { $_.Status -eq 'Stopped' -and $_.Name -like 'T*' }
```

```powershell
$targetServices = Get-Service | Where-Object { $_.Status -eq 'Stopped' -and $_.Name -like 'T*' }
$targetServices.Count
```

```text
Example value on the current system:
6
```

**Alternative (compact):**

```text
First filter, then store in a variable, then count.
```

---

## Tests

|Item|Expected|✓|
|---|---|---|
|Status filter|only `Stopped`|✅|
|Name filter|only `T*`|✅|
|Count|readable from variable|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|Where-Object|Filters objects based on conditions.|
|Variable|Saves the intermediate result for reuse.|
|Count|Counts entries in a collection.|

---

## Rules / Logic

```text
Only if both conditions are true does the service remain in the result.
```

---

## Notes

- **Important:** The exact number may vary from system to system.
- **Tip:** Use `$targetServices | Format-Table Name,DisplayName` to check the result more quickly.

---

## Optional: Extensions

- Filter further by startup type.
- Display names instead of internal service names.

