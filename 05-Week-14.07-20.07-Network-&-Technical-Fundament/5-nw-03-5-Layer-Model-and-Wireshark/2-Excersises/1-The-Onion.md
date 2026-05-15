# The Onion (5-Layer Model & Wireshark)

**Course:** Cyber Security Analyst – Network Technology | **Date:** 18 July 2025

---

## Task

**Objective:**  
Map an HTTP GET packet in Wireshark to the layers of the 5-layer model.

**Requirements:**

- Visit `http://neverssl.com`.
- Find the GET request in Wireshark.
- Describe the Data Link, Network, Transport and Application layers.
- Name the protocols and key data.

---

## Solution

```text
Data Link Layer:
In typical home networks, you will see Ethernet II here.
The Type value usually shows IPv4 (0x0800).

Network Layer:
Protocol: IPv4
Source IP: the local client IP
Destination IP: the destination IP of neverssl.com

Transport Layer:
Protocol: TCP
Source Port: a temporary ephemeral port of the client
Destination Port: 80

Application Layer:
Protocol: HTTP
Request: GET / HTTP/1.1
Resource: /
```

**Alternative (compact):**

```text
Ethernet -> IPv4 -> TCP -> HTTP GET /
```

---

## Tests

|Scenario|Expected|Result|✓|
|---|---|---|---|
|Apply HTTP filter|GET packet visible|correct|✅|
|Open packet details|Layers clearly separated|correct|✅|
|Examine GET request|`GET / HTTP/1.1` visible|correct|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|Encapsulation|Each layer wraps its own headers around the payload.|
|Ephemeral Port|Temporary client port for outgoing connections.|
|HTTP GET|Request for a resource at the application layer.|

---

## Rules / Logic

```text
The Link Layer transports frames.
The Network Layer transports IP packets.
The Transport Layer transports TCP segments.
The Application Layer contains the HTTP request.
```

---

## Notes

- **Concept:** A packet is not a single entity, but rather several layers stacked on top of one another.
- **Syntax:* * In Wireshark, expand the Ethernet, IP, TCP and HTTP sections.
- **Order is important:**
    1. Start capture
    2. Load the target page
    3. Filter for GET requests
- **Edge cases:**
    - With HTTPS, HTTP would not be visible in plain text.
    - With Wi-Fi, the Link Layer looks different.
    - Redirects can generate further requests.
- **Tip:** `neverssl.com` is useful because HTTP remains deliberately unencrypted there.

---

## Optional: Extensions

- Analyse the response packet.
- Also examine MAC addresses.
- Compare this with HTTPS.

