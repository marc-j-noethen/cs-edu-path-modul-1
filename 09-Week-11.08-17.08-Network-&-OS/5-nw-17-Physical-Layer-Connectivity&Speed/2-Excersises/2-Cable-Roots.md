# 🐍 Cable Roots (Physical Layer)

**Course:** Cyber Security Analyst - Network Technology | **Date:** 15 August 2025

---

## Task

**Objective:**  
Describe and correctly identify the cables and connectors in a typical home network installation.

**Requirements:**

- Identify the ISP connection to the router/modem.
- Describe local end-device cabling via Ethernet.
- Name connector types and possible Cat markings.
- Formulate the documentation as a clearly legible sample submission.

- Output:

    - Description of the internet connection
    - Description of the RJ45 LAN cables
    - Reference to Cat markings

---

## Solution

```text
Sample observation of a typical home installation:

1. Internet connection:
- Type: Coaxial cable from the wall socket to the cable modem / router
- Connector: F-type screw connector
- Function: routes the ISP connection to the modem or combined device

2. Internal LAN cabling:
- Type: Ethernet patch cable
- Connector: RJ45
- Connections:
  - Router -> Desktop PC
  - Router -> Switch / Access Point / Console (if applicable)

3. Markings:
- Often visible: `Cat 5e`, `Cat 6` or `Cat 6a`
- Example: `Cat 6 UTP`

Brief summary:
A typical home installation uses a WAN connection from the ISP (often coaxial, DSL or fibre optic)
and, within the local network, almost always RJ45-based Ethernet patch cables for wired devices.

Note:
This task is context-dependent.
If your own installation uses fibre optic or DSL instead of coax, for example, the type and connector must be replaced accordingly.
```

**Alternative (compact):**

```text
The ISP connection and the local Ethernet are two different things: WAN in, RJ45 LAN out in the home.
```

---

## Tests

|Input 1|Input 2|Input 3|Expected|Result|✓|
|---|---|---|---|---|---|
|`WAN cable`|`connector`|`router`|`identifiable`|`typical`|✅|
|`LAN patch cable`|`RJ45`|`device link`|`identifiable`|`typical`|✅|
|`Cat marking`|`cable jacket`|`readable`|`documentable`|`typical`|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|Coax / DSL / Fibre|Possible physical media for the provider connection.|
|RJ45|The standard connector type for Ethernet patch cables in home and office LANs.|
|Category Rating|Cat standards describe the performance and bandwidth of twisted-pair cables.|

---

## Rules / Logic

```text
Not every home connection is Ethernet right up to the wall.
The ISP connection and the internal LAN may use different media and connectors.
Photos and labels are the actual evidence required for this task.
```

---

## Notes

- **Important:** The answer above is a technically correct example, not a requirement for every home.
- **Tip:** With fibre optics, a thin fibre optic cable or an ONT would be expected rather than coaxial cable.
- **Observation:** Cat markings are often only printed in small letters on the sheath and are best read in good light.

---

## Optional: Extensions

- Addition: Distinguish between UTP and STP on the cable sheath itself.
- Compare coaxial, DSL and fibre home connections in a table.


