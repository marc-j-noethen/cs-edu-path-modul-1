# Capturing Names (DNS in Wireshark)

**Course:** Cyber Security Analyst – Network Technology | **Date:** 29 July 2025

---

## Task

**Objective:**  
Correctly map and interpret DNS queries and responses in Wireshark.

**Requirements:**

- Record `dig` lookups.
- Explain ports, IDs, CNAME behaviour and error codes.
- Recognise the differences between A, AAAA and NXDOMAIN.

---

## Solution

```text
1. Linking the request and response:
The request and response belong together via the DNS Transaction ID.
Source/destination, port 53 and the queried name also match.

2. Ports:
Request: Source port = ephemeral client port, destination port = 53
Response: Source port = 53, destination port = the same ephemeral client port
The port reverses because the server is responding to the client’s request.

3. CNAME chain:
When a CNAME response provides a canonical name, the client often queries the final A or AAAA record directly.
The reason: A CNAME provides only the alias, not the actual IP address.

4. Comparison of A vs. AAAA:
The response types are clearly distinguished by the record type:
A = IPv4, AAAA = IPv6.

5. Error handling:
If a domain does not exist, the DNS header displays the response code `NXDOMAIN`.
The field is called `Response Code (RCODE)`.
```

**Alternative (compact):**

```text
DNS = Request, matching ID, matching response.
NXDOMAIN = Name does not exist.
```

---

## Tests

|Item|Expected|✓|
|---|---|---|
|ID matching|Request/response can be linked|✅|
|Ports|ephemeral -> 53 / 53 -> ephemeral|✅|
|Error code|NXDOMAIN detected|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|Transaction ID|Short ID for mapping DNS messages.|
|Ephemeral port|Temporary client port for the request.|
|RCODE|Field for success or error of the DNS server.|

---

## Rules / Logic

```text
CNAME resolves to an alias, not an end IP.
A = IPv4.
AAAA = IPv6.
NXDOMAIN = Domain name does not exist.
```

---

## Notes

- **Tip:** Always expand the `Domain Name System` section in the packet details area.
- **Concept:** DNS over UDP is small, fast and easy to analyse.

---

## Optional: Extensions

- Compare DNS over TCP with large responses.
- Observe caching effects during repeated lookups.
