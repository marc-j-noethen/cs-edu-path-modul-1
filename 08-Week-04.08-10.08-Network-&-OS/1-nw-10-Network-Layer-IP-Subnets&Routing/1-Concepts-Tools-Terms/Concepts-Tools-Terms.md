# 📊 Summary based on the 80/20 principle

### **The network layer: The internet’s postal service**

The **network layer (Layer 3)** is like the postal service that works out **where** a packet needs to go and **which route** it should take – even over thousands of kilometres.

**Three main tasks**:

1. **Logical addressing**: Assigning unique IP addresses to devices
2. **Routing**: Determining the best path for packets
3. **Packet switching**: Sending packets from router to router

**Analogy**: IP address = postal address | Router = postal sorting centres | Routing = route finding

### **IP (Internet Protocol): The workhorse**

**Two key characteristics**:

**1. Connectionless**:

- No connection established before sending
- Each packet is treated independently
- Like sending each page of a letter in its own envelope

**2. Best-Effort Delivery**:

- IP does its best, **but guarantees nothing**
- Packets can be lost, duplicated or arrive in the wrong order
- Reliability is the responsibility of higher layers (e.g. TCP)

### **IPv4 addresses: The 32-bit system**

**Format**: 32-bit number in **dotted decimal notation**

**Example**: `192.168.1.100`

- Four **octets** (groups of 8 bits)
- Each octet: value from 0 to 255
- Total: 4.3 billion possible addresses (not enough for today’s world!)

### **Subnetting: Dividing networks**

An IP address consists of **two parts**:

The **subnet mask** indicates the separation:

```
IP address:     192.168.1.100
Subnet mask:   255.255.255.0
                ─────────── ───
                Network part Host part
```

- **Network part**: Identifies the network (here: `192.168.1`)
- **Host part**: Identifies the device (here: `.100`)

**CIDR notation**: Shorter notation

- `255.255.255.0` = `/24` (24 bits for network)
- `192.168.1.100/24` defines IP and subnet

**Why subnetting?**

- ✅ **Organisation**: Clear structure
- ✅ **Security**: Isolation of network segments
- ✅ **Performance**: Less broadcast traffic
- ✅ **Efficiency**: Better use of addresses

### **Special IPv4 addresses**

|Address type|Example|Meaning|
|---|---|---|
|**Network address**|192.168.1.0|Represents the entire network (all host bits = 0)|
|**Broadcast address**|192.168.1.255|Sends to all devices on the network (all host bits = 1)|
|**Loopback**|127.0.0.1|Packet sent to itself (network stack test)|

### **Public vs. Private IP Addresses**

**Public IP Addresses**:

- ✅ Globally unique
- ✅ Routable on the internet
- ✅ Assigned by the ISP
- Example: Your home router is assigned one by your provider

**Private IP-Address ranges**:

- `10.0.0.0/8` (10.0.0.0 bis 10.255.255.255)
- `172.16.0.0/12` (172.16.0.0 bis 172.31.255.255)
- `192.168.0.0/16` (192.168.0.0 bis 192.168.255.255)

**Characteristics of private IP addresses**:

- ❌ Not routable on the internet
- ✅ For internal networks (home, office)
- ✅ Can be used multiple times (across different networks)

**NAT (Network Address Translation)**:

- Routers translate private → public IP addresses
- Many devices share a single public IP address
- Solution to IPv4 address scarcity

### **Useful commands (Windows version)**

**View network configuration**:

```cmd
ipconfig
```

(Displays IP address, subnet mask, default gateway)

**Detailed information**:

```powershell
ipconfig /all
```

**Ping yourself (loopback test)**:

```cmd
ping 127.0.0.1
```

**Ping the gateway**:

```cmd
ping [gateway IP]
```

**View routing table**:

```cmd
netstat -rn
```

or

```cmd
route print
```

**View IPv6 address**:

```powershell
ipconfig | findstr IPv6
```

**IPv6 ping**:

```cmd
ping -6 2001:4860:4860::8888
```

(Google DNS via IPv6)

### **IPv6: The Future**

**Problem with IPv4**: Only ~4.3 billion addresses → **Address exhaustion**

**IPv6 solution**:

- **128-bit addresses** (vs. 32-bit in IPv4)
- **3.4 × 10³⁸ addresses** (practically inexhaustible!)

**Format**: Eight groups of hexadecimal digits

```
2001:0db8:85a3:0000:0000:8a2e:0370:7334
```

**Abbreviation rules**:

1. Omit leading zeros: `0db8` → `db8`
    
2. Replace a sequence of zeros with `::` (only once!):
    
    ```
    2001:0db8:0000:0000:0000:0000:0000:0001→ 2001:db8::1
    ```
    

**IPv6 advantages**:

- ✅ Huge address space
- ✅ Simplified header (more efficient processing)
- ✅ No NAT required (end-to-end connectivity)
- ✅ Built-in IPSec support (security)

**Dual-stack**: Many networks run IPv4 and IPv6 in parallel

### **Routing: Finding the way**

**Routers**: Specialised devices that forward packets between networks

**Routing table** contains:

- **Destination network**: Where is the packet going?
- **Next hop**: IP address of the next router
- **Interface**: Which interface to use?
- **Metric**: ‘Cost’ of the route (hops, speed)

**Routing process**:

1. Router receives packet
2. Checks destination IP in packet header
3. Searches for best match in routing table
4. Forwards packet to next hop

**Two types of routing**:

|Static routing|Dynamic routing|
|---|---|
|✏️ Manually configured|🤖 Automatically adjusted|
|✅ Simple for small networks|✅ Scalable for large networks|
|❌ Not flexible|✅ Adapts to changes|
|Example: Home network|Example: Internet, corporate networks|

**Routing protocols** (dynamic):

- **OSPF** (Open Shortest Path First)
- **BGP** (Border Gateway Protocol) – Internet backbone
- **RIP** (Routing Information Protocol)
- **EIGRP** (Enhanced Interior Gateway Routing Protocol)

### **Default Gateway: The gateway to the Internet**

**What is it?**

- Router in your local network
- Knows the route to external networks (Internet)
- End devices send all external requests there

**Rule**:

- **Destination on the local network?** → Send directly
- **Destination outside?** → Send to default gateway

**Analogy**: The gateway is like the exit from your neighbourhood – without it, you can’t get out of the area!

### **Subnet example: Working through the calculation**

**Given**:

- IP: `10.0.1.50`
- Subnet mask: `255.255.0.0` (= `/16`)

**Analysis**:

```
IP:          10 . 0  . 1  . 50
Mask:      255 .255 . 0  . 0
            ──────── ────────
            Network Host Part
```

**Result**:

- **Network address**: `10.0.0.0` (all host bits set to 0)
- **Broadcast address**: `10.0.255.255` (all host bits set to 1)
- **Available hosts**: 10.0.0.1 to 10.0.255.254 (65,534 devices!)

### **Cisco Packet Tracer: Network simulation**

**Tool for**:

- Setting up virtual networks
- Configuring routers and switches
- Testing network scenarios
- Learning to troubleshoot

**Installation** (Windows):

1. Create a NetAcad account: [netacad.com](https://www.netacad.com/)
2. Download Packet Tracer for Windows
3. Install the `.exe` file
4. Log in with your NetAcad credentials

**Tip**: Increase the font size (Options → Preferences → Font → CLI to 18)

### **Key message**

The **network layer** is the foundation of internet communication:

**IP addresses** = Unique identification of devices **Subnetting** = Organised network division **Routing** = Intelligent pathfinding for packets

**IPv4** solves the "Where to?" question, but is reaching its limit → **IPv6** offers virtually unlimited addresses

**Routers** are the intelligent mail sorters that use **routing tables** to find the best route for every packet.

**Difference from higher layers**:

- Layer 3 (Network): **Where** is the destination? **How** do I get there?
- Layer 4 (Transport): **Which application** receives the data?
- Layer 7 (Application): **What** does the data mean?

Without the network layer, there would be no internet – it is the glue that connects all networks worldwide! 🌐📬🗺️

---

## Summary table

| **Category**        | **Details**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Tools used**      | • **Terminal/Command Prompt**: Run network commands (macOS: Terminal; Windows: CMD, PowerShell)<br>• **ifconfig**: Display network interfaces (macOS; Windows: `ipconfig`)<br>• **ip address**: Modern alternative to ifconfig (macOS: `ip a`; Windows: `Get-NetIPAddress` in PowerShell)<br>• **ping**: Test network connection (both systems: `ping`)<br>• **ping6**: IPv6 ping (macOS: `ping6`; Windows: `ping -6`)<br>• **netstat**: Routing tables and network statistics (both systems: `netstat -rn` or `netstat -nr`)<br>• **traceroute/tracert**: Packet tracing (macOS: `traceroute`; Windows: `tracert`)<br>• **Cisco Packet Tracer**: Network simulation and configuration tool (Windows & macOS)<br>• **Wireshark**: Packet analysis tool for IP packets<br>• **nslookup**: DNS queries<br>• **arp**: View ARP table (both systems)<br>• **route**: Manipulate routing table (Windows: `route print`, `route add`)<br>• **Get-NetRoute**: PowerShell cmdlet for routing (Windows)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **Technical terms** | • **Network Layer**: Network layer (Layer 3 in the OSI model)<br>• **IP** (Internet Protocol): The main protocol of the network layer<br>• **IPv4**: Internet Protocol Version 4 (32-bit addresses)<br>• **IPv6**: Internet Protocol Version 6 (128-bit addresses)<br>• **IP address**: Unique numerical identifier for network devices<br>• **Dotted decimal notation**: Dotted decimal notation (e.g. 192.168.1.100)<br>• **Octet**: 8-bit group in an IPv4 address (value 0–255)<br>• **Hexadecimal**: Hexadecimal notation (IPv6)<br>• **Subnet**: Logical subdivision of an IP network<br>• **Subnetting**: Process of network subdivision<br>• **Subnet mask**: Separation of the network and host portions<br>• **CIDR** (Classless Inter-Domain Routing): Slash notation (e.g. /24)<br>• **Network Portion**: Network portion of the IP address<br>• **Host Portion**: Host portion of the IP address<br>• **Network Address**: Network address (all host bits = 0)<br>• **Broadcast Address**: Broadcast address (all host bits = 1)<br>• **Loopback Address**: Loopback address (127.0.0.1)<br>• **Public IP Address**: Public IP address (globally unique)<br>• **Private IP Address**: Private IP address (not routable on the internet)<br>• **NAT** (Network Address Translation): Network address translation<br>• **Router**: Switching device between networks<br>• **Routing**: Path selection for packets<br>• **Routing Table**: Routing table<br>• **Default Gateway**: Router for external connections<br>• **Next Hop**: Next router on the path<br>• **Metric**: Cost value of a route<br>• **Static Routing**: Static routing (manual configuration)<br>• **Dynamic Routing**: Dynamic routing (automatic adjustment)<br>• **Routing Protocol**: Routing protocol (OSPF, BGP, RIP, EIGRP)<br>• **Connectionless**: Connectionless<br>• **Best-Effort Delivery**: Best-effort delivery without guarantee<br>• **Packet**: Data packet<br>• **Packet Forwarding**: Packet forwarding<br>• **Interface**: Network interface (e.g. en0, eth0)<br>• **Dual-Stack**: Simultaneous operation of IPv4 and IPv6<br>• **IPSec**: Internet Protocol Security<br>• **Address Exhaustion**: Address exhaustion (IPv4)<br>• **Logical Addressing**: Logical addressing |
| **Key vocabulary**  | • **Layer 3**: Network layer in the OSI model<br>• **Postal service analogy**: The network layer is like the postal service for letters<br>• **Unique address**: Unmistakable identification<br>• **Cross-network**: Across different networks<br>• **Best path**: Optimal route for packets<br>• **Packet switching**: Forwarding of packets<br>• **32-bit number**: IPv4 address length<br>• **128-bit number**: IPv6 address length<br>• **Dotted decimal notation**: Format such as 192.168.1.1<br>• **Octet**: 8-bit segment (0–255)<br>• **Network segmentation**: Division into subnets<br>• **Organisational structure**: Logical structure<br>• **Security isolation**: Separation of network areas<br>• **Broadcast domain**: Area for broadcast traffic<br>• **Address management**: Efficient use of IP addresses<br>• **Binary ones**: 1-bits in subnet mask (network part)<br>• **Binary zeros**: 0-bits in subnet mask (host part)<br>• **Slash notation**: /24, /16 etc.<br>• **Network representation**: Representation of the entire network<br>• **All devices**: Broadcast to all hosts<br>• **Self-addressing**: Loopback for internal testing<br>• **Globally unique**: Public IPs on the Internet<br>• **Non-routable**: Private IPs valid only locally<br>• **Address translation**: NAT mechanism<br>• **Shared public IP**: Multiple devices use one IP<br>• **Router function**: Packet switching between networks<br>• **Path selection**: Choosing the best route<br>• **Next hop**: Next hop to the destination<br>• **Cost of a route**: Metric (hops, speed)<br>• **Manual configuration**: Static routing<br>• **Automatic adjustment**: Dynamic routing<br>• **External connections**: Access to other networks<br>• **Local network**: Directly connected devices<br>• **Hexadecimal notation**: IPv6 format<br>• **Astronomical number**: Huge IPv6 address space<br>• **End-to-end connectivity**: Direct connection without NAT<br>• **Simplified header**: More efficient processing                                                                                                                                                                                                                                                       |