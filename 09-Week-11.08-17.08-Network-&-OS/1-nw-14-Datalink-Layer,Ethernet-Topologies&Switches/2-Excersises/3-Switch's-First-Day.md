# Switch's First Day (Switch Learning)

**Course:** Cyber Security Analyst – Network Technology | **Date:** 11 August 2025

---

## Task

**Objective:**  
Demonstrate how a switch learns source MAC addresses and populates its MAC table.

**Requirements:**

- Connect three PCs to a switch.
- Trigger pings from PC0 to PC1 and PC2.
- Explain `show mac address-table`.

---

## Solution

```text
Typical table after the pings:
- MAC of PC0 -> Fa0/1
- MAC of PC1 -> Fa0/2
- MAC of PC2 -> Fa0/3

How does the switch learn PC0?
It reads the source MAC from an incoming frame from PC0 and notes: this MAC arrived via Fa0/1.

How does the switch learn PC1?
When PC1 responds (e.g. to an ARP or ping), the switch sees the source MAC of PC1 on Fa0/2 and stores it there.

Important:
A switch always learns MAC addresses from the source address of incoming frames, not from the destination address.
```

**Alternative (compact):**

```text
Switches learn from what comes in – more precisely: from the source MAC.
```

---

## Tests

|Item|Expected|✓|
|---|---|---|
|Fa0/1|MAC of PC0 learnt|✅|
|Fa0/2|MAC of PC1 learned|✅|
|Fa0/3|MAC of PC2 learned|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|MAC table|Maps known MAC addresses to ports.|
|Flooding|Unknown destinations are sent to multiple ports.|
|Learning|Switch stores the source MAC of the incoming frame.|

---

## Rules / Logic

```text
Unknown destination -> Flooding.
Response frame returns -> Source MAC is learned.
```

---

## Notes

- **Tip:** Before the first traffic arrives, the table is often almost empty.
- **Concept:** It is only through traffic that the switch becomes "intelligent".

---

## Optional: Extensions

- Observe MAC ageing.
- Compare behaviour for broadcast and unknown unicast.

