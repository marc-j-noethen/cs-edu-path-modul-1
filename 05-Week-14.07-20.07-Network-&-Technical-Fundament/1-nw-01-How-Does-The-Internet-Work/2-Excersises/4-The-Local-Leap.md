# 🌐 The Local Leap

**Course:** Cyber Security Analyst – Network Technology | **Date:** 14 July 2025

---

## Task

**Objective:** Use `tracert` (Windows) or `traceroute` (Linux) to identify the first hops and determine the entry point to the ISP network.

---

## Environment

```
Tool:           tracert (Windows Command Prompt)
Destination:      www.google.com
Local IP:      192.168.0.92
Router IP:      192.168.0.1
ISP:            Tele Columbus AG
```

---

## Procedure

**Command executed:**
```bash
tracert google.com
```

**Note:** The full output is not included in the document, but the structure can be analysed based on the other tracert outputs.

**Expected output (first 5 hops):**
```
  1     1 ms     1 ms     1 ms  192.168.0.1
  2     *        *        *     Request timed out.
  3     9 ms     9 ms     9 ms  172.17.166.37
  4    10 ms     9 ms     9 ms  172.17.166.21
  5    10 ms     9 ms     9 ms  172.17.80.161
```

---

## Analysis

### Hop analysis (first 5 hops)

| Hop | IP address | Average latency | Identification | Description |
|-----|------------|------------------ -|----------------|--------------|
| 1 | 192.168.0.1 | 1 ms | Home router | Local gateway (private IP range) |
| 2 | * | Timeout | ISP equipment | Does not respond to ICMP (firewall policy) |
| 3 | 172.17.166.37 | 9 ms | ISP router | Tele Columbus infrastructure |
| 4 | 172.17.166.21 | 9 ms | ISP router | Tele Columbus infrastructure |
| 5 | 172.17.80.161 | 9–10 ms | ISP router | Tele Columbus infrastructure |

### Latency comparison

| Hop | Average latency | Note |
|-----|------------------------- -|-----------|
| 1 (Home router) | ~1 ms | Very fast – direct local access |
| 3-5 (ISP) | ~9-10 ms | Significantly higher – external network hops |

**Latency difference:** approx. 8-9 ms between Hop 1 and Hops 3-5

---

## Answers

**Question 4:** Is the first hop IP a typical private router address?

**Answer:** 
- **Yes**, 192.168.0.1 is a typical private IP address for home routers
- It lies within the 192.168.0.0/16 range (Class C private address range, RFC 1918)
- This corresponds to the default gateway from Exercise 1

**Question 5:** ISP-related hostnames in hops 2–4?

**Answer:**
- **Hop 2:** No response (timeout) – common with ISP equipment for security reasons
- **Hops 3–5:** IP addresses in the 172.17.x.x range
- These belong to the private address range 172.16.0.0/12 and are used internally by the ISP Tele Columbus
- No resolved hostnames visible, but IP structure points to ISP infrastructure

**Question 6:** Latency comparison and explanation

**Comparison:**
- **Hop 1 (router):** ~1 ms
- **Hops 3–4 (ISP):** ~9–10 ms
- **Difference:** 9-10 times higher

**Explanation of why Hop 1 is the fastest:**

1. **Physical distance:**
   - Hop 1 is the home router in the same room/building
   - Only a few metres of cable (CAT5/6 or Wi-Fi)

2. **Direct connection:**
   - No intermediate devices
   - Direct Layer 2 access (Ethernet/Wi-Fi)

3. **No additional processing:**
   - Minimal routing decisions
   - No complex firewall rules or traffic shaping

4. **ISP hops take longer due to:**
   - Longer physical distances (to the ISP distribution point/backbone)
   - Multiple router hops with routing decisions
   - Queue processing and traffic management
   - Potentially slower upstream connection (DSL/cable)

---

## Notes

- `* * *` at hop 2 does not mean that the hop does not exist, but that it does not respond to ICMP
- Private IP ranges: 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16
- ISPs often use private IPs in their infrastructure (carrier-grade NAT)
- The first 3–5 hops typically show the infrastructure from the home network to the ISP backbone
- The further away, the higher the latency (speed of light limit + routing delays)

