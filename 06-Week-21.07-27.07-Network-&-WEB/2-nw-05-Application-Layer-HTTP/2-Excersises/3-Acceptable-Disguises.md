# Acceptable Disguises (HTTP)

**Course:** Cyber Security Analyst – Network Technology | **Date:** 22 July 2025

---

## Task

**Objective:**  
Use `curl` to set your own headers and check whether the server returns them.

**Requirements:**

- Send a single GET request to `http://httpbin.org/anything`.
- Set `User-Agent` to `MyCustomClient/1.1`.
- Set `Accept` to `text/plain`.

---

## Solution

```bash
curl http://httpbin.org/anything -H "User-Agent: MyCustomClient/1.1" -H "Accept: text/plain"
```

```text
Confirmation:
- Is the User-Agent correct? Yes
- Is the Accept correct? Yes
```

**Alternative (compact):**

```text
httpbin returns the request headers in JSON under `headers`.
```

---

## Tests

|Item|Expected|Result|✓|
|---|---|---|---|
|User-Agent set|`MyCustomClient/1.1`|Yes|✅|
|Accept set|`text/plain`|Yes|✅|
|Single command|only one `curl` call|Yes|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|Header manipulation|Clients can set headers specifically.|
|Accept|Informs the server of the preferred response type.|
|Echo endpoint|`httpbin` displays the received request.|

---

## Rules / Logic

```text
`-H` adds headers.
Multiple `-H` options -> multiple headers.
Echo API -> good test case for verification.
```

---

## Notes

- **Tip:** Always compare header values exactly.
- **Concept:** HTTP is text-based and therefore easy to observe.

---

## Optional: Extensions

- Set `Accept-Language` additionally.
- Observe the difference between HTTP and HTTPS when using proxies.


