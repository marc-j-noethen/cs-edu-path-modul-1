# Ping Pong (ARP in Packet Tracer)

**Course:** Cyber Security Analyst – Network Technology | **Date:** 12 August 2025

---

## Task

**Objective:**  
Compare ARP for local and remote destinations in Packet Tracer.

**Requirements:**

- Examine a local ping from PC0 to PC1.
- Examine a remote ping, e.g. to `8.8.8.8`.
- Justify the destination IP in the ARP payload.

---

## Solution

```text
Local ping (Step 3):
- Destination IP in the ARP request = 192.168.1.11

Remote ping (Step 4):
- Destination IP in the ARP request = 192.168.1.1

Why is this different?
For a local destination, PC0 needs the MAC address of PC1 directly.
With a remote destination, PC0 only needs the MAC address of the default gateway,
because the router forwards the packet to the remote network.
```

**Alternative (compact):**

```text
Local = query direct destination.
Remote = query gateway.
```

---

## Tests

|Scenario|ARP destination IP|✓|
|---|---|---|
|Local|192.168.1.11|✅|
|Remote|192.168.1.1|✅|
|Explanation|Routing principle understood|✅|

---

## Explanation / Concepts

|Concept|Description|
|Local destination|Direct delivery within the subnet.|
|Remote destination|Forwarding via the default gateway.|
|ARP in PT|Clearly visible in simulation mode.|

---

## Rules / Logic

```text
Only local neighbours are resolved directly via ARP.
```

---

## Notes

- **Tip:** Clear the ARP cache before each test.
- **Concept:** Packet Tracer clearly illustrates the difference between local and remote neighbours.

---

## Optional: Extensions

- Add a second VLAN and check the behaviour again.
- Monitor ARP requests and ICMP side by side in the simulation window.

