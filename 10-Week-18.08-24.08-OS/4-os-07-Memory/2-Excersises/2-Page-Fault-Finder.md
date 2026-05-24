# Page Fault Finder (Page Faults)

**Course:** Cyber Security Analyst – OS Technology | **Date:** 21 August 2025

---

## Task

**Objective:**  
Classify page faults during idle and under load.

**Requirements:**

- Monitor `Page Faults/sec`.
- Measure again under load.
- Draw conclusions about system performance.

---

## Solution

```text
Sample answer:
- At idle, `Page Faults/sec` is usually low or fluctuates only slightly.
- When opening many tabs and apps, `Page Faults/sec` increases significantly.
- A high number of page faults indicates that memory contents frequently need to be reloaded or moved between RAM and virtual memory.

Important note:
Not every page fault is a problem. Many are soft faults.
However, persistently high rates under memory stress may indicate bottlenecks and reduced responsiveness.
```

**Alternative (compact):**

```text
More memory stress -> more page faults.
```

---

## Tests

|Item|Expected|✓|
|---|---|---|
|Idle|low rate|✅|
|Memory load|rate increases|✅|
|Evaluation|Performance correlation established|✅|

---

## Explanation / Concepts

|Concept|Description|
|Page Fault|Requested memory page is not immediately available in the appropriate RAM context.|
|Soft Fault|Page is present elsewhere in RAM or cache.|
|Hard Fault|Page must be reloaded from slower storage.|

---

## Rules / Logic

```text
Increased active memory demand raises the likelihood of page faults.
```

---

## Notes

- **Tip:** Always compare idle and load states against each other.
- **Concept:** Page faults are a symptom, not conclusive proof of a problem on their own.

---

## Optional: Extensions

- Interpret `% Usage` of the paging file in parallel.
- Test browsers and Office applications against each other.

