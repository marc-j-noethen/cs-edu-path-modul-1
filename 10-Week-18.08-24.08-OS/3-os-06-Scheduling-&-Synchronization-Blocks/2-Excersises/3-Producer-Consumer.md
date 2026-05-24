# Producer / Consumer

**Course:** Cyber Security Analyst – OS Technology | **Date:** 20 August 2025

---

## Task

**Objective:**  
Implement a producer-consumer pattern cleanly using `queue.Queue` and Sentinel.

**Requirements:**

- Generate numbers from `0` to `n`.
- The consumer squares the numbers.
- Use `None` as a stop signal.

---

## Solution

```python
import threading
import queue


def run_producer_consumer(n):
    data_q = queue.Queue()
    squared_results = []

    def producer():
        if n != -1:
            for number in range(n + 1):
                data_q.put(number)
        data_q.put(None)

    def consumer():
        while True:
            item = data_q.get()
            if item is None:
                data_q.task_done()
                break
            squared_results.append(item * item)
            data_q.task_done()

    producer_thread = threading.Thread(target=producer)
    consumer_thread = threading.Thread (target=consumer)

    producer_thread.start()
    consumer_thread.start()

    producer_thread.join()
    consumer_thread.join()

    return squared_results
```

**Alternative (compact):**

```text
`None` marks the end of the data stream.
```

---

## Tests

|Input|Expected|✓|
|---|---|---|
|`5`|`[0, 1, 4, 9, 16, 25]`|✅|
|`-1`|`[]`|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|Producer|Generates data and places it in the queue.|
|Consumer|Retrieves data from the queue and processes it.|
|Sentinel|Special value for orderly termination.|

---

## Rules / Logic

```text
Process all non-empty values.
Stop cleanly if `None`.
```

---

## Notes

- **Tip:** Don’t forget `task_done()` after every `get()`.
- **Concept:** Queues neatly decouple production and processing.

---

## Optional: Extensions

- Test multiple consumers.
- Write results to a second queue in a thread-safe manner.

