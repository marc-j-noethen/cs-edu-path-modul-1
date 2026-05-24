# The Process Paparazzi (PowerShell)

**Course:** Cyber Security Analyst – OS Technology | **Date:** 18 August 2025

---

## Task

**Objective:**  
Filter, sort and display a selection of processes via a pipeline.

**Requirements:**

- Retrieve processes.
- Sort in descending order by `WS`.
- Display only the top 5 with `Name` and `WS`.

---

## Solution

```powershell
Get-Process | Sort-Object WS -Descending | Select-Object -First 5 Name, WS
```

```text
Sample output from the current system:
- Memory Compression  803864576
- dwm                 764813312
- explorer            567459840
- ProtonVPN.Client    484421632
- Obsidian            376176640
```

**Alternative (compact):**

```text
Sort first, then truncate.
```

---

## Tests

|Item|Expected|✓|
|---|---|---|
|Sorting|largest WS first|✅|
|Filter|only 5 processes|✅|
|Columns|only `Name` and `WS`|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|Pipeline|Passes objects to the next command.|
|Sort-Object|Sorts by a property.|
|Select-Object|Selects columns and quantity.|

---

## Rules / Logic

```text
Get-Process -> Sort-Object -> Select-Object
```

---

## Notes

- **Tip:** `WS` stands for Working Set in memory.
- **Concept:** Small object pipelines are often more readable in PowerShell than single-line commands with complex logic.

---

## Optional: Extensions

- Output `Id` as well.
- Sort by CPU rather than memory.


