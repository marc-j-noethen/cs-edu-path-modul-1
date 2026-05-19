# Hosts File Hijinks (DNS / Hosts)

**Course:** Cyber Security Analyst – Network Technology | **Date:** 29 July 2025

---

## Task

**Objective:**  
To understand why the local `hosts` file affects programmes such as `ping`, but often does not affect `dig`.

**Requirements:**

- Redirect a domain locally to `127.0.0.1`.
- Compare `ping` and `dig`.
- Explain the difference.

---

## Solution

```text
Answer 1:
After adding the entry `127.0.0.1 example.com`, `ping example.com` resolves to `127.0.0.1`.

Answer 2:
`dig A example.com` continues to show the public DNS responses,
e.g. currently `104.20.23.154` and `172.66.147.243`.

Answer 3:
`ping` uses the operating system’s name resolution and therefore also the local `hosts` file.
`dig` queries the DNS service directly and typically ignores the local `hosts` file.
That is why `ping` sees the override, but `dig` sees the actual DNS entry.
```

**Alternative (compact):**

```text
`hosts` affects the local resolver, not the DNS zone on the internet.
```

---

## Tests

|Tool|Expected|✓|
|---|---|---|
|`ping example.com`|`127.0.0.1`|✅|
|`dig A example.com`|public IP(s)|✅|
|Explanation|Resolver vs. DNS server separated|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|hosts file|Local static name mapping.|
|OS Resolver|Involves `hosts`, cache and DNS.|
|`dig`|Queries DNS directly and often bypasses local overrides.|

---

## Rules / Logic

```text
Local resolution is not the same as public DNS resolution.
```

---

## Notes

- **Important:** Remove the entry after testing.
- **Tip:** Flush the DNS cache after making changes.

---

## Optional: Extensions

- Compare the same behaviour with `nslookup`.
- Redirect your own local test domain to a dev server.

