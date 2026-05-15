# 🐍 Packet Fishing in Aquarium (Wireshark filters)

**Course:** Cyber Security Analyst – Network Technology | **Date:** 18 July 2025

---

## Task

**Objective:**  
Formulate correct Wireshark display filters and analyse the offline file `http.cap` using reproducible count values.

**Requirements:**

- Specify the correct display filter for all six live capture scenarios.
- Determine the exact hit counts for the offline capture `http.cap`.
- Use logical operators such as `&&`, `||` and `!` correctly.
- Distinguish between a general port filter and a true protocol filter.
- Output:
    - `Part A: six correct display filters`
    - `Part B: GET = 2, non-HTTP at 145.254.168.237 = 0`
    - `Part B: ARP/DNS = 1, HTTP with frame.len > 400 = 5`

---

## Solution

```python
# Inputs
capture_file = "http.cap"
live_ip = "8.8.8.8"
target_ip = "145.254.168.237"

# Main logic
if capture_file != "http.cap":
    print("This sample solution was derived for the original file http.cap.")
elif live_ip == "8.8.8.8":
    print("Filter: ip.addr == 8.8.8.8 | http | icmp | tcp.port == 80 | icmp && ip.src == 8.8.8.8 | !http")
elif target_ip == "145.254.168.237":
    print("Counts: GET = 2 | ip.addr == 145.254.168.237 without port 80 = 0")
else:
    print("Further matches: arp.opcode == 1 || dns.flags.response == 0 -> 1 | http && frame.len > 400 -> 5")
```

**Alternative (compact):**

```python
print("Part A: ip.addr == 8.8.8.8 | http | icmp | tcp.port == 80 | icmp && ip.src == 8.8.8.8 | !http")
print('Part B: "GET"=2 | non-HTTP @145.254.168.237=0 | ARP request or DNS query=1 | HTTP >400 bytes=5')
```

---

## Tests

|Input 1|Input 2|Input 3|Expected|Result|✓|
|---|---|---|---|---|---|
|`http.request.method == "GET"`|`http.cap`|`GET requests`|`2`|`2`|✅|
|`ip.addr == 145.254.168.237 && !(tcp.port == 80 || udp.port == 80)`|`http.cap`|`non-HTTP`|`0`|`0`|✅|
|`http && frame.len > 400`|`http.cap`|`large HTTP frames`|`5`|`5`|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|`ip.addr`|Applies to source **or** destination IP.|
|`tcp.port`|Applies to source **or** destination port.|
|Display filter|Filters already recorded frames, not the capture process itself.|

---

## Rules / Logic

```
For an IP in both directions: ip.addr == X
For a TCP port in both directions: tcp.port == N
Negation of a protocol: !http
```

---

## Notes

- **Concept:** A protocol filter such as `http` is more precise than a pure port filter such as `tcp.port == 80`.
- **Syntax:** `icmp && ip.src == 8.8.8.8`
- **Order is important:**
    1. Formulate the expression
    2. Apply the filter
    3. Check the number of hits at the bottom of Wireshark
- **Edge cases:**
    - `tcp.port == 80` may also match non-HTTP data on port 80.
    - `!http` only hides HTTP traffic recognised by Wireshark.
    - With `ip.addr == 145.254.168.237`, no packets remain in this capture after excluding port 80.
- **Tip:** For more complex filters, place the brackets first and then add the logical operators.

---

## Optional: Extensions

- Add a filter for HTTP responses only.
- Check the number of hits for `tcp.port == 80 && !http`.
- Test your own filters using `frame contains`.
- Explain the differences between `http` and `tcp.port == 80`.

