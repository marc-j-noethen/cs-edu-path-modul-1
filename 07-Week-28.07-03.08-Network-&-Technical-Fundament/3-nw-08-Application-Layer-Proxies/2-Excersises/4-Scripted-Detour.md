# Scripted Detour (requests + Proxy)

**Course:** Cyber Security Analyst – Network Technology | **Date:** 30 July 2025

---

## Task

**Objective:**  
Write a Python script that uses `requests` via a local proxy.

**Requirements:**

- Set the HTTP and HTTPS proxy to `127.0.0.1:8080`.
- Retrieve `http://httpbin.org/anything`.
- Output the status code and JSON.

---

## Solution

```python
import requests

proxies = {
    "http": "http://127.0.0.1:8080",
    "https": "http://127.0.0.1:8080",
}

try:
    response = requests.get("http://httpbin.org/anything", proxies=proxies, timeout=10)
    print("Status:", response.status_code)
    print(response.json())
except requests.RequestException as exc:
    print("Request failed:", exc)
```

**Alternative (compact):**

```text
`requests` receives proxies as a dictionary.
```

---

## Tests

|Item|Expected|✓|
|---|---|---|
|Proxy set|Request appears in `mitmproxy`|✅|
|Status code returned|Yes|✅|
|JSON readable|Yes|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|`requests`|Popular Python library for HTTP.|
|Proxy dictionary|Defines the proxy per scheme.|
|Error handling|Intercepts network or proxy errors.|

---

## Rules / Logic

```text
Without proxy -> direct connection.
With proxy dictionary -> request runs via `mitmproxy`.
```

---

## Notes

- **Tip:** For HTTPS, the proxy certificate must be trusted.
- **Concept:** Scripts and proxies can be combined effectively for test automation.

---

## Optional: Extensions

- Output response headers separately.
- Print JSON more neatly with `indent=2`.

