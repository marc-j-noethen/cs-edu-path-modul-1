# Quack Quack (DuckDNS)

**Course:** Cyber Security Analyst – Network Technology | **Date:** 29 July 2025

---

## Task

**Objective:**  
Create a DuckDNS subdomain with an A record pointing to `1.2.3.4` and verify it using `dig`.

**Requirements:**

- Log in to DuckDNS.
- Create a subdomain.
- Evaluate `dig A <subdomain>.duckdns.org`.

---

## Solution

```text
Sample response:
Subdomain: your-unique-name.duckdns.org
Expected `dig` output in the ANSWER SECTION:
`your-unique-name.duckdns.org. ... IN A 1.2.3.4`

Summary:
The A record has been set correctly if `dig` shows the IP `1.2.3.4` in the ANSWER SECTION.
```

**Alternative (compact):**

```text
A record = Name points to IPv4 address.
```

---

## Tests

|Item|Expected|✓|
|---|---|---|
|Subdomain created|Name exists|✅|
|A record set|`1.2.3.4` visible|✅|
|`dig` check|Response from ANSWER SECTION|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|DuckDNS|Simple dynamic DNS service.|
|A-record|Maps a hostname to an IPv4 address.|
|Propagation|DNS changes sometimes take a short while.|

---

## Rules / Logic

```text
Name -> A-record -> IPv4 address.
`dig` confirms the published DNS response.
```

---

## Notes

- **Important:** The specific subdomain depends on the user.
- **Tip:** If the response is empty, wait 1 to 2 minutes and check again.

---

## Optional: Extensions

- Set an additional TXT record.
- Update the subdomain later via API.

