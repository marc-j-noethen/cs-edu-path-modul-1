# Hunting Down Memory Hogs (Memory Analysis)

**Course:** Cyber Security Analyst – OS Technology | **Date:** 21 August 2025

---

## Task

**Objective:**  
Identify memory hogs using the working set and commit.

**Requirements:**

- Simulate high memory usage.
- Identify the top process.
- Briefly explain the difference between working set and commit.

---

## Solution

```text
Sample answer:
- A browser with many tabs often appears as a memory hog.
- `Memory (active private working set)` shows the process’s private memory currently active in RAM.
- `Commit size` shows how much virtual memory has been allocated/reserved for the process.

Difference:
- Working Set = what is currently physically active in RAM.
- Commit = what has been allocated to the process in virtual memory, even if not all of it is currently in RAM.
```

**Alternative (concise):**

```text
Working Set is what is currently present in RAM; Commit is the larger allocation in virtual memory.
```

---

## Tests

|Item|Expected|✓|
|---|---|---|
|Memory hog found|Yes|✅|
|Working Set explained|Yes|✅|
|Commit explained|Yes|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|Working Set|Active physical memory of the process.|
|Commit Size|Reserved virtual memory.|
|Private Memory|Memory not shared with other processes.|

---

## Rules / Logic

```text
A process can have a large Commit size without keeping everything in physical RAM at the same time.
```

---

## Notes

- **Important:** Exact values depend on the workload.
- **Tip:** In Task Manager, sort by Working Set and then by Commit.

---

## Optional: Extensions

- Compare Shared vs. Private Memory in Resource Monitor.
- Test multiple browser profiles against each other.

