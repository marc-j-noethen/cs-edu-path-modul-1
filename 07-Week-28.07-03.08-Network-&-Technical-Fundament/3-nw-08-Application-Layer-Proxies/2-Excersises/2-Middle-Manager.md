# Middle Manager (mitmproxy Forward Proxy)

**Course:** Cyber Security Analyst – Network Technology | **Date:** 30 July 2025

---

## Task

**Objective:**  
Use `mitmproxy` to intercept a local proxy request and understand why `httpbin` can still see the real public IP.

**Requirements:**

- Start `mitmproxy --mode regular --listen-port 8080`.
- Send `curl` via `127.0.0.1:8080`.
- Explain the `origin` field.

---

## Solution

```bash
mitmproxy --mode regular --listen-port 8080
curl -x http://127.0.0.1:8080 http://httpbin.org/get
```

```text
`origin` still shows the connection’s real public IP.
Reason: The proxy is running locally on the same machine or behind the same NAT connection.
It simply intercepts the request and then forwards it itself via your normal internet connection.
For `httpbin`, the connection therefore still comes from your real public IP.
```

**Alternative (compact):**

```text
A local forward proxy changes the point of view locally, but does not automatically change the internet exit IP.
```

---

## Tests

|Item|Expected|✓|
|---|---|---|
|Request visible in `mitmproxy`|Yes|✅|
|`origin` read|Public IP visible|✅|
|Explanation correct|Local forwarding, no other exit|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|Local Proxy|Runs on your own computer and intercepts requests.|
|Origin|Source IP observed by `httpbin`.|
|NAT|Multiple local processes often share the same public IP.|

---

## Rules / Logic

```text
Local proxy ≠ external exit proxy.
As long as the same internet connection is used, the visible exit IP remains the same.
```

---

## Notes

- **Tip:** For a genuine IP change, an external proxy or VPN is required.
- **Concept:** `mitmproxy` is primarily an analysis tool.

---

## Optional: Extensions

- Test HTTPS with an installed mitmproxy certificate.
- Compare request and response headers directly.

