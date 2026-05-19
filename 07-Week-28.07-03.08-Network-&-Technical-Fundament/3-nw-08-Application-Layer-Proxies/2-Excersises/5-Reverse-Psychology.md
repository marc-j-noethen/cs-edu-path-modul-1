# Reverse Psychology (mitmproxy Reverse Proxy)

**Course:** Cyber Security Analyst – Network Technology | **Date:** 30 July 2025

---

## Task

**Objective:**  
Run `mitmproxy` as a reverse proxy and add a header using an inline script.

**Requirements:**

- Start the reverse proxy on `localhost:8080`.
- Forward every request to `http://httpbin.org`.
- Automatically set `X-Proxied-By: AwesomeStudent`.

---

## Solution

```bash
mitmdump --mode reverse: http://httpbin.org -p 8080 -s add_proxy_header.py
```

```python
# add_proxy_header.py
from mitmproxy import http


def request(flow: http.HTTPFlow) -> None:
    flow.request.headers["X-Proxied-By"] = "AwesomeStudent"
```

```text
Test:
curl http://localhost:8080/get

Expected in the JSON response under `headers`:
"X-Proxied-By": "AwesomeStudent"
```

**Alternative (compact):**

```text
Reverse proxy accepts requests locally and forwards them to the target server.
```

---

## Tests

|Item|Expected|✓|
|---|---|---|
|Reverse proxy accessible|`localhost:8080` responds|✅|
|Header set|`X-Proxied-By` appears|✅|
|Script works|Every request is modified|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|Reverse Proxy|Sits in front of the target server.|
|Inline Script|Intervenes programmatically in requests.|
|mitmdump|Non-interactive CLI variant of `mitmproxy`.|

---

## Rules / Logic

```text
Client -> Reverse Proxy -> Target server.
Script runs before forwarding.
```

---

## Notes

- **Tip:** For reproducible tests, `mitmdump` is often more convenient than the UI.
- **Concept:** Reverse proxies are central to gateway, cache and security architectures.

---

## Optional: Extensions

- Path-based routing to multiple backends.
- Additionally mark response headers.


