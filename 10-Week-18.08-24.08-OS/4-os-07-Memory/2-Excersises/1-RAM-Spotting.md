# RAM Spotting (Memory Basics)

**Course:** Cyber Security Analyst – OS Technology | **Date:** 21 August 2025

---

## Task

**Objective:**  
Understand basic memory metrics in Task Manager and Resource Monitor.

**Requirements:**

- Monitor total RAM and in-use values.
- Explain `Standby`.
- Identify a process with a high working set.

---

## Solution

```text
Sample answer:
- Allocated physical RAM: depends on the VM configuration
- In-use after opening several apps: increases noticeably
- Standby memory: cache already filled with data, which can be quickly released again if needed
- Process with the highest working set: often a browser, Explorer or a memory-intensive app

Key technical point:
`Standby` is not ‘lost’ RAM, but cached memory that Windows reuses when needed.
```

**Alternative (compact):**

```text
More open apps -> more `In Use`; `Standby` remains flexibly usable.
```

---

## Tests

|Point|Expected|✓|
|---|---|---|
|Open apps|`In Use` increases|✅|
|Standby explained|Cache memory|✅|
|Top process|Identifiable via Working Set|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|Working Set|Memory of a process currently active in RAM.|
|Standby|Cache that can be quickly recycled.|
|Commit|Reserved virtual memory.|

---

## Rules / Logic

```text
RAM is not simply free or occupied – part of it serves as a useful cache.
```

---

## Notes

- **Important:** Specific figures depend on the size of the VM and the apps running.
- **Tip:** Compare first when idle, then under load.

---

## Optional: Extensions

- Compare the Task Manager and Resource Monitor directly.
- Compare the Working Set and Commit per process.

