# Segmented Sanctuaries (VLANs)

**Course:** Cyber Security Analyst – Network Technology | **Date:** 13 August 2025

---

## Task

**Objective:**  
Set up two VLANs on a switch and verify their isolation.

**Requirements:**

- Create VLAN 10 `Sales` and VLAN 20 `Tech`.
- Assign ports correctly.
- Test pings within and between VLANs.

---

## Solution

```text
Expected results:
- PC0 -> PC1: successful (both in VLAN 10)
- PC0 -> PC2: failed (different VLANs)
- PC2 -> PC3: successful (both in VLAN 20)
- PC2 -> PC0: failed (different VLANs)

Reasoning:
A switch separates broadcast domains and Layer 2 communication per VLAN.
Without a router or Layer 3 switch, there is no communication between VLAN 10 and VLAN 20.
```

**Alternative (compact):**

```text
Same VLAN = direct communication.
Different VLANs = isolation.
```

---

## Tests

|Test|Expected|✓|
|---|---|---|
|PC0 -> PC1|Success|✅|
|PC0 -> PC2|Failure|✅|
|`show vlan brief`|Ports correctly assigned|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|VLAN|Logical separation at Layer 2.|
|Access Port|Port belongs to exactly one VLAN.|
|Isolation|Frames remain within their VLAN.|

---

## Rules / Logic

```text
Without Layer 3 routing, there is no inter-VLAN communication.
```

---

## Notes

- **Tip:** `show vlan brief` is the quickest way to check.
- **Concept:** VLANs are a fundamental tool for segmentation and security.

---

## Optional: Extensions

- Set up a router-on-a-stick.
- Establish a trunk port to a second switch.

