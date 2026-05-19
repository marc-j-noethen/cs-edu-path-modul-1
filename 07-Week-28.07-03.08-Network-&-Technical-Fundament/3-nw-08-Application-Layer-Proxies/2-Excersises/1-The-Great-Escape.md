# The Great Escape (Proxies)

**Course:** Cyber Security Analyst – Network Technology | **Date:** 30 July 2025

---

## Task

**Objective:**  
Demonstrate that a web proxy can change the source IP address visible to the outside world.

**Requirements:**

- Retrieve your own public IP directly.
- Access the same page via a web proxy.
- Explain the difference.

---

## Solution

```text
Sample answer:
Yes, the displayed IP address is usually different.
Without a proxy, `ifconfig.me` sees your real public IP.
With a web proxy, the destination server sees the proxy server’s IP address because the proxy sends the request on your behalf.
```

**Alternative (concise):**

```text
The proxy becomes the visible sender of the request.
```

---

## Tests

|Condition|Expected|✓|
|---|---|---|
|Direct call|own public IP|✅|
|Proxy call|different visible IP|✅|
|Explanation|Proxy becomes new exit point|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|Forward proxy|Receives requests and forwards them.|
|Exit IP|The sender IP perceived by the destination server.|
|Web proxy|Browser traffic is sent via an intermediary.|

---

## Rules / Logic

```text
The destination server always sees the last network sender of the request.
With a proxy, this is not the client itself, but the proxy.
```

---

## Notes

- **Important:** Free proxies are often slow and insecure.
- **Tip:** Never send sensitive data via third-party web proxies.

---

## Optional: Extensions

- Compare proxies with VPNs.
- Examine HTTP headers such as `Via` or `X-Forwarded-For`.

