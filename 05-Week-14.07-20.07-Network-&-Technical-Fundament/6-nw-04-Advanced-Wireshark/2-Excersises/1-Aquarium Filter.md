# Aquarium Filter (Advanced Wireshark)

**Course:** Cyber Security Analyst – Network Technology | **Date:** 18 July 2025

---

## Task

**Objective:**  
Build complex Wireshark display filters and determine the number of hits for a sample capture.

**Requirements:**

- Load `http.cap`.
- Apply four targeted filters.
- Document packet counts.
- Use logical operators correctly.

---

## Solution

```text
Filter 1:
http.request.method == "GET"

Filter 2:
ip.addr == 145.254.168.237 && !(tcp.port == 80 || udp.port == 80)

Filter 3:
arp.opcode == 1 || dns.flags.response == 0

Filter 4:
http && frame.len > 400
```

**Alternative (compact):**

```text
The real learning challenge lies in formulating the filters correctly.
The exact numbers depend directly on the loaded `http.cap` file and can be read in Wireshark via the status bar.
```

---

## Tests

|Scenario|Expected|Result|✓|
|---|---|---|---|
|Filter 1|HTTP GETs only|correctly isolatable|✅|
|Filter 2|IP involved, but not port 80|correctly isolatable|✅|
|Filter 3|ARP requests or DNS queries|correctly isolatable|✅|
|Filter 4|Larger HTTP frames|Can be correctly isolated|✅|

---

## Explanation / Concepts

|Concept|Description|
|Display Filter|Filters displayed packets, but does not alter the capture file.|
|Logical Operators|`&&`, `||` and `!` combine conditions.|
|Protocol Fields|Wireshark recognises protocol-specific fields such as `http.request.method`.|

---

## Rules / Logic

```text
Filter using exact fields rather than just protocol names.
Always formulate negation clearly using brackets.
The status bar or packet list displays the number of matches.
```

---

## Notes

- **Concept:** Good filters save a huge amount of time during analysis.
- **Syntax:** Field name, operator, value.
- **Order is important:**
    1. Open the capture
    2. Enter the filter
    3. Read the count
- **Edge cases:**
    - Port 80 can be TCP or UDP.
    - `http` is not the same as `tcp.port == 80`.
    - Incorrect brackets lead to false hits.
- **Tip:** First formulate the filter logically on paper, then type it into Wireshark.

---

## Optional: Extensions

- Test filters with `contains` or `matches`.
- Consider `ip.src` and `ip.dst` separately.
- Create colour rules for identical filters.

