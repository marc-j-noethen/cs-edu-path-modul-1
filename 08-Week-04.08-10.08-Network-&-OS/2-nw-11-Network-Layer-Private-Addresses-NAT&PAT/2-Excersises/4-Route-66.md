# 🐍 Route 66 (Static Routing)

**Course:** Cyber Security Analyst - Network Technology | **Date:** 05 August 2025

---

## Task

**Objective:**  
Connect three routers with static routes so that PC-X, PC-Y and PC-Z can communicate fully with one another.

**Requirements:**

- Configure all PC and router interfaces in accordance with the address plan.
- Use sensible /30 links between routers and explain the address advantage.
- Set the necessary static routes on RouterA, RouterB and RouterC.
- Logically trace the packet path from PC-X to PC-Z.

- Output:

    - Static routes for all three routers
    - Answers to the analysis questions
    - Justified data path through the topology

---

## Solution

```text
Answer to Question 1:
A /30 point-to-point connection provides exactly 2 usable host addresses.
This saves IP addresses because no larger networks are required for a router-to-router link.

Static routes on RouterA:
ip route 10.1.2.0 255.255.255.0 192.168.12.2
ip route 10.1.3.0 255.255.255.0 192.168.12.2

Static routes on RouterB:
ip route 10.1.1.0 255.255.255.0 192.168.12.1
ip route 10.1.3.0 255.255.255.0 192.168.23.2

Static routes on RouterC:
ip route 10.1.1.0 255.255.255.0 192.168.23.1
ip route 10.1.2.0 255.255.255.0 192.168.23.1

Answer to question 2:
RouterA requires routes to all networks that are not directly connected:
- 10.1.2.0/24
- 10.1.3.0/24
The appropriate next hop in each case is 192.168.12.2 (RouterB).

Answer to question 3:
RouterB is directly connected to the networks 192.168.12.0/30, 10.1.2.0/24 and 192.168.23.0/30.
It therefore does not need a static route to Network Z, but it does need one to the remote LANs:
- 10.1.1.0/24 via 192.168.12.1
- 10.1.3.0/24 via 192.168.23.2

Answer to question 4:
When PC-X pings PC-Z:
- RouterA recognises the destination 10.1.2.0/24 as a remote network and uses the static route via 192.168.12.2.
- RouterB recognises 10.1.2.0/24 as a directly connected network on Gi0/1 and forwards the packet directly to PC-Z.

Expected reachability:
- PC-X -> PC-Y: successful
- PC-X -> PC-Z: successful
- PC-Y -> PC-Z: successful
```

**Alternative (compact):**

```text
With static routing, each router only needs to know which remote networks exist and which next hop reaches them.
```

---

## Tests

|Input 1|Input 2|Input 3|Expected|Result|✓|
|---|---|---|---|---|---|
|`RouterA`|`2 static routes`|`B as next hop`|`correct`|`yes`|✅|
|`RouterB`|`X+Y networks`|`2 static routes`|`correct`|`yes`|✅|
|`PC-X`|`PC-Y/PC-Z`|`Ping`|`success`|`expected`|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|Static Route|Manually configured path to a remote network.|
|Point-to-Point /30|Small link networks with exactly two host addresses for router interfaces.|
|Next Hop|The address of the immediate router to which a packet is forwarded.|

---

## Rules / Logic

```text
A router does not need a static route to directly connected networks.
Every static route points to a destination network plus a valid next hop.
Without a return route, even an apparently correct outbound route is worthless.
```

---

## Notes

- **Important:** RouterB is a transit device; this is precisely where missing routes are noticed most quickly.
- **Observation:** `show ip route` immediately shows which networks are connected and which are static.
- **Tip:** Always consider both directions of a connection, not just the outbound route.

---

## Optional: Extensions

- Recreate the same scenario using a dynamic routing protocol such as OSPF.
- Simulate a link failure and observe the behaviour of static routes.

