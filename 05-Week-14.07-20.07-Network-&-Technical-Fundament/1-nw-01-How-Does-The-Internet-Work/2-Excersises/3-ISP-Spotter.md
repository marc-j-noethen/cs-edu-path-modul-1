# 🌐 ISP Spotter

**Course:** Cyber Security Analyst – Network Technology | **Date:** 14 July 2025

---

## Task

**Objective:** To understand the difference between local and public IP addresses and to recognise the role of the ISP in IP registrations.

---

## Environment

```
Local IP:      192.168.0.92 (from Task 1)
Public IP:     92.206.120.5
Tool:           https://whatismyipaddress.com/
Whois tool:     IP Lookup Service
```

---

## Procedure

**Step 1 – Determine the public IP:**
- **Service:** whatismyipaddress.com
- **IPv4 result:** 92.206.120.5
- **IPv6 result:** 2001:4860:7:610::ec

**Step 2 – Whois Lookup:**
```
IP:             92.206.120.5
Country:        Germany
Country ISO:    DE
State:          Saxony-Anhalt
City:           Halberstadt
Postcode:    38820
Latitude:       51.8956
Longitude:      11.0562
Organisation:   Tele Columbus AG
ISP:            Tele Columbus AG
```

---

## Analysis

### IP Address Comparison

| Type | IP Address | Scope | Purpose |
|-----|------------|--------------------|-- -----|
| Local (private) | 192.168.0.92 | Home network | Communication between devices on the local network |
| Public | 92.206.120.5 | Internet (global) | Communication with the Internet |

### ISP Information

| Parameter | Value |
|---------- -|------|
| Organisation | Tele Columbus AG |
| ISP | Tele Columbus AG |
| Country | Germany (DE) |
| Federal state | Saxony-Anhalt |
| City | Halberstadt |

---

## Answers

**Question:** Explain the difference between a local and a public IP address and describe the role of the ISP and the router.

**Answer:**

**Local IP address (192.168.0.92):**
- Assigned by the router in the home network
- Valid only within your own network
- Enables communication between devices on the same network (e.g. laptop ↔ smartphone ↔ printer)
- Not routable on the internet
- Private address range (RFC 1918)

**Public IP address (92.206.120.5):**
- Assigned by the ISP (Tele Columbus AG)
- Globally unique on the internet
- Identifies the router/connection externally
- Enables communication with the rest of the world
- Shared by all devices on the home network

**Role of the router:**
- Translates between local and public IP addresses (NAT – Network Address Translation)
- Manages the local network (DHCP)
- Forwards requests from the home network to the internet
- Receives responses from the internet and forwards them to the correct local device

**Role of the ISP:**
- Provides the internet connection
- Assigns the public IP address (dynamic or static)
- Routes data traffic between the home network and the internet
- Manages IP address blocks (here: 92.206.120.x range)

**Communication path:**
```
Laptop (192.168.0.92) → Router (192.168.0.1 local / 92.206.120.5 public) 
    → ISP (Tele Columbus) → Internet → Destination server → ISP → Router → Laptop
```

---

## Notes

- NAT (Network Address Translation) allows multiple devices to share a public IP
- Private IP ranges: 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16
- The public IP may change (dynamic IP) if the ISP reassigns it
- IPv6 allows each device to have its own public address (here: 2001:4860:7:610::ec)


