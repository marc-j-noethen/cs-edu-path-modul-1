# 🐍 Wired (Cable Selection)

**Course:** Cyber Security Analyst - Network Technology | **Date:** 15 August 2025

---

## Task

**Objective:**  
Select the appropriate cabling for a campus scenario based on distance and EMI exposure.

**Requirements:**

- Assess A-B (80 m) and A-C (250 m, EMI) differently.
- Connect intra-building PCs appropriately to their switches.
- Establish connectivity within the shared IP network.
- Justify the cable selection for both inter-building links.

- Output:

    - Suitable link type for Building A-B
    - Suitable link type for Building A-C
    - Brief justification regarding distance and EMI

---

## Solution

```text
Selected cables:
- Building A -> Building B (80 m): Copper cross-over between the switches
- Building A -> Building C (250 m, EMI environment): Fibre connection between the switches
- PCs -> local switch: Copper straight-through

Justification:
1. A-B at 80 m:
   80 metres fall within the standard 100-metre limit for copper Ethernet.
   At this distance, copper is viable for a standard campus link without significant sources of interference.

2. A-C at 250 m and EMI:
   250 metres is well above the typical copper limit for Ethernet.
   Furthermore, fibre optic cable is immune to electromagnetic interference.
   Therefore, fibre is the technically correct choice here.

Ping result:
- Within Building B: successful
- Within Building C: successful
- Between Building B and Building C: successful
```

**Alternative (compact):**

```text
Short distances with low interference can often still be managed with copper; long distances with high EMI levels call for fibre optic.
```

---

## Tests

|Input 1|Input 2|Input 3|Expected|Result|✓|
|---|---|---|---|---|---|
|`80 m`|`switch-switch`|`Copper`|`acceptable`|`yes`|✅|
|`250 m + EMI`|`switch-switch`|`Fibre`|`preferred`|`yes`|✅|
|`PC on the left`|`straight-through`|`same subnet`|`pings work`|`expected`|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|Distance Limit|Copper Ethernet has typical range limits; fibre optic has significantly more leeway.|
|EMI|Electromagnetic interference affects copper, but not fibre optic cables in the same way.|
|Cable Type Choice|The correct choice of medium is a combination of distance, interference environment and device type.|

---

## Rules / Logic

```text
Copper Ethernet cannot be extended indefinitely.
Fibre optic is almost always the more robust choice for long distances and in the presence of EMI.
The connection from the end device to the switch remains straight-through by default in Packet Tracer.
```

---

## Notes

- **Important:** The task asks for the most technically appropriate cable, not just any cable that works.
- **Tip:** In Packet Tracer, the different cables are also visually distinct – this helps when taking a screenshot.
- **Observation:** The 250-metre link in particular is the clear key factor in this task.

---

## Optional: Extensions

- Compare multimode and single-mode fibre optically in concept.
- Additionally, plan redundancy paths and Spanning Tree as an extension.

