# 🐍 Homegrown HTTPS (Certificates & Signatures)

**Course:** Cyber Security Analyst - Technical Fundamentals | **Date:** 17 July 2025

---

## Task

**Objective:**  
Generate a self-signed certificate for `mysecuredev.lab`, run a small Python HTTPS server and explain the browser warning message in a technically accurate manner.

**Requirements:**

- Use OpenSSL for the key + self-signed certificate with `CN` and `SAN = mysecuredev.lab`.
- Configure `mysecuredev.lab` locally via the hosts file to point to `127.0.0.1`.
- Run `basic_https_server.py` on port `8443` using the generated key pair.
- Explain the browser warning, name a local trust method and revert the hosts file change at the end.

- Output:

    - OpenSSL commands for key and certificate
    - Complete Python HTTPS server
    - Explained browser warning + local trust procedure

---

## Solution

```text
OpenSSL command:
openssl req -x509 -newkey rsa:2048 -sha256 -nodes ^
  -keyout mysecuredev.lab.key ^
  -out mysecuredev.lab.crt ^
  -days 14 ^
  -subj "/CN=mysecuredev.lab" ^
  -addext "subjectAltName=DNS:mysecuredev.lab"

Hosts file:
127.0.0.1 mysecuredev.lab

basic_https_server.py:
from http.server import BaseHTTPRequestHandler, HTTPServer
import ssl

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = b"<html><body><h1>Welcome to mysecuredev.lab!</h1></body></html>"
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, fmt, *args):
        return

server = HTTPServer(("127.0.0.1", 8443), Handler)
ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ctx.load_cert_chain("mysecuredev.lab.crt", "mysecuredev.lab.key")
server.socket = ctx.wrap_socket(server.socket, server_side=True)
server.serve_forever()

Why is the browser issuing a warning?
The certificate is self-signed and the issuing CA is not present in the browser’s or operating system’s trust store.
As a result, the browser cannot validate the chain of trust back to a known root CA.

Correct local trust method:
Import the self-signed certificate into the local certificate store "Trusted Root Certification Authorities" for lab purposes only,
or explicitly trust it in the certificate settings in Firefox.
https://mysecuredev.lab:8443 will then load without a warning.

Cleanup:
- Remove the entry from the hosts file
- Delete the self-imported certificate from the local trust store

Note:
The screenshots of the browser warning and the successful HTTPS page are GUI-dependent artefacts.
Technically speaking, a warning appears first and the page loads normally after the local trust import.
```

**Alternative (compact):**

```text
Self-signed certificates work technically straight away, but are only displayed as trusted after the local trust store has been imported.
```

---

## Tests

|Input 1|Input 2|Input 3|Expected|Result|✓|
|---|---|---|---|---|---|
|`SAN set`|`Port 8443`|`Hosts entry`|`HTTPS accessible`|`technically correct`|✅|
|`without trust`|`Browser`|`self-signed`|`Warning`|`expected`|✅|
|`with trust`|`same URL`|`same certificate`|`Page loads`|`expected`|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|Self-Signed Certificate|A certificate where the issuer and holder are identical; without a separate trust chain.|
|SAN|The Subject Alternative Name is the field relevant today for hostname validation.|
|Trust Store|Browsers and operating systems only trust certificates whose root or intermediate certificates are known.|

---

## Rules / Logic

```text
CN alone is no longer sufficient; for hostnames, the SAN must match.
Self-signed certificates generate encryption, but without imported trust, they lack browser-side trustworthiness.
Local laboratory changes such as the hosts file and root trust must be removed again.
```

---

## Notes

- **Important:** For modern browsers, `subjectAltName=DNS:mysecuredev.lab` is mandatory.
- **Observation:** The warning does not confirm that TLS is broken, but rather that the trust chain is unknown.
- **Tip:** For development purposes, it is better to use short validity periods such as 7–14 days.

---

## Optional: Extensions

- Instead of using a self-signed certificate, build your own small dev-CA and sign multiple local hostnames.
- Add an HTTP-to-HTTPS redirect as a second exercise.

