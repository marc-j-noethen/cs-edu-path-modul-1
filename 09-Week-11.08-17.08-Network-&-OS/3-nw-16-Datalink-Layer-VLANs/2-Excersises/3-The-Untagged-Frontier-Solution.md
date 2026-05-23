# 🐍 The Untagged Frontier (Native VLAN)

**Course:** Cyber Security Analyst - Network Technology | **Date:** 13 August 2025

---

## Task

**Objective:**  
Correctly configure native VLANs on trunks, explain a native VLAN mismatch and identify the security risk.

**Requirements:**

- Explain the default native VLAN without special configuration.
- Set up VLAN 77 as the native VLAN on both sides for untagged traffic.
- Test and explain the effects of a mismatch between VLAN 77 and VLAN 1.
- Identify a realistic attack scenario.

- Output:

    - Trunk commands for correct Native VLAN operation
    - Correct success/failure predictions for the pings
    - Specific security justification

---

## Solution

```text
Task 1 - Default state:
Cisco switches use VLAN 1 as the Native VLAN by default.
As long as nothing is changed on the trunk, VLAN 10 frames remain tagged and VLAN 77 frames also remain tagged if VLAN 77 is not set as the native VLAN.
Therefore, communication in VLAN 10 functions normally after a clean VLAN/trunk configuration,
whilst VLAN 77 is not treated as ‘untagged as native’.

Task 2 – Correct configuration with VLAN 77 as native:
interface fa0/24
 switchport mode trunk
 switchport trunk native vlan 77
 switchport trunk allowed vlan 10,77

Why does this work?
- VLAN 77 is transported untagged on the trunk because it is defined as the native VLAN.
- VLAN 10 remains tagged.
- Therefore, PC2 and PC4 (VLAN 77) can communicate via untagged traffic, whilst PC1 and PC3 (VLAN 10) remain properly tagged.

Task 3 - Native VLAN Mismatch:
- SwitchA native VLAN 77
- SwitchB native VLAN 1

Expected / observed results:
- PC1 (VLAN 10) -> PC3 (VLAN 10): continues to work because VLAN 10 is transmitted tagged.
- PC2 (VLAN 77) -> PC4 (VLAN 77): fails because untagged frames from SwitchA are sorted into VLAN 1 on SwitchB, not into VLAN 77.

Security risk:
An attacker can exploit a native VLAN mismatch for VLAN hopping or the misassignment of untagged traffic.
Double tagging is particularly critical: a frame can be designed so that the first tag is removed on the native VLAN link whilst the second tag remains effective in the destination switch.
This allows an attacker, under certain conditions, to infiltrate a VLAN that is actually isolated.
```

**Alternative (compact):**

```text
Native VLAN means: untagged trunk traffic ends up exactly there – and that is precisely why a mismatch is dangerous.
```

---

## Tests

|Input 1|Input 2|Input 3|Expected|Result|✓|
|---|---|---|---| ---|---|
|`native 77 / native 77`|`VLAN 77 traffic`|`untagged`|`success`|`expected`|✅|
|`native 77 / native 1`|`VLAN 77 traffic`|`untagged`|`fail`|`expected`|✅|
|`VLAN 10 tagged`|`Mismatch`|`same tag`|`success`|`expected`|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|Native VLAN|The VLAN whose frames are transported untagged on an 802.1Q trunk.|
|Mismatch|Two trunk ends interpret the same untagged traffic differently.|
|VLAN Hopping|A technique whereby an attacker gains unauthorised access to other VLANs.|

---

## Rules / Logic

```text
Native VLAN settings must be identical at both ends.
Tagged VLANs often continue to behave normally in the event of a native mismatch.
Untagged traffic is dangerous precisely where interpretation and expectation diverge.
```

---

## Notes

- **Important:** The task deliberately tests the difference between tagged VLAN-10 traffic and untagged native VLAN traffic.
- **Tip:** `show interfaces trunk` displays native VLANs and allowed VLANs immediately.
- **Security:** A mismatch is not only an availability issue but also a segmentation risk.

---

## Optional: Extensions

- Monitor Syslog/CDP alerts for Native VLAN mismatches.
- Additional exercise: explicitly define an unused VLAN as a Native VLAN and justify your choice.

