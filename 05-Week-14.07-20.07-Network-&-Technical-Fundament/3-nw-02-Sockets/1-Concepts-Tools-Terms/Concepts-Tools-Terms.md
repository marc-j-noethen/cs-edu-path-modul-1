## 📊 Summary based on the 80/20 principle

**1. What is a socket?**

- A socket = **IP address + port number**
- Like a full postal address: IP = street/house number, port = flat number
- Enables targeted data exchange between specific programmes

**2. Basic client-server principle:**

- **Server**: Waits passively `bind()` → `listen()` → `accept()`)
- **Client**: Actively initiates the connection `connect()`)
- Like a restaurant (server) and a guest (client)

**3. The 4 most important socket functions:**

```python
# SERVER:
server_socket.bind(("0.0.0.0", 9999))  # Reserve port
server_socket.listen(1)                 # Wait for connections
connection, addr = server_socket.accept()  # Accept client

# CLIENT:
client_socket.connect(("127.0.0.1", 9999))  # Connect to the server
```

**4. Sending/receiving data:**

- Everything is transmitted as **bytes**
- String → Bytes: `.encode('utf-8')`
- Bytes → String: `.decode('utf-8')`

```python
socket.sendall("Hello".encode('utf-8'))  # Send
data = socket.recv(1024).decode('utf-8') # Receive
```

**5. Practical example:**

- Server starts on port 9999 and waits
- Client connects to `localhost:9999`
- Client sends "Hi server!"
- Server receives the message
- Both close the connection

**Windows 11 Specific Feature:**

- Open Terminal: `Windows key + R` → `cmd` or `powershell`
- Open two terminals in parallel for server and client
- Run Python: `python server.py` or `python client.py`

**Key point:** A socket is the combination of an IP address (which computer) and a port (which programme). Servers listen, clients connect.

---

## Tools used

|Tools used|Description|
|---|---|
|Python `socket` library|Built-in Python module for creating network connections|
|VS Code|Code editor for writing and running Python scripts|
|Terminal / PowerShell (Windows 11)|Command line for running Python scripts (`python server.py`)|
|`127.0.0.1` / `localhost`|Loopback address – refers to your own computer|

---

## Technical terms

|Technical terms|Meaning|
|---|---|
|**Socket**|Communication endpoint of an application on the network (IP + port)|
|**Port**|Number (0–65535) used to identify a specific application on a computer|
|**IP address**|Unique address of a computer on the network (e.g. `192.168.1.10`)|
|**Client-server model**|Communication pattern: server waits, client initiates the connection|
|**bind()**|Function for the server to ‘reserve’ an IP address and a port|
|**listen()**|Server waits for incoming connections|
|**accept()**|Server accepts a client connection and creates a new socket for it|
|**connect()**|Client establishes a connection to the server|
|**sendall()**|Sends data via the socket (as bytes)|
|**recv()**|Receives data via the socket (as bytes)|
|**encode() / decode()**|Conversion between strings and bytes (UTF-8)|
|**Well-Known Ports**|Standard ports 0–1023 for known services (e.g. port 80 for HTTP, 443 for HTTPS)|
|**Key terms**||
|**Endpoint**|Endpoint of a network connection|
|**Listening**|State of the server whilst waiting for connections|
|**Binding**|Linking a socket to an IP address and a port|
|**Connection**|Active connection between client and server|
|**localhost**|Your own computer (127.0.0.1)|
|**Interface**|Network interface (e.g. Wi-Fi, LAN)|
|**0.0.0.0**|Means "all available network interfaces" on the server|


