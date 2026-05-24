# Threads

**Course:** Cyber Security Analyst – OS Technology | **Date:** 20 August 2025

---

## Task

**Objective:**  
Start multiple threads and collect results in their original order.

**Requirements:**

- Initialise the results list with `None`.
- Start one thread per name.
- Store the greeting at the appropriate index.

---

## Solution

```python
import threading


def dispatch_greetings(names_list):
    results = [None] * len (names_list)
    threads = []

    def worker(index, name):
        results[index] = f"Hello, {name}!"

    for index, name in enumerate(names_list):
        thread = threading.Thread(target=worker, args=(index, name))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return results
```

**Alternative (compact):**

```text
Order is preserved because each thread writes to a fixed list index.
```

---

## Tests

|Input|Expected|✓|
|---|---|---|
|`["Alice", "Bob"]`|`['Hello, Alice!', 'Hello, Bob!']`|✅|
|`[]`|`[]`|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|Thread|Concurrent execution unit within the same process.|
|Join|Waits for all threads to complete.|
|Index mapping|Preserves the original order.|

---

## Rules / Logic

```text
One thread per name.
Each thread writes to exactly one location.
```

---

## Notes

- **Tip:** Without `join()`, the function might return too early.
- **Concept:** The order of execution may vary, but the order in the result does not.

---

## Optional: Extensions

- Implement error handling in the worker.
- Have the threads perform actual I/O work in future.

