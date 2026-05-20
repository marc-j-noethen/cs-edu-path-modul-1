# 📊 Summary based on the 80/20 principle

### **The problem: IPv4 addresses are running out**

**IPv4** offers only **~4.3 billion addresses** (2³²)

**Problem**:

- Billions of devices worldwide (computers, smartphones, IoT, servers)
- Not enough unique public IPs for everyone
- **IPv4 address exhaustion** = No more free public IPs

**Solution**:

- Long term: **IPv6** (128-bit, practically infinite)
- Short term: **Private IPs + NAT** (optimal use of existing IPv4 addresses)

### **Private IP addresses: Your internal network**

**RFC 1918** defines three **private IP address ranges**:

|Range|CIDR notation|Number of addresses|Typical use|
|---|---|---|---|
|**10.0.0.0 - 10.255.255.255**|10.0.0.0/8|~16 million|Large enterprises|
|**172.16.0.0 - 172.31.255.255**|172.16.0.0/12|~1 million|Medium-sized companies|
|**192.168.0.0 - 192.168.255.255**|192.168.0.0/16|~65,000|Home networks, small offices|

**Characteristics of private IP addresses**:

✅ **Not globally unique**:

- The same IP (e.g. 192.168.1.100) can exist simultaneously in millions of different networks
- Your laptop at home and a printer in an office in Japan can both have 192.168.1.100

❌ **Not routable on the internet**:

- Internet routers discard packets with private IPs as the source or destination
- Private devices cannot be reached directly from the internet

✅ **Freely usable**:

- No registration or authorisation required
- Anyone can use these ranges on their private network

🛡️ **Enhanced security** (as a side effect):

- Devices with private IPs cannot be attacked directly from the internet
- Additional layer of protection

### **Quick check: Your IP address (Windows 11)**

**Method 1: Settings**

1. Open **Settings** (Windows + I)
2. **Network & Internet** → **Properties**
3. Look for **IPv4 address**
4. Is it in one of the private ranges? (Probably yes!)

**Method 2: Command line**

```cmd
ipconfig
```

Look for **IPv4 address** under your active connection

**Find the default gateway**:

```cmd
ipconfig | findstr "Default Gateway"
```

This is your router's IP address on the local network (e.g. 192.168.1.1)

### **NAT (Network Address Translation): The solution**

**Problem**: Private IPs do not work on the internet

**Solution**: **NAT** = Router translates private IPs → public IP

**Router has two IP addresses**:

- **Private IP** on the LAN (e.g. 192.168.1.1) = Default gateway
- **Public IP** from the ISP (e.g. 80.100.20.30) = Globally unique

### **How NAT works: The translation process**

#### **Step 1: Outgoing traffic (LAN → Internet)**

```
Your computer (192.168.1.100) wants to reach Google (142.250.180.196)

BEFORE (on the LAN):
┌────────────────────────────────┐
│ Source IP:  192.168.1.100       │ (private)
│ Destination IP:   142.250.180.196     │ (public)
└────────────────────────────────┘

[Packet reaches router – NAT translation takes place]

AFTERWARDS (on the internet):
┌────────────────────────────────┐
│ Source IP:  80.100.20.30        │ (router's public IP)
│ Destination IP:   142.250.180.196     │ (public)
└────────────────────────────────┘

Router stores in NAT table:
192.168.1.100 ↔ 80.100.20.30
```

#### **Step 2: Incoming traffic (Internet → LAN)**

```
Google responds to the router's public IP

ARRIVAL at the router:
┌────── ──────────────────────────┐
│ Source IP:  142.250.180.196     │ (Google)
│ Destination IP:   80.100.20.30        │ (Router's public IP)
└────────────────────────────────┘

[Router checks NAT table: "Who initiated this request?"]
[Finds: 192.168.1.100]

AFTER reverse translation (on the LAN):
┌────────────────────────────────┐
│ Source IP:  142.250.180.196     │ (Google)
│ Destination IP:   192.168.1.100       │ (your computer)
└────────────────────────────────┘

Packet is forwarded to your computer
```

**Router = Proxy**: All devices appear to come from the router's public IP

### **PAT (Port Address Translation): Multiple devices, one IP**

**Problem**: How does the router distinguish between multiple devices that all share the same public IP?

**Solution**: **PAT = NAT + Port Translation**

Also known as: **NAT Overload**

#### **How PAT works**

Each packet has not only IPs but also **port numbers**:

- **Source port**: Randomly assigned by the operating system (e.g. 51000)
- **Destination port**: Standard port of the service (e.g. 443 for HTTPS)

**PAT example with two devices**:

```
SCENARIO: 
- Laptop (192.168.1.100) browsing YouTube
- Smartphone (192.168.1.101) checking emails

┌─────────────────────────────────────────────────────────────┐
│                    NAT/PAT table in router                  │
├──────────────┬─────────────┬───────────────┬────────────────┤
│ Private IP   │ Priv. Port  │ Public IP     │ Public Port    │
├──────────────┼─────────────┼───────────────┼────────────────┤
│ 192.168.1.100│ 51000       │ 80.100.20.30  │ 34001          │
│ 192.168.1.101│ 52000       │ 80.100.20.30  │ 34002          │
└──────────────┴─────────────┴───────────────┴────────────────┘
```

**Outgoing**:

```
Laptop sends:
Source IP: 192.168.1.100 | Source Port: 51000
→ Router translates to:
Source IP: 80.100.20.30 | Source Port: 34001

Smartphone sends:
Source IP: 192.168.1.101 | Source Port: 52000
→ Router translates to:
Source IP: 80.100.20.30 | Source Port: 34002
```

**Incoming (responses)**:

```
Response arrives at: 80.100.20.30:34001
→ Router checks table: "Port 34001 belongs to 192.168.1.100:51000"
→ Forwards to laptop

Response arrives at: 80.100.20.30:34002
→ Router: "Port 34002 belongs to 192.168.1.101:52000"
→ Forwards to smartphone
```

**Key**: Each session gets a **unique port combination** on the public side!

### **Why PAT is so important**

**A single public IP** can support **thousands of devices**:

- 65,535 possible ports
- In practice: Several thousand simultaneous connections
- Your entire household shares one IP from the ISP

**Scalability**:

- Without PAT: 1 public IP = 1 device
- With PAT: 1 public IP = ~65,000 simultaneous sessions

### **NAT types overview**

|Type|Description|Use|
|---|---|---|
|**Static NAT**|1:1 mapping (one private IP → one public IP)|Servers in the LAN that need to be reachable from outside|
|**Dynamic NAT**|Pool of public IPs, dynamically assigned|Medium-sized companies with multiple public IPs|
|**PAT/NAT Overload**|Many private IPs → one public IP (with ports)|Home networks, small offices (standard!)|

### **NAT as a basic firewall**

**Security aspect of NAT/PAT**:

❌ **Unwanted incoming packets are blocked**:

```
Hacker attempts to send packet to 80.100.20.30:12345

Router checks NAT table:
"Is there an entry for port 12345?"
→ NO
→ Packet is DISCARDED
```

✅ **Only expected responses get through**:

- Router remembers outgoing connections
- Only responses to these connections are forwarded
- Unsolicited packets are blocked

🛡️ **NAT = Stateful Inspection Firewall** (basic):

- Tracks the state of all connections
- Only allows "known" traffic back through

**But**: NAT is **not a complete firewall** – additional security measures recommended!

### **Port Forwarding: Enabling incoming connections**

**Problem**: What if you run a server in the LAN that should be reachable from outside?

**Solution**: **Port Forwarding**

**Example**: Web server in the LAN (192.168.1.50) on port 80

```
Router configuration:
"All incoming packets on port 80 (HTTP) 
 → forward to 192.168.1.50:80"

┌──────────────────────────────────────────┐
│ External request: 80.100.20.30:80        │
│           ↓                              │
│ Router: "Port 80 → 192.168.1.50:80"     │
│           ↓                              │
│ Internal delivery: 192.168.1.50:80       │
└──────────────────────────────────────────┘
```

**Typical use cases**:

- Hosting web servers
- Running gaming servers
- Remote desktop access
- Making IP cameras accessible from outside

### **Limitations and problems of NAT**

⚠️ **End-to-end connectivity broken**:

- Devices in the LAN not directly reachable from outside
- Contradiction to the original internet design

⚠️ **Problems with certain protocols**:

- **FTP** (Active Mode): Expects incoming connection from server
- **VoIP/SIP**: Embeds IP addresses in payload
- **IPSec**: Can be impaired by NAT
- **P2P applications**: Direct connections difficult

⚠️ **Complexity**:

- Port forwarding must be configured manually
- NAT traversal techniques required (STUN, TURN, ICE)

⚠️ **IPv6 philosophy**:

- IPv6 has enough addresses → **NAT not needed**
- Every device can have a public IPv6 address
- NAT is considered a "workaround", not a permanent solution

### **Checking public vs. private IP**

**Your private IP** (in the LAN):

```cmd
ipconfig
```

→ Shows e.g. 192.168.1.100

**Your public IP** (on the internet):

1. Visit https://www.whatismyip.com
2. Or in PowerShell:

```powershell
Invoke-RestMethod -Uri "https://api.ipify.org"
```

**Observation**: Both IPs are **different** – that is NAT in action!

### **Core message**

**Private IPs + NAT/PAT** are the **rescue for IPv4**:

1. **Private IPs** enable reusable addresses in isolated networks
2. **NAT** translates private → public IPs at the router
3. **PAT** uses ports to support many devices with one public IP

**Analogy**:

- **Private IPs** = Apartment numbers in a building (not globally unique)
- **Public IP** = Street address of the building (globally unique)
- **Router with NAT** = Doorman who receives and distributes mail for all apartments

**Result**:

- Billions of devices worldwide use the same private IP ranges
- Only a handful of public IPs needed per household/company
- IPv4 remains usable until IPv6 takes over completely

**Important**: NAT is a **workaround**, not a permanent solution – IPv6 is the future! 🌐🔄🛡️

---

## Summary table

|**Category**|**Details**|
|---|---|
|**Tools Used**|• **System Settings/Settings**: Display network configuration (macOS: System Settings → Network; Windows: Settings → Network & Internet → Properties)<br>• **ipconfig**: Display IP configuration (Windows: `ipconfig`; macOS: `ifconfig`)<br>• **Router web interface**: View NAT table (browser: e.g. 192.168.1.1 or 192.168.0.1)<br>• **netstat**: Display network connections and ports (both systems)<br>• **tracert/traceroute**: Packet tracing (Windows: `tracert`; macOS: `traceroute`)<br>• **nslookup**: Test DNS resolution<br>• **ping**: Connection tests to gateway and internet<br>• **arp**: Display ARP table (both systems: `arp -a`)<br>• **PowerShell/Terminal**: `Get-NetIPConfiguration` (Windows), `networksetup` (macOS)<br>• **Wireshark**: Analyse NAT translations<br>• **Online IP checker**: WhatIsMyIP.com, IPChicken.com (shows public IP)<br>• **Router admin tools**: Configure port forwarding|
|**Technical Terms**|• **Private IP Address**: Private IP address (not routable on the internet)<br>• **Public IP Address**: Public IP address (globally unique)<br>• **NAT** (Network Address Translation): Network address translation<br>• **PAT** (Port Address Translation): Port address translation<br>• **NAT Overload**: Many devices sharing one public IP (with ports)<br>• **RFC 1918**: Standard for private IP address ranges<br>• **IPv4 Address Exhaustion**: Depletion of available IPv4 addresses<br>• **NAT Table**: Translation table<br>• **Translation**: Conversion of addresses<br>• **Source IP/Port**: Source IP/source port<br>• **Destination IP/Port**: Destination IP/destination port<br>• **Inside Local**: Private IP in the internal network<br>• **Inside Global**: Public IP after NAT translation<br>• **Outside Local/Global**: External IP addresses<br>• **Static NAT**: Static NAT (1:1 mapping)<br>• **Dynamic NAT**: Dynamic NAT (pool of public IPs)<br>• **Port Forwarding**: Enabling incoming connections<br>• **Port Mapping**: Port assignment<br>• **Gateway**: Gateway to the internet (router)<br>• **ISP** (Internet Service Provider): Internet service provider<br>• **Session**: Communication session<br>• **State Table**: State table<br>• **Inbound/Outbound Traffic**: Incoming/outgoing traffic<br>• **Edge Router**: Border router (between LAN and WAN)<br>• **Firewall**: Security barrier (NAT as basic firewall)<br>• **End-to-End Connectivity**: Uninterrupted connectivity|
|**Important Vocabulary**|• **Address scarcity**: Lack of available IPv4 addresses<br>• **Reserved ranges**: IP ranges reserved for private use<br>• **Not routable**: Cannot be forwarded on the internet<br>• **Globally unique**: Worldwide unique IP address<br>• **Locally reusable**: Private IPs can be used multiple times<br>• **Isolated network**: Separated from other networks<br>• **Shared use**: Multiple devices share one IP<br>• **Translation process**: Conversion of private to public addresses<br>• **Border**: Transition between private and public network<br>• **Outgoing traffic**: From LAN to internet<br>• **Incoming traffic**: From internet to LAN<br>• **Source translation**: Changing the source IP/port<br>• **Destination translation**: Changing the destination IP/port<br>• **Reverse translation**: Converting back to private IP<br>• **Session tracking**: Tracking active connections<br>• **Unique assignment**: Each session has its own port combination<br>• **Transparency**: NAT is invisible to end devices<br>• **Proxy function**: Router as intermediary<br>• **Hidden identity**: Private devices not directly reachable<br>• **Protection layer**: Additional security through NAT<br>• **Scalability**: Supporting many devices with few IPs<br>• **IPv6 transition**: Gradual transition to IPv6<br>• **Free use**: Private IPs usable without registration<br>• **Packet modification**: Changing IP header information<br>• **Stateful**: NAT remembers active connections|