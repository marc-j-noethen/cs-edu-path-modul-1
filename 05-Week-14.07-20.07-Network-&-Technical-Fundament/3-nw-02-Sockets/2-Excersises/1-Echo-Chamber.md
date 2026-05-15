# Echo Chamber (Sockets)

**Course:** Cyber Security Analyst – Network Technology | **Date:** 16 July 2025

---

## Task

**Objective:**  
Build a simple echo server and a corresponding client using Python sockets.

**Requirements:**

- The server binds to port 9999 and listens.
- The client connects locally.
- The message sent is returned exactly as it was.
- Simple error handling is in place.

---

## Solution

```python
# echo_server.py
import socket

HOST = "0.0.0.0"
PORT = 9999

try:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(1)
    print(f"Listening on {HOST}:{PORT}")

    conn, addr = server.accept()
    print("Connected by", addr)
    data = conn.recv(1024)
    print("Received:", data.decode())
    conn.sendall(data)
    conn.close()
    server.close()
except Exception as e:
    print("Server error:", e)
```

```python
# echo_client.py
import socket

HOST = "127.0.0.1"
PORT = 9999
MESSAGE = "Hello Echo!"

try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))
    print("Connected to server")
    client.sendall(MESSAGE.encode())
    print("Sent:", MESSAGE)
    echoed = client.recv(1024).decode()
    print("Server echoed:", echoed)
    client.close()
except Exception as e:
    print("Client error:", e)
```

**Alternative (compact):**

```text
The server reads bytes using recv() and sends the same bytes back using sendall().
```

---

## Tests

|Input 1|Input 2|Input 3|Expected|Result|✓|
|---|---|---|---| ---|---|
|`Hello Echo!`|Client -> Server|TCP|same text returned|correct|✅|
|empty or no connection|Client|Timeout/Error|Error message or termination|covered|✅|
|Start server first|Port 9999|Connection|Client connects successfully|correct|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|Socket|Programming interface for network connections.|
|TCP|Connection-oriented and reliable.|
|Echo service|Server responds with exactly the same data it received.|

---

## Rules / Logic

```text
Server: socket -> bind -> listen -> accept -> recv -> sendall -> close
Client: socket -> connect -> sendall -> recv -> close
TCP transmits bytes, not strings by default.
```

---

## Notes

- **Concept:** Echo is the simplest meaningful request-response architecture.
- **Syntax:** `recv()` returns bytes, so use `.decode()`.
- **Order is important:**
    1. Start the server
    2. Connect the client
    3. Send and receive a message
- **Edge cases:**
    - Port already in use.
    - Firewalls are blocking the port.
    - Server terminates after exactly one connection.
- **Tip:** Test with `localhost` first, then extend to external targets later.

---

## Optional: Extensions

- Serve multiple clients in succession.
- Implement a `while` loop for continuous echo.
- Check message length before closing.

