# Web Surfer (Sockets)

**Course:** Cyber Security Analyst – Network Technology | **Date:** 16 July 2025

---

## Task

**Objective:**  
Send a simple HTTP request to a real web server using a raw TCP socket.

**Requirements:**

- Determine the target IP for `example.com`.
- Connect via socket on port 80.
- Send a correct HTTP/1.1 GET request.
- Output the beginning of the response.

---

## Solution

```python
# http_client.py
import socket

host = "example.com"
ip_address = socket.gethostbyname(host)
port = 80

request = (
    f"GET / HTTP/1.1\r\n"
    f"Host: {host}\r\n"
    f"Connection: close\r\n\r\n"
)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((ip_address, port))
client.sendall(request.encode())
response = client.recv(4096)
print(response.decode(errors="ignore"))
client.close()
```

**Alternative (compact):**

```text
At the end of the day, HTTP is just formatted text over TCP.
```

---

## Tests

|Input 1|Input 2|Input 3|Expected|Result|✓|
|---|---|---|---|---|---|
|`example.com`|Port 80|GET `/`|Status line + headers + start of HTML|correct|✅|
|incorrect hostname|DNS|connect|error|expected|✅|
|missing Host header|HTTP/1.1|server response|possible error or unexpected behaviour|informative|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|HTTP Request|Text-based protocol with start line, headers and blank line.|
|Host Header|Essential for virtual hosts in HTTP/1.1.|
|Socket Client|Establishes the TCP connection to the server.|

---

## Rules / Logic

```text
HTTP/1.1 requires CRLF line endings.
The headers are followed by a blank line.
With `Connection: close`, the client signals that the server may terminate the connection.
```

---

## Notes

- **Concept:** Browsers hide a lot of complexity; at its core, it is a TCP connection with clear syntax.
- **Syntax:** Don’t forget `\r\n`.
- **Order is important:**
    1. Resolve host
    2. Connect socket
    3. Send request
- **Edge cases:**
    - HTTPS does not work over raw HTTP on port 80.
    - Some servers respond with a redirect.
    - `recv(4096)` only reads the beginning of the response.
- **Tip:** To get the full response, read it later in a loop until `recv()` returns empty.

---

## Optional: Extensions

- Read the full response in a loop.
- Parse the status code separately.
- Add HTTPS later using `ssl.wrap_socket`.

