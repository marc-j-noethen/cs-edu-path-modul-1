# Certificates and Signatures

## 📊 Summary based on the 80/20 principle

### 1. Digital signatures establish trust in identity and integrity
The essence of the 80/20 principle is this: a digital signature does not prove confidentiality, but rather authenticity, integrity and non-repudiation. A certificate complements this by credibly linking a public key to an identity.

### 2. Step-by-step core process
1. The sender generates a hash from the original data.
2. This hash is signed with the private key.
3. The recipient decrypts the signature using the public key.
4. They then hash the received data themselves once more.
5. If both hash values match, identity and integrity are plausibly confirmed.
6. To ensure the public key is trustworthy, it is usually verified via a certificate and a CA chain.

### 3. Interactive mode / Tool usage
In everyday life, you encounter this topic on every `https://` page. Simply clicking on the padlock in the browser shows that secure communication is underpinned by certificates, validity periods, issuers and a chain of trust.

### 4. The key concepts with code examples
- **Authenticity:** The message originates from the claimed sender.
- **Integrity:** The content has not been altered since signing.
- **Non-repudiation:** The sender cannot credibly deny having signed the message at a later date.
- **Certificate Authority:** A trusted authority confirms who owns a public key.

```python
message_hash = sha256(message)
signature = sign_with_private_key(message_hash)

received_hash = sha256(received_message)
verified_hash = verify_with_public_key(signature)

is_valid = verified_hash == received_hash
```

### 5. Comparison: Digital Signature vs. Digital Certificate
- The **digital signature** protects and authenticates a specific message or file.
- The **digital certificate** confirms the link between identity and public key.
- Only together do they form the chain of trust required for HTTPS, signed software and many PKI processes.

### 6. Why is this important / Benefits
Without signatures and certificates, there would be no reliable way to verify whether websites are genuine, software is unaltered, or a communication partner is truly who they claim to be.

**Quick Start Checklist**
- ☐ I can distinguish between authenticity, integrity and non-repudiation.
- ☐ I understand why signatures combine hashing and asymmetric cryptography.
- ☐ I know what is typically contained in a certificate.
- ☐ I am familiar with the role of Certificate Authorities.
- ☐ I have a basic understanding of what is meant by a chain of trust.

**Key point**
The signature proves that data is genuine and unaltered, and the certificate proves who actually owns the corresponding public key.

---

## Table 1: Tools used
| Tool | Description |
|---|---|
| Web browser | Displays certificates and trust information for HTTPS |
| Hash Function | Generates a unique fingerprint of data |
| Private Key | Used for signing and remains secret |
| Public Key | Used to verify the signature |

## Table 2: Technical Terms
| Term | Meaning |
|---|---|
| Digital Signature | Cryptographic proof of authenticity and integrity |
| Certificate | Electronic document linking identity and public key |
| Certificate Authority | Trusted body that issues certificates |
| Chain of Trust | Chain of trust from end certificate via intermediate authorities to the root CA |
| PKI | Comprehensive system for managing certificates and keys |
| Revocation | Revocation of a compromised or invalid certificate |

## Table 3: Key terms
| Term | Meaning |
|---|---|
| issuer | Issuer |
| subject | Holder / Data subject |
| validity period | Validity period |
| verify | Verify / Check |
| revoke | Revoke |
| trust store | Trust store |


