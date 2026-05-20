# The Lone IP Ranger (NAT / PAT)

**Course:** Cyber Security Analyst – Network Technology | **Date:** 05 August 2025

---

## Task

**Objective:**  
Configure PAT so that multiple internal hosts share a single public IP address.

**Requirements:**

- Define the internal network `192.168.1.0/24`.
- Set `ip nat inside source list 1 interface G0/1 overload`.
- Evaluate the translation table following a ping.

---

## Solution

```text
Key entries in the NAT table:
- Inside local: 192.168.1.10:<icmp-id>
- Inside global: 203.0.113.1:<icmp-id or translated identifier>
- Outside global: 203.0.113.2

Interpretation:
PC-A sends using its private address 192.168.1.10.
The router replaces this with the single public address 203.0.113.1 for the outward path.
PAT additionally distinguishes concurrent sessions via ports or ICMP identifiers.
```

**Alternative (compact):**

```text
Many private hosts -> one public IP + different session identifiers.
```

---

## Tests

|Item|Expected|✓|
|---|---|---|
|Ping to server PT|successful|✅|
|NAT translation|Visible internally and globally|✅|
|PAT principle|A single public IP is shared|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|Inside local|Private address on the internal network.|
|Inside global|Public address visible externally.|
|PAT|Multiple internal sessions via a single public IP.|

---

## Rules / Logic

```text
Private source -> Router translates -> public source.
Session separation is performed via port or ICMP identifier.
```

---

## Notes

- **Tip:** Run `show ip nat translations` immediately after a ping.
- **Concept:** NAT changes addresses, not the actual content of the application.

---

## Optional: Extensions

- Have a second PC ping simultaneously.
- Compare NAT without overload using multiple public IPs.


