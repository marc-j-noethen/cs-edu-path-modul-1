# Categorisation ARP (Address Resolution Protocol)

### **The problem: Knowing the IP, but needing the MAC**

**Scenario**: Computer A wants to send data to Computer B on the **same local network**

```
Computer A knows:
- Own IP: 192.168.1.10
- Own MAC: AA:AA:AA:AA:AA:AA
- Destination IP: 192.168.1.20

Computer A does NOT know:
- Destination MAC: ??? (but needs MAC for Ethernet frame!)
```

**Why is this a problem?**

**Layer 3 (IP)**: Routing between networks → IP addresses **Layer 2 (Ethernet)**: Delivery in local network → MAC addresses

```
┌──────────────────────────────────────────┐
│  IP packet (Layer 3)                     │
│  Source IP: 192.168.1.10                 │
│  Dest. IP:  192.168.1.20                 │
└──────────────────────────────────────────┘
           ↓ Must be encapsulated
┌──────────────────────────────────────────┐
│  Ethernet frame (Layer 2)                │
│  Source MAC: AA:AA:AA:AA:AA:AA           │
│  Dest. MAC:  ??? (UNKNOWN!)              │
│  Payload: [IP packet]                    │
└──────────────────────────────────────────┘
```

**Question**: How does Computer A find the MAC address of Computer B?

**Answer**: **ARP (Address Resolution Protocol)**! 🔍

### **What is ARP? The IP-to-MAC translator**

**ARP (Address Resolution Protocol)** = Protocol for **resolving IP addresses to MAC addresses** in the local network

**Function**: Dynamic lookup for IP ↔ MAC mapping

**Properties**:

- ⚙️ Operates between Layer 2 and Layer 3
- 📡 Only within the **local network segment** (not across routers)
- 🔄 **Stateless** (no persistent connection)
- 📋 **Request-response mechanism**

**Analogy**: ARP is like a **phone book for the local network** – you know the name (IP), and look up the phone number (MAC)

### **How ARP works: The 5-step process**

#### **Step 1: Check ARP cache** 🗂️

```
Computer A: "Want to send to 192.168.1.20..."
          ↓
Computer A checks ARP cache:
"Do I already have the MAC for 192.168.1.20?"

Case A: YES → Send directly (no ARP needed)
Case B: NO  → Start ARP request
```

**ARP cache** = Temporary storage for IP ↔ MAC mappings

#### **Step 2: Send ARP request (broadcast) 📢**

```
Computer A creates ARP request:
"Who has IP 192.168.1.20? Please reply to 192.168.1.10!"

Ethernet frame:
┌────────────────────────────────────────┐
│ Source MAC:  AA:AA:AA:AA:AA:AA (A)     │
│ Dest. MAC:   FF:FF:FF:FF:FF:FF (broadcast!) │
│ Type: ARP                              │
│ ──────────────────────────────────────│
│ ARP request:                           │
│  - Opcode: 1 (request)                 │
│  - Sender MAC: AA:AA:AA:AA:AA:AA       │
│  - Sender IP:  192.168.1.10            │
│  - Target MAC: 00:00:00:00:00:00 (?)   │
│  - Target IP:  192.168.1.20            │
└────────────────────────────────────────┘

Frame is sent to ALL devices on the local network!
```

**Important**: **Broadcast MAC** = `FF:FF:FF:FF:FF:FF` → Switch floods to all ports

#### **Step 3: Process ARP request** 🎯

```
All devices on the network receive the broadcast:

Computer B (192.168.1.20):
"Hey, that's my IP! I'll respond!"
→ Also stores: A's IP (192.168.1.10) ↔ MAC (AA:AA:AA:AA:AA:AA)

Computer C (192.168.1.30):
"Not my IP, ignore."
→ Silently discard

Computer D (192.168.1.40):
"Also not my IP, ignore."
→ Silently discard
```

**Only the target device responds!**

#### **Step 4: Send ARP reply (unicast) 📬**

```
Computer B creates ARP reply:
"I have IP 192.168.1.20, my MAC is BB:BB:BB:BB:BB:BB!"

Ethernet frame:
┌────────────────────────────────────────┐
│ Source MAC:  BB:BB:BB:BB:BB:BB (B)     │
│ Dest. MAC:   AA:AA:AA:AA:AA:AA (A, unicast!) │
│ Type: ARP                              │
│ ──────────────────────────────────────│
│ ARP reply:                             │
│  - Opcode: 2 (reply)                   │
│  - Sender MAC: BB:BB:BB:BB:BB:BB       │
│  - Sender IP:  192.168.1.20            │
│  - Target MAC: AA:AA:AA:AA:AA:AA       │
│  - Target IP:  192.168.1.10            │
└────────────────────────────────────────┘

Frame is sent DIRECTLY to Computer A (no broadcast)
```

#### **Step 5: Update ARP cache & send data** ✅

```
Computer A receives ARP reply:
"Great! 192.168.1.20 has MAC BB:BB:BB:BB:BB:BB"

Computer A stores in ARP cache:
192.168.1.20 → BB:BB:BB:BB:BB:BB

Now A can finally send:
┌────────────────────────────────────────┐
│ Ethernet frame:                        │
│ Source MAC:  AA:AA:AA:AA:AA:AA         │
│ Dest. MAC:   BB:BB:BB:BB:BB:BB (NOW KNOWN!) │
│ Payload: [original IP packet]          │
└────────────────────────────────────────┘

Data is delivered! 🎉
```

### **Visual flow**

```
┌─────────────┐         ┌─────────────┐         ┌─────────────┐
│ Computer A  │         │   Switch    │         │ Computer B  │
│ 192.168.1.10│         │             │         │ 192.168.1.20│
│ AA:AA:...:AA│         │             │         │ BB:BB:...:BB│
└─────────────┘         └─────────────┘         └─────────────┘
      │                        │                        │
      │  1. ARP request        │                        │
      │  "Who has .20?"        │                        │
      │ ──────────────────────>│                        │
      │  (broadcast)           │  2. Flooding           │
      │                        │ ──────────────────────>│
      │                        │                        │
      │                        │  3. "That's me!"       │
      │                        │ <──────────────────────│
      │  4. ARP reply          │                        │
      │  "My MAC: BB..."       │                        │
      │ <──────────────────────│                        │
      │  (unicast)             │                        │
      │                        │                        │
      │  5. Data packet        │                        │
      │  with correct MAC      │                        │
      │ ──────────────────────>│ ──────────────────────>│
      │                        │                        │
```

### **The ARP cache: Efficiency through storage**

**Problem**: An ARP request for **every** packet would be inefficient

**Solution**: **ARP cache** stores learned mappings

**Properties**:

**Dynamic entries**:

- Automatically learned through the ARP process
- **Time-limited** (timeout: often 1–20 minutes, OS-dependent)
- After expiry: entry deleted, resolved again when needed

**Static entries**:

- Added manually (rare)
- **Permanent** (until manually deleted)
- For special network configurations

**Why timeout?**

- IP addresses can change (DHCP)
- Devices can leave the network
- Prevents outdated/incorrect mappings

### **Viewing the ARP cache (Windows 11)**

**Method 1: Command line**

```cmd
arp -a
```

**Example output**:

```
Interface: 192.168.1.10 --- 0x4
  Internet address      Physical address      Type
  192.168.1.1           1c-2d-3e-4f-5a-6b     dynamic
  192.168.1.20          bb-bb-bb-bb-bb-bb     dynamic
  192.168.1.255         ff-ff-ff-ff-ff-ff     static
  224.0.0.22            01-00-5e-00-00-16     static
```

**Explanation**:

- **Internet address**: IP address
- **Physical address**: MAC address (with `-` instead of `:`)
- **Type**: dynamic (time-limited) or static (permanent)

**Method 2: PowerShell**

```powershell
Get-NetNeighbor -AddressFamily IPv4
```

**Further ARP commands**:

**Delete single entry**:

```cmd
arp -d 192.168.1.20
```

**Delete entire cache**:

```cmd
arp -d *
```

**Add static entry**:

```cmd
arp -s 192.168.1.20 BB-BB-BB-BB-BB-BB
```

### **Practical test**

**1. Check cache before ping**:

```cmd
arp -a | findstr "192.168.1.1"
```

(Possibly no entry)

**2. Ping device**:

```cmd
ping 192.168.1.1
```

**3. Check cache after ping**:

```cmd
arp -a | findstr "192.168.1.1"
```

(Entry should now be present!)

**Result**: The ping triggered ARP resolution → entry in cache

### **ARP message format**

**Important fields** (simplified):

```
┌─────────────────────────────────────┐
│ Hardware type: Ethernet (1)         │
│ Protocol type: IPv4 (0x0800)        │
│ Hardware addr length: 6 bytes       │
│ Protocol addr length: 4 bytes       │
│ Opcode: 1=request, 2=reply          │
├─────────────────────────────────────┤
│ Sender MAC address (6 bytes)        │
│ Sender IP address (4 bytes)         │
│ Target MAC address (6 bytes)        │
│   - Request: 00:00:00:00:00:00      │
│   - Reply: known MAC                │
│ Target IP address (4 bytes)         │
└─────────────────────────────────────┘
```

**Opcode values**:

- **1**: ARP request
- **2**: ARP reply

### **Special case: Gateway communication**

**What happens with destinations outside the local network?**

```
Computer A (192.168.1.10) wants to reach Google (8.8.8.8)

8.8.8.8 is NOT on the local network!

Computer A:
1. "8.8.8.8 is not local (different subnet mask)"
2. "Must send to default gateway"
3. ARP request for gateway IP (e.g. 192.168.1.1)
4. Send frame with gateway MAC, but IP packet for 8.8.8.8

Router/gateway:
- Receives frame (its MAC)
- Opens IP packet (destination: 8.8.8.8)
- Forwards to the internet
```

**Important**: Computer A does not need Google's MAC, but the **MAC of the gateway**!

### **ARP security issues**

⚠️ **ARP spoofing/poisoning** (main problem)

**Problem**: ARP **trusts blindly** – no authentication!

**Attack**:

```
Attacker sends fake ARP reply:
"I am 192.168.1.1 (gateway), my MAC is ATTACKER-MAC!"

Victim updates ARP cache:
192.168.1.1 → ATTACKER-MAC (WRONG!)

Now:
Victim → sends internet traffic to attacker
Attacker → intercepts data, (optionally) forwards it
```

**Result**: **Man-in-the-middle (MITM) attack** 🕵️

**Example**:

```
Normal:
PC → Router → Internet

With ARP spoofing:
PC → Attacker → Router → Internet
     ↑
 Reads everything!
```

**Further ARP attacks**:

- **ARP flooding**: Mass fake ARP messages → switch overload
- **Gratuitous ARP abuse**: Unsolicited ARP to overwrite caches

### **ARP security measures**

✅ **Static ARP entries** (for critical devices):

```cmd
arp -s 192.168.1.1 AA-BB-CC-DD-EE-FF
```

Disadvantage: Manual management is complex

✅ **Dynamic ARP Inspection (DAI)** (managed switches):

- Switch validates ARP messages
- Only authorised devices may send ARP replies

✅ **Port security** (switches):

- Limits MAC addresses per port

✅ **ARP monitoring tools**:

- `arpwatch` (Linux)
- Warning on unusual ARP changes

✅ **Network segmentation** (VLANs):

- Limits broadcast domains
- Reduces attack surface

### **Why not just use IP addresses?**

**Question**: Why Layer 2 addresses (MAC) when we have Layer 3 (IP)?

**Answers**:

**1. Layer separation** 🏗️:

- **Layer 2 (Ethernet)**: Developed for local delivery with MACs
- **Layer 3 (IP)**: Developed for global routing
- Each layer has its own role!

**2. Switches operate at Layer 2** 🔀:

- Switches read **only** MAC addresses
- Switches do **not** inspect IP packets
- Ethernet frames need MACs for forwarding

**3. Flexibility** 🔄:

- IP can change (DHCP)
- MAC stays (mostly) the same
- Layer 2 independent of Layer 3 protocol

**4. Historical reasons** 📜:

- Ethernet existed before IP
- MACs were the original mechanism

**Analogy**:

- **MAC address** = House number on the street (local)
- **IP address** = Complete postal address with city (global)
- You need **both** for delivery!

### **Gratuitous ARP (unsolicited ARP)**

**What is it?** ARP request/reply **without a prior request**

**Purposes**:

**1. IP conflict check** 🔍:

```
Device receives new IP (e.g. via DHCP)
Sends gratuitous ARP: "Does anyone already have this IP?"
If response: IP conflict!
```

**2. Cache update** 🔄:

```
Device changes MAC address (e.g. failover)
Sends gratuitous ARP: "My IP now has a new MAC!"
All devices update cache
```

**3. Faster communication** ⚡:

```
Device proactively shares its IP ↔ MAC
Other devices don't need to ask first
```

### **IPv6 and Neighbor Discovery**

**Important**: ARP is **IPv4-specific**!

**IPv6** uses **Neighbor Discovery Protocol (NDP)**:

- Part of ICMPv6
- Similar function to ARP
- Additional features (router discovery, redirect, etc.)

**Neighbor Solicitation** = IPv6 equivalent of ARP request **Neighbor Advertisement** = IPv6 equivalent of ARP reply

### **Core message**

**ARP** is the **invisible helper** that resolves IP addresses to MAC addresses:

**Problem**:

- Layer 3 uses IP addresses
- Layer 2 (Ethernet) needs MAC addresses
- **Gap between layers**

**Solution**:

- **ARP request** (broadcast): "Who has this IP?"
- **ARP reply** (unicast): "Me! Here is my MAC"
- **ARP cache**: Stores mappings for efficiency

**The process**:

```
1. Check cache → If present: send directly
2. If not: ARP request (broadcast) to all
3. Target device responds: ARP reply (unicast)
4. Update cache
5. Send data with correct MAC
```

**Security**: ⚠️ ARP is **not authenticated** → vulnerable to spoofing/poisoning 🛡️ Protective measures: DAI, port security, monitoring, VLANs

**Final analogy**: ARP is like a **local phone directory service** – you call in (broadcast), ask for the number (MAC) matching a name (IP), and the owner responds. Everyone else hears the call but doesn't answer because it wasn't meant for them! 📞📋🔍

## Overview table

|**Category**|**Details**|
|---|---|
|**Tools Used**|• **Terminal/Command Prompt**: Display ARP cache (macOS: `arp -a`; Windows: `arp -a` or `arp /a`)<br>• **PowerShell**: `Get-NetNeighbor` (shows ARP cache in Windows)<br>• **arp**: Manage ARP table (both systems: `arp -a`, `arp -d`, `arp -s`)<br>• **Wireshark**: Analyse and capture ARP packets<br>• **tcpdump**: Capture ARP traffic (macOS: `tcpdump arp`; Windows: WinDump)<br>• **arping**: Send ARP requests manually (Linux/macOS; Windows: via tools)<br>• **ping**: Initiate communication (triggers ARP)<br>• **netsh**: Network configuration (Windows: `netsh interface ipv4 show neighbors`)<br>• **System Settings/Settings**: Check network settings<br>• **Network Monitor**: Advanced network analysis (Windows)<br>• **arpwatch**: ARP monitoring tool (Unix/Linux)<br>• **Packet Tracer**: ARP simulation in Cisco environments|
|**Technical Terms**|• **ARP** (Address Resolution Protocol): Address resolution protocol<br>• **IP address**: Internet Protocol address (Layer 3)<br>• **MAC address**: Media Access Control address (Layer 2)<br>• **Layer 2**: Data Link Layer<br>• **Layer 3**: Network Layer<br>• **Address resolution**: Translation of IP to MAC<br>• **ARP request**: ARP query (broadcast)<br>• **ARP reply**: ARP response (unicast)<br>• **ARP cache/table**: Temporary storage of IP ↔ MAC mappings<br>• **Broadcast**: Transmission to all devices<br>• **Unicast**: Transmission to one specific device<br>• **Broadcast MAC address**: FF:FF:FF:FF:FF:FF<br>• **Local network segment**: Directly connected network area<br>• **Broadcast domain**: Area reached by broadcast frames<br>• **Ethernet frame**: Structured Layer 2 data unit<br>• **NIC** (Network Interface Card): Network adapter<br>• **Default gateway**: Router address for leaving local network<br>• **Dynamic entry**: Time-limited cache entry<br>• **Static entry**: Permanent cache entry<br>• **Timeout/TTL**: Expiry time/validity period<br>• **Opcode**: Operation code (1=request, 2=reply)<br>• **Hardware type**: Hardware type (e.g. Ethernet)<br>• **Protocol type**: Protocol type (e.g. IPv4)<br>• **Sender MAC/IP**: Sender MAC/IP address<br>• **Target MAC/IP**: Target MAC/IP address<br>• **ARP spoofing/poisoning**: ARP deception attack<br>• **MITM** (Man-in-the-Middle): Attack via ARP manipulation<br>• **Gratuitous ARP**: Unsolicited ARP (IP conflict check)<br>• **Proxy ARP**: ARP proxy (router responds for other networks)<br>• **Reverse ARP (RARP)**: Reverse ARP (MAC → IP, outdated)<br>• **IPv6 Neighbor Discovery**: IPv6 neighbour discovery (replaces ARP)|
|**Important Vocabulary**|• **Address resolution**: Translation from IP to MAC<br>• **Local network segment**: Directly connected network area<br>• **Physical address**: Hardware address (MAC)<br>• **Logical address**: Network address (IP)<br>• **Look up**: Search for a mapping<br>• **Mapping**: Association of IP ↔ MAC<br>• **Temporary cache**: Short-term storage<br>• **Recently learned**: Dynamically acquired entries<br>• **Expiry time**: Timeout period<br>• **Stale information**: Outdated data<br>• **Boundary**: Interface between layers<br>• **Stateless**: No persistent connection<br>• **Request-response**: Request-response mechanism<br>• **Flooding**: Broadcast on all ports<br>• **Silently discard**: Discard without notification<br>• **Encapsulate**: Wrap in Ethernet frame<br>• **Forward**: Forwarding<br>• **Burned-in**: Permanently programmed into hardware<br>• **Final delivery**: Last-hop delivery<br>• **Shared**: Common segment<br>• **Bridging**: Connection between layers<br>• **Verification**: Checking identity<br>• **Abuse**: Security violation<br>• **Trust**: Reliance on ARP system<br>• **Spoofed reply**: Fake reply<br>• **Compromise**: Security breach|