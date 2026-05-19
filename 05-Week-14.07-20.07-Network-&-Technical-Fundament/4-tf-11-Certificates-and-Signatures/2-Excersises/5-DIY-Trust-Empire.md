# 🐍 DIY Trust Empire (Certificates & Signatures)

**Course:** Cyber Security Analyst - Technical Fundamentals | **Date:** 17 July 2025

---

## Task

**Objective:**  
Set up a mini-PKI with a root CA, a server certificate for `localhost`, an HTTPS server and a Python client that trusts only the self-signed root CA.

**Requirements:**

- Generate a root CA key and a self-signed root certificate `MySecretRootCA.pem`.
- Issue a CSR and server certificate for `localhost` with SAN `DNS:localhost`.
- Run an HTTPS server on `https://localhost:4443` using the signed server certificate.
- The Python client should fail once with normal verification and succeed once with `verify='MySecretRootCA.pem'`.

- Output:

    - all OpenSSL commands used
    - complete server and client code
    - brief explanation of why the explicit root CA is necessary

---

## Solution

```text
OpenSSL commands:
1. Root CA key
   openssl genrsa -out MySecretRootCA.key 4096

2. Root CA certificate
   openssl req -x509 -new -key MySecretRootCA.key -sha256 -days 365 ^
     -out MySecretRootCA.pem ^
     -subj "/CN=MySecretRootCA"

3. Server key
   openssl genrsa -out secretlocalhost.key 2048

4. CSR with SAN for localhost
   openssl req -new -key secretlocalhost.key -out secretlocalhost.csr ^
     -subj "/CN=localhost" ^
     -addext "subjectAltName=DNS:localhost"

5. Sign the server certificate with the root CA
   openssl x509 -req -in secretlocalhost.csr ^
     -CA MySecretRootCA.pem -CAkey MySecretRootCA.key -CAcreateserial ^
     -out secretlocalhost.crt -days 30 -sha256 ^
     -extfile <(printf "subjectAltName=DNS:localhost")

custom_pki_server.py:
from http.server import BaseHTTPRequestHandler, HTTPServer
import ssl

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = b"<html><body><h1>Server Response: Custom Root CA Trust Verified! </h1></body></html>"
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, fmt, *args):
        return

server = HTTPServer(("localhost", 4443), Handler)
ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ctx.load_cert_chain("secretlocalhost.crt", "secretlocalhost.key")
server.socket = ctx.wrap_socket(server.socket, server_side=True)
server.serve_forever()

custom_pki_client.py:
import requests
from requests.exceptions import SSLError

url = "https://localhost:4443"

print("[1] Standard validation without custom CA")
try:
    requests.get(url, timeout=5)
except SSLError as exc:
    print("Expected failure:", exc)

print("[2] Validation with MySecretRootCA.pem")
response = requests.get(url, timeout=5, verify="MySecretRootCA.pem")
print("Status:", response.status_code)
print("Body:", response.text[:80])

Why was `verify="MySecretRootCA.pem"` necessary?
By default, the Requests client does not recognise the private, self-signed root CA.
Only by explicitly trusting this specific CA can it verify the certificate chain without disabling global SSL verification.
This preserves the core PKI principle: trust only a known root of trust.
```

**Alternative (compact):**

```text
Without an explicit CA bundle, the connection fails correctly; with `verify=MySecretRootCA.pem`, TLS verification remains active and the connection is valid.
```

---

## Tests

|Input 1|Input 2|Input 3|Expected|Result|✓|
|---|---|---|---|---|---|
|`without verify`|`Requests`|`localhost`|`SSL error`|`expected`|✅|
|`with verify`|`Root CA file`|`localhost`|`200 OK`|`expected`|✅|
|`SAN localhost`|`CRT`|`Handshake`|`Hostname matches`|`expected`|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|Root CA|The top-level trust root used to sign other certificates.|
|CSR|The Certificate Signing Request contains the public key and identity data for the signature.|
|Explicit Trust|The client trusts only the specified CA certificate rather than accepting every TLS connection indiscriminately.|

---

## Rules / Logic

```text
TLS verification must not be disabled with `verify=False` for the connection to succeed.
The server name `localhost` must be included in the SAN.
A private Root CA can only be used securely if clients specifically and consciously trust it.
```

---

## Notes

- **Important:** The Root CA private key must be handled separately from the server key.
- **Note:** On Windows, the `<(printf ...)` variant is only appropriate in context; alternatively, use a small SAN configuration file.
- **Tip:** Show the failure case first, then the success case – that is exactly what the task requires.

---

## Optional: Extensions

- Add Mutual TLS with a client certificate as the next level of implementation.
- Check the certificate details using `openssl x509 -text -noout -in secretlocalhost.crt`.

