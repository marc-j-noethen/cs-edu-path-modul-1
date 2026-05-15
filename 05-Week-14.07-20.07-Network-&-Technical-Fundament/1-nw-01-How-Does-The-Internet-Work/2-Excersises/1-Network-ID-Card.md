# 🌐 Network ID Card

**Course:** Cyber Security Analyst – Network Technology | **Date:** 14 July 2025

---

## Task

**Objective:** Identify the IPv4 address of your own computer using `ipconfig` (Windows) or `ifconfig` (Linux) and specify the command to check connectivity.

---

## Environment

```
Interface:   WLAN (Wireless LAN adapter)
Local IP:   192.168.0.92
Router IP:   192.168.0.1
Tool:        ipconfig (Windows Command Prompt)
DNS suffix:  utopia.net
Subnet mask: 255.255.255.0
```

---

## Procedure

**Command executed:**
```bash
ipconfig
```

**Output:**
```
Wireless LAN adapter WLAN:
   Connection-specific DNS suffix: utopia.net
   IPv4 address  . . . . . . . . . . : 192.168.0.92
   Subnet mask  . . . . . . . . . . : 255.255.255.0
   Default gateway . . . . . . . . . : 192.168.0.1
```

---

## Analysis

### Network configuration

| Parameter | Value |
|---------- -|------|
| Active interface | WLAN (Wireless LAN adapter) |
| IPv4 address | 192.168.0.92 |
| Subnet mask | 255.255.255.0 |
| Default gateway | 192.168.0.1 |
| DNS suffix | utopia.net |

### Connection test

**Command for reachability check:**
```bash
ping www.google.com
```

---

## Answers

**Task 1-4:** Identify the IPv4 address
- **Answer:** `192.168.0.92`
- **Interface:** Wireless LAN adapter WLAN (status: active)

**Task 5:** Command for connection test
- **Answer:** `ping www.google.com`

---

## Notes

- The IPv4 address 192.168.0.92 is a private IP address (Class C)
- The active interface is the WLAN adapter
- The default gateway (router) has the IP address 192.168.0.1
- The `ping` command sends ICMP Echo Request packets to check connectivity



