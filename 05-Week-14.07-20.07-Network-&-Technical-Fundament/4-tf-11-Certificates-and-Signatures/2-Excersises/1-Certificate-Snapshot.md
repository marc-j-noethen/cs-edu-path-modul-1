# Certificate Snapshot (Certificates & Signatures)

**Course:** Cyber Security Analyst - Technical Fundamentals | **Date:** 17 July 2025

---

## Task

**Objective:**  
Examine a real TLS certificate and understand the issuer, SAN, validity period and AIA.

**Requirements:**

- Examine a genuine Let's Encrypt site.
- Note down the issuer and SAN.
- Explain the validity period.
- Describe the AIA and its use in the trust chain.

---

## Solution

```text
Site examined:
https://community.letsencrypt.org

Issuer:
O = Let's Encrypt
CN = R13

Subject:
CN = community.letsencrypt.org

SAN:
community.letsencrypt.org

Validity Period:
Not Before: 2026-04-20 02:02:09 UTC
Not After: 2026-07-19 02:02:08 UTC
Validity: 90 days

Why 90 days?
Let's Encrypt uses short validity periods so that compromised or incorrectly issued certificates expire more quickly, ensuring that renewal remains automated.

AIA / CA Issuers:
http://r13.i.lencr.org/

Benefits of the AIA:
The browser can use it to find the issuer certificate or intermediate certificate, thereby better establishing the chain of trust.
```

**Alternative (compact):**

```text
Let's Encrypt certificates are short-lived and designed for automation.
```

---

## Tests

|Scenario|Expected|Result|✓|
|---|---|---|---|
|Check issuer|Let's Encrypt visible|`CN=R13, O=Let's Encrypt`|✅|
|Check SAN|Hostname is covered|`community.letsencrypt.org` present|✅|
|Check AIA|CA issuer’s URL present|`http://r13.i.lencr.org/` found|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|Issuer|The certification authority or intermediate that signed the certificate.|
|SAN|List of all DNS names for which the certificate is valid.|
|AIA|Helps clients retrieve certificate information and issuer details.|

---

## Rules / Logic

```text
The Subject Name alone is no longer sufficient; SAN is crucial.
Short validity periods reduce risk and encourage automatic renewal.
AIA assists the browser in establishing the chain of trust.
```

---

## Notes

- **Concept:** Modern browsers validate hostnames primarily via SAN.
- **Syntax:** Issuer, Subject, SAN, AIA, Not Before, Not After.
- **Order is important:**
    1. Open the certificate
    2. Read the Issuer and Subject
    3. Check the SAN, Validity and AIA
- **Edge Cases:**
    - Wildcard or multi-domain certificates.
    - A very large number of SAN entries.
    - Difference between Root, Intermediate and Leaf.
- **Tip:** SANs are particularly important because a single certificate can securely cover multiple hostnames.

---

## Optional: Extensions

- Compare other Let’s Encrypt pages.
- Examine Intermediate `R13` in more detail.
- Add CRL and OCSP as topics on revocation.

