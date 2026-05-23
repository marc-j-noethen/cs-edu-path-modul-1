# Categorisation Wi-Fi & Wireless Communication

### **What is Wireless Communication?**

**Wireless Communication** = Transmission of information **without physical cables** through **electromagnetic waves** (radio waves, infrared, light)

**Examples**:

- 📺 TV remote control (infrared)
- 📱 Smartphone internet (Wi-Fi, mobile network)
- 📻 Car radio (FM/AM)
- 🎮 Bluetooth controller

**In a network context**: **Wi-Fi** = WLAN (Wireless Local Area Network)

### **Wi-Fi vs. Wired Networks**

|Feature|**Wi-Fi (Wireless)**|**Ethernet (Wired)**|
|---|---|---|
|**Medium**|Air (radio waves)|Cable (copper, fibre optic)|
|**Mobility**|✅ High (anywhere in range)|❌ Low (tied to cable)|
|**Speed**|Up to ~10 Gbps (Wi-Fi 6E)|Up to 100+ Gbps (fibre optic)|
|**Stability**|⚠️ Variable (interference)|✅ Very stable|
|**Security**|⚠️ More vulnerable (air)|✅ More secure (physically limited)|
|**Range**|🏠 ~30-50m (indoors), depends on obstacles|🔌 100m (UTP), km (fibre optic)|
|**Interference**|⚠️ High (other devices)|✅ Low (shielded)|
|**Setup**|✅ Easy|⚠️ Cabling required|

### **Radio Waves: The Foundation of Wi-Fi**

**Radio waves** = Electromagnetic waves with long wavelengths

#### **Frequency** – The Number of Oscillations

**Frequency** = Oscillations per second (Hertz, Hz)

```
1 Hz  = 1 oscillation/second
1 MHz = 1 million oscillations/second
1 GHz = 1 billion oscillations/second
```

**Wi-Fi frequency bands**:

|Band|Frequency|Properties|
|---|---|---|
|**2.4 GHz**|2.4 billion oscillations/s|✅ Greater range<br>✅ Better penetration (walls)<br>❌ Slower<br>❌ Lots of interference (many devices)|
|**5 GHz**|5 billion oscillations/s|✅ Faster<br>✅ Less interference<br>❌ Shorter range<br>❌ Worse penetration|
|**6 GHz**|6 billion oscillations/s (Wi-Fi 6E)|✅ Very fast<br>✅ Barely any interference (new)<br>❌ Even shorter range<br>❌ Very poor penetration|

**Rule of thumb**:

- **2.4 GHz**: For large homes, through many walls
- **5 GHz**: For speed, less range
- **6 GHz**: For maximum speed, same room

#### **Channels** – Subdividing the Spectrum

**Problem**: All devices on the same frequency → interference!

**Solution**: **Channels** (subdivisions within the band)

**2.4 GHz**:

- 11-14 channels (depending on country)
- **Only 3 non-overlapping**: Channel 1, 6, 11
- **Many devices** = congestion!

**5 GHz**:

- ~24 channels
- **More non-overlapping** channels
- **Less congestion**

**6 GHz** (Wi-Fi 6E):

- ~59 channels
- **Completely free** (new, barely any devices)

**Best practice**: Router on channel with **lowest usage** (auto-select or manual)

#### **Interference** – Sources of Disruption

**What interferes with Wi-Fi?**

**In the 2.4 GHz band**:

- 🍴 Microwave ovens (~2.45 GHz!)
- 🎧 Bluetooth devices
- 📞 Cordless phones
- 🏠 Neighbour WLANs (same channel)

**Physical obstacles**:

- 🧱 Thick walls (concrete, brick)
- 🔩 Metal (doors, cabinets, aluminium foil)
- 💧 Water (aquariums, people = ~70% water!)
- 🌳 Plants (in large quantities)

### **Wi-Fi Standards (IEEE 802.11 Family)**

**IEEE 802.11** = Official Wi-Fi standards

|Standard|Marketing name|Year|Frequency|Max. speed|Feature|
|---|---|---|---|---|---|
|**802.11b**|-|1999|2.4 GHz|11 Mbps|Outdated|
|**802.11a**|-|1999|5 GHz|54 Mbps|First 5 GHz|
|**802.11g**|-|2003|2.4 GHz|54 Mbps|Backwards compatible with b|
|**802.11n**|**Wi-Fi 4**|2009|2.4/5 GHz|600 Mbps|MIMO (multiple antennas)|
|**802.11ac**|**Wi-Fi 5**|2013|5 GHz|1.3+ Gbps|"Gigabit Wi-Fi"|
|**802.11ax**|**Wi-Fi 6/6E**|2019|2.4/5/6 GHz|9.6+ Gbps|OFDMA, better in dense environments|

**Trend**:

- Always faster
- More efficient use of spectrum
- Better performance with many devices

**Standard today**: Wi-Fi 5 (802.11ac) or Wi-Fi 6 (802.11ax)

### **Wi-Fi Components: The Hardware**

#### **1. Wireless Access Point (WAP/AP)** 📡

**Function**: Sends and receives Wi-Fi signals

**Types**:

- **Standalone AP**: WLAN function only
- **Wireless Router**: AP + router + switch combined (typical for home networks)

**Task**:

- Broadcasting the SSID
- Authenticating clients
- Bridge between WLAN and wired network

#### **2. Wireless NIC (WNIC)** 📶

**Function**: WLAN adapter in the device

**Forms**:

- **Integrated**: In laptop/smartphone
- **USB adapter**: Externally attachable
- **PCIe card**: Internally in desktop

**Task**: Sending/receiving radio waves

#### **3. Antennas** 📻

**Types**:

- **External**: Visible (often on routers)
- **Internal**: Hidden (most modern devices)

**Orientation matters**:

- Vertical for horizontal spread
- Horizontal for vertical spread

### **SSID: The Network Name**

**SSID (Service Set Identifier)** = Name of the WLAN network

**Examples**: "MyHomeWiFi", "Starbucks_WiFi", "FRITZ!Box 7590"

**Broadcast**:

- **Default**: SSID is **broadcast** (visible in device list)
- **Hidden SSID**: SSID is **not** broadcast

**Hidden SSID = Security?**

```
❌ NO! Only "security through obscurity"
⚠️ SSID still detectable (with tools like Wireshark)
✅ Real security: Strong password + WPA2/WPA3
```

### **Wi-Fi Connection Process**

```
┌──────────┐                      ┌──────────────┐
│  Device  │                      │ Access Point │
└────┬─────┘                      └──────┬───────┘
     │                                   │
     │  1. Scan (search for networks)    │
     │ ──────────────────────────────────>│
     │                                   │
     │  2. SSID broadcast                │
     │ <──────────────────────────────────│
     │                                   │
     │  3. Authentication (password)     │
     │ ──────────────────────────────────>│
     │                                   │
     │  4. Authentication success        │
     │ <──────────────────────────────────│
     │                                   │
     │  5. Connection                    │
     │ ──────────────────────────────────>│
     │                                   │
     │  6. Connection confirmed          │
     │ <──────────────────────────────────│
     │                                   │
     │  ╔════════════════════════════╗   │
     │  ║ Data now encrypted!        ║   │
     │  ╚════════════════════════════╝   │
     │ <──────────────────────────────────>│
```

### **Wi-Fi Security: Authentication & Encryption**

#### **Security Standards (Evolution)**

|Standard|Year|Encryption|Security|Recommendation|
|---|---|---|---|---|
|**Open**|-|❌ None|❌❌❌|**NEVER use!**|
|**WEP**|1997|RC4 (weak)|❌|**NEVER use!** (hackable in minutes)|
|**WPA**|2003|TKIP|⚠️|Outdated|
|**WPA2**|2004|AES (CCMP)|✅✅✅|**Standard today**|
|**WPA3**|2018|AES (SAE)|✅✅✅✅|**Best standard**|

**Encryption algorithms**:

- **TKIP**: Temporal Key Integrity Protocol (outdated, vulnerabilities)
- **AES**: Advanced Encryption Standard (strong, modern standard)
- **SAE**: Simultaneous Authentication of Equals (WPA3, even stronger)

#### **WPA2/WPA3 Modes**

**Personal (PSK - Pre-Shared Key)**:

- One shared password for everyone
- For home networks, small offices
- **Setup**: Password in router → everyone uses the same password

**Enterprise (802.1X/RADIUS)**:

- Individual login per user
- For companies, universities
- **Setup**: Central authentication server (RADIUS)

**Recommendation for home networks**:

```
✅ WPA2-Personal (AES) or WPA3-Personal
✅ Strong password (min. 12 characters, mixed)
❌ NEVER WEP or Open
```

### **Wi-Fi Security Threats**

#### **1. Unauthorised Access** 🚪

**Scenario**: Weak/no password

**Consequences**:

- Bandwidth usage (your internet gets slower)
- Access to network resources (printers, NAS)
- Legal issues (if attacker conducts illegal activities via your IP)

**Protection**:

- ✅ Strong WPA2/WPA3 password
- ✅ Guest network for visitors (isolated from main network)

#### **2. Eavesdropping** 👂

**Scenario**: Attacker intercepts radio waves

**Without encryption**:

```
Attacker with Wireshark:
→ Sees all passwords, emails, chat histories in plain text!
```

**With WPA2/WPA3**:

```
Attacker only sees:
→ Encrypted "data scramble" (AES)
→ Practically impossible to decrypt
```

**Additional protection**:

- ✅ HTTPS for websites (end-to-end)
- ✅ VPN in public WLANs

#### **3. Rogue Access Point (Fake AP)** 🎣

**Scenario**: "Evil Twin" – attacker sets up fake AP

**Process**:

```
Real AP:  "Starbucks_WiFi"
Fake AP:  "Starbucks_WiFi" (same name!)

User connects to fake
    ↓
Attacker = Man-in-the-Middle
    ↓
Reads ALL traffic
```

**Protection**:

- ⚠️ Caution with open WLANs
- ✅ Use VPN (encrypts all traffic)
- ✅ Only known/trusted networks
- ✅ Take certificate warnings seriously

#### **4. Deauthentication Attack (DoS)** 💥

**Scenario**: Attacker sends "deauth" packets

**Process**:

```
Attacker → Deauth packet to client
    ↓
Client thinks: "AP is kicking me out"
    ↓
Connection is dropped
    ↓
Repeated attacks = DoS (denial of service)
```

**Protection**:

- ✅ WPA3 (Management Frame Protection - MFP)
- ✅ Enable 802.11w (Protected Management Frames)

### **Displaying Wi-Fi Connection Details (Windows 11)**

**Method 1: GUI (Settings)**

1. **Settings** → **Network & Internet** → **Wi-Fi**
2. Click connected network → **Properties**
3. Shows:
    - SSID
    - Security type (WPA2, WPA3)
    - Frequency band (2.4 GHz, 5 GHz)
    - Link speed

**Method 2: Command Prompt**

```cmd
netsh wlan show interfaces
```

**Output**:

```
Name                   : Wi-Fi
Description            : Intel(R) Wi-Fi 6 AX201 160MHz
SSID                   : MyHomeWiFi
BSSID                  : aa:bb:cc:dd:ee:ff
Network type           : Infrastructure
Radio type             : 802.11ax
Authentication         : WPA2-Personal
Cipher                 : CCMP
Channel                : 36
Receive rate           : 95%
Transmit rate          : 100%
Signal                 : 92%
```

**Method 3: PowerShell (detailed)**

```powershell
Get-NetAdapter | Where-Object {$_.Name -like "*Wi-Fi*"} | Get-NetAdapterStatistics
```

**Scan available networks**:

```cmd
netsh wlan show networks mode=bssid
```

### **RSSI: Understanding Signal Strength**

**RSSI (Received Signal Strength Indicator)** = Received signal strength

**Unit**: **dBm** (Decibel-milliwatt)

**Scale** (negative value!):

```
-30 dBm  ════════════  Excellent (right next to AP)
-40 dBm  ═══════════
-50 dBm  ══════════   Very good
-60 dBm  ════════     Good
-70 dBm  ═════        OK (usable)
-80 dBm  ══           Weak
-90 dBm  ═            Very weak (barely usable)
-100 dBm              No signal
```

**Rule of thumb**:

- **-30 to -50 dBm**: ✅ Excellent
- **-50 to -70 dBm**: ✅ Good to okay
- **-70 to -80 dBm**: ⚠️ Weak (slow)
- **< -80 dBm**: ❌ Very weak (connection drops)

**Closer to 0 = better!** (less negative)

### **Wi-Fi Best Practices**

✅ **Security**:

- WPA2-Personal (AES) or WPA3-Personal
- Strong password (min. 12 characters)
- Change default admin password
- Keep firmware up to date

✅ **Performance**:

- 5 GHz for speed (short distance)
- 2.4 GHz for range (long distance)
- Place AP centrally (elevated)
- Choose channel with lowest usage

✅ **Network organisation**:

- Guest WLAN for visitors (isolated)
- IoT devices in separate VLAN
- SSID broadcast on (hiding provides little security)

❌ **Avoid**:

- Open networks (without password)
- WEP (completely insecure)
- Weak passwords ("12345678")
- AP in corner/basement (poor coverage)

### **Core Message**

**Wi-Fi** enables **wireless network communication** through **radio waves**:

**Frequency bands**:

- **2.4 GHz**: Wider range, more penetrating, slower, crowded
- **5 GHz**: Faster, shorter range, less crowded
- **6 GHz**: Very fast, very short range, empty (Wi-Fi 6E)

**Standards**: 802.11n/ac/ax (Wi-Fi 4/5/6) – always faster and more efficient

**Components**: Access point (transmits) + Wireless NIC (receives) + Antennas

**Security**:

- **WPA2/WPA3** = Standard (AES encryption)
- **WEP/Open** = Disaster (never use!)
- **Strong password** = Mandatory

**Threats**: Unauthorised access, eavesdropping, rogue APs, DoS

**Final analogy**: Wi-Fi is like an **invisible cable made of radio waves** – flexible and convenient, but vulnerable to "eavesdroppers in the air". Encryption (WPA2/WPA3) is like a **locked tunnel** through that air – only you have the key! 📡🔐🌊

## Overview Table

|**Category**|**Details**|
|---|---|
|**Tools Used**|• **Wi-Fi Settings**: Manage network connections (macOS: Wi-Fi icon + Option key; Windows: Settings → Network & Internet → Wi-Fi)<br>• **Command Prompt/PowerShell**: WLAN commands (Windows: `netsh wlan show interfaces`, `netsh wlan show networks`)<br>• **Wi-Fi Analyser Apps**: inSSIDer, NetSpot, WiFi Analyzer (Windows & Android)<br>• **Wireshark**: WLAN packet analysis (both systems, monitor mode adapter required)<br>• **Aircrack-ng**: WLAN security testing (Linux, via WSL on Windows)<br>• **Network Utility/Resource Monitor**: Connection details (macOS: outdated; Windows: Resource Monitor)<br>• **System Information**: Network adapter details (Windows: `msinfo32`)<br>• **Router web interface**: WLAN configuration (browser: usually 192.168.1.1 or 192.168.0.1)<br>• **Speedtest apps**: Ookla Speedtest, Fast.com (throughput measurement)<br>• **WiFi Explorer**: macOS tool for WLAN analysis<br>• **Acrylic WiFi**: Windows tool for WLAN scanning<br>• **Wireless Diagnostics**: macOS integrated WLAN diagnostic tool|
|**Technical Terms**|• **Wireless Communication**: Wireless communication<br>• **Wi-Fi**: Wireless Fidelity (WLAN technology)<br>• **Radio Waves**: Radio waves<br>• **Electromagnetic Waves**: Electromagnetic waves<br>• **Frequency**: Frequency (oscillations per second)<br>• **Hertz (Hz)**: Unit of measurement for frequency<br>• **GHz** (Gigahertz): Billions of oscillations per second<br>• **2.4 GHz Band**: 2.4 gigahertz frequency band<br>• **5 GHz Band**: 5 gigahertz frequency band<br>• **6 GHz Band**: 6 gigahertz frequency band (Wi-Fi 6E)<br>• **Radio Spectrum**: Radio frequency spectrum<br>• **Channel**: Channel (subdivision of the frequency band)<br>• **Interference**: Interference/disruption<br>• **IEEE 802.11**: Wi-Fi standard family<br>• **802.11b/a/g/n/ac/ax**: Various Wi-Fi generations<br>• **Wi-Fi 6 (802.11ax)**: Sixth Wi-Fi generation<br>• **Wi-Fi 6E**: Wi-Fi 6 Extended (with 6 GHz)<br>• **MIMO** (Multiple Input Multiple Output): Multiple antenna technology<br>• **OFDMA** (Orthogonal Frequency-Division Multiple Access): Efficiency improvement in Wi-Fi 6<br>• **WAP/AP** (Wireless Access Point): WLAN access point<br>• **WNIC** (Wireless Network Interface Card): WLAN network card<br>• **SSID** (Service Set Identifier): WLAN network name<br>• **Hidden SSID**: Non-broadcast network name<br>• **Broadcast**: Broadcasting of the SSID<br>• **Authentication**: Authentication/login<br>• **Encryption**: Encryption<br>• **WEP** (Wired Equivalent Privacy): Outdated encryption (INSECURE!)<br>• **WPA** (Wi-Fi Protected Access): First secure encryption<br>• **WPA2**: Second generation (AES-based, standard)<br>• **WPA3**: Third generation (latest standard, improved security)<br>• **PSK** (Pre-Shared Key): Pre-shared key (password)<br>• **TKIP** (Temporal Key Integrity Protocol): Old encryption algorithm (vulnerable)<br>• **AES** (Advanced Encryption Standard): Modern encryption algorithm<br>• **CCMP**: AES-based protocol for WPA2<br>• **RSSI** (Received Signal Strength Indicator): Received signal strength<br>• **dBm** (Decibel-milliwatt): Unit of measurement for signal strength<br>• **Tx Rate** (Transmit Rate): Transmission rate<br>• **PHY Mode**: Physical mode (used 802.11 standard)<br>• **Rogue Access Point**: Fraudulent/fake access point<br>• **Evil Twin**: Fake WLAN with the same name<br>• **Packet Sniffing**: Packet capture from the air<br>• **DoS** (Denial of Service): Service blockade<br>• **Deauthentication Attack**: Forced disconnection from WLAN|
|**Key Vocabulary**|• **Wireless**: Without cable<br>• **Electromagnetic radiation**: Radio waves<br>• **Wavelength**: Distance between wave peaks<br>• **Oscillate**: To swing/repeat<br>• **Cycle**: Oscillation<br>• **Spectrum**: Frequency range<br>• **Allocated**: Reserved for a specific purpose<br>• **Overlapping**: Intersecting<br>• **Disruption**: Interference<br>• **Attenuation**: Signal becomes weaker<br>• **Microwave oven**: Source of interference for 2.4 GHz<br>• **Thick walls**: Physical obstacles<br>• **Metal objects**: Signal blocking<br>• **Backwards compatible**: Compatible with older standards<br>• **Theoretical maximum speed**: Ideal speed<br>• **Dense environments**: Many WLAN devices<br>• **Bridge**: Connection between wireless and wired<br>• **Transceiver**: Transmitter-receiver<br>• **Visible external antennas**: Antennas outside the device<br>• **Internal antennas**: Hidden antennas<br>• **Orientation**: Positioning of antennas<br>• **Broadcasting**: Broadcasting<br>• **Scanning**: Searching for networks<br>• **Authorisation**: Access permission<br>• **Eavesdropping**: Eavesdropping<br>• **Unauthorised access**: Access without permission<br>• **Bandwidth usage**: Internet consumption<br>• **Shared files**: Shared resources<br>• **Impersonating**: Mimicking/spoofing<br>• **Intercepting**: Intercepting<br>• **Legitimate**: Real/authentic<br>• **Intrusion**: Intrusion<br>• **Mitigation**: Mitigation<br>• **Range**: Coverage/range<br>• **Mobility**: Freedom of movement<br>• **Tethered**: Bound (by cable)<br>• **Susceptible**: Susceptible<br>• **Obstacles**: Obstructions<br>• **Atmospheric conditions**: Weather conditions|

---