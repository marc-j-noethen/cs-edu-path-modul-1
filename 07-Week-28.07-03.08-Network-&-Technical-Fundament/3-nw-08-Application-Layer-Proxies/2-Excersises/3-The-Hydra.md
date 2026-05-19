# The Hydra (mitmproxy Header Injection)

**Course:** Cyber Security Analyst – Network Technology | **Date:** 30 July 2025

---

## Task

**Objective:**  
Modify a request in the proxy and verify that the new header appears in the target system.

**Requirements:**

- Send `curl` via `mitmproxy`.
- Insert `X-Cyber-Trainee: YourName`.
- Check the response from `httpbin`.

---

## Solution

```text
Expected result:
After inserting the header, the JSON response from `http://httpbin.org/get` shows, for example, in the `headers` field:

"X-Cyber-Trainee": "YourName"

This proves that the request was successfully modified in the proxy before it reached the target server.
```

**Alternative (compact):**

```text
Proxy modifies request -> Server reflects the modified header back.
```

---

## Tests

|Item|Expected|✓|
|---|---|---|
|Header inserted|`X-Cyber-Trainee` present|✅|
|Request forwarded|Response comes from `httpbin`|✅|
|Manipulation confirmed|Header visible in JSON|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|Request Interception|Request is intercepted before being forwarded.|
|Header Injection|New HTTP header is inserted.|
|Echo API|Target server displays the received header.|

---

## Rules / Logic

```text
If the server returns the header, the manipulation worked before the request was sent.
```

---

## Notes

- **Tip:** `httpbin` is ideal for precisely this kind of testing.
- **Concept:** Proxies can not only observe requests, but also modify them.

---

## Optional: Extensions

- Manipulate response headers as well.
- Test multiple custom headers in a single run.

