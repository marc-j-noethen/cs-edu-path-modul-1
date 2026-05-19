## 📊 Summary based on the 80/20 principle

### **What are TCP and UDP? The transport layer protocols**

**TCP (Transmission Control Protocol)** is a **connection-oriented protocol** at the **transport layer** (layer 4) that guarantees **reliable, ordered and error-checked** data transmission between applications.

**Analogy**: TCP is like a meticulous postal service with registered post and proof of delivery – every packet is guaranteed to arrive, in the correct order and undamaged.

**UDP (User Datagram Protocol)** is a **connectionless, unreliable but extremely fast** transport protocol. Unlike TCP's "registered post with return receipt", UDP is like a **postcard**: you write it, address it, pop it in the post – without establishing a connection, without confirmation of receipt, without any guarantee.

**Core principle UDP**: **Speed and simplicity over reliability and order**

### **The role of the transport layer**

The transport layer sits between:

- **Network layer** (IP addresses, routing between hosts)
- **Application layer** (HTTP, DNS, email)

**Task**: Routing data to the **correct application** on the destination host – like a post sorting room in a computer.

**The two main protocols**:

- **TCP**: Reliable, slower (e.g. websites, email, file transfer)
- **UDP**: Fast, unreliable (e.g. live streaming, gaming)

---

### **TCP vs. UDP: The direct comparison**

|Feature|UDP|TCP|
|---|---|---|
|**Connection**|❌ Connectionless|✅ Connection-oriented|
|**Reliability**|❌ Best-Effort|✅ Guaranteed|
|**Order**|❌ Not guaranteed|✅ Guaranteed|
|**Header size**|8 bytes (minimal)|20+ bytes|
|**Speed**|⚡ Very fast|🐢 Slower|
|**Overhead**|Low|Higher|
|**Flow control**|❌ No|✅ Yes|
|**Congestion control**|❌ No|✅ Yes|
|**Retransmission**|❌ No|✅ Yes|
|**Applications**|Streaming, gaming, DNS|Web, email, file transfer|

**Rule of thumb**:

- **Do I need every single bit?** → TCP
- **Is speed more important?** → UDP

---

### **The 5 key characteristics of TCP**

#### **1. Connection-oriented**

Before data is exchanged, a **connection is established** via the **three-way handshake**:

```
Client                          Server
  |                               |
  |-------- SYN (seq=x) -------->|  (Step 1: "Can I connect?")
  |                               |
  |<----- SYN-ACK (seq=y) -------|  (Step 2: "Yes, ready!")
  |        (ack=x+1)              |
  |                               |
  |-------- ACK (ack=y+1) ------>|  (Step 3: "Confirmed, let's go!")
  |                               |
  [Connection established – data can flow]
```

**Note**: SYN → SYN-ACK → ACK = "Hello → Hello back → Let's go!"

#### **2. Reliable Delivery**

TCP **guarantees** data arrival through:

- **Sequence numbers**: Each byte is assigned a number
- **Acknowledgements (ACKs)**: The recipient confirms receipt of data
- **Retransmission**: No acknowledgement = automatic retransmission

**Example**:

```
Sender: "Here are bytes 1–100"
Receiver: "ACK – now expecting byte 101"
[No ACK after timeout?] → Sender sends again
```

#### **3. Ordered Data Transfer**

IP packets can take different routes and arrive out of order. TCP **sorts** them into the correct order using sequence numbers before passing them on to the application.

#### **4. Flow Control**

**Problem**: The receiver has limited buffer memory

**Solution**: **Sliding Window** – the receiver indicates how much space it has left (Window Size in the header), and the sender adapts accordingly.

**Prevents**: Receiver overload

#### **5. Congestion Control**

**Problem**: The network itself can become overloaded

**Solution**: TCP detects congestion signals (lost packets) and **automatically throttles** the transmission rate.

**Prevents**: Network collapse

---

### **The 5 main characteristics of UDP**

#### **1. Connectionless**

- **No handshake** before data transmission
- Each datagram is an **independent unit**
- No connection establishment or termination phase

**Comparison**:

- **TCP**: "May I send?" → "Yes!" → "OK, here it comes" (3-way handshake)
- **UDP**: _sends the packet straight away_ 📮

#### **2. Unreliable**

- **No delivery guarantee**
- **No acknowledgements (ACKs)**
- **No automatic retransmission** in case of loss
- Lost packets are simply gone ❌

**Best-Effort Delivery**: UDP does its best, but guarantees nothing.

#### **3. No order guarantee (Not Ordered)**

If you send 3 packets (1, 2, 3), they might arrive as:

- 3, 1, 2
- 1, 3 (packet 2 lost)
- 2, 1, 3
- Or in any order

**UDP doesn't care about sorting!**

#### **4. Minimal Overhead (Low Overhead)**

**UDP Header**: Only **8 bytes** (vs. TCP's minimum of 20 bytes)

|Field|Size|Function|
|---|---|---|
|**Source Port**|16 bits|Sender port (optional)|
|**Destination Port**|16 bits|Destination port (required)|
|**Length**|16 bits|Total length (header + data)|
|**Checksum**|16 bits|Error checking|

**That's it!** No sequence numbers, no flags, no window sizes.

#### **5. Fast**

Because:

- ✅ No connection establishment
- ✅ No waiting for acknowledgements
- ✅ Minimal header
- ✅ No flow control
- ✅ No congestion control

**Result**: UDP is **significantly faster** than TCP!

---

### **Ports: The flat numbers in the computer building**

**Port numbers** (0–65535) identify **specific applications** on a host.

**Analogy**:

- **IP address** = Address of the building
- **Port number** = Flat number in the building

|Port range|Name|Usage|Examples|
|---|---|---|---|
|**0-1023**|Well-known ports|Standard services|HTTP (80), HTTPS (443), SSH (22), FTP (21)|
|**1024-49151**|Registered ports|Registered applications|MySQL (3306), PostgreSQL (5432)|
|**49152-65535**|Ephemeral Ports|Client source ports|Randomly assigned by the OS|

**Socket** = IP address + port number (unique identification of a process)

**Well-known UDP ports**:

- **53**: DNS
- **67/68**: DHCP
- **69**: TFTP
- **123**: NTP (Network Time Protocol)
- **161/162**: SNMP
- **514**: Syslog

---

### **The TCP header: control centre**

The most important fields in the TCP header:

|Field|Size|Function|
|---|---|---|
|**Source Port**|16 bits|Sending application|
|**Destination Port**|16 bits|Receiving application|
|**Sequence Number**|32 bits|Byte number of the first data byte|
|**Acknowledgement Number**|32 bits|Next expected byte|
|**Flags**|Bits|SYN, ACK, FIN, RST, PSH, URG|
|**Window Size**|16 bits|Available buffer memory|
|**Checksum**|16 bits|Error checking|

**The most important flags**:

- **SYN**: Initiate connection
- **ACK**: Acknowledge data
- **FIN**: Terminate connection (gracefully)
- **RST**: Reset connection (abruptly)

---

### **TCP connection lifecycle**

**1. Establishment**: Three-way handshake (SYN → SYN-ACK → ACK)

**2. Data transmission**:

- Segments with sequence numbers
- ACKs for acknowledgements
- Flow and congestion control active

**3. Termination**: Four-way handshake

```
Side A: FIN →
Side B: ← ACK
Side B: FIN →
Side A: ← ACK
[Connection closed]
```

---

### **UDP Checksum: The only error checking**

**Purpose**: Detection of corrupted packets

**Function**:

1. Calculates checksum using: UDP header + data + pseudo-header (from IP)
2. Recipient recalculates
3. **Doesn't match?** → Packet is **silently discarded** (no error message!)

**Important**:

- **IPv4**: Checksum **optional** (can be set to 0)
- **IPv6**: Checksum **mandatory**

---

### **When to use which protocol?**

**Use TCP for**:

- ✅ Websites (HTTP/HTTPS)
- ✅ Email (SMTP, IMAP)
- ✅ File transfer (FTP, SFTP)
- ✅ Anything where **reliability is more important than speed**

**Use UDP for**:

|Application Type|Examples|Why UDP?|
|---|---|---|
|**Streaming Media**|YouTube Live, Twitch, Spotify|One lost frame < delay|
|**VoIP (Voice over IP)**|Zoom, Skype, Teams, Discord|Audio glitch < delay|
|**Online Gaming**|Multiplayer games, FPS|Old position is useless, current position matters|
|**DNS Queries**|Name resolution|Small requests, fast response, on loss → resend|
|**DHCP**|IP address assignment|Local network, low packet loss|
|**TFTP**|Trivial FTP, firmware updates|Simple file transfer in trusted networks|
|**SNMP**|Network monitoring|Fast status queries|
|**Multicast/Broadcast**|Video conferences, IPTV|One sender → many receivers|

**Why?** TCP's reliability mechanisms (retransmissions, acknowledgements) cause **delays**. With live streams, a lost frame is less of a problem than a delay – the stream simply carries on.

---

### **What happens to lost UDP packets?**

**Answer**: They are **gone forever**! 💀

UDP itself does **nothing**. The **application layer** must take care of it:

**Examples of application-level recovery**:

1. **DNS client**: Timeout → resend request
2. **VoIP (Zoom/Skype)**: Audio packet lost → brief glitch, but conversation continues – **no recovery attempt**, as the audio packet would already be outdated
3. **Video streaming**: Frame lost → pixelation/blocking for a moment – **Prediction**: Next frames are based on previous ones; **Forward Error Correction**: Sending redundant data along
4. **Online gaming**: Position update lost → client interpolates/extrapolates movement; next update corrects the position

---

### **UDP security aspects**

**Advantages**:

- ✅ No three-way handshake → harder to exploit for TCP-based attacks (SYN flood)

**Disadvantages**:

- ⚠️ **UDP flood attacks**: Easy to generate, hard to filter
- ⚠️ **UDP amplification**: DNS/NTP servers as amplifiers for DDoS
- ⚠️ **Spoofing**: Easier, as there is no connection verification

---

### **Practical tests (Windows 11)**

**View active TCP connections**:

```powershell
netstat -an | findstr "ESTABLISHED"
```

**Display UDP connections**:

```powershell
netstat -an -p udp
```

**TCP port test with PowerShell**:

```powershell
Test-NetConnection google.com -Port 443
```

**Testing a TCP connection manually**:

```powershell
telnet google.com 80
```

(Telnet must be enabled via "Windows Features")

**DNS query (uses UDP port 53)**:

```powershell
nslookup google.com
```

**Test UDP port with PowerShell**:

```powershell
Test-NetConnection -ComputerName 8.8.8.8 -Port 53 -InformationLevel Detailed
```

**UDP scan with nmap** (administrator rights required):

```powershell
nmap -sU -p 53,67,123,161 192.168.1.1
```

---

### **Key messages**

**TCP** is the **backbone of reliable internet communication**. Through its **three-way handshake**, **sequence numbers**, **ACKs**, **flow and congestion control**, it guarantees:

✅ **Reliability** – No data loss ✅ **Order** – Correct sorting ✅ **Error checking** – Corrupted data is detected

The cost: **overhead and latency** due to connection establishment and acknowledgements.

**UDP** is the **"fire-and-forget" protocol** of the internet – optimised for **speed and simplicity**, not reliability.

- TCP says: "I guarantee that everything arrives perfectly, no matter how long it takes."
- UDP says: "I throw it over as fast as I can. Whatever arrives, arrives!" 🚀

**Understanding the trade-off**: TCP = Quality over speed | UDP = Speed over quality

Both protocols are essential for cybersecurity analysis – understanding headers, flags, connection states and attack vectors forms the basis for network traffic analysis and attack detection! 🔒🌐

---

## Summary table

|**Category**|**Details**|
|---|---|
|**Tools used**|• **Wireshark**: Network analysis tool for capturing and analysing TCP & UDP packets (Windows & macOS)<br>• **tcpdump**: Command-line packet analyser (pre-installed on macOS; Windows: WinDump or via WSL)<br>• **netstat**: Displays active TCP connections and UDP ports (both systems: `netstat -an` / `netstat -an -p udp`)<br>• **telnet**: For testing TCP connections to specific ports (Windows: can be enabled via Features; macOS: pre-installed)<br>• **nmap**: Port scanner for checking open TCP and UDP ports (`nmap -sU` for UDP; installation required on both systems)<br>• **iperf/iperf3**: TCP and UDP bandwidth and performance tests<br>• **nslookup/dig**: DNS query tools (use UDP port 53)<br>• **hping3**: Packet generator for UDP tests<br>• **traceroute**: Partially uses UDP (macOS: `traceroute`; Windows: `tracert` uses ICMP)<br>• **Resource Monitor/Activity Monitor**: Monitor network connections (Windows: Resource Monitor; macOS: Activity Monitor)<br>• **PowerShell/Terminal**: `Test-NetConnection` (Windows), `nc` / `nc -u` (macOS) for TCP and UDP tests|
|**Technical terms**|• **TCP** (Transmission Control Protocol): Connection-oriented transport protocol<br>• **UDP** (User Datagram Protocol): Connectionless transport protocol<br>• **Transport Layer**: Layer 4 in the OSI model<br>• **Connection-Oriented**: Requires connection establishment (TCP)<br>• **Connectionless**: No prior connection establishment required (UDP)<br>• **Three-Way Handshake**: Three-way handshake to establish a TCP connection<br>• **Four-Way Handshake**: Four-way handshake for TCP connection termination<br>• **SYN** (Synchronize): Synchronisation flag to initiate a connection<br>• **ACK** (Acknowledgment): Acknowledgement flag for received data<br>• **FIN** (Finish): Termination flag for closing the connection<br>• **RST** (Reset): Resetting the connection (abrupt termination)<br>• **PSH** (Push): Immediate data transfer to the application<br>• **URG** (Urgent): Urgency flag for priority data<br>• **Sequence Number**: Sequence number for data sorting (TCP)<br>• **ISN** (Initial Sequence Number): Initial sequence number<br>• **Datagram**: UDP data unit (independent data packet)<br>• **Segment**: TCP data unit<br>• **Best-Effort Delivery**: Delivery attempted without guarantee (UDP)<br>• **Unreliable**: No delivery guarantee (UDP)<br>• **Port Number**: Port number for application identification (0–65535)<br>• **Socket**: Combination of IP address and port number<br>• **Well-Known Ports**: Standard ports (0–1023) for known services<br>• **Registered Ports**: Registered ports (1024–49151)<br>• **Ephemeral Ports**: Dynamic/temporary ports (49152–65535)<br>• **Sliding Window**: Window mechanism for flow control (TCP)<br>• **Window Size**: Window size (available buffer memory)<br>• **Flow Control**: Prevents receiver overload (TCP)<br>• **Congestion Control**: Prevents network overload (TCP)<br>• **Retransmission**: Retransmission of lost packets (TCP)<br>• **Checksum**: Checksum for error detection (both protocols)<br>• **Pseudo-Header**: Part of the IP header used for UDP checksum calculation<br>• **Overhead**: Additional protocol information (minimal with UDP, higher with TCP)<br>• **TCP Header**: TCP header containing control information (min. 20 bytes)<br>• **UDP Header**: UDP header (only 8 bytes)<br>• **Multicast**: Sending to multiple recipients simultaneously<br>• **Broadcast**: Sending to all recipients in the subnet<br>• **One-to-Many**: One sender, multiple receivers<br>• **Packet Loss**: Loss of packets<br>• **Out-of-Order**: Not arriving in the correct sequence<br>• **Application-Level Recovery**: Error handling at the application layer (UDP)<br>• **Real-time Protocol**: Real-time protocol<br>• **Latency**: Delay/latency<br>• **Buffer**: Buffer memory for received data<br>• **RFC 793**: Technical specification of the TCP protocol<br>• **IANA** (Internet Assigned Numbers Authority): Organisation responsible for port registration|
|**Key vocabulary**|• **Reliable delivery**: Guaranteed data transmission without loss (TCP)<br>• **Ordered transmission**: Data arrives in the correct order (TCP)<br>• **Error checking**: Detection of corrupted data (both protocols)<br>• **Connection establishment**: Establishing a communication link<br>• **Connection termination**: Terminating an existing connection<br>• **Handshake**: "Handshake" – coordination procedure between sender and receiver<br>• **Logical communication**: Virtual connection between applications<br>• **Postcard analogy**: UDP like sending a postcard – no delivery confirmation<br>• **Reliable postal service**: TCP metaphor for guaranteed delivery<br>• **Sorting office analogy**: TCP as a "postal sorting office" in the computer<br>• **Residential building analogy**: IP = building, port = flat number<br>• **Acknowledgement**: Receipt confirmation for data received (TCP)<br>• **No acknowledgement**: Receiver does not send an ACK back (UDP)<br>• **No retransmission**: Lost packets are not resent (UDP)<br>• **No order guarantee**: Packets can arrive out of sequence (UDP)<br>• **Silent discard**: Faulty packets are dropped without notification (UDP)<br>• **Independent datagrams**: Each UDP packet stands on its own<br>• **Minimal header**: Only 8 bytes of protocol information (UDP)<br>• **Low overhead**: Little additional data (UDP)<br>• **Timeout**: Time limit before retransmission (TCP) / before retry (UDP)<br>• **Packet loss**: Data packets that have not arrived<br>• **Network congestion**: Overloading of the network<br>• **Loss-tolerant**: Applications that accept occasional packet loss (UDP use cases)<br>• **Real-time applications**: Time-critical programmes (streaming, gaming)<br>• **Request-response protocols**: Query-response patterns (e.g. DNS)<br>• **Glitch**: Brief disruption in audio/video<br>• **Frame**: Single image in a video stream<br>• **Irrelevant data**: Old data that is no longer useful<br>• **Routing**: Routing of packets through the network<br>• **Reassembly**: Putting data segments back together<br>• **Abrupt termination**: Immediate termination without proper shutdown<br>• **Administrator rights**: Elevated permissions (for ports 0–1023)|