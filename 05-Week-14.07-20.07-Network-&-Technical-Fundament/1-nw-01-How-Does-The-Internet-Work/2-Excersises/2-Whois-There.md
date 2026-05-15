# 🌐 Who Is There

**Course:** Cyber Security Analyst - Network Technology | **Date:** 14 July 2025

---

## Task

**Objective:** Test the connection to a public server, identify the organisation behind the IP block, and compare it with a non-routable address.

---

## Environment

```
Tool:           ping (Windows Command Prompt)
Target IP 1:      1.1.1.1 (Cloudflare DNS)
Target IP 2:      192.0.2.1 (Documentation IP)
Whois tool:     Online IP Whois Lookup
```

---

## Procedure

**Test 1 - Reachable IP:**
```bash
ping -n 5 1.1.1.1
```

**Output:**
```
Pinging 1.1.1.1 with 32 bytes of data:
Reply from 1.1.1.1: bytes=32 time=15ms TTL=54
Ping statistics for 1.1.1.1:
    Packets: Sent = 5, Received = 5, Lost = 0
    (0% loss),
Approximate times in milliseconds:
    Minimum = 14ms, Maximum = 23ms, Average = 16ms
```

**Test 2 - Non-routable IP:**
```bash
ping 192.0.2.1
```

**Output:**
```
Ping is being performed for 192.0.2.1 with 32 bytes of data:
Request timed out.
Ping statistics for 192.0.2.1:
    Packets: Sent = 4, Received = 0, Lost = 4
    (100% loss),
```

---

## Analysis

### Ping comparison

| IP address | Type | Packets sent | Received | Lost | Average | Behaviour |
|------------|-----|-----------------|-----------|----------|--------------|-----------|
| 1.1.1.1 | Public DNS | 5 | 5 | 0 (0%) | 16ms | Successful |
| 192.0.2.1 | Documentation IP | 4 | 0 | 4 (100%) | - | Timeout |

### Whois result for 1.1.1.1

```
org-name: APNIC Research and Development
```

---

## Answers

**Question 4:** Organisation of the 1.1.1.1 IP block
- **Answer:** APNIC Research and Development
- **Note:** Cloudflare uses this IP block for its public DNS service

**Question 5:** Difference in behaviour between 1.1.1.1 and 192.0.2.1

**Answer:**
- **1.1.1.1:** All 5 packets were successfully received with an average latency of 16ms
- **192.0.2.1:** All 4 packets were lost (100% packet loss) with a "request timed out" error

**Explanation:**
- 192.0.2.1 is a documentation IP address (TEST-NET-1, RFC 5737) and is not routable on the internet
- This IP address is reserved exclusively for documentation purposes
- No routers on the internet forward packets to this address

---

## Notes

- The `-n 5` parameter in Windows corresponds to `-c 5` in Linux
- 1.1.1.1 is Cloudflare’s public DNS server (fast and reliable)
- TTL=54 indicates that the packet has 54 hops remaining (originally probably 64)
- Documentation IPs (192.0.2.0/24, 198.51.100.0/24, 203.0.113.0/24) should never be routed on the Internet

