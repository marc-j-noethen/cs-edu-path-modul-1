# VPN Voyage (VPN & Tunneling)

**Course:** Cyber Security Analyst – Network Technology | **Date:** 07 August 2025

---

## Task

**Objective:**  
Investigate the effect of a VPN on the public IP address and on the visibility of data traffic.

**Requirements:**

- Compare the public IP address before and after establishing a VPN connection.
- Examine the Wireshark capture during an active VPN session.
- Evaluate protocols and payload data.

---

## Solution

```text
Sample answer:
- The public IP address changes after the connection is established.
- The approximate geolocation typically matches the selected VPN server.
- In Wireshark, you will mainly see encrypted tunnel traffic, often via UDP or a VPN-specific transport protocol.
- The payload is not readable, but appears random or encrypted.

Technical conclusion:
The VPN tunnel encapsulates or encrypts the actual application traffic, so that local captures no longer show the traffic content in plain text.
```

**Alternative (compact):**

```text
VPN changes the visible exit point and protects the content of the traffic.
```

---

## Tests

|Item|Expected|✓|
|---|---|---|
|IP before/after|different|✅|
|Server location|roughly matches the VPN server|✅|
|Payload|unreadable|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|VPN|Virtual tunnel to a remote exit point.|
|Exit IP|Address of the VPN server visible to the outside world.|
|Encryption|Hides payload data from local observers.|

---

## Rules / Logic

```text
Browser traffic goes through the tunnel.
The destination server sees the VPN server’s IP, not the original client IP.
```

---

## Notes

- **Important:** Specific IPs and protocols depend on the VPN provider and client.
- **Tip:** Filter by the connection to the VPN server, not by websites.

---

## Optional: Extensions

- Switch the VPN on and off and compare the same request.
- Check DNS behaviour with and without the VPN.

