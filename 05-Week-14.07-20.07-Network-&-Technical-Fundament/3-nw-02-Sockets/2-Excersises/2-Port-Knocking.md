# Port Knocking (Sockets)

**Course:** Cyber Security Analyst – Network Technology | **Date:** 16 July 2025

---

## Task

**Objective:**  
Write a simple TCP port scanner that detects open ports on a target system.

**Requirements:**

- Scan `127.0.0.1`.
- Check the port range using a loop.
- Set a short timeout.
- Output open ports clearly.

---

## Solution

```python
# port_scanner.py
import socket

target = "127.0.0.1"
start_port = 1
end_port = 100

for port in range(start_port, end_port + 1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.1)
    try:
        sock.connect((target, port))
        print(f"Port {port} is open")
    except (socket.timeout, socket.error):
        pass
    finally:
        sock.close()
```

**Alternative (compact):**

```text
An open port is one where connect() succeeds without raising an exception.
```

---

## Tests

|Input 1|Input 2|Input 3|Expected|Result|✓|
|---|---|---|---|---|---|
|`127.0.0.1`|1-100|no service|usually no open ports|correct|✅|
|`127.0.0.1`|9999|Echo server active|Port 9999 open|correct|✅|
|closed port|Timeout 0.1|connect|no output|correct|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|Port scan|Tests which ports a service is listening on.|
|Timeout|Prevents the scanner from waiting too long for responses.|
|TCP connect()|A successful connection usually indicates an open port.|

---

## Rules / Logic

```text
Open port -> connect() successful.
Closed or filtered port -> Error or timeout.
Use a new socket per port.
```

---

## Notes

- **Concept:** A port scan is often the first reconnaissance step.
- **Syntax:** `settimeout`, `connect`, `finally`.
- **Order is important:**
    1. Select port range
    2. Create socket
    3. Evaluate result
- **Edge cases:**
    - Firewalls cause timeouts instead of ‘Refused’.
    - Too large a port range takes longer.
    - Very short timeouts may miss open ports.
- **Tip:** Run a well-known test service such as the Echo server in the background to validate the scanner.

---

## Optional: Extensions

- Read the service banner after a successful connection.
- Add threading for faster scans.
- Collect results in a list or file.
