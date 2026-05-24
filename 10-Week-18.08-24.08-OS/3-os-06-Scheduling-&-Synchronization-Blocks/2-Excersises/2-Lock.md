# Lock

**Course:** Cyber Security Analyst – OS Technology | **Date:** 20 August 2025

---

## Task

**Objective:**  
Increment a shared counter in a thread-safe manner using `Lock`.

**Requirements:**

- Start `num_threads` threads.
- Each thread increments the counter multiple times.
- Use `threading.Lock`.

---

## Solution

```python
import threading


def increment_counter_fixed(num_threads, increments_per_thread):
    score = 0
    lock = threading.Lock()
    threads = []

    def worker():
        nonlocal score
        for _ in range(increments_per_thread):
            with lock:
                score += 1

    for _ in range(num_threads):
        thread = threading.Thread(target=worker)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return score
```

**Alternative (compact):**

```text
Lock prevents race conditions during concurrent writing.
```

---

## Tests

|Input|Expected|✓|
|---|---|---|
|`(2, 1000)`|`2000`|✅|
|`(5, 10)`|`50`|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|Race Condition|Multiple threads modify the same state simultaneously.|
|Lock|Allows only one thread at a time to enter the critical section.|
|Critical section|Here: `score += 1`.|

---

## Rules / Logic

```text
Reading + incrementing + writing back must be protected atomically.
```

---

## Notes

- **Tip:** `nonlocal` is required because `score` lives in the outer function.
- **Concept:** Locking costs a little speed, but ensures correctness.

---

## Optional: Extensions

- Build a version without a lock as a counterexample.
- Continue practising with `queue` or `Semaphore`.


