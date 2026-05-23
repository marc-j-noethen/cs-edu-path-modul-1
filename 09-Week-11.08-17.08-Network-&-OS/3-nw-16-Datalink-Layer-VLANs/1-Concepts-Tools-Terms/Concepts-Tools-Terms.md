# Categorisation VLANs (Virtual Local Area Networks)

### **What is a LAN? Recap**

**LAN (Local Area Network)** = Local network in a limited geographic area

**Traditional LAN**:

```
┌──────────────────────────────────────┐
│  ONE broadcast domain                │
│                                      │
│  [PC1] [PC2] [PC3] [Printer] [Server]│
│         All on the same switch       │
│                                      │
│  Broadcast from PC1 → ALL receive    │
└──────────────────────────────────────┘
```

**Property**: All devices = one broadcast domain = all hear all broadcasts

### **The problem: Large LANs become unmanageable**

**4 main problems of large, flat LANs**:

#### **1. Security risks** 🔓

```
Guest Wi-Fi + finance server on the SAME network?

Guest laptop (compromised)
    ↓
Can access finance server
    ↓
Data breach! 💀
```

#### **2. Performance issues** 🐌

```
1000 devices on the same LAN
    ↓
Every broadcast goes to ALL 1000 devices
    ↓
Bandwidth wasted, CPU load on all devices
```

#### **3. Management chaos** 😵

```
Sales, Engineering, HR, Guests - all mixed together
→ Hard to manage
→ Hard to enforce policies
```

#### **4. Lack of flexibility** 🔌

```
Employee changes department
→ Physically move cables?
→ Inefficient and expensive!
```

**Solution**: **Network segmentation** through **VLANs**!

### **What are VLANs? Virtual mini-networks**

**VLAN (Virtual Local Area Network)** = **Virtual** subdivision of a **physical** LAN into **multiple logically separate** networks

**Core idea**:

```
ONE physical switch
     ↓
Logically divided into multiple "virtual switches"
     ↓
Each VLAN = its own broadcast domain
```

**Analogy**: An open-plan office building → VLANs are like **invisible partition walls** that isolate departments, even though they are in the same building (switch)

### **VLAN example: Before vs. after**

#### **WITHOUT VLANs (traditional)**:

```
Physical separation required:

┌──────────────┐      ┌──────────────┐      ┌──────────────┐
│  Switch 1    │      │  Switch 2    │      │  Switch 3    │
│  (Sales)     │      │  (Engineering)│     │  (HR)        │
├──────────────┤      ├──────────────┤      ├──────────────┤
│ PC1  PC2  PC3│      │ PC4  PC5  PC6│      │ PC7  PC8  PC9│
└──────────────┘      └──────────────┘      └──────────────┘

Requires: 3 switches, lots of cabling, expensive!
```

#### **WITH VLANs (modern)**:

```
Logical separation on ONE switch:

┌─────────────────────────────────────────────────────┐
│           ONE physical switch                       │
├─────────────────────────────────────────────────────┤
│  VLAN 10 (Sales)  │ VLAN 20 (Eng)  │ VLAN 30 (HR)  │
│  ┌──┬──┬──┐       │ ┌──┬──┬──┐     │ ┌──┬──┬──┐   │
│  │P1│P2│P3│       │ │P4│P5│P6│     │ │P7│P8│P9│   │
│  └──┴──┴──┘       │ └──┴──┴──┘     │ └──┴──┴──┘   │
└─────────────────────────────────────────────────────┘

Requires: 1 VLAN-capable switch (managed switch)
Advantages: Cheaper, more flexible, simpler!
```

**Important**: Devices in **VLAN 10** cannot communicate **directly** with devices in **VLAN 20** (without a router/Layer 3 switch)!

### **How VLANs work: VLAN tagging (802.1Q)**

**Problem**: How does a switch know which VLAN a frame belongs to?

**Solution**: **VLAN tag** in the Ethernet frame

**IEEE 802.1Q standard**:

```
Normal Ethernet frame:
┌────────┬────────┬──────────┬─────────┬─────┐
│Dest.MAC│Src. MAC│ EtherType│ Payload │ FCS │
└────────┴────────┴──────────┴─────────┴─────┘

With 802.1Q VLAN tag:
┌────────┬────────┬──────────┬──────────┬─────────┬─────┐
│Dest.MAC│Src. MAC│ 802.1Q   │ EtherType│ Payload │ FCS │
│        │        │ VLAN tag │          │         │     │
│        │        │ (4 bytes)│          │         │     │
└────────┴────────┴──────────┴──────────┴─────────┴─────┘
                      ↑
                VLAN ID (VID): e.g. 10
```

**VLAN tag contains**:

- **VLAN ID (VID)**: Number 1–4094 (identifies VLAN)
- **Priority**: QoS priority
- **Tag Protocol Identifier (TPID)**: 0x8100 (marks 802.1Q)

### **Access ports vs. trunk ports: The two port types**

#### **Access port** 🚪

**Properties**:

- Belongs to **ONE VLAN**
- For **end devices** (PCs, printers, phones)
- Devices are **VLAN-unaware** (know nothing about VLANs)
- Switch **adds** VLAN tag when sending (to trunk)
- Switch **removes** VLAN tag when receiving (from trunk)

**Example**:

```
PC1 (VLAN 10) → Access port 1
PC2 (VLAN 20) → Access port 2

PC1 sends normal frame (without tag)
    ↓
Switch port 1 (access, VLAN 10):
"This is VLAN 10 traffic"
    ↓
Adds tag "VLAN 10" (if going to trunk)
```

**Configuration** (Cisco example):

```
interface FastEthernet0/1
  switchport mode access
  switchport access vlan 10
```

#### **Trunk port** 📦

**Properties**:

- Carries traffic for **MULTIPLE VLANs**
- For **inter-switch connections** or **router connections**
- Frames retain **VLAN tag** (802.1Q)
- Receiver can identify VLAN from tag

**Example**:

```
┌────────────┐                    ┌────────────┐
│  Switch A  │                    │  Switch B  │
│            │                    │            │
│ VLAN 10 ──┐│ Trunk (carries all)│┌── VLAN 10 │
│ VLAN 20 ──┼┼────────────────────┼┼── VLAN 20 │
│ VLAN 30 ──┘│  VLANs 10, 20, 30  │└── VLAN 30 │
└────────────┘                    └────────────┘

Over trunk, frames flow with tags:
[VLAN 10] [VLAN 20] [VLAN 10] [VLAN 30]...
```

**Configuration** (Cisco example):

```
interface GigabitEthernet0/1
  switchport mode trunk
  switchport trunk allowed vlan 10,20,30
```

### **Access vs. trunk: Comparison table**

|Feature|Access port|Trunk port|
|---|---|---|
|**VLANs**|ONE VLAN|MULTIPLE VLANs|
|**Connects**|End devices|Switches, routers|
|**VLAN tag**|Removed/added|Retained|
|**Device awareness**|VLAN-unaware|VLAN-aware|
|**Use**|PC, printer, phones|Inter-switch links|
|**Example**|PC on port 5|Switch-to-switch|

### **Native VLAN: The special case**

**Native VLAN** = VLAN for **untagged** traffic on trunk ports

**Default**: VLAN 1 (default VLAN)

**How it works**:

```
Trunk receives frame WITHOUT tag
    ↓
"This must be the native VLAN!"
    ↓
Assigned to native VLAN (e.g. VLAN 1)
```

**Why does it matter?**

- Backward compatibility with non-802.1Q devices
- Management traffic (CDP, VTP) often in native VLAN

**Security note**: Native VLAN **should be changed** (don't use VLAN 1) → prevents VLAN hopping attacks

### **Practical VLAN example**

**Scenario**: Company with 3 departments on one switch

```
┌───────────────────────────────────────────────────┐
│           Managed switch                          │
├───────────────────────────────────────────────────┤
│ Port 1-5:   VLAN 10 (Sales)       - Access ports │
│ Port 6-10:  VLAN 20 (Engineering) - Access ports │
│ Port 11-15: VLAN 30 (Guest)       - Access ports │
│ Port 24:    Trunk to router       - Trunk port   │
└───────────────────────────────────────────────────┘
```

**Communication**:

**Within a VLAN** (e.g. VLAN 10):

```
PC1 (port 1, VLAN 10) → PC2 (port 3, VLAN 10)
    ✅ Works directly (same broadcast domain)
```

**Between VLANs** (e.g. VLAN 10 → VLAN 20):

```
PC1 (VLAN 10) → PC6 (VLAN 20)
    ❌ Does NOT work directly!
    ✅ Needs router (inter-VLAN routing)

Flow with router:
1. PC1 → switch (VLAN 10)
2. Switch → router (over trunk, tag: VLAN 10)
3. Router: routing decision
4. Router → switch (over trunk, tag: VLAN 20)
5. Switch → PC6 (VLAN 20)
```

### **Inter-VLAN routing: Communication between VLANs**

**Problem**: VLANs are **isolated** → no direct communication

**Solution**: **Router** or **Layer 3 switch**

**Method 1: Router-on-a-stick**

```
┌────────────┐
│   Router   │
│  (1 port)  │
└──────┬─────┘
       │ Trunk (sub-interfaces)
       │ - VLAN 10: 192.168.10.1/24
       │ - VLAN 20: 192.168.20.1/24
       │ - VLAN 30: 192.168.30.1/24
       │
┌──────┴─────────────────────────┐
│    Managed switch               │
│  VLANs 10, 20, 30              │
└────────────────────────────────┘
```

**Method 2: Layer 3 switch** (more modern):

```
Layer 3 switch with routing:
- Can route directly between VLANs
- Faster than external routers
- SVIs (Switch Virtual Interfaces) for each VLAN
```

### **Advantages of VLANs: The 5 main benefits**

#### **1. Improved security** 🔒

```
VLAN 10 (Employees) → Access to internal resources
VLAN 99 (Guests)    → Internet access only

Guests CANNOT reach company servers!
```

#### **2. Reduced broadcast traffic** 📉

```
Without VLANs:
Broadcast → 500 devices receive

With VLANs (5 VLANs with 100 devices each):
Broadcast in VLAN 10 → only 100 devices receive
75% less broadcast traffic!
```

#### **3. Cost savings** 💰

```
Without VLANs: 5 physical switches needed
With VLANs: 1 managed switch is enough

Savings: Hardware, cabling, power, maintenance
```

#### **4. Flexibility** 🔄

```
Employee moves from Sales to Engineering:

Without VLANs: Physically move cable
With VLANs: Change port configuration (30 seconds!)

switchport access vlan 20  (instead of vlan 10)
```

#### **5. Simplified management** 🎯

```
Logical grouping by function, not location:

Accounting VLAN (VLAN 50):
- All accounting PCs
- Regardless of floor 1, floor 3, or branch office
- Same security policies for all
```

### **VLAN security: Attacks and protection**

⚠️ **VLAN hopping** (main attack)

**Attack 1: Double tagging**

```
Attacker in VLAN 10 sends frame:
[Outer tag: VLAN 10] [Inner tag: VLAN 20] [Payload]

Switch 1: Removes outer tag (VLAN 10)
    ↓
Frame now only has inner tag (VLAN 20)
    ↓
Switch 2: "This is VLAN 20!" → Forwards to VLAN 20

Attacker bypasses VLAN isolation! 💀
```

**Attack 2: Switch spoofing**

```
Attacker sends DTP packets (Dynamic Trunking Protocol)
    ↓
Tricks switch: "I am another switch!"
    ↓
Port becomes trunk
    ↓
Attacker receives traffic of all VLANs
```

**Protective measures**:

✅ **Change native VLAN** (not VLAN 1):

```
switchport trunk native vlan 999
```

✅ **Disable DTP** (no auto-trunking):

```
switchport mode access
switchport nonegotiate
```

✅ **Disable unused ports**:

```
interface range FastEthernet0/10-24
  shutdown
  switchport access vlan 999  (unused VLAN)
```

✅ **Port security**:

```
switchport port-security
switchport port-security maximum 2
switchport port-security violation shutdown
```

### **VLAN best practices**

1. **Do not use VLAN 1** → Security risk as it is the default
2. **Change native VLAN** → Prevents double tagging
3. **Separate management VLAN** → Isolate switch administration
4. **Voice VLANs for VoIP** → QoS for phones
5. **Documentation** → Which VLAN is for what?
6. **VLAN naming** → Meaningful names (not just numbers)
7. **Least privilege** → Only allow necessary VLANs on trunks

### **VLAN configuration (Cisco example)**

**Create VLAN**:

```
Switch(config)# vlan 10
Switch(config-vlan)# name Sales
Switch(config-vlan)# exit

Switch(config)# vlan 20
Switch(config-vlan)# name Engineering
Switch(config-vlan)# exit
```

**Configure access port**:

```
Switch(config)# interface FastEthernet0/1
Switch(config-if)# switchport mode access
Switch(config-if)# switchport access vlan 10
Switch(config-if)# exit
```

**Configure trunk port**:

```
Switch(config)# interface GigabitEthernet0/1
Switch(config-if)# switchport mode trunk
Switch(config-if)# switchport trunk allowed vlan 10,20,30
Switch(config-if)# switchport trunk native vlan 99
Switch(config-if)# exit
```

**Display VLANs**:

```
Switch# show vlan brief
Switch# show interfaces trunk
```

### **Core message**

**VLANs** enable **logical network segmentation** on **one physical switch**:

**Problem**:

- Large, flat LANs = insecure, slow, inflexible, hard to manage

**Solution**:

- **VLANs** divide one physical LAN into **multiple virtual LANs**
- Each VLAN = **its own broadcast domain**
- Devices in different VLANs **isolated** from each other

**Technology**:

- **IEEE 802.1Q**: VLAN tagging standard
- **Access ports**: One VLAN, for end devices
- **Trunk ports**: Multiple VLANs, for inter-switch links

**Advantages**:

- ✅ **Security** (isolation)
- ✅ **Performance** (fewer broadcasts)
- ✅ **Flexibility** (logical assignment)
- ✅ **Cost savings** (less hardware)
- ✅ **Simplified management** (central configuration)

**Inter-VLAN communication**: Requires **router** or **Layer 3 switch**

**Final analogy**: VLANs are like **invisible partition walls in an open-plan office** – physically one room (switch), but logically several separate areas (VLANs). Each department (VLAN) has its own area and cannot disturb the others, even though everyone is in the same building (switch)! 🏢🔀🛡️

## Overview table

|**Category**|**Details**|
|---|---|
|**Tools Used**|• **Managed switch**: VLAN-capable switch (e.g. Cisco Catalyst, HP ProCurve, Netgear)<br>• **Switch web interface**: VLAN configuration via browser<br>• **Cisco IOS CLI**: Command-line interface for Cisco switches<br>• **Packet Tracer**: Cisco network simulator for VLAN exercises (Windows & macOS)<br>• **GNS3**: Network emulator with VLAN support<br>• **Wireshark**: Analyse 802.1Q VLAN tags<br>• **VLAN management software**: Vendor-specific tools<br>• **Network diagram tools**: Visio, draw.io, Lucidchart (draw VLAN topologies)<br>• **SNMP tools**: VLAN monitoring (e.g. PRTG, SolarWinds)<br>• **Terminal/SSH client**: CLI access to switches (PuTTY for Windows)<br>• **PowerShell**: Network VLAN configuration (Windows Server Hyper-V VLANs)<br>• **Linux VLANs**: `vconfig`, `ip link` for VLAN interfaces|
|**Technical Terms**|• **VLAN** (Virtual Local Area Network): Virtual local area network<br>• **LAN** (Local Area Network): Local area network<br>• **Broadcast domain**: Area reached by broadcast frames<br>• **Network segmentation**: Division of networks into separate segments<br>• **IEEE 802.1Q**: VLAN tagging standard<br>• **VLAN tagging**: VLAN marking in Ethernet frames<br>• **VLAN ID (VID)**: VLAN identification number (1–4094)<br>• **Access port**: Port belonging to one VLAN<br>• **Trunk port**: Port carrying multiple VLANs<br>• **Native VLAN**: Default VLAN for untagged traffic on trunk<br>• **Untagged traffic**: Traffic without VLAN tag<br>• **Tagged traffic**: Traffic with 802.1Q tag<br>• **Inter-VLAN routing**: Routing between VLANs<br>• **Layer 2 segmentation**: Segmentation at Layer 2<br>• **Layer 3 switch**: Switch with routing capabilities<br>• **VLAN Trunking Protocol (VTP)**: Cisco protocol for VLAN management<br>• **Private VLAN**: Isolated VLAN segments within a VLAN<br>• **Voice VLAN**: Special VLAN for VoIP phones<br>• **Management VLAN**: VLAN for switch administration<br>• **Default VLAN**: Default VLAN (usually VLAN 1)<br>• **VLAN hopping**: Attack to cross VLAN boundaries<br>• **Dynamic VLAN**: Dynamic VLAN assignment (e.g. via RADIUS)<br>• **Static VLAN**: Static port-to-VLAN assignment<br>• **SVI** (Switch Virtual Interface): Virtual interface for VLAN<br>• **EtherChannel/Port Channel**: Bundled trunk connections|
|**Important Vocabulary**|• **Logical segmentation**: Virtual division without physical separation<br>• **Broadcast traffic**: Transmissions to all devices<br>• **Physical infrastructure**: Hardware network (cables, switches)<br>• **Independent areas**: Separate network segments<br>• **Isolation**: Separation of network traffic<br>• **Excessive traffic**: Too much network traffic<br>• **Flat networks**: Non-segmented networks<br>• **Department-based**: Organised by department<br>• **Security requirements**: Data protection and security regulations<br>• **Physical re-cabling**: Manual cable relocation<br>• **Cost savings**: Financial savings<br>• **Scalability**: Capacity for expansion<br>• **Simplified management**: Easier administration<br>• **Flexibility**: Adaptability<br>• **Mini-switches**: Virtual switch segments<br>• **Insert tag**: Add VLAN marking<br>• **Remove tag**: Delete VLAN marking<br>• **VLAN-aware**: VLAN-capable<br>• **Unaware**: Not VLAN-capable<br>• **Traverse**: Traffic passes through<br>• **Retain**: Tag is kept<br>• **Inter-switch link**: Connection between switches<br>• **Bandwidth consumption**: Network traffic usage<br>• **Performance loss**: Reduction in performance<br>• **Unauthorised access**: Access without permission<br>• **Compromised devices**: Infected/hacked devices<br>• **Malware propagation**: Spread of malicious software|