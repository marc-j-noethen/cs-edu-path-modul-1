# Banner Grabbing Bonanza (Common Protocols)

**Course:** Cyber Security Analyst – Network Technology | **Date:** 28 July 2025

---

## Task

**Objective:**  
Identify open TCP services by their banners or connection behaviour.

**Requirements:**

- Check multiple hosts/ports using `telnet`.
- Note down successful connections and banners.
- Explain the reconnaissance value of the banners.

---

## Solution

```text
Sample answer:
- google.com 80 -> TCP connection successful, but no actual banner; a response is only received after sending an HTTP request.
- ftp.dlptest.com 21 -> typical FTP banner, e.g. `220 ...`.
- smtp.googlemail.com 25 -> typical SMTP banner, e.g. `220 ... ESMTP`.
- whois.iana.org 43 -> often no classic banner; the service simply waits for a search query.
- dict.org 2628 -> typical DICT banner, e.g. `220 dict.dict.org ...`.
- localhost 9999 -> `Connection refused` or similar connection error.

Recon value:
Banners often reveal the protocol, service name, server type and sometimes even versions.
Even a missing banner provides information: the port is open, but the service only responds after a valid protocol step.
```

**Alternative (compact):**

```text
Banner = the first identity card of a network service.
```

---

## Tests

|Host/Port|Expected|✓|
|---|---|---|
|`ftp.dlptest.com:21`|FTP banner|✅|
|`smtp.googlemail.com:25`|SMTP banner or connection info|✅|
|`localhost:9999`|Connection refused|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|Banner Grabbing|Using early protocol responses for reconnaissance.|
|Recon|Gathering information prior to deeper analysis.|
|Open Port|An open port confirms an accessible service.|

---

## Rules / Logic

```text
Open port ≠ automatically readable banner.
Many text protocols give themselves away early on.
Versions and greetings aid in fingerprinting.
```

---

## Notes

- **Important:** Banners may vary depending on the time and server.
- **Tip:** Some services only respond after a matching protocol command.

---

## Optional: Extensions

- Test the same with `nc` instead of `telnet`.
- Compare banners with `nmap -sV`.

