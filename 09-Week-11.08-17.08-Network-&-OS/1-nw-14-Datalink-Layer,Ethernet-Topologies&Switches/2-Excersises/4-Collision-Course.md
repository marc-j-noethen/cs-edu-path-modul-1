# 🐍 Collision Course (Ethernet Topologies)

**Course:** Cyber Security Analyst – Network Technology | **Date:** 11 August 2025

---

## Task

**Objective:**  
Demonstrate in Packet Tracer why simultaneous transmissions on a hub lead to collisions, but not on a switch.

**Requirements:**

- Set up a small hub scenario and a small switch scenario, each with at least two PCs.
- Induce simultaneous traffic in the simulation.
- Describe the behaviour of the hub scenario.
- Explain the behaviour of the switch scenario using collision domains.

- Output:

    - brief description of both simulation setups
    - observed differences between the hub and the switch
    - explanation of collision domains and Layers 1/2

---

## Solution

```text
Simulation setup:
- Hub network: two to three PCs connected to a hub, all on the same IP network
- Switch network: the same number of PCs connected to a switch, also on the same IP network
- For simultaneous traffic, parallel pings or multiple Simple PDUs were initiated in simulation mode

Observations in the hub network:
- Collisions occur when two hosts transmit almost simultaneously.
- Frames are repeated to all ports.
- This leads to backoff / retransmissions and consequently to reduced efficiency.

Observations in the switch network:
- No visible collisions between separate switch ports during the same test.
- The switch learns MAC addresses and forwards frames specifically to the required port only.
- Simultaneous transmissions can take place in parallel on different ports.

Why is this the case?
- A hub operates at Layer 1 and forms exactly one shared collision domain for all connected hosts.
- A switch operates at Layer 2 and separates collision domains on a per-port basis.
- Therefore, simultaneous transmissions collide on the hub, whilst a switch neatly separates the same transmissions.
```

**Alternative (compact):**

```text
Hub = a single shared collision domain. Switch = separate collision domains per port.
```

---

## Tests

|Input 1|Input 2|Input 3|Expected|Result|✓|
|---|---|---|---|---|---|
|`Hub`|`simultaneous transmission`|`simulation`|`collision visible`|`yes`|✅|
|`Switch`|`simultaneous transmission`|`simulation`|`no collision`|`yes`|✅|
|`MAC learning`|`targeted forwarding`|`Switch`|`correct`|`yes`|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|Collision domain|Area in which simultaneous transmissions can collide.|
|Hub|Physical Layer 1 repeater without intelligent forwarding logic.|
|Switch|Layer 2 device with MAC learning and targeted frame forwarding.|

---

## Rules / Logic

```text
Collisions only occur where the medium and collision domain are shared.
Switching reduces collisions through port segmentation.
MAC learning is the reason why a switch does not have to constantly flood the network.
```

---

## Notes

- **Important:** The task requires an observation in simulation mode, not just theory.
- **Observation:** With a hub, broadcast-like behaviour is much more pronounced, even with unicast.
- **Tip:** In Packet Tracer, run the simulation at a slow speed so that collision events remain visible.

---

## Optional: Extensions

- Compare the same scenario using full-duplex versus half-duplex.
- Additionally, observe broadcast and unicast traffic separately.

