# Local vs. Remote Rendezvous (ARP)

**Course:** Cyber Security Analyst – Network Technology | **Date:** 12 August 2025

---

## Task

**Objective:**  
To understand that, for remote destinations, it is the gateway rather than the remote host that is sought via ARP.

**Requirements:**

- Observe ARP when pinging the gateway.
- Observe ARP when pinging a remote IP.
- Compare the destination IP in the ARP payload.

---

## Solution

```text
Step 4 (Ping to the gateway):
- Destination IP in the ARP request = GW_IP

Step 7 (Ping to the remote IP):
- Destination IP in the ARP request = also GW_IP

Why?
ARP only resolves the MAC address of the next local hop.
For a destination outside the local network, this is not the remote IP itself,
but the router or the default gateway.
The computer therefore needs the gateway’s MAC address to send the IP packet there.
```

**Alternative (compact):**

```text
Remote destination at IP level, gateway destination at MAC level.
```

---

## Tests

|Scenario|ARP destination IP|✓|
|---|---|---|
|Ping to gateway|GW_IP|✅|
|Ping to remote IP|GW_IP|✅|
|Explanation|Next-hop principle understood|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|ARP|Resolves local IP-to-MAC mapping.|
|Default Gateway|Next hop for external networks.|
|Local vs. Remote|Only local destinations are addressed directly via ARP.|

---

## Rules / Logic

```text
ARP only operates within the local broadcast domain.
Remote destinations are never queried directly via ARP.
```

---

## Notes

- **Tip:** Delete the gateway entry before each test, otherwise you will not see a new ARP request.
- **Concept:** ARP thinks locally, routing thinks globally.

---

## Optional: Extensions

- Compare the same for a local destination on the same subnet.
- Document the ARP cache before and after the ping.

