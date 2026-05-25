# Hide-n’-Seek (Unix Process Hunt)

**Course:** Cyber Security Analyst – OS Technology | **Date:** 30 August 2025

---

## Task

**Objective:**  
Find a running `sleep` process and terminate it cleanly.

**Requirements:**

- Find the PID using `ps` and `grep`.
- Terminate the process using `kill`.
- Briefly explain your approach.

---

## Solution

```bash
ps aux | grep '[s]leep 1000'
kill <PID>
```

Why `grep '[s]leep 1000'`?
This ensures that the `grep` process itself does not appear as a false hit in the output.

```text
Correct interpretation:
- The `sleep` process appears with its PID in `ps aux`.
- After `kill <PID>`, it disappears again.
- By default, `kill` first sends `SIGTERM`, i.e. a normal termination request.
```

**Alternative (compact):**

```text
Find PID -> Terminate PID.
```

---

## Tests

|Item|Expected|✓|
|---|---|---|
|`ps aux`|`sleep 1000` visible|✅|
|`kill <PID>`|Process terminated|✅|
|Command syntax|`grep` does not match itself|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|PID|Unique process ID.|
|`ps aux`|Displays running processes. |
|`kill`|Sends a signal to a process.|

---

## Rules / Logic

```text
Processes are uniquely identified by their PID.
`kill` with default behaviour first attempts a clean termination.
```

---

## Notes

- **Important:** Not every process responds to `SIGTERM` at the same speed.
- **Tip:** If `SIGTERM` is not enough, `kill -9 <PID>` is the hard option – but only if necessary.

---

## Optional: Extensions

- Solve the same problem using `pgrep` and `pkill`.
- Explain the difference between `SIGTERM` and `SIGKILL`.

