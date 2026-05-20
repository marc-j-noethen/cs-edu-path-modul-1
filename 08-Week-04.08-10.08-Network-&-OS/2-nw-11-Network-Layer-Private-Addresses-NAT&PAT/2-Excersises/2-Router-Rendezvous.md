# 🐍 Router Rendezvous (Routing Basics)

**Course:** Cyber Security Analyst - Network Technology | **Date:** 05 August 2025

---

## Task

**Objective:**  
Connect two /24 subnets via a router and correctly explain the connected routes.

**Requirements:**

- Configure PC-A to `192.168.1.0/24` and PC-B to `192.168.2.0/24`.
- Correctly address and enable Gi0/0 and Gi0/1 on the router.
- Successfully test pings between both PCs.
- Explain `show ip route`, focusing on the `C` routes.

- Output:

    - Correct end-device and router addresses
    - Successful ping
    - Technically correct explanation of the connected routes

---

## Solution

```text
IP configuration used:
- PC-A: 192.168.1.10 /24, gateway 192.168.1.1
- Router Gi0/0: 192.168.1.1 /24
- PC-B: 192.168.2.10 /24, gateway 192.168.2.1
- Router Gi0/1: 192.168.2.1 /24

Cisco IOS configuration:
enable
configure terminal
interface gigabitEthernet0/0
 ip address 192.168.1.1 255.255.255.0
 no shutdown
exit
interface gigabitEthernet0/1
 ip address 192.168.2.1 255.255.255.0
 no shutdown
exit
end

Expected ping result:
- PC-A -> 192.168.2.10: successful
- PC-B -> 192.168.1.10: successful
- The very first ping may fail again due to ARP, but communication will work thereafter.

Answer to question 8:
The `C` routes in `show ip route` stand for `Connected`.
They appear automatically as soon as a router interface is configured with an IP address and is administratively active (`no shutdown`).
In this case, the router learns the following directly:
- C 192.168.1.0/24 is directly connected, GigabitEthernet0/0
- C 192.168.2.0/24 is directly connected, GigabitEthernet0/1
```

**Alternative (compact):**

```text
The router does not need static routes for directly connected networks – active interfaces generate the `C` entries automatically.
```

---

## Tests

|Input 1|Input 2|Input 3|Expected|Result|✓|
|---|---|---|---|---|---|
|`192.168.1.10`|`192.168.2.10`|`Ping`|`success`|`expected`|✅|
|`Gi0/0 up`|`Gi0/1 up`|`show ip route`|`2x C route`|`expected`|✅|
|`Gateway correct`|`Mask correct`|`ARP`|`Routing works`|`yes`|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|Default Gateway|The next hop for destinations outside the local subnet.|
|Connected Route|Automatically created route for a network directly connected to the interface.|
|ARP Warm-up|The first ping may fail because MAC resolution has yet to take place.|

---

## Rules / Logic

```text
Without a correct gateway, hosts cannot leave their own subnet.
An interface must not only be configured with an address, but also set to `no shutdown`.
Directly connected networks appear automatically in the routing table.
```

---

## Notes

- **Important:** The PCs’ default gateways must point exactly to the router IP of their respective segment.
- **Observation:** `show ip route` is the quickest way to verify that both networks are recognised by the router.
- **Tip:** In Packet Tracer, always check the interface status as well as the red/yellow link colour.

---

## Optional: Extensions

- Use `tracert` or `traceroute` to verify that exactly one router hop is being used.
- Add a third network and then compare static routes.

