# 📊 Summary based on the 80/20 principle

### **What is a VPN? The secure courier service for your data**

**VPN (Virtual Private Network)** = **Virtual Private Network**

**Analogy**:

- **Without VPN**: Your data travels through the internet like an **open postcard** – anyone can read it
- **With VPN**: Your data travels in a **sealed, armoured envelope** – nobody can see the contents

**Core idea**: VPN creates an **encrypted tunnel** between your device and a VPN server

```
Your device  →→→  [Encrypted tunnel]  →→→  VPN server  →→→  Internet
             🔒 Nobody can intercept 🔒
```

### **The 5 core benefits of VPN**

|Benefit|Meaning|Example|
|---|---|---|
|**1. Confidentiality** 🔐|Encryption makes data unreadable|Hackers in café Wi-Fi only see "data scramble"|
|**2. Integrity** ✅|Protection against data manipulation|Nobody can alter your requests|
|**3. Authentication** 🔑|Verification of identity|You connect to the real server|
|**4. Anonymity** 🕵️|Concealment of your IP address|Websites see VPN server IP, not yours|
|**5. Access** 🌐|Access to remote networks|From home office into the company network|

### **How does a VPN work? The 4-step process**

#### **Step 1: Initiation 🚀**

```
You start the VPN client on your device
Client knows the VPN server address
```

#### **Step 2: Authentication 🔑**

```
Client ↔ Server: Who are you?
- Username/password
- Digital certificate
- Multi-factor authentication (MFA)

Both sides verify each other
```

#### **Step 3: Tunnel establishment 🛡️**

```
Encrypted tunnel is established:

┌──────────────────────────────────────┐
│   Your device  ←→  VPN server        │
│   🔒 AES-256 encryption 🔒           │
└──────────────────────────────────────┘

All data is now encrypted!
```

#### **Step 4: Data routing 📡**

```
OUTGOING:
1. Your browser: "I want google.com"
2. VPN client: encrypts → sends to VPN server
3. VPN server: decrypts → sends to Google
4. Google thinks: "Request comes from the VPN server"

INCOMING:
1. Google: sends response to VPN server
2. VPN server: encrypts → sends to your client
3. VPN client: decrypts → displays webpage

You see the webpage, but nobody could intercept it!
```

**Visually**:

```
┌─────────────┐         ┌─────────────┐         ┌─────────────┐
│  Your PC    │ 🔒══════│ VPN server  │═════════│   Google    │
│ (encrypted) │ Tunnel  │ (visible)   │ Normal  │ (thinks VPN │
│             │         │             │         │ is client)  │
└─────────────┘         └─────────────┘         └─────────────┘
```

### **Key concepts: The three pillars of VPN**

#### **1. Tunneling (Encapsulation) 📦**

**What is it?** One protocol is "wrapped" inside another

**Analogy**:

```
Smaller envelope (your data)
      ↓
You put it inside a larger, more secure envelope (VPN protocol)
      ↓
Outer envelope conceals the inner one
```

**Technically**:

```
[HTTP request] → Original data packet
      ↓ Encapsulate
[VPN header [HTTP request]] → Encrypted VPN packet
      ↓ Send through tunnel
      ↓ At VPN server: Unpack
[HTTP request] → Original packet is forwarded
```

#### **2. Encryption 🔐**

**What is it?** Conversion of readable data into unreadable code

**Example**:

```
BEFORE (plaintext):
"My password is: secret123"

AFTER (encrypted with AES-256):
"a7k3!x9#mQ@pL5vR$nZ8wY2tF6..."

Only readable again with the key!
```

**Common algorithms**:

- **AES-256**: Industry standard, very secure
- **ChaCha20**: Modern, fast on mobile devices

#### **3. Authentication 🎫**

**Two directions**:

**A) User → Server** (You prove who you are):

- Username/password
- Digital certificate
- MFA (SMS code, authenticator app)

**B) Server → Client** (Server proves it is genuine):

- Digital certificate from the server
- Prevents man-in-the-middle attacks

### **VPN protocols: The different "languages"**

|Protocol|Security|Speed|Use|Recommendation|
|---|---|---|---|---|
|**WireGuard**|⭐⭐⭐⭐⭐|⚡⚡⚡⚡⚡|Modern, simple|✅ **Highly recommended**|
|**OpenVPN**|⭐⭐⭐⭐⭐|⚡⚡⚡|Flexible, proven|✅ **Recommended**|
|**IPsec**|⭐⭐⭐⭐|⚡⚡⚡|Enterprise, robust|✅ Good|
|**SSL/TLS VPN**|⭐⭐⭐⭐|⚡⚡⚡|Browser-based|✅ Good|
|**L2TP/IPsec**|⭐⭐⭐|⚡⚡|Widespread|⚠️ OK|
|**PPTP**|⭐|⚡⚡⚡⚡|Outdated|❌ **DO NOT use!**|

**Rule of thumb**: Choose WireGuard or OpenVPN!

### **VPN types: Remote access vs. site-to-site**

#### **Remote Access VPN (Client-to-Site) 🏠→🏢**

**What is it?** A single device connects to a network

**Use**:

```
┌──────────────┐         ┌──────────────────┐
│  Employee    │ 🔒══════│ Company network  │
│ (home office)│  VPN    │ (internal servers)│
└──────────────┘         └──────────────────┘
```

**Typical scenarios**:

- 💼 Home office access to company intranet
- ✈️ Secure browsing on public Wi-Fi (airports, cafés)
- 🎭 Bypassing geographic restrictions (secondary)

**Example**:

```
You are sitting in a café:
- Without VPN: Café Wi-Fi → Internet (insecure!)
- With VPN: Café Wi-Fi → VPN server → Internet (secure!)
```

#### **Site-to-Site VPN (Network-to-Network) 🏢↔🏢**

**What is it?** Two complete networks are connected

**Use**:

```
┌──────────────┐         ┌──────────────────┐
│ Headquarters │ 🔒══════│ Branch office    │
│  (Berlin)    │  VPN    │   (Munich)       │
└──────────────┘         └──────────────────┘
```

**Advantage**:

- All devices in both networks can communicate with each other
- As if they were on the **same local network**!

**Example**:

```
Company with 3 locations:
Berlin (HQ) ←VPN→ Munich (branch)
      ↓ VPN
  Hamburg (branch)

Result: All locations = One virtual network
```

### **Practical VPN use (Windows 11)**

#### **Method 1: Built-in Windows VPN function**

1. Open **Settings** (Windows + I)
2. **Network & Internet** → **VPN**
3. **Add a VPN**
4. Enter:
    - VPN provider: Windows (built-in)
    - Connection name: e.g. "Company VPN"
    - Server address: vpn.company.com
    - VPN type: Automatic (or select specific)
    - Sign-in info: Username/password
5. **Connect**

#### **Method 2: Dedicated VPN client software**

**Example: OpenVPN**

1. Install OpenVPN client (openvpn.net)
2. Obtain configuration file (.ovpn) from VPN provider
3. Import configuration file
4. Click connect
5. Enter authentication details

**Example: WireGuard**

1. Install WireGuard (wireguard.com)
2. Import configuration file or scan QR code
3. Activate tunnel

#### **Check VPN status**

**Check IP address before/after VPN**:

```powershell
# Before VPN:
Invoke-RestMethod -Uri "https://api.ipify.org"
# → Shows your real IP

# Activate VPN

# After VPN:
Invoke-RestMethod -Uri "https://api.ipify.org"
# → Shows VPN server IP (different!)
```

**Or browser**: https://www.whatismyip.com

### **Tunneling: Broader than just VPN**

**Tunneling concept** = Encapsulation of one protocol inside another

**Why?**

- ✅ **Security**: Encryption over insecure networks
- ✅ **Interoperability**: Transport IPv6 over IPv4 network
- ✅ **Routing**: Redirect traffic in a targeted manner

#### **Further tunneling examples**

**1. SSH tunneling (port forwarding) 🔧**

```
Problem: Database on server only reachable from "localhost"

Solution: SSH tunnel
ssh -L 3306:localhost:3306 user@remote-server

Now: localhost:3306 on your PC → database on server!
```

**Use cases**:

- Secure access to remote databases
- Bypassing firewalls (caution: observe policies!)
- Encrypting insecure protocols

**2. GRE (Generic Routing Encapsulation) 📦**

```
Tunnels arbitrary protocols over IP
BUT: No encryption!
→ Often combined with IPsec
```

**3. IPv6-over-IPv4 tunnel 🌐**

```
Mechanisms: 6to4, Teredo, ISATAP
Problem: IPv6 packet must travel over IPv4 network
Solution: Wrap IPv6 packet inside IPv4 packet
```

### **Split tunneling vs. full tunneling**

**Full tunneling** (default):

```
ALL traffic → VPN server → Internet

Advantage: Maximum security
Disadvantage: Slower (everything goes through VPN)
```

**Split tunneling**:

```
Company traffic → VPN server → Company network
Normal traffic → Directly to internet (no VPN)

Advantage: Faster for Netflix, YouTube etc.
Disadvantage: Company data better protected than private traffic
```

**Configure** (depending on VPN client):

- OpenVPN: Routing settings
- Windows VPN: Checkbox "Use default gateway on remote network"

### **Important VPN features**

**Kill switch**:

```
If VPN connection drops:
→ Internet connection is COMPLETELY cut off
→ Prevents "data leak" (no unencrypted packets)
```

**DNS leak protection**:

```
Problem: DNS requests could run outside the VPN
Solution: Force all DNS requests through VPN tunnel
```

**Multi-hop/Double VPN**:

```
Your device → VPN server 1 → VPN server 2 → Internet
Extra security layer (but slower)
```

### **VPN security: What to watch out for**

✅ **Good VPN providers**:

- **No-logs policy** (no activity logs)
- **Strong encryption** (AES-256, WireGuard)
- **Kill switch**
- **DNS leak protection**
- **Headquartered in a privacy-friendly country**

⚠️ **Be cautious with**:

- **Free VPNs** (often sell your data!)
- **VPNs with poor reputation**
- **Browser VPN extensions** (often just proxies, no real encryption)

❌ **VPN does NOT protect against**:

- Viruses/malware (you need antivirus)
- Phishing (you need common sense)
- Compromised devices (you need updates and patches)

### **Typical VPN use cases**

**1. Home office** 💼:

```
Company → Set up VPN server
Employees → Install VPN client
Result: Secure access to intranet, file servers, databases
```

**2. Public Wi-Fi** ☕:

```
Café Wi-Fi → insecure (man-in-the-middle possible)
Activate VPN → all data encrypted
Hackers only see: "Encrypted data scramble"
```

**3. Travelling** ✈️:

```
In country X: Certain websites blocked
VPN → server in country Y
Websites think: Request comes from country Y
Access possible (observe legal situation!)
```

**4. Privacy** 🕵️:

```
ISP tracks your activities
With VPN: ISP only sees "connection to VPN server"
ISP does NOT know which websites you visit
```

### **Core message**

**VPN** creates an **encrypted tunnel** through the internet that:

- 🔒 **Protects** your data (encryption)
- 🕵️ **Conceals** your identity (IP masking)
- 🌐 Gives you **access** to remote networks

**Tunneling** is the underlying concept: **Encapsulating one protocol inside another**

**Final analogy**: VPN is like an **armoured underwater tunnel** between two islands:

- Nobody sees who is passing through (anonymity)
- Nobody can see the contents of the vehicles (encryption)
- Secure against attacks from outside (integrity)

**Important**: VPN is **not a cure-all**, but a **powerful tool** for security and privacy on the internet! 🛡️🔐🌐

---

## Tools Used

|**Category**|**Details**|
|---|---|
|**Tools Used**|• **VPN client software**: OpenVPN, WireGuard, ProtonVPN, NordVPN, Mullvad (Windows & macOS)<br>• **Windows VPN**: Built-in VPN function (Settings → Network & Internet → VPN)<br>• **macOS VPN**: System Settings → Network → VPN (macOS; Windows: see above)<br>• **OpenVPN client**: Open-source VPN client (both systems)<br>• **WireGuard**: Modern VPN client (both systems)<br>• **Cisco AnyConnect**: Enterprise VPN solution<br>• **FortiClient**: VPN client for FortiGate<br>• **Pulse Secure**: VPN client for enterprises<br>• **SSH**: Secure Shell for SSH tunneling (Terminal/PuTTY)<br>• **PuTTY**: SSH client with tunneling function (Windows)<br>• **Wireshark**: Packet analysis for encrypted VPN traffic<br>• **traceroute/tracert**: Trace VPN route<br>• **ping**: Test VPN connection<br>• **Browser extensions**: VPN browser add-ons (caution: limited functionality)<br>• **Router VPN**: VPN directly on router (DD-WRT, OpenWrt)<br>• **IPsec tools**: racoon, strongSwan, Libreswan|

---

## Technical Terms

|**Category**|**Details**|
|---|---|
|**Technical Terms**|• **VPN** (Virtual Private Network): Virtual private network<br>• **Tunneling**: Encapsulation of one protocol inside another<br>• **Encapsulation**: Wrapping of data packets<br>• **Encryption**: Encryption of data<br>• **Decryption**: Decryption of data<br>• **VPN server**: Server side of the VPN connection<br>• **VPN client**: Client software on the end device<br>• **VPN tunnel**: Encrypted virtual channel<br>• **Authentication**: Authentication/identity verification<br>• **Confidentiality**: Confidentiality of data<br>• **Integrity**: Data integrity (protection against manipulation)<br>• **Anonymity**: Anonymity (concealment of identity)<br>• **IP masking**: IP address concealment<br>• **IPsec** (Internet Protocol Security): Protocol suite for VPN<br>• **SSL/TLS VPN**: VPN based on SSL/TLS protocols<br>• **OpenVPN**: Open-source VPN protocol and application<br>• **WireGuard**: Modern, fast VPN protocol<br>• **PPTP** (Point-to-Point Tunneling Protocol): Outdated VPN protocol<br>• **L2TP** (Layer 2 Tunneling Protocol): Tunneling without encryption<br>• **L2TP/IPsec**: Combination of L2TP and IPsec<br>• **Remote Access VPN**: Client-to-site VPN (single user → network)<br>• **Site-to-Site VPN**: Network-to-network connection<br>• **Split tunneling**: Split tunnel (only certain traffic over VPN)<br>• **Full tunneling**: All traffic over VPN<br>• **Kill switch**: Emergency shutdown when VPN drops<br>• **GRE** (Generic Routing Encapsulation): Tunneling protocol without encryption<br>• **SSH tunneling**: Port forwarding over SSH<br>• **Port forwarding**: Port forwarding<br>• **6to4, Teredo, ISATAP**: IPv6-over-IPv4 tunnel mechanisms<br>• **Certificate**: Digital certificate for authentication<br>• **Multi-factor authentication (MFA)**: Multi-factor authentication<br>• **Endpoint**: Endpoint of the VPN connection<br>• **Gateway**: VPN gateway (entry point into the network)<br>• **Encryption algorithm**: Encryption algorithm (AES, ChaCha20)<br>• **Key exchange**: Key exchange mechanism|

---

## Important Vocabulary

|**Category**|**Details**|
|---|---|
|**Important Vocabulary**|• **Secure tunnel**: Encrypted communication channel<br>• **Encrypted traffic**: Coded data traffic<br>• **Interception**: Unauthorised reading of data<br>• **Hacker**: Attacker in insecure networks<br>• **Public Wi-Fi**: Insecure public network<br>• **ISP** (Internet Service Provider): Internet provider<br>• **Tampering**: Manipulation of data<br>• **Identity verification**: Verification of user identity<br>• **Concealment**: Hiding the actual IP<br>• **Tracing**: Tracking of online activities<br>• **Privacy**: Protection of personal data<br>• **Geographic restrictions**: Regional access blocks<br>• **Remote access**: Remote access to networks<br>• **Internal network**: Private corporate network<br>• **Intermediary**: Intermediate station (VPN server)<br>• **Encapsulation**: Wrapping of data packets<br>• **Outer protocol**: Wrapping protocol (tunnel)<br>• **Inner protocol**: Encapsulated original protocol<br>• **Unpacking**: Removal of encapsulation<br>• **Encoded format**: Encrypted state<br>• **Decryption key**: Key for decoding<br>• **Unintelligible data**: Unreadable encrypted data<br>• **Unauthorised access**: Access without permission<br>• **Impostor**: Fake/false server<br>• **Security vulnerability**: Weakness in the protocol<br>• **Branch office**: Subsidiary/branch location<br>• **Headquarters**: Central office/company headquarters<br>• **Seamless communication**: Smooth connection<br>• **Wide Area Network (WAN)**: Large-scale network<br>• **Untrusted network**: Insecure network<br>• **Interoperability**: Cooperation of different systems<br>• **Network policy**: Network guidelines<br>• **Point-to-point connection**: Direct connection between two points<br>• **Localhost**: Local computer (127.0.0.1)|