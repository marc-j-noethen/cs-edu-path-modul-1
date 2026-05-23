# Traceroute Trails (Ethernet / Routing)

**Course:** Cyber Security Analyst – Network Technology | **Date:** 11 August 2025

---

## Task

**Objective:**  
To understand which destination MAC address is used for outgoing Internet packets in the local segment.

**Requirements:**

- Record `traceroute 8.8.8.8`.
- Compare the first and second outgoing packets.
- Identify the local Layer 2 next hop.

---

## Solution

```text
Sample answer:
- Source MAC of the first outgoing packet: MAC of your own computer
- Destination MAC of the first outgoing packet: MAC of the router / default gateway

- Source MAC of the second outgoing packet: still the MAC of your own computer
- Destination MAC of the second outgoing packet: still the MAC of the router

Has it changed?
No. As long as the destination lies outside the local network, the next local hop is always the router.

Answer to step 9:
For any Internet packets, the computer always uses the MAC address of the default gateway as the destination MAC in the Ethernet frame,
because only the router can forward the packet to other networks.
```

**Alternative (compact):**

```text
Remote destination at IP level, router as destination at MAC level.
```

---

## Tests

|Item|Expected|✓|
|---|---|---|
|1st packet|Destination MAC = router|✅|
|2nd packet|Destination MAC remains router|✅|
|Explanation|Next-hop principle understood|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|Next Hop|Next device in the local segment.|
|Gateway|Router for destinations outside one’s own network.|
|Traceroute|Shows IP hops, not Layer 2 hops.|

---

## Rules / Logic

```text
A local Ethernet frame always travels only as far as the next local hop.
For Internet destinations, this is the default gateway.
```

---

## Notes

- **Tip:** TTL changes affect IP, not the local destination MAC.
- **Concept:** Layer 2 and Layer 3 must always be considered separately.

---

## Optional: Extensions

- Repeat the same process for a local destination on the same subnet.
- Record the ARP resolution of the gateway as well.

