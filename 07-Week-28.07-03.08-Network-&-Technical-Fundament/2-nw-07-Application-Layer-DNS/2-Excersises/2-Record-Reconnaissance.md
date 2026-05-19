# Record Reconnaissance (DNS)

**Course:** Cyber Security Analyst – Network Technology | **Date:** 29 July 2025

---

## Task

**Objective:**  
To query and interpret specific types of DNS records.

**Requirements:**

- Find the A record for `cloudflare.com`.
- Find the AAAA record for `google.com`.
- Collect the NS record for `wikipedia.org`, the MX record for `gmail.com` and the SPF-TXT record for `microsoft.com`.

---

## Solution

```text
A record for cloudflare.com:
- 104.16.132.229
- 104.16.133.229

AAAA record for google.com:
- 2a00:1450:400f:807::200e

NS for wikipedia.org:
- ns0.wikimedia.org
- ns1.wikimedia.org
- ns2.wikimedia.org

MX for gmail.com:
- 5 gmail-smtp-in.l.google.com
- 10 alt1.gmail-smtp-in.l.google.com
- 20 alt2.gmail-smtp-in.l.google.com
- 30 alt3.gmail-smtp-in.l.google.com
- 40 alt4.gmail-smtp-in.l.google.com

SPF-TXT for microsoft.com:
- v=spf1 include:_spf-a.microsoft.com include:_spf-b.microsoft.com include:_spf-c.microsoft.com include:_spf-ssg-a.msft.net include:_spf1-meo.microsoft.com -all
```

**Alternative (compact):**

```text
A = IPv4, AAAA = IPv6, NS = Name server, MX = Mail server, TXT = Free text/Policy.
```

---

## Tests

|Type|Expected|✓|
|---|---|---|
|A|IPv4 addresses found|✅|
|AAAA|IPv6 address found|✅|
|MX|Mail servers with priorities found|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|A / AAAA|Name resolution to IPv4 or IPv6.|
|MX|Specifies mail receiving servers and their order.|
|SPF|TXT-based policy for permitted mail senders.|

---

## Rules / Logic

```text
Lower MX priority = preferred mail server.
Multiple A/AAAA records = load balancing or redundancy.
TXT may contain policies and verification.
```

---

## Notes

- **Important:** DNS entries may change over time.
- **Tip:** For reference, note the time of the query.

---

## Optional: Extensions

- Compare the same queries using `dig` and `nslookup`.
- Evaluate TTL values as well.

