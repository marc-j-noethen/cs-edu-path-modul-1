# 🐍 The VLAN Voyager (VLAN Trunks)

**Course:** Cyber Security Analyst - Network Technology | **Date:** 13 August 2025

---

## Task

**Objective:**  
Connect two switches via a trunk so that the same VLANs can communicate across switches.

**Requirements:**

- Create VLAN 10 `Sales` and VLAN 20 `Tech` on Switch1 as well.
- Assign appropriate addresses to PC4 in VLAN 10 and PC5 in VLAN 20.
- Configure Fa0/24 on both switches as a trunk for VLANs 10 and 20.
- Demonstrate a successful ping within the same VLAN and a failed ping across VLAN boundaries.

- Output:

    - Trunk configuration on both switches
    - Expected ping results for same vs. different VLANs
    - Brief explanation of the behaviour

---

## Solution

```text
Switch0:
vlan 10
 name Sales
vlan 20
 name Tech
interface fa0/24
 switchport mode trunk
 switchport trunk allowed vlan 10,20

Switch1:
vlan 10
 name Sales
vlan 20
 name Tech
interface fa0/1
 switchport mode access
 switchport access vlan 10
interface fa0/2
 switchport mode access
 switchport access vlan 20
interface fa0/24
 switchport mode trunk
 switchport trunk allowed vlan 10,20

New PCs:
- PC4: 192.168.10.12/24 in VLAN 10
- PC5: 192.168.20.12/24 in VLAN 20

Expected tests:
- PC0 (VLAN 10) -> PC4 (VLAN 10): successful
- PC2 (VLAN 20) -> PC5 (VLAN 20): successful
- PC0 (VLAN 10) -> PC5 (VLAN 20): failed

Why?
The trunk carries frames from both VLANs between the switches.
However, the segmentation remains in place; without Layer 3 routing, there is no communication between VLAN 10 and VLAN 20.
```

**Alternative (compact):**

```text
A trunk connects identical VLANs across multiple switches, but does not remove the VLAN separation.
```

---

## Tests

|Input 1|Input 2|Input 3|Expected|Result|✓|
|---|---| ---|---|---|---|
|`Fa0/24 trunk`|`VLAN 10,20`|`show interfaces trunk`|`visible`|`yes`|✅|
|`VLAN 10`|`PC0 -> PC4`|`Ping`|`success`|`expected`|✅|
|`VLAN 10 -> 20`|`PC0 -> PC5`|`Ping`|`fail`|`expected`|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|Trunk Port|Transports multiple VLANs between switches over a single link.|
|Access Port|Transports exactly one VLAN for an end device.|
|Segmentation|VLANs logically separate broadcast domains and Layer 2 communication from one another.|

---

## Rules / Logic

```text
Same VLAN over trunk = communication possible.
Different VLANs without routing = communication not possible.
`show interfaces trunk` checks the trunk side faster than the GUI.
```

---

## Notes

- **Important:** Both sides of the trunk must be configured identically.
- **Tip:** Set up VLANs and access ports first, then establish the trunk.
- **Observation:** A successful same VLAN across two switches is the key proof of this task.

---

## Optional: Extensions

- Set up a Router-on-a-Stick for inter-VLAN routing as a follow-up exercise.
- Deliberately set the native VLAN and allowed VLAN list incorrectly and observe the error.

