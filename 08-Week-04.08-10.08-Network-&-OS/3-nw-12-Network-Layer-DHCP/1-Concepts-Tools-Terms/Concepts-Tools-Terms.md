# 📊 Summary based on the 80/20 principle

### **What is DHCP? The automatic network librarian**

**DHCP (Dynamic Host Configuration Protocol)** is a **network protocol** that **automatically** assigns IP addresses and other network settings to devices.

**Analogy**:

- **Without DHCP**: Like a library without a librarian – everyone finds their own seat → chaos, double bookings
- **With DHCP**: Friendly librarian assigns everyone a unique seat → order, no conflicts

**Core function**: Automatic assignment of:

- ✅ IP address
- ✅ Subnet mask
- ✅ Default gateway (router)
- ✅ DNS server addresses
- ✅ Additional network parameters

### **Why is DHCP so important? The 5 main advantages**

|Advantage|Without DHCP|With DHCP|
|---|---|---|
|**Automation**|❌ Configure every device manually|✅ Automatic configuration|
|**Accuracy**|❌ High error rate (typos, conflicts)|✅ No IP conflicts|
|**Efficiency**|❌ Wasted IP addresses|✅ IP recycling through leasing|
|**Central management**|❌ Change every device individually|✅ Distribute changes centrally|
|**Scalability**|❌ Impossible with many devices|✅ Thousands of devices without issues|

**Example**:

- **Without DHCP**: 1000 new employees → IT must configure 1000 computers individually (days!)
- **With DHCP**: 1000 new employees → plug in and immediately online (seconds!)

### **Basic network concepts (brief recap)**

**IP address**: Unique "street address" in the network (e.g. 192.168.1.100)

**Subnet mask**: Separates network and host part (e.g. 255.255.255.0)

**Default gateway**: Router address for leaving the local network (e.g. 192.168.1.1)

**DNS server**: Translates names → IP addresses (e.g. google.com → 172.217.160.142)

### **Checking network configuration (Windows 11)**

**Method 1: Settings (GUI)**

1. Open **Settings** (Windows + I)
2. **Network & Internet** → **Properties**
3. Look for **IP assignment**: "Automatic (DHCP)" means DHCP is active!
4. Displays: IP address, subnet mask, gateway, DNS servers

**Method 2: Command line**

```cmd
ipconfig /all
```

Look for:

- **DHCP enabled**: Yes/No
- **DHCP server**: IP address of the DHCP server
- **Lease obtained**: Timestamp of IP assignment
- **Lease expires**: Expiry time

### **The DORA process: How DHCP works**

**DORA** = **D**iscover, **O**ffer, **R**equest, **A**cknowledge (4-step handshake)

#### **Step 1: DISCOVER 📡**

```
New device starts in the network:
"Hello? Is there a DHCP server here?"

Client sends DHCPDISCOVER broadcast:
Source IP:  0.0.0.0      (has no IP yet!)
Dest. IP:   255.255.255.255 (broadcast to all)
```

**Meaning**: Client searches for a DHCP server in the local network

#### **Step 2: OFFER 📬**

```
DHCP server responds:
"Yes, I'm here! Here is an offer for you:"

Server sends DHCPOFFER (unicast or broadcast):
- Offered IP: 192.168.1.100
- Subnet mask: 255.255.255.0
- Gateway: 192.168.1.1
- DNS servers: 8.8.8.8, 8.8.4.4
- Lease duration: 24 hours
```

**Note**: Multiple DHCP servers can respond → client chooses (usually the first offer)

#### **Step 3: REQUEST 🙋**

```
Client selects an offer:
"I want the IP 192.168.1.100 from server 192.168.1.1!"

Client sends DHCPREQUEST broadcast:
- Informs chosen server: "I accept your offer"
- Informs other servers: "I decline your offers"
```

**Important**: Broadcast, so all servers are informed!

#### **Step 4: ACKNOWLEDGE ✅**

```
Server finalises lease:
"Confirmed! The IP is yours for 24 hours."

Server sends DHCPACK (unicast):
- Confirms all parameters
- Client configures network interface
- Client is now online! 🎉
```

**Alternative**: **DHCPNAK** (Negative Acknowledge) = rejection → client must restart

### **Visual DORA flow**

```
┌────────────┐                           ┌─────────────┐
│   Client   │                           │ DHCP Server │
│ (Your PC)  │                           │  (Router)   │
└────────────┘                           └─────────────┘
      │                                          │
      │  1. DHCPDISCOVER (Broadcast)            │
      │ ──────────────────────────────────────> │
      │  "Who can give me an IP?"               │
      │                                          │
      │  2. DHCPOFFER (Unicast/Broadcast)       │
      │ <────────────────────────────────────── │
      │  "Here: 192.168.1.100, 24h lease"       │
      │                                          │
      │  3. DHCPREQUEST (Broadcast)             │
      │ ──────────────────────────────────────> │
      │  "I accept 192.168.1.100!"              │
      │                                          │
      │  4. DHCPACK (Unicast)                   │
      │ <────────────────────────────────────── │
      │  "Confirmed! Enjoy!"                    │
      │                                          │
      ▼                                          ▼
[Client configures IP and is online]
```

**Time required**: The entire DORA process takes only **a few seconds**!

### **IP leasing: Time-limited assignment**

**Why not permanent?**

- ✅ **Efficient resource use**: Departed devices release IPs
- ✅ **Flexibility**: Devices can switch between networks
- ✅ **Dynamic adjustment**: Parameter changes are distributed

**Lease duration**:

- **Home network**: Typically 24 hours
- **Corporate network**: Often 8 hours (working day)
- **Public Wi-Fi**: 1–2 hours

**Lease renewal**:

```
Lease timeline (24 hours):

0h ────────────── 12h ────────────── 24h
│                  │                   │
IP assigned        Attempt             Expiry
                   renewal             (if no
                   (50% reached)       renewal)
```

**Automatic renewal**:

- At **50%** of lease duration: Client sends **DHCPREQUEST** directly to server
- At **87.5%** of lease duration: If no response, retry (broadcast)
- At **100%**: If no response → restart DORA process

**Result**: Client notices nothing – seamless renewal in the background!

### **Important DHCP information (DHCP options)**

**Standard parameters**:

- **IP address**: Unique address in the network
- **Subnet mask**: Define network boundaries
- **Default gateway**: Router IP
- **DNS server**: Name resolution
- **Lease duration**: Validity period

**Additional options** (optional):

- **Domain name**: e.g. "company.local"
- **NTP server**: Time synchronisation
- **TFTP server**: Network boot
- **WINS server**: Windows name resolution (outdated)
- **And many more** (over 100 defined DHCP options!)

### **DHCP roles**

**DHCP server**:

- Manages pool of IP addresses
- Responds to client requests
- Maintains leasing database
- **Typical**: Router, dedicated server, Windows Server

**DHCP client**:

- Requests IP configuration
- Renews lease automatically
- **Almost every device**: Computers, smartphones, printers, smart TVs, IoT devices

### **Practical DHCP commands (Windows 11)**

**Release IP address** (return lease):

```cmd
ipconfig /release
```

→ Client releases IP address

**Request new IP address**:

```cmd
ipconfig /renew
```

→ DORA process is started

**Display DHCP information**:

```cmd
ipconfig /all
```

→ Shows DHCP server, lease times, etc.

**Combination** (restart network):

```cmd
ipconfig /release && ipconfig /renew
```

### **What happens without a DHCP server? APIPA**

**Scenario**: Device configured for DHCP, but no DHCP server reachable

**Solution**: **APIPA (Automatic Private IP Addressing)** = **Link-Local Addressing**

```
Sending DHCP request...
No response...
Timeout...

→ Operating system assigns its own IP:
   169.254.x.x (e.g. 169.254.123.45)
   Subnet mask: 255.255.0.0
```

**APIPA properties**:

- ✅ Communication with other APIPA devices on the **same local segment** possible
- ❌ **No** gateway (no internet access)
- ❌ **No** DNS servers
- ❌ **No** communication with other networks

**Error messages**:

- Windows: "Limited connectivity"
- macOS: "Self-assigned IP address"
- Typical sign: IP starts with **169.254.x.x**

**Troubleshooting**:

1. Check DHCP server (is it running?)
2. Check network connection (cable, Wi-Fi)
3. Run `ipconfig /renew`

### **DHCP reservations: Fixed IPs for special devices**

**Problem**: Some devices always need the same IP (e.g. printers, servers)

**Solution**: **DHCP reservation** (static leasing)

```
DHCP server configuration:
"When device with MAC address AA:BB:CC:DD:EE:FF
 requests an IP, always assign 192.168.1.50"
```

**Advantages**:

- ✅ Device always keeps the same IP
- ✅ Still DHCP-managed (central administration)
- ✅ No manual configuration on the device required

**Typical use cases**:

- Network printers (so everyone knows the fixed IP)
- Servers (for DNS entries)
- Network cameras
- Gaming consoles (port forwarding)

### **DHCP relay agent: DHCP across network boundaries**

**Problem**: DHCP DISCOVER is broadcast → only reaches local network

**Scenario**: Company with multiple VLANs, one central DHCP server

**Solution**: **DHCP relay agent** (also: IP helper)

```
Client (VLAN 10)  →  Router (Relay)  →  DHCP Server (VLAN 1)
                     converts broadcast
                     to unicast
```

**Function**:

- Router receives DHCP broadcast
- Forwards as **unicast** to DHCP server
- Server responds → router forwards back to client

**Result**: One DHCP server can serve **multiple networks**!

### **DHCP security: Potential risks**

⚠️ **Rogue DHCP server**:

- Attacker sets up their own DHCP server
- Distributes false gateway/DNS addresses
- **Result**: Man-in-the-middle attack, traffic redirection

⚠️ **DHCP starvation attack**:

- Attacker requests all available IPs
- Pool exhausted → legitimate clients receive no IP
- **Result**: Denial of Service (DoS)

⚠️ **DHCP spoofing**:

- Attacker impersonates a DHCP server
- Responds faster than the legitimate server

**Protective measures**:

- ✅ **DHCP snooping** (switch feature): Only allow authorised DHCP servers
- ✅ **Port security**: Limit MAC addresses
- ✅ **802.1X**: Network authentication

### **Core message**

**DHCP** is the **invisible helper** that makes modern networks practical in the first place:

**Without DHCP**:

- ❌ Configure every device manually
- ❌ IP conflicts frequent
- ❌ Changes = enormous effort
- ❌ Not scalable

**With DHCP**:

- ✅ Plug-and-play: Plug in and get started
- ✅ No conflicts
- ✅ Central management
- ✅ Thousands of devices without issues

**The DORA process** (Discover → Offer → Request → Acknowledge) happens **in a flash** and **automatically** – you don't even notice it running!

**Final analogy**: DHCP is like a **self-service parking machine** – you drive in, automatically get assigned a free space, use it for a certain time, and when you leave it becomes free for others again. No chaos, no double bookings, maximum efficiency! 🚗🅿️📶

---

## Overview table

|**Category**|**Details**|
|---|---|
|**Tools Used**|• **System Settings/Settings**: Check network configuration (macOS: System Settings → Network; Windows: Settings → Network & Internet → Properties)<br>• **ipconfig**: Display DHCP information (Windows: `ipconfig /all`, `ipconfig /release`, `ipconfig /renew`)<br>• **ifconfig**: Display network interfaces (macOS; Windows: `ipconfig`)<br>• **DHCP server software**: Windows Server DHCP, ISC DHCP Server, Dnsmasq<br>• **Router web interface**: DHCP server settings (browser: e.g. 192.168.1.1)<br>• **Wireshark**: DHCP packet analysis (observe DORA process)<br>• **netsh**: DHCP configuration (Windows: `netsh interface ip show config`)<br>• **PowerShell**: `Get-NetIPConfiguration`, `Get-DhcpServerv4Lease`<br>• **dhcpcd**: DHCP client daemon (Linux/macOS)<br>• **Event Viewer**: Log DHCP events (Windows)<br>• **Terminal**: `sudo ipconfig set en0 DHCP` (restart macOS DHCP)<br>• **Network Troubleshooter**: Windows network problem resolution|
|**Technical Terms**|• **DHCP** (Dynamic Host Configuration Protocol): Protocol for automatic IP configuration<br>• **DHCP server**: Server that assigns IP addresses<br>• **DHCP client**: Device that requests an IP address<br>• **DORA process**: Discover, Offer, Request, Acknowledge (4-step handshake)<br>• **DHCPDISCOVER**: Client discovery message (broadcast)<br>• **DHCPOFFER**: Server offer message<br>• **DHCPREQUEST**: Client request message<br>• **DHCPACK**: Server acknowledgement message<br>• **DHCPNAK**: Negative acknowledgement<br>• **IP lease**: IP address lease/rental agreement<br>• **Lease duration/time**: Lease period<br>• **Lease renewal**: Extension/renewal of lease<br>• **IP address pool**: Pool of available IP addresses<br>• **Scope**: DHCP scope/address range<br>• **Reservation**: Reservation (fixed IP for specific MAC)<br>• **Broadcast**: Transmission to all devices (255.255.255.255)<br>• **Unicast**: Direct transmission to one specific device<br>• **MAC address**: Hardware address of the network card<br>• **APIPA** (Automatic Private IP Addressing): Automatic private IP assignment<br>• **Link-local address**: Local link address (169.254.x.x)<br>• **Default gateway**: Default gateway (router address)<br>• **DNS server**: Domain Name System server<br>• **Subnet mask**: Subnet mask<br>• **DHCP options**: Additional configuration parameters<br>• **Relay agent**: DHCP relay/forwarding agent<br>• **IP conflict**: IP address conflict (two devices, one IP)<br>• **Static IP**: Static/fixed IP address<br>• **Dynamic IP**: Dynamic IP address|
|**Important Vocabulary**|• **Automatic configuration**: Independent setup without manual input<br>• **Assignment**: Distribution of IP addresses<br>• **Unique address**: Usable only once in the network<br>• **Manual configuration**: Manually entering network settings<br>• **Error-prone**: High risk of human error<br>• **Tedious**: Time-consuming and labour-intensive<br>• **Leasing**: Time-limited assignment<br>• **Return**: Release the IP address again<br>• **Pool**: Supply/collection of available addresses<br>• **Transient devices**: Temporary/changing devices<br>• **Central management**: Administration from a single point<br>• **Broadcast message**: Notification sent to all<br>• **Source IP**: Sender IP address<br>• **Destination IP**: Recipient IP address<br>• **Proposed IP**: Offered IP address<br>• **Accept offer**: Confirmation of IP address<br>• **Decline offer**: Rejection of IP address<br>• **Finalise lease**: Complete the lease agreement<br>• **Expire**: Run out/lapse over time<br>• **Renew**: Extend the lease duration<br>• **Reserved range**: IP range set aside for special purposes<br>• **Limited connectivity**: Restricted connection capability<br>• **Self-assigned IP**: Automatically assigned fallback IP<br>• **Mobility**: Ability to move between networks<br>• **Scalability**: Adaptability to growing number of devices<br>• **Efficiency**: Optimal use of resources|