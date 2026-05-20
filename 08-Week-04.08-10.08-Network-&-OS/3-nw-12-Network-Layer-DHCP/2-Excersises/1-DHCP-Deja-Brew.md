# DHCP Deja Brew (DHCP)

**Course:** Cyber Security Analyst – Network Technology | **Date:** 06 August 2025

---

## Task

**Objective:**  
Observe the DORA process and explain the first IP address obtained.

**Requirements:**

- Set up a DHCP server with the `OfficePool` pool.
- Set the client to DHCP.
- Evaluate the discover and the lease received.

---

## Solution

```text
Question 1:
In the first DHCP discover, the client typically has:
- Source IP: 0.0.0.0
- Destination IP: 255.255.255.255

Why?
The client does not yet have a valid IP address and does not yet know the DHCP server.
That is why it sends a broadcast to everyone.

Question 2:
Typical first lease received from this pool:
- IP address: 192.168.1.10
- Subnet mask: 255.255.255.0
- Default gateway: 192.168.1.1
```

**Alternative (compact):**

```text
Without its own IP, DHCP must start with a broadcast.
```

---

## Tests

|Item|Expected|✓|
|---|---|---|
|Discover|0.0.0.0 -> 255.255.255.255|✅|
|Offer/Ack|Address from the pool|✅|
|Client configuration|IP/gateway set correctly|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|DORA|Discover, Offer, Request, Acknowledge.|
|Broadcast|Required if the client does not yet know a server.|
|Lease|Network configuration assigned for a limited time.|

---

## Rules / Logic

```text
No client IP status -> Broadcast Discover.
Server assigns an address from the configured pool.
```

---

## Notes

- **Tip:** In simulation mode, filter only DHCP.
- **Concept:** DHCP automates not only IP, but usually also gateway and DNS.

---

## Optional: Extensions

- Change lease time.
- Have two clients addressed one after the other.

