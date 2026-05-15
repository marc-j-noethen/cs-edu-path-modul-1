# Chatter Box (Sockets)

**Course:** Cyber Security Analyst – Network Technology | **Date:** 16 July 2025

---

## Task

**Objective:**  
Build a relay server that connects two clients and forwards messages from one client directly to the other.

**Requirements:**

- Accept exactly two clients.
- Forward messages in both directions.
- Handle user-side sending and receiving.
- Support clean termination.

---

## Solution

```python
# relay_server.py
import socket
import select

HOST = "0.0.0.0"
PORT = 9998

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(2)
print(f"Relay server listening on {HOST}:{PORT}")

client1, addr1 = server.accept()
print("Client 1:", addr1)
client2, addr2 = server.accept()
print("Client 2:", addr2)

clients = [client1, client2]

while True:
    readable, _, _ = select.select(clients, [], [])
    for sock in readable:
        data = sock.recv(1024)
        if not data:
            print("Client disconnected")
            for c in clients:
                c.close()
            server.close()
            raise SystemExit
        other = client2 if sock is client1 else client1
        other.sendall(data)
```

```python
# relay_client.py
import socket
import threading

HOST = "127.0.0.1"
PORT = 9998

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
print("Connected. Type /quit to exit.")


def receive_messages():
    while True:
        try:
            data = client.recv(1024)
            if not data:
                break
            print("\nOther:", data.decode())
        except Exception:
            break


threading.Thread(target=receive_messages, daemon=True).start()

while True:
    message = input("You: ")
    if message == "/quit":
        client.close()
        break
    client.sendall(message.encode())
```

**Alternative (compact):**

```text
The server reads from Socket A and sends to Socket B, and vice versa.
```

---

## Tests

|Input 1|Input 2|Input 3|Expected|Result|✓|
|---|---|---|---|---|---|
|Client 1 sends `hello`|Client 2 connected|Relay|Client 2 sees `hello`|correct|✅|
|Client 2 sends `hi back`|Client 1 connected|Relay|Client 1 sees `hi back`|correct|✅|
|Client types `/quit`|Close connection|Shutdown|Client exits cleanly|correct|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|Relay|Server acts as an intermediary between two endpoints.|
|select|Allows waiting for multiple sockets simultaneously.|
|Concurrency|The client needs to send and receive simultaneously.|

---

## Rules / Logic

```text
Server waits for exactly two connections.
Incoming data from Client A is sent to Client B.
Receiving and typing must be possible in parallel on the client side.
```

---

## Notes

- **Concept:** This is the smallest viable chat topology.
- **Syntax:** `select.select` on the server, `threading.Thread` on the client.
- **Order is important:**
    1. Start the server
    2. Connect two clients
    3. Relay messages
- **Edge cases:**
    - A client disconnects abruptly.
    - Empty messages on disconnect.
    - The console becomes cluttered with background output.
- **Tip:** Add a username or prefix to messages later.

---

## Optional: Extensions

- Support more than two clients.
- Turn it into a broadcast chat.
- Introduce nicknames and join/leave messages.

