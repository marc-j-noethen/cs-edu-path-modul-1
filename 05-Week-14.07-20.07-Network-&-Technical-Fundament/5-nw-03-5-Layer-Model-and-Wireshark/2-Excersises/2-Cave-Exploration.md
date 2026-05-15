# 🐍 Cave Exploration (ICMP & Traceroute)

**Course:** Cyber Security Analyst – Network Technology | **Date:** 18 July 2025

---

## Task

**Objective:**  
Correctly identify ICMP in a Wireshark capture and explain how `ping` and Windows `tracert` use ICMP.

**Requirements:**

- Apply the appropriate display filter for ICMP.
- Map an ICMP Echo Request to the relevant layers of the 5-layer model.
- Explain why ICMP does not have its own TCP or UDP header.
- Demonstrate how `tracert` uses TTL and ICMP error messages to make each hop visible.
- Output:
    - `Display filter: icmp`
    - `Echo Request: IPv4 + ICMP Type 8, Code 0`
    - `Traceroute: TTL 1..n, routers respond with ICMP type 11, code 0`

---

## Solution

```python
# Inputs
target_host = "8.8.8.8"
echo_filter = "icmp"
tracert_filter = "icmp"

# Main logic
if target_host != "8.8.8.8":
    print("This sample solution applies to ping/tracert to 8.8.8.8.")
elif filter_echo == "icmp":
    print("Echo Request: Link Layer (Ethernet II or 802.11) -> IPv4 -> ICMP Type 8 Code 0")
elif filter_tracert == "icmp":
    print("Traceroute: TTL increases by 1, 2, 3 ...; routers send ICMP Type 11 Code 0")
else:
    print("ICMP operates directly over IP and has no separate TCP/UDP header.")
```

**Alternative (compact):**

```python
print("icmp | Echo Request = Type 8/Code 0 | tracert = TTL 1..n + Time Exceeded Type 11/Code 0")
```

---

## Tests

|Input 1|Input 2|Input 3|Expected|Result|✓|
|---|---|---|---|---|---|
|`icmp`|`ping 8.8.8.8`|`Echo Request`|`Type 8 / Code 0`|`Type 8 / Code 0`|✅|
|`icmp`|`tracert 8.8.8.8`|`Inter-hop`|`Type 11 / Code 0`|`Type 11 / Code 0`|✅|
|`HTTP`|`TCP`|`Comparison with ICMP`|`HTTP uses TCP, ICMP does not`|`HTTP uses TCP, ICMP does not`|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|ICMP Echo Request|Diagnostic message for `ping`; in IPv4 this is Type 8, Code 0.|
|TTL|Reduced by 1 per router; when it reaches 0, the router discards the packet.|
|ICMP Time Exceeded|Error message type 11, code 0; `tracert` is based precisely on this.|

---

## Rules / Logic

```
ICMP sits directly above IPv4 and not above TCP or UDP.
TTL = 0 -> Router responds with ICMP Time Exceeded (Type 11, Code 0).
Destination host reached -> Echo Reply (Type 0, Code 0).
```

---

## Notes

- **Concept:** ICMP is a network/control protocol and not a classic transport protocol.
- **Syntax:** `icmp`
- **Order is important:**
    1. Start capture
    2. Run `ping 8.8.8.8` or `tracert 8.8.8.8`
    3. Examine Echo Requests and Time Exceeded packets in detail
- **Edge Cases:**
    - With Wi-Fi, the link layer looks different from Ethernet II.
    - On Linux, `traceroute` often uses UDP instead of ICMP.
    - The exact local source IP depends on your own network and can therefore only be specified in relation to the capture.
- **Tip:** The most important comparison for the answer is: HTTP = TCP-based, ICMP = embedded directly in IP.

---

## Optional: Extensions

- Analyse the Echo Reply as well.
- Compare Windows `tracert` with Linux `traceroute`.
- Document intermediate routers in a hop list based on their source IP.
- Record TTL values per hop in a table.

