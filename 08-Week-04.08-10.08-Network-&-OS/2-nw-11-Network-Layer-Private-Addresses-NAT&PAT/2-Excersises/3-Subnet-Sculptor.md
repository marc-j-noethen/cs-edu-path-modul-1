# 🐍 Subnet Sculptor (Subnetting)

**Course:** Cyber Security Analyst - Network Technology | **Date:** 05 August 2025

---

## Task

**Objective:**  
Divide the network `172.16.0.0/16` into /18 subnets, calculate the first two subnets and make them operational via a router.

**Requirements:**

- Calculate Subnet 1 and Subnet 2, including the network address, host range and broadcast address.
- Explain the borrowing of bits from /16 to /18.
- Assign valid addresses from the two subnets to PC1, PC2 and router interfaces.
- Explain the role of `no shutdown` and the significance of successful pings.

- Output:

    - Complete /18 calculation for the first two networks
    - Specific host and gateway addresses
    - Cisco commands and technical analysis

---

## Solution

```text
Subnet calculation:
Initial network: 172.16.0.0/16
New mask: /18 = 255.255.192.0

Borrowed bits:
When moving from /16 to /18, 2 host bits are borrowed for subnetting.
Result:
- Number of subnets: 2^2 = 4
- Hosts per subnet: 2^(32-18) - 2 = 16382

Subnet 1:
- Network: 172.16.0.0/18
- Host range: 172.16.0.1 - 172.16.63.254
- Broadcast: 172.16.63.255

Subnet 2:
- Network: 172.16.64.0/18
- Host range: 172.16.64.1 - 172.16.127.254
- Broadcast: 172.16.127.255

Selected configuration:
- PC1: 172.16.0.10 /18, gateway 172.16.0.1
- Router Gi0/0: 172.16.0.1 /18
- PC2: 172.16.64.10 /18, Gateway 172.16.64.1
- Router Gi0/1: 172.16.64.1 /18

Router commands:
enable
configure terminal
interface gigabitEthernet0/0
 ip address 172.16.0.1 255.255.192.0
 no shutdown
exit
interface gigabitEthernet0/1
 ip address 172.16.64.1 255.255.192.0
 no shutdown
exit
end

Answer to question 2:
Successful pings show that both hosts are located in correctly configured, separate networks,
the router has a valid interface address in each network,
and the hosts correctly forward their traffic to the router for external networks.

Answer to question 3:
`no shutdown` is critical because Cisco interfaces are administratively down by default.
Without this command, a configuration exists, but the interface does not participate in traffic.
```

**Alternative (compact):**

```text
From /16 to /18 means: borrow 2 bits for subnets, get 4 subnets and keep each subnet very large.
```

---

## Tests

|Input 1|Input 2|Input 3|Expected|Result|✓|
|---|---|---|---|---|---|
|`/16 -> /18`|`2 borrowed bits`|`4 subnets`|`correct`|`yes`|✅|
|`PC1 172.16.0.10`|`PC2 172.16.64.10`|`Ping`|`success`|`expected`|✅|
|`no shutdown`|`Gi0/0+Gi0/1`|`Interface up`|`Routing active`|`yes`|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|Borrowed Bits|Host bits are used to form additional subnets.|
|Broadcast Address|The last address in a subnet; cannot be assigned to hosts.|
|Inter-Subnet Routing|A router connects logically separate IP networks with one another.|

---

## Rules / Logic

```text
The step size of a /18 in the third octet is 64.
First address = network address, last address = broadcast.
Successful routing requires a valid IP, mask, gateway and active router interfaces.
```

---

## Notes

- **Mnemonic:** /18 means 255.255.192.0 and thus 64-bit increments in the third octet.
- **Important:** Hosts and routers must use the same subnet mask within the same local subnet.
- **Tip:** Work out the subnet on paper first, then enter it into Packet Tracer.

---

## Optional: Extensions

- Calculate and document the remaining two /18 networks as well.
- Additionally, split the same source network into /20 and /24 subnets and compare them.

