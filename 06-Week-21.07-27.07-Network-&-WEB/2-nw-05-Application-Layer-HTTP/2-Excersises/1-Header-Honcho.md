# Header Honcho (HTTP)
**Course:** Cyber Security Analyst – Network Technology | **Date:** 22 July 2025

---

## Task

**Objective:**  
Read the request and response headers of a `curl` request and distinguish between them correctly.

**Requirements:**

- Run `curl -v https://example.com`.
- Identify `User-Agent`, `Server`, `Content-Type` and the status line.
- Use only values from the output.

---

## Solution

```text
Command:
curl -v https://example.com

Responses:
- User-Agent: curl/8.18.0
- Server: cloudflare
- Content-Type: text/html
- Status: HTTP/1.1 200 OK
```

**Alternative (compact):**

```text
Request headers show what the client sends.
Response headers show what the server returns.
```

---

## Tests

|Item|Expected|Result|✓|
|---|---|---|---|
|User-Agent visible|`curl/...`|`curl/8.18.0`|✅|
|Server visible|Response server identifiable|`cloudflare`|✅|
|Status visible|200 OK|`HTTP/1.1 200 OK`|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|User-Agent|Identifies the client to the server.|
|Server|Indicates which server software or platform is responding.|
|Content-Type|Describes the type of response content.|

---

## Rules / Logic

```text
Client -> sends request headers.
Server -> sends response headers.
The status line appears at the beginning of the HTTP response.
```

---

## Notes

- **Concept:** Clearly separate the request from the response.
- **Tip:** In `curl -v`, request lines often begin with `>` and response lines with `<`.

---

## Optional: Extensions

- Use `-I` to retrieve headers only.
- Use `-H` to set custom headers.


