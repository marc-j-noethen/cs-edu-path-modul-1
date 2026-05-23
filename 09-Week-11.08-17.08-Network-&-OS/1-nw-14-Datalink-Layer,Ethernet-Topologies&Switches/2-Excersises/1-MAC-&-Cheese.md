# MAC and Cheese (Ethernet)

**Course:** Cyber Security Analyst – Network Technology | **Date:** 11 August 2025

---

## Task

**Objective:**  
Read the source and destination MAC addresses of a local ping packet.

**Requirements:**

- Ping the router.
- Check the Echo Request and Echo Reply in Wireshark.
- Explain the address swap.

---

## Solution

```text
Sample response:
Echo Request:
- Source MAC = MAC address of your own computer
- Destination MAC = MAC address of the local router

Echo Reply:
- Source MAC = MAC address of the router
- Destination MAC = MAC address of your own computer

How have the addresses changed?
They have been swapped for the return path.
This is correct because the reply now travels from the router to your own computer.
```

**Alternative (compact):**

```text
Outbound: Client -> Router.
Return: Router -> Client.
```

---

## Tests

|Packet|Expected|✓|
|---|---|---|
|Echo Request|own MAC -> Router MAC|✅|
|Echo Reply|Router MAC -> own MAC|✅|
|Comparison|Change of direction visible|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|Source MAC|Physical sender address in the local segment.|
|Destination MAC|Next local recipient in the Ethernet frame.|
|ICMP Echo|Ping message at IP level, carried by Ethernet.|

---

## Rules / Logic

```text
Ethernet addresses apply only to the local hop.
In a reply, the source and destination are reversed.
```

---

## Notes

- **Important:** The exact MAC values depend on the network.
- **Tip:** Check the `Ethernet II` section in Wireshark.

---

## Optional: Extensions

- Test the same with a different local host.
- Compare broadcast and multicast MACs.

