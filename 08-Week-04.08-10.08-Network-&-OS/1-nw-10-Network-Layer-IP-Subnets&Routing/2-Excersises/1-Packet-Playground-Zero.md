# Packet Playground Zero (IP / Subnet)

**Course:** Cyber Security Analyst – Network Technology | **Date:** 04 August 2025

---

## Task

**Objective:**  
Set up a mini-network with two PCs on the same subnet and check connectivity.

**Requirements:**

- Connect the two PCs directly.
- Set static IPs `192.168.1.10/24` and `192.168.1.11/24`.
- Successfully test ping in both directions.

---

## Solution

```text
PC0:
- IP: 192.168.1.10
- Subnet mask: 255.255.255.0

PC1:
- IP: 192.168.1.11
- Subnet mask: 255.255.255.0

Result:
The pings between PC0 and PC1 are successful.
Both hosts are on the same /24 subnet and do not require a gateway for this direct connection.
```

**Alternative (compact):**

```text
Same subnet + physical connection = direct communication possible.
```

---

## Tests

|Test|Expected|✓|
|---|---|---|
|`ping 192.168.1.11` from PC0|Reply|✅|
|`ping 192.168.1.10` from PC1|Reply|✅|
|IP configuration|Both in the same /24|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|Subnet|Defines which hosts are locally accessible.|
|Direct connection|No router required as long as both hosts are on the same network.|
|Mask `/24`|Network portion 192.168.1.x, host portion last octet.|

---

## Rules / Logic

```text
192.168.1.10/24 and 192.168.1.11/24 belong to the same network 192.168.1.0/24.
```

---

## Notes

- **Tip:** When creating direct connections in Packet Tracer, ensure you use the correct cable type.
- **Concept:** Get Layer 1/2 right first; only then is it worth troubleshooting ping errors at Layer 3.

---

## Optional: Extensions

- Add a third device.
- Test communication with a deliberately incorrect subnet mask.

