# Categorisation Physical Layer - Layer 1

### **The Physical Layer (Layer 1): The Foundation of the Network**

**Physical Layer** = **Lowest layer** in the network model (OSI/TCP-IP)

**Core task**: Transmission of **raw bits** (0 and 1) as **physical signals**

**Analogy**: If the internet is a motorway, then Layer 1 is the **asphalt, the bridges and the tunnels** – the physical infrastructure

### **The 5 Main Tasks of Layer 1**

1. **Physical connection** 🔌: Cables, connectors, radio waves
2. **Bit-to-signal conversion** ⚡: 0/1 → Electricity/Light/Radio waves
3. **Transmission rate** 🚀: Speed (bps, Mbps, Gbps)
4. **Time synchronisation** ⏱️: Sender and receiver in sync
5. **Data flow direction** ↔️: Half-Duplex vs. Full-Duplex

### **Cable Types: The Three Main Categories**

#### **1. Twisted Pair (Copper Cable) – The Standard for LANs**

**UTP (Unshielded Twisted Pair)** – Unshielded:

```
┌────────────────────────────────────┐
│  Cable Categories & Speeds         │
├────────────────────────────────────┤
│ Cat 5e: up to 1 Gbps (100m)        │
│ Cat 6:  up to 10 Gbps (55m)        │
│ Cat 6a: up to 10 Gbps (100m)       │
│ Cat 7:  up to 10 Gbps (100m, better│
└────────────────────────────────────┘
```

**Properties**:

- ✅ **Affordable** and **flexible**
- ✅ Standard **RJ45 connector** (like a thicker phone plug)
- ❌ Susceptible to **EMI** (Electromagnetic Interference)
- 🎯 **Usage**: Home networks, offices, LANs

**STP (Shielded Twisted Pair)** – Shielded:

- ✅ Extra **shielding** against interference
- ❌ More expensive, less flexible
- 🎯 **Usage**: Factories, environments with high EMI

**Why twisted?** → Reduces **crosstalk** (interference between cable pairs)

#### **2. Coaxial Cable (Copper) – Cable TV & Internet**

```
Structure (cross-section):
┌─────────────────────────┐
│   Outer jacket          │  (Plastic)
│ ┌─────────────────────┐ │
│ │ Braided shield      │ │  (Metal)
│ │ ┌─────────────────┐ │ │
│ │ │   Insulation    │ │ │
│ │ │ ┌─────────────┐ │ │ │
│ │ │ │ Centre core │ │ │ │  (Copper)
│ │ │ └─────────────┘ │ │ │
│ │ └─────────────────┘ │ │
│ └─────────────────────┘ │
└─────────────────────────┘
```

**Properties**:

- **F-type connector** (screw connection)
- 🎯 **Usage**: Cable TV, cable internet modem

#### **3. Fibre Optic Cable – The High-Speed Champions**

**How it works**: **Light pulses** through thin glass fibres

```
Bit 1 → Light ON   💡
Bit 0 → Light OFF  ⚫
```

**Two types**:

|Type|Single-Mode (SMF)|Multi-Mode (MMF)|
|---|---|---|
|**Core**|Very thin (9 µm)|Thick (50-62.5 µm)|
|**Light source**|Laser|LED or cheaper laser|
|**Distance**|Very long (km, underwater!)|Short (m to km)|
|**Cost**|Expensive|Cheaper|
|**Usage**|Telecom backbone, undersea cables|Data centres, campus|

**Advantages**:

- ⚡ **Extremely fast** (Tbps possible!)
- 🌍 **Long distances** (low attenuation)
- 🛡️ **Immune to EMI** (no electricity → no interference)

**Connectors**:

- **LC**: Small, high-density (popular)
- **SC**: Square, push-pull

**Why immune to EMI?** → Light instead of electricity, no electromagnetic fields!

### **Further Important Hardware**

#### **NIC (Network Interface Card) – The Network Interface**

```
┌────────────────────────────┐
│   Computer/Device          │
│  ┌──────────────────────┐  │
│  │   NIC                │  │
│  │  - MAC Address       │  │
│  │  - Ethernet port     │  │
│  │  - OR WLAN antenna   │  │
│  └──────────┬───────────┘  │
└─────────────┼──────────────┘
              │
         [RJ45 cable]
```

**Function**: Connects device to network (Layer 1 + Layer 2)

**Windows: Check NIC status**:

```powershell
Get-NetAdapter
```

Shows: Name, status, link speed, MAC address

#### **Modem – The Signal Converter**

**Modem** = **Mod**ulator-**Dem**odulator

**Function**:

```
Computer (digital) ←→ Modem ←→ Medium (often analogue)

Modulation:   Digital → Analogue (Sending)
Demodulation: Analogue → Digital (Receiving)
```

**Types**:

- **DSL Modem**: Phone line → Internet
- **Cable Modem**: Coax (TV cable) → Internet
- **ONT** (Fibre): Fibre optic → Ethernet (not really a "modem", but similar)

### **Performance Metrics: The 6 Key Figures**

#### **1. Bandwidth 📏**

**Definition**: **Theoretical maximum** for data transmission

**Units**: bps, Mbps, Gbps (bits per second)

**Analogy**: **Width of a pipe** – wider pipe = more water (data) can flow through

**Examples**:

- Cat 5e: 1 Gbps
- Cat 6: 10 Gbps (short distance)
- Fibre optic: Tbps (Terabits/s) possible

#### **2. Throughput 📊**

**Definition**: **Actual** transmission rate (usually < bandwidth)

**Analogy**: **How much water actually flows** – despite a wide pipe, less can get through (congestion, leaks)

**Why lower than bandwidth?**

- Network congestion
- Protocol overhead (headers, etc.)
- Latency
- Errors/retransmissions

**Measurement (Windows)**:

```powershell
# With iperf3 (installation required):
iperf3 -c server-ip

# Simple online test:
speedtest.net in browser
```

#### **3. Latency ⏱️**

**Definition**: **Delay** from sender to receiver

**Unit**: Milliseconds (ms)

**Causes**:

- **Distance** (speed of light!)
- **Medium** (fibre faster than copper)
- **Processing time** in switches/routers
- **Congestion**

**Measurement (Windows)**:

```cmd
ping google.com

Reply from 142.250.185.46: bytes=32 time=15ms TTL=115
                                        ↑
                                    Latency!
```

**Rule of thumb**:

- < 50 ms: **Excellent** (gaming, VoIP)
- 50-100 ms: **Good** (most applications)
- > 150 ms: **Noticeable** (lag in games, VoIP delay)
    

#### **4. Jitter (Latency Variation) 📉📈**

**Definition**: **Variation** of latency over time

```
Stable latency (no jitter):
Ping 1: 20ms
Ping 2: 20ms
Ping 3: 20ms
→ Good for VoIP, video

High jitter:
Ping 1: 20ms
Ping 2: 80ms
Ping 3: 15ms
Ping 4: 120ms
→ Bad! Audio stutters, video freezes
```

**Problem for**: VoIP, video conferences, online gaming

#### **5. Attenuation 📉**

**Definition**: **Signal loss** over distance

```
Signal strength
    │
100%│██████╲
    │      ╲
 50%│       ╲██████
    │              ╲
  0%│               ╲
    └─────────────────→ Distance
    0m     50m    100m
```

**Problem**: The longer the cable, the weaker the signal

**Solution**:

- **Repeater/Amplifier**: Amplifies signal
- **Observe maximum lengths**: e.g. UTP Ethernet = 100m max

**Fibre vs. Copper**:

- Fibre optic: **Much less** attenuation → longer distances
- Copper: **More** attenuation → shorter distances

#### **6. Noise/Interference 📻**

**EMI (Electromagnetic Interference)**:

**Sources**:

- Electric motors
- Power lines
- Fluorescent lights
- Microwaves
- Radio equipment

**Crosstalk**:

- Signal from one cable interferes with neighbouring cable
- **Solution**: Twisting of cable pairs!

**Remedies**:

- ✅ **STP** (shielded cables)
- ✅ **Grounding**
- ✅ **Fibre optic** (immune!)

### **Ethernet Speed Standards**

|Standard|Speed|Cable|Distance|Usage|
|---|---|---|---|---|
|**100BASE-TX** (Fast Ethernet)|100 Mbps|Cat 5e UTP|100m|Older LANs|
|**1000BASE-T** (Gigabit Ethernet)|1 Gbps|Cat 5e/6 UTP|100m|**Standard today**|
|**10GBASE-T** (10 Gigabit Ethernet)|10 Gbps|Cat 6a/7 UTP or Fibre|100m (UTP), km (Fibre)|High-end LANs, servers|

**Decoding the naming convention**:

```
1000BASE-T
 │   │   │
 │   │   └─ Medium (T = Twisted Pair)
 │   └───── Baseband (digital signal)
 └───────── Speed (Mbps)
```

**Other suffixes**:

- **-SX, -LX, -LR**: Fibre optic (S=Short, L=Long, R=Range)

### **Duplex Modes: Simultaneous or Alternating?**

#### **Half-Duplex 🔄**

**Rule**: Send **OR** receive (not simultaneously)

**Analogy**: **Walkie-talkie** – one speaks, others listen

```
Time →
Computer A: ████████────────████████────────
Computer B: ────────████████────────████████
            Sending  Receiving Sending  Receiving
```

**Problem**: **Collisions** possible (both send simultaneously)

**Usage**: Old hubs, outdated networks

#### **Full-Duplex ⇄**

**Rule**: Send **AND** receive **simultaneously**

**Analogy**: **Phone call** – both can talk at the same time

```
Time →
Computer A: ████████████████████████████████ (Sending)
Computer B: ████████████████████████████████ (Sending)
            Both send simultaneously, no collisions!
```

**Advantages**:

- ✅ **Double bandwidth** (e.g. 1 Gbps send + 1 Gbps receive = 2 Gbps total)
- ✅ **No collisions**
- ✅ **Higher efficiency**

**Usage**: **Modern switches** (standard today!)

#### **Auto-Negotiation**

```
Device A and Device B connect:

Device A: "I can: 1 Gbps Full-Duplex, 100 Mbps Full-Duplex"
Device B: "I can: 1 Gbps Full-Duplex, 100 Mbps Half-Duplex"

Negotiation: "We will use 1 Gbps Full-Duplex!"
```

**Important**: **Duplex Mismatch** = disaster!

```
Device A: Full-Duplex
Device B: Half-Duplex
→ Massive performance problems, errors
```

### **Signal Conversion: From Bits to Physical Signals**

**Copper cable**:

```
Bit 1 → +5V (voltage)
Bit 0 → 0V  (no voltage)

or other voltage level schemes
```

**Fibre optic**:

```
Bit 1 → Light ON   💡
Bit 0 → Light OFF  ⚫
```

**Wireless (WLAN)**:

```
Bits → Radio frequency modulation
- Amplitude (strength)
- Frequency (oscillation)
- Phase (shift)
```

**Encoding** = Coding bits → signals (for timing, error detection)

**Modulation** = Transmitting digital signals over analogue medium (modem!)

### **Checking NIC Status (Windows 11)**

**Method 1: Device Manager (GUI)**

1. **Windows + X** → **Device Manager**
2. Expand **Network Adapters**
3. Adapter **right-click** → **Properties**
4. Tab **Advanced**: Link Speed, Duplex Mode

**Method 2: PowerShell**

```powershell
Get-NetAdapter | Select-Object Name, Status, LinkSpeed, MediaType

# Detailed info:
Get-NetAdapterAdvancedProperty -Name "Ethernet" | Where-Object {$_.RegistryKeyword -like "*Speed*"}
```

**Method 3: Network Connections**

```cmd
ncpa.cpl
```

→ Adapter → Status → Details

### **Cable Maximum Lengths**

|Cable type|Maximum length|Reason|
|---|---|---|
|**UTP Ethernet** (Cat 5e/6)|**100 metres**|Attenuation, timing|
|**Coaxial**|500m (10BASE5)|Outdated|
|**Single-Mode Fibre**|**40-80 km** (without repeater)|Very low attenuation|
|**Multi-Mode Fibre**|**550m (1Gbps)**|Higher attenuation than SMF|

**Beyond these lengths?** → Use repeaters, switches as amplifiers

### **Practical Troubleshooting Tips**

**Slow connection?**

1. Check speed/duplex (`Get-NetAdapter`)
2. Check cable quality (Cat 5e for Gigabit?)
3. Cable length < 100m?
4. Throughput test (`iperf3`, Speedtest)

**High latency?**

```cmd
ping -t 8.8.8.8
```

Continuous ping → recognise latency patterns

**Connection drops intermittently?**

- Cable damaged? (cable tester)
- EMI source nearby? (use STP)
- Duplex mismatch? (check auto-negotiation)

### **Core Message**

**Layer 1 (Physical Layer)** is the **physical foundation** of the network:

**Task**: Transmission of **bits as physical signals** over media

**Three main media**:

1. **Twisted Pair (Copper)**: Standard for LANs (Cat 5e, Cat 6)
2. **Coaxial**: Cable TV/Internet
3. **Fibre Optic**: High-speed, long distances, immune to EMI

**Performance metrics**:

- **Bandwidth**: Theoretical maximum
- **Throughput**: Actual rate
- **Latency**: Delay
- **Jitter**: Latency variation
- **Attenuation**: Signal loss
- **Noise**: Interference

**Modern standards**:

- **Gigabit Ethernet (1000BASE-T)**: 1 Gbps, standard today
- **Full-Duplex**: Send + receive simultaneously

**Important**: Layer 1 problems (bad cables, EMI, duplex mismatch) often cause hard-to-diagnose network issues at higher layers!

**Final analogy**: Layer 1 is like the **road network** of a city – no matter how good your cars (higher layers) are, without good roads (cables, signals) you won't get anywhere! 🛣️⚡🌐

## Overview Table

|**Category**|**Details**|
|---|---|
|**Tools Used**|• **Cable Tester**: Checking network cables (Fluke, Klein Tools)<br>• **Multimeter**: Measuring electrical signals<br>• **OTDR** (Optical Time-Domain Reflectometer): Fibre optic measurement device<br>• **Crimping Tool**: Tool for attaching RJ45 connectors<br>• **Cable Stripper**: Wire stripping tool for cables<br>• **Tone Generator & Probe**: Cable tracing kit<br>• **Network Analyser**: Wireshark, tcpdump (analyses higher layers, but shows Physical Layer problems)<br>• **Speed Test Tools**: Iperf, Speedtest.net (measures throughput)<br>• **Ping/Traceroute**: Latency measurement (Windows: `ping`, `tracert`; macOS: `ping`, `traceroute`)<br>• **Device Manager**: NIC status and configuration check (Windows)<br>• **System Information**: Network adapter details (macOS: "About This Mac" → System Report → Network)<br>• **PowerShell**: `Get-NetAdapter`, `Test-Connection` (Windows)<br>• **ethtool**: Check link status (Linux, via WSL on Windows)<br>• **Fibre Optic Cleaning Kit**: Cleaning set for fibre optic connectors<br>• **Light Meter**: Light intensity measurement device for fibre optics|
|**Technical Terms**|• **Physical Layer**: Layer 1 in the OSI model<br>• **Bit**: Smallest unit of data (0 or 1)<br>• **Signal**: Physical representation of bits<br>• **Transmission Medium**: Transmission medium (cable, wireless)<br>• **Twisted Pair**: Twisted copper cable<br>• **UTP** (Unshielded Twisted Pair): Unshielded twisted cable<br>• **STP** (Shielded Twisted Pair): Shielded twisted cable<br>• **Cat 5e/Cat 6/Cat 6a**: Cable categories with different specifications<br>• **RJ45 Connector**: Standard Ethernet connector<br>• **Coaxial Cable**: Coaxial cable<br>• **F-type Connector**: Coaxial connector (cable TV/internet)<br>• **Fibre Optic Cable**: Fibre optic cable<br>• **Single-Mode Fibre (SMF)**: Single-mode fibre optic (long distances)<br>• **Multi-Mode Fibre (MMF)**: Multi-mode fibre optic (short distances)<br>• **LC/SC Connector**: Fibre optic connector types<br>• **LED**: Light source for multimode fibre optic<br>• **Laser**: Light source for singlemode fibre optic<br>• **NIC** (Network Interface Card): Network card/network adapter<br>• **MAC Address**: Hardware address of the NIC<br>• **Modem**: Modulator-Demodulator<br>• **DSL Modem**: Modem for phone lines<br>• **Cable Modem**: Modem for cable TV lines<br>• **ONT** (Optical Network Terminal): Fibre optic modem<br>• **Bandwidth**: Theoretical maximum speed<br>• **Throughput**: Actual transmission rate<br>• **Latency**: Delay<br>• **Jitter**: Variation in latency<br>• **Attenuation**: Signal attenuation/signal loss<br>• **Noise**: Noise/interference signals<br>• **EMI** (Electromagnetic Interference): Electromagnetic interference<br>• **Crosstalk**: Interference between cables<br>• **Repeater**: Signal amplifier<br>• **Amplifier**: Amplifier<br>• **Modulation**: Signal conversion (digital → analogue)<br>• **Demodulation**: Signal back-conversion (analogue → digital)<br>• **Encoding**: Encoding bits into signals<br>• **Baseband**: Baseband transmission<br>• **Half-Duplex**: Alternating send/receive<br>• **Full-Duplex**: Simultaneous send/receive<br>• **Fast Ethernet (100BASE-TX)**: 100 Mbps Ethernet<br>• **Gigabit Ethernet (1000BASE-T)**: 1 Gbps Ethernet<br>• **10 Gigabit Ethernet (10GBASE-T)**: 10 Gbps Ethernet<br>• **Auto-Negotiation**: Automatic speed/duplex negotiation<br>• **Collision**: Collision (simultaneous transmission)<br>• **Synchronisation**: Time synchronisation between sender/receiver|
|**Key Vocabulary**|• **Raw bits**: Unprocessed binary data (0 and 1)<br>• **Physical connection**: Hardware connection<br>• **Electrical impulses**: Voltage changes for signals<br>• **Light pulses**: Light signals in fibre optic<br>• **Radio waves**: Electromagnetic waves (WLAN)<br>• **Transmission rate**: Speed of data transmission<br>• **Time synchronisation**: Alignment between sender and receiver<br>• **Data flow direction**: Direction of communication<br>• **Information motorway**: Internet metaphor<br>• **Road surface**: Physical infrastructure<br>• **Wireless paths**: WLAN connections<br>• **Twisting**: Twisting of cable pairs<br>• **Interference reduction**: Reduction of interference<br>• **Shielding**: Shielding against EMI<br>• **Centre core**: Copper core in coaxial cable<br>• **Braided shield**: Metal braid in coax<br>• **Outer jacket**: Protective cover of the cable<br>• **Glass strands**: Thin glass fibres<br>• **Light source**: LED or laser<br>• **Total internal reflection**: Light guidance in fibre optic<br>• **Detector**: Light receiver<br>• **Capacity**: Transmission capacity<br>• **Signal loss**: Attenuation over distance<br>• **Immune**: Insensitive (to EMI)<br>• **Undersea cable**: Submarine cable<br>• **Telecommunications backbone**: Main connection network<br>• **Data centre**: Data center<br>• **Campus**: Company grounds<br>• **High-density**: High-density (many connections)<br>• **Physical address**: MAC address<br>• **Antenna**: Radio antenna<br>• **Conversion**: Conversion<br>• **Analogue**: Continuous signals<br>• **Digital**: Discrete 0/1 signals<br>• **Theoretical maximum**: Bandwidth<br>• **Actual value**: Throughput<br>• **Pipe width**: Bandwidth metaphor<br>• **Water flow**: Throughput metaphor<br>• **Delay**: Latency<br>• **Variation**: Jitter<br>• **Distorted audio**: Caused by jitter<br>• **Choppy video**: Caused by jitter/packet loss<br>• **Weakening**: Attenuation<br>• **Amplification**: Amplification<br>• **Maximum length**: Length limit of cables<br>• **Unwanted signals**: Interference<br>• **Motors**: EMI source<br>• **Power lines**: EMI source<br>• **Fluorescent lights**: EMI source<br>• **Adjacent wires**: Crosstalk source<br>• **Grounding**: Grounding (EMI protection)<br>• **Voltage levels**: Voltage levels<br>• **Light presence**: On/off state in fibre optic<br>• **Amplitude**: Signal strength<br>• **Frequency**: Signal oscillation<br>• **Phase**: Signal shift<br>• **Walkie-talkie**: Half-duplex metaphor<br>• **Phone call**: Full-duplex metaphor<br>• **Negotiation**: Auto-negotiation<br>• **Discrepancy**: Mismatch (duplex/speed)|

---