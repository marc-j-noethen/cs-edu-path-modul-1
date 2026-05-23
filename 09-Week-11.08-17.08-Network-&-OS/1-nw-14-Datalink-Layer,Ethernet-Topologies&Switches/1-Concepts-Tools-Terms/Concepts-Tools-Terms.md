## 📊 Summary based on the 80/20 principle

### **The Data Link Layer (Layer 2): The local neighbourhood manager**

**Layer 2 (Data Link Layer)** = Management of communication **within a local network segment**

**Three-layer overview**:

```
┌─────────────────────────────────────────────┐
│ Layer 3 (Network Layer)                     │
│ → IP addresses                              │
│ → Routing between networks                  │
│ → "Traffic between cities"                  │
└─────────────────────────────────────────────┘
              ▲
              │
┌─────────────────────────────────────────────┐
│ Layer 2 (Data Link Layer)                   │
│ → MAC addresses                             │
│ → Frames                                    │
│ → Communication in local network            │
│ → "Local neighbourhood traffic"             │
└─────────────────────────────────────────────┘
              ▲
              │
┌─────────────────────────────────────────────┐
│ Layer 1 (Physical Layer)                    │
│ → Bits (0 and 1)                            │
│ → Cables, radio waves                       │
│ → "Pure signal transmission"                │
└─────────────────────────────────────────────┘
```

**Analogy**:

- **Layer 1**: The road (bits travel on it)
- **Layer 2**: Local postmen (deliver within the neighbourhood using house numbers = MAC addresses)
- **Layer 3**: National postal service (deliver between cities using city names = IP addresses)

### **The 5 main functions of Layer 2**

#### **1. Framing 📦**

**What is it?** Raw bits are organised into **structured frames**

```
Bits from Layer 1: 01001000 01100101 01101100 01101100...

Layer 2 organises into frame:
┌────────────┬────────────┬──────────┬─────────┬─────┐
│  Header    │  Dest. MAC │ Src. MAC │ Payload │ FCS │
│ (Preamble) │  (6 bytes) │ (6 bytes)│  (data) │     │
└────────────┴────────────┴──────────┴─────────┴─────┘
```

**Frame structure**: Header + addressing + data + trailer

#### **2. Physical addressing (MAC addresses) 🏠**

Devices in the local network are identified by **unique hardware addresses**

**MAC address** = 48-bit (6 bytes) hexadecimal

**Format**: `00:1A:2B:3C:4D:5E`

```
00:1A:2B  :  3C:4D:5E
────────     ────────
   OUI       Device ID
(Vendor)    (unique)
```

**Example OUIs**:

- `00:1A:2B` → Cisco
- `00:50:56` → VMware
- `3C:22:FB` → Apple

#### **3. Error detection ✅**

**Frame Check Sequence (FCS)** in the trailer detects transmission errors

```
Sender calculates checksum → FCS in frame
Receiver calculates again → comparison
Doesn't match? → Discard frame
```

**Important**: Layer 2 detects errors, **but does not correct them** (higher layers handle that)

#### **4. Flow control 🚦**

Prevents a fast sender from overwhelming a slow receiver

**Mechanism**: Receiver signals "pause" when buffer is full

#### **5. Media Access Control (MAC) 🎛️**

Regulates **who may transmit when** on a shared medium

**Previously (shared medium)**: CSMA/CD

- **C**arrier **S**ense: Listen whether line is free
- **M**ultiple **A**ccess: Multiple devices share the medium
- **C**ollision **D**etection: Detect collision → wait → retry

**Today (switched networks)**: Largely obsolete, as switches create separate collision domains

### **Ethernet: The dominant LAN technology**

**Ethernet** = Standard for wired local area networks (LANs)

**History**:

- **1970s**: Invention, shared coaxial cable
- **Today**: Twisted-pair cable + switches (modern networks)

**Ethernet frame structure**:

```
┌──────────┬────────────┬────────────┬──────────┬─────────┬─────┐
│ Preamble │  Dest. MAC │  Src. MAC  │EtherType │ Payload │ FCS │
│ (8 bytes)│  (6 bytes) │  (6 bytes) │ (2 bytes)│(46-1500)│(4 B)│
└──────────┴────────────┴────────────┴──────────┴─────────┴─────┘
```

**Important fields**:

- **Dest. MAC**: Recipient in local network
- **Src. MAC**: Sender in local network
- **EtherType**: Which protocol? (e.g. 0x0800 = IPv4, 0x86DD = IPv6)
- **Payload**: The actual data (e.g. IP packet)
- **FCS**: Error checking

### **Hub vs. switch: The crucial difference**

#### **Hub (Layer 1 – outdated) 🔊**

**Function**: Dumb multiport repeater

```
Signal arrives at port 1
          ↓
Hub sends signal to ALL other ports
          ↓
All devices receive EVERYTHING (even what isn't meant for them)
```

**Properties**:

- ❌ No intelligence (doesn't look at MAC addresses)
- ❌ **One collision domain** (all ports share the medium)
- ❌ **Half-duplex** (transmit OR receive)
- ❌ **Inefficient** (many collisions with many devices)
- ❌ **Outdated** (practically no longer used today)

**Analogy**: Like a loudspeaker – shouts everything at everyone

#### **Switch (Layer 2 – modern) 🧠**

**Function**: Intelligent forwarding device

```
Frame arrives at port 1
          ↓
Switch reads destination MAC address
          ↓
Switch searches MAC address table: Where is the destination?
          ↓
Switch sends frame ONLY to port with destination device
```

**MAC address table (learning process)**:

```
Port | MAC address        | Learned from
-----|--------------------|---------------
1    | 00:1A:2B:3C:4D:5E | Frame from port 1
2    | AA:BB:CC:DD:EE:FF | Frame from port 2
3    | 11:22:33:44:55:66 | Frame from port 3
```

**How the switch learns**:

1. Frame arrives at port 1 with source MAC `00:1A:2B:3C:4D:5E`
2. Switch: "Aha! Device with MAC `00:1A:2B:3C:4D:5E` is at port 1!"
3. Entry in table
4. Next time frame for `00:1A:2B:3C:4D:5E` → send only to port 1

**Properties**:

- ✅ **Intelligent** (learns MAC addresses)
- ✅ **Separate collision domains** per port (no collisions between ports!)
- ✅ **Full-duplex** (simultaneous transmitting AND receiving)
- ✅ **Efficient** (targeted forwarding)
- ✅ **Standard in modern networks**

**Analogy**: Like an intelligent postman – knows every address and only delivers mail to the right house

### **Hub vs. switch: Comparison table**

|Feature|Hub|Switch|
|---|---|---|
|**Layer**|1 (Physical)|2 (Data Link)|
|**Intelligence**|❌ None|✅ MAC address learning|
|**Forwarding**|To ALL ports|Only to destination port|
|**Collision domain**|One (all ports)|One per port|
|**Broadcast domain**|One|One (default)|
|**Duplex**|Half-duplex|Full-duplex|
|**Efficiency**|❌ Very low|✅ Very high|
|**Status today**|Outdated|Standard|

### **Collision domain vs. broadcast domain**

**Collision domain** 💥:

```
Area where simultaneous transmissions can collide

Hub: ONE collision domain (all ports)
┌─────────────────────────────────┐
│ [PC1] [PC2] [PC3] [PC4]         │
│  All share the medium           │
└─────────────────────────────────┘

Switch: Separate collision domain per port
┌───┐ ┌───┐ ┌───┐ ┌───┐
│PC1│ │PC2│ │PC3│ │PC4│
└─┬─┘ └─┬─┘ └─┬─┘ └─┬─┘
  └─────┼─────┼─────┘
      [Switch]
    No collisions!
```

**Broadcast domain** 📢:

```
Area where broadcast frames reach everyone

Hub/Switch: ONE broadcast domain
Frame to FF:FF:FF:FF:FF:FF → all ports

Router: Separates broadcast domains
Broadcasts are NOT forwarded
```

### **MAC addresses: The hardware identity**

**MAC (Media Access Control) address** = 48-bit hardware address

**Format**: 6 bytes hexadecimal

```
00:1A:2B:3C:4D:5E
│       │
│       └─ Device ID (assigned by manufacturer)
└───────── OUI (vendor ID)
```

**Properties**:

- ✅ **Globally unique** (theoretically)
- ✅ **Burned in by manufacturer** (permanently programmed into NIC)
- ✅ **For Layer 2 communication** (within local network)
- ⚠️ **Can be changed in software** (MAC spoofing)

**Special MAC addresses**:

- **Broadcast**: `FF:FF:FF:FF:FF:FF` (to all in local network)
- **Multicast**: Starts with `01:00:5E` (IPv4 multicast)

**MAC vs. IP**:

```
MAC address:
- Layer 2 (Data Link Layer)
- Local network
- Hardware-based
- Does not normally change
- Example: 00:1A:2B:3C:4D:5E

IP address:
- Layer 3 (Network Layer)
- Global internet
- Software-based
- Changes (DHCP, new networks)
- Example: 192.168.1.100
```

**Why both?**

- **IP**: Finds the route through the internet (routing)
- **MAC**: Delivers within the local network (switching)

**Analogy**:

- **IP address** = Postcode + street + house number (for routing)
- **MAC address** = Name on the doorbell (for local delivery)

### **Finding your MAC address (Windows 11)**

**Method 1: Settings (GUI)**

1. **Settings** → **Network & Internet**
2. **Properties** of the active connection
3. Look for **Physical address (MAC)**

**Method 2: Command line**

```cmd
ipconfig /all
```

Look for **Physical address** under your adapter

**Method 3: PowerShell**

```powershell
Get-NetAdapter | Select-Object Name, MacAddress
```

**Method 4: getmac**

```cmd
getmac /v
```

### **Network topologies: How devices are connected**

**Topology** = Arrangement/layout of network connections

#### **1. Bus topology 🚌 (outdated)**

```
[PC1]──┬──[PC2]──┬──[PC3]──┬──[PC4]
       │         │         │
    Shared cable (bus)
  Terminators at both ends
```

**Properties**:

- ✅ Simple, inexpensive
- ❌ Cable failure → entire network down
- ❌ Many collisions
- ❌ **Outdated**

#### **2. Ring topology 🔄 (rare)**

```
     [PC1]
    ↗     ↘
[PC4]       [PC2]
    ↖     ↙
     [PC3]
```

**Properties**:

- Token passing (orderly transmission)
- ❌ Failure of one device → ring breaks
- ❌ Less common

#### **3. Star topology ⭐ (STANDARD!)**

```
      [PC1]
        │
[PC2]─[Switch]─[PC3]
        │
      [PC4]
```

**Properties**:

- ✅ **Today's standard for LANs**
- ✅ Easy to install/manage
- ✅ Cable failure → only 1 device affected
- ✅ Easy to expand
- ✅ With switch: Separate collision domains + full-duplex
- ❌ Switch failure → entire segment down
- ❌ More cabling required

**Why star topology is most popular?**

- Reliable
- Scalable
- Efficient (with switch)
- Easy to troubleshoot

#### **4. Mesh topology 🕸️ (high availability)**

```
Full mesh:
[PC1]─────[PC2]
  │  ╲   ╱  │
  │   ╲ ╱   │
  │   ╱ ╲   │
  │  ╱   ╲  │
[PC3]─────[PC4]
(Everyone connected to everyone)
```

**Properties**:

- ✅ **Highest redundancy**
- ✅ Failure of one connection → alternative paths
- ❌ Very expensive (many cables)
- ❌ Complex to configure
- 🎯 **Use**: Internet backbone, critical networks

#### **5. Hybrid topology 🔀**

```
Combination of multiple topologies
e.g. multiple star networks connected via backbone
```

**Properties**:

- ✅ Flexible, scalable
- ❌ Complex

### **Home network example**

**Typical setup**:

```
      Internet
         │
    [Router/Modem]
         │
      (Wi-Fi)
   ╱    │    ╲
[Laptop] [Smartphone] [Smart TV]
```

**Topology**: **Star** (all devices connect centrally to the router)

### **Practical example: Switch forwarding**

**Scenario**:

```
Port 1: PC-A (MAC: AA:AA:AA:AA:AA:AA)
Port 2: PC-B (MAC: BB:BB:BB:BB:BB:BB)
Port 3: PC-C (MAC: CC:CC:CC:CC:CC:CC)

PC-A wants to send a frame to PC-C
```

**Process**:

```
1. PC-A sends frame:
   Source MAC: AA:AA:AA:AA:AA:AA
   Dest. MAC:  CC:CC:CC:CC:CC:CC

2. Frame arrives at switch port 1

3. Switch learns:
   "MAC AA:AA:AA:AA:AA:AA is at port 1"
   → Entry in MAC table

4. Switch looks at destination MAC:
   "Where is CC:CC:CC:CC:CC:CC?"
   → In table: port 3

5. Switch sends frame ONLY to port 3

6. PC-C receives frame
   PC-A and PC-B receive NOTHING (efficient!)
```

**If destination MAC is unknown**:

```
Switch does not know destination MAC
→ Sends frame to ALL ports (except source port)
→ "Flooding"
→ Correct device responds
→ Switch learns MAC address
```

### **Core message**

**Layer 2 (Data Link Layer)** manages **local network communication**:

**Frames** = Structured data units with MAC addresses **MAC addresses** = Hardware identity for Layer 2 communication **Switches** = Intelligent devices that forward frames in a targeted manner

**Evolution**:

```
Previously: Hub + shared medium
           → Many collisions, half-duplex, inefficient

Today: Switch + star topology
      → Separate collision domains, full-duplex, highly efficient
```

**The switch** was the **revolution in LAN**:

- Intelligent forwarding
- Separate collision domains per port
- Full-duplex operation
- Drastically higher efficiency

**Interaction with other layers**:

- **Layer 1**: Transmit bits
- **Layer 2**: Distribute frames in local network (MAC addresses)
- **Layer 3**: Route packets between networks (IP addresses)

**Final analogy**: Layer 2 is like a **local postal centre** that distributes mail within a city/neighbourhood (MAC = house numbers), while Layer 3 is like the **national postal system** that handles delivery between cities (IP = city names)! 📬🏘️🔀

---

## Tools Used

|Term|Meaning|
|---|---|
|**System Settings/Settings**|Display MAC address (macOS: System Settings → Network → Details → Hardware; Windows: Settings → Network & Internet → Properties)|
|**Terminal/Command Prompt**|Display network interfaces (macOS: `ifconfig en0`; Windows: `ipconfig /all`, `getmac`)|
|**arp**|Display ARP table (both systems: `arp -a`)|
|**Wireshark**|Analyse Ethernet frames and MAC addresses|
|**tcpdump**|Packet analysis at Layer 2 (macOS; Windows: WinDump)|
|**PowerShell**|`Get-NetAdapter`, `Get-NetAdapterStatistics`|
|**Device Manager**|Manage network adapters (Windows)|
|**Network Utility**|Network diagnostics (macOS: outdated, replaced by terminal commands)|
|**Sysinternals Suite**|Network troubleshooting tools (Windows)|
|**Switch management software**|Web interface or CLI for managed switches|
|**MAC Address Lookup**|Online tools for OUI vendor lookup|
|**Ethernet tester**|Hardware tools for cable testing|
|**Network analyser**|Professional Layer 2 analysis tools|

---

## Technical Terms

|Term|Meaning|
|---|---|
|**Data Link Layer**|Layer 2 in the OSI model|
|**Frame**|Data unit at Layer 2 (structured data frame)|
|**MAC address** (Media Access Control)|Hardware/physical address|
|**Physical Layer**|Layer 1|
|**Network Layer**|Layer 3|
|**Ethernet**|Widely used LAN technology|
|**Frame Check Sequence (FCS)**|Error checking field in the frame trailer|
|**Media Access Control**|Access control for shared medium|
|**CSMA/CD** (Carrier Sense Multiple Access with Collision Detection)|Collision detection for Ethernet|
|**Hub**|Simple Layer 1 device (repeater)|
|**Switch**|Intelligent Layer 2 device|
|**MAC address table/CAM table**|MAC address mapping table in the switch|
|**Collision domain**|Area where collisions can occur|
|**Broadcast domain**|Area reached by broadcast frames|
|**Half-duplex**|Transmit or receive, not simultaneously|
|**Full-duplex**|Simultaneous transmitting and receiving|
|**NIC** (Network Interface Card)|Network adapter/card|
|**OUI** (Organizationally Unique Identifier)|Vendor identifier (first 6 hex digits)|
|**EtherType**|Protocol identifier in the Ethernet frame|
|**Payload**|User data in the frame|
|**Broadcast address**|Broadcast address (FF:FF:FF:FF:FF:FF)|
|**Unicast**|Point-to-point transmission|
|**Multicast**|Transmission to a group|
|**Twisted-pair cable**|Twisted copper cable (e.g. Cat5e, Cat6)|
|**Coaxial cable**|Coaxial cable (outdated)|
|**Network topology**|Arrangement of network devices|
|**Star topology**|Central connection of all devices|
|**Bus topology**|Shared cable topology|
|**Ring topology**|Circular connection topology|
|**Mesh topology**|Interconnected topology|
|**Hybrid topology**|Combination of multiple topologies|
|**Managed switch**|Configurable switch|
|**Unmanaged switch**|Non-configurable switch|
|**VLAN** (Virtual LAN)|Virtual local area network|
|**STP** (Spanning Tree Protocol)|Loop prevention protocol|
|**ARP** (Address Resolution Protocol)|IP-to-MAC resolution|

---

## Important Vocabulary

|Vocabulary|Meaning|
|---|---|
|**Local network segment**|Area of direct Layer 2 communication|
|**Raw bits**|Unstructured binary data|
|**Structured units**|Organised data frames|
|**Neighbourhood traffic**|Local network communication|
|**Hardware address**|Physical device identifier|
|**Error checking**|Detection of corrupted data|
|**Flow control**|Adjustment of transmission rate|
|**Shared medium**|Cable used by multiple devices|
|**Collision**|Simultaneous transmission by multiple devices|
|**Corrupted data**|Transmission damaged by collision|
|**Multiport repeater**|Hub as signal amplifier|
|**Intelligent device**|Switch with learning capability|
|**Forwarding**|Targeted frame transmission|
|**Broadcast**|Transmission to all devices|
|**Burned-in identifier**|Address permanently programmed into hardware|
|**Hexadecimal digits**|Base-16 system (0–9, A–F)|
|**Vendor identifier**|OUI for manufacturer identification|
|**Star topology**|Central connection of all devices|
|**Central device**|Hub or switch at the centre of a star|
|**Redundant paths**|Multiple connection routes (mesh)|
|**Fault tolerance**|Resilience against device failure|
|**Cabling**|Physical network connections|
|**Configuration**|Setup and adjustment|
|**Backbone network**|Main interconnection network|
|**Critical availability**|High operational reliability|
|**Scalability**|Capacity for expansion|
|**Troubleshooting**|Fault finding and resolution|
|**Token passing**|Passing of transmission rights|
|**Terminators**|Termination resistors at cable ends|
|**Dual ring**|Double ring for redundancy|