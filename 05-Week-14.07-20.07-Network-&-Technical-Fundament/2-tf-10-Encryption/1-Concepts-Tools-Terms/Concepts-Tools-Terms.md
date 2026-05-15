## Note on macOS vs. Windows 11

The document mentions **FileVault** (macOS) for Full-Disk Encryption. For **Windows 11**, use the following instead:

- **BitLocker**: Windows built-in disk encryption
- Activation: Settings → Privacy & Security → Device Encryption (or Control Panel → BitLocker Drive Encryption)

---

## 📊 Summary Based on the 80/20 Principle

### What is Encryption?

**Encryption** is a method of transforming readable information into unreadable code so that only authorized persons can read it.

**The basic process**:

```
Plaintext 
    → [Algorithm + Key] → 
        Ciphertext 
            → [Algorithm + Key] → 
                Plaintext
```

**Main goal**: **Confidentiality** – protecting information from unauthorized access

---

### The 4 Basic Concepts (80% of Understanding)

|Term|Meaning|Example|
|---|---|---|
|**Plaintext**|Readable original message|"My password is cat123"|
|**Ciphertext**|Encrypted message|"aGv#7!kLp"|
|**Algorithm**|Encryption method|AES, RSA|
|**Key**|Secret key|Like a password for encryption/decryption|

**Key takeaway**: Without the correct **key**, the **ciphertext** is worthless, even if you know the **algorithm**.

---

### The 2 Main Types of Encryption

#### 1. Symmetric Encryption (One Key for Everything)

**Concept**: Sender and receiver use the same secret key

**Analogy**: Diary with a lock – only someone with the identical key can open it

**Process**:

```
1. Alice and Bob agree on a secret key
2. Alice encrypts message with key → Ciphertext
3. Alice sends Ciphertext to Bob
4. Bob decrypts with the same key → Plaintext
```

**Examples**:

- **AES** (Advanced Encryption Standard) – modern standard
- DES/3DES (outdated, insecure)

**Advantages** ✅:

- **Very fast** – ideal for large amounts of data
- Simple implementation

**Disadvantages** ❌:

- **Key Distribution Problem**: How do you share the key securely?
- Many communication partners = many different keys needed

**Applications**:

- Disk encryption (BitLocker)
- Wi-Fi encryption (WPA2/WPA3)
- Encryption of large files

---

#### 2. Asymmetric Encryption (Two Keys: Public + Private)

**Concept**: Each person has a key pair

**The two keys**:

- **Public Key**: Can be freely shared
- **Private Key**: Must remain absolutely secret

**Mailbox analogy**:

- Anyone can drop a letter into your mailbox (= encrypt with Public Key)
- Only you have the key to open it (= decrypt with Private Key)

**Process**:

```
1. Bob publishes his Public Key
2. Alice encrypts message with Bob's Public Key
3. Alice sends Ciphertext to Bob
4. Only Bob can decrypt with his Private Key
```

**Mathematical relationship**:

- Public Key + Message = Ciphertext
- Only the matching Private Key can decrypt Ciphertext
- Private Key CANNOT be calculated from Public Key

**Examples**:

- **RSA** (Rivest-Shamir-Adleman)
- **ECC** (Elliptic Curve Cryptography)

**Advantages** ✅:

- Solves the Key Distribution Problem
- Enables digital signatures
- No prior secret communication needed

**Disadvantages** ❌:

- **Slow** – computationally intensive, not suitable for large amounts of data

**Applications**:

- HTTPS connections (initial handshake)
- Email encryption (PGP/GPG)
- Digital signatures
- SSH connections

---

### Hybrid Encryption: The Best of Both Worlds

**Problem**:

- Symmetric = fast, but key exchange insecure
- Asymmetric = secure key exchange, but slow

**Solution – Hybrid approach** (this is how HTTPS works):

```
Step 1: Asymmetric Encryption
├─ Use Public/Private Keys
└─ Securely transfer a temporary symmetric key

Step 2: Symmetric Encryption
├─ Use the exchanged symmetric key
└─ Encrypt all further data (fast!)
```

**Real-world example – Online shopping**:

1. Browser contacts Amazon
2. **Asymmetric**: Browser and server agree on a Session Key
3. **Symmetric**: All data (login, credit card) is encrypted with Session Key
4. Session ends → new Session Key on next visit

**Advantage**: Security of Asymmetric + Speed of Symmetric

---

### Hashing: The One-Way Cousin of Encryption

**Important**: Hashing ≠ Encryption!

**Key differences**:

|Property|Encryption|Hashing|
|---|---|---|
|Direction|Two-way (there + back)|One-way (there only)|
|Main goal|Confidentiality|Integrity|
|Reversible?|Yes (with key)|No (mathematically impossible)|
|Output length|Variable length|Fixed length|

**What is a hash?**

- Input (any size) → Hash function → Hash value (fixed length)
- Example: "Hello World" → SHA-256 → "3d38e1..." (always 64 characters)

**Properties of hashes**:

1. **Deterministic**: Same input = always same hash
2. **One-way**: Hash → Original is impossible
3. **Fixed length**: 1 byte or 1 GB input → always same hash length
4. **Avalanche Effect**: 1 bit change → completely different hash

**Hash functions**:

- ❌ **MD5** (128 bit) – outdated, insecure
- ⚠️ **SHA-1** (160 bit) – insecure, no longer use
- ✅ **SHA-256** (256 bit) – secure, widely used
- ✅ **SHA-3** – latest standard

**Practical applications**:

**1. Verifying file integrity**:

```
Software download:
├─ Website provides SHA-256 hash: "a3f4b2..."
├─ You download the file
├─ Calculate hash yourself: "a3f4b2..."
└─ Hashes identical? → File unchanged ✓
```

**2. Password storage**:

```
Registration:
├─ You: Enter password "cat123"
├─ Server: Calculate hash → store "8d969eef..."
└─ Original password is deleted

Login:
├─ You: Enter password "cat123"
├─ Server: Calculate hash → "8d969eef..."
├─ Server: Compare with stored hash
└─ Hashes identical? → Login successful
```

**Salting** (important additional technique):

- Problem: Same passwords = same hashes
- Solution: Add random data (salt) before hashing
- Example: "cat123" + "randomSalt123" → Hash

---

### The 5 Most Important Use Cases

#### 1. HTTPS – Secure Websites

**Symbol**: 🔒 Padlock + `https://`

**Process**:

1. Browser contacts website
2. **Asymmetric**: Exchange of a Session Key
3. **Symmetric**: Encryption of all data with Session Key
4. Your login data, credit cards etc. are protected

**Protection against**: Eavesdropping on the network, man-in-the-middle attacks

---

#### 2. Disk Encryption (BitLocker for Windows 11)

**What it does**: Encrypts ALL data on the hard drive

**Type**: Symmetric encryption (AES)

**Scenario**:

- Laptop gets stolen
- Thief can physically access the hard drive
- Without password/key → all data unreadable

**Activation Windows 11**:

```
Settings → Privacy & Security → Device Encryption
or
Control Panel → BitLocker Drive Encryption
```

---

#### 3. VPN (Virtual Private Network)

**What it does**: Creates an encrypted tunnel for internet traffic

**Process**:

```
Your device → [Encrypted Tunnel] → VPN Server → Internet
```

**Type**: Hybrid (asymmetric for setup, symmetric for data)

**Protection against**:

- Eavesdropping on public Wi-Fi (café, airport)
- ISP surveillance
- Geo-blocking

---

#### 4. Encrypted Emails (PGP/GPG)

**Type**: Hybrid encryption

**Process**:

1. Email is encrypted with a symmetric key (fast)
2. Symmetric key is encrypted with recipient's Public Key
3. Recipient decrypts key with Private Key
4. Recipient decrypts email with symmetric key

---

#### 5. Password Manager

**What it does**: Stores all passwords in an encrypted vault

**Type**: Symmetric encryption (AES)

**Principle**:

- You remember: 1 master password
- Password manager remembers: all other passwords (encrypted)

**Examples**:

- Bitwarden (Open Source)
- KeePass (Windows 11)
- 1Password
- LastPass

---

### Encryption vs. Hashing – The Critical Differences

|Criterion|Encryption|Hashing|
|---|---|---|
|**Purpose**|Confidentiality|Integrity|
|**Reversible?**|Yes (with key)|No|
|**Needs key?**|Yes|No|
|**Output length**|Variable|Fixed|
|**Use case**|Protecting secrets|Detecting changes|
|**Example**|Transmitting login data|Storing passwords|

**Simple rule**:

- Does the data need to be readable again? → **Encryption**
- Does the data only need to be comparable? → **Hashing**

---

### Security Principles – What Encryption Provides

|Principle|Meaning|Technique|
|---|---|---|
|**Confidentiality**|Only authorized parties can read|Encryption|
|**Integrity**|Data has not been altered|Hashing|
|**Authenticity**|Sender is genuine|Digital signatures|
|**Non-Repudiation**|Sender cannot deny|Digital signatures|

**CIA Triad in Cybersecurity**:

- **C**onfidentiality
- **I**ntegrity
- **A**vailability

Encryption primarily addresses **C** and helps with **I**.

---

### Key Takeaways for Practice

1. **Symmetric** = One key for both (fast, key exchange problematic)
2. **Asymmetric** = Two keys, Public + Private (slow, secure exchange)
3. **Hybrid** = Asymmetric for key exchange, then symmetric for data
4. **Hashing ≠ Encryption** = One-way vs. two-way
5. **Private Key** = Keep absolutely secret, like your PIN
6. **Public Key** = Share freely, like your postal address
7. **HTTPS** = Your connection is encrypted (padlock symbol)
8. **Same hash** = Same input (useful for integrity)
9. **AES** = Modern symmetric standard
10. **RSA/ECC** = Modern asymmetric standards

---

### Practical Windows 11 Commands

**Calculate a file hash** (PowerShell):

```powershell
Get-FileHash -Path "C:\Users\Download\file.exe" -Algorithm SHA256
```

**Check BitLocker status**:

```powershell
manage-bde -status
```

**Enable BitLocker**:

```powershell
manage-bde -on C:
```

---

### Common Misconceptions

❌ **Wrong**: "Hashing is a type of encryption"  
✅ **Correct**: Hashing is one-way, encryption is two-way

❌ **Wrong**: "Asymmetric encryption is always better"  
✅ **Correct**: Each has its application (asymmetric for keys, symmetric for data)

❌ **Wrong**: "If I keep the algorithm secret, it's more secure"  
✅ **Correct**: Security lies in the key, not in the secret algorithm (Kerckhoffs's principle)

❌ **Wrong**: "MD5 hashes are fine for passwords"  
✅ **Correct**: MD5 is broken, use SHA-256 or better bcrypt/Argon2

❌ **Wrong**: "VPN makes me completely anonymous"  
✅ **Correct**: VPN encrypts traffic, but the VPN provider can see activity

---

## Tools Used

|**Category**|**Term**|**Meaning**|
|---|---|---|
|**Tools Used**|BitLocker (Windows 11)|Windows tool for full disk encryption|
||VPN software|Programs for creating encrypted tunnels for internet traffic|
||Password Manager|Applications for encrypted storage of passwords (e.g. KeePass, Bitwarden)|
||OpenSSL|Command-line tool for encryption and certificate management|
||GPG/PGP|Tools for asymmetric encryption of emails and files|
||Web browser (Chrome, Edge, Firefox)|Display HTTPS encryption via padlock symbol|
||HashCalc / certutil (Windows 11)|Tools for calculating hash values of files|

---

## Technical Terms

|**Category**|**Term**|**Meaning**|
|---|---|---|
|**Technical Terms**|Plaintext|Original text or data in readable form before encryption|
||Ciphertext|Encrypted, unreadable text after encryption|
||Algorithm/Cipher|Mathematical method for encrypting and decrypting data|
||Key|Secret information used by the algorithm for encryption/decryption|
||Encryption|Conversion of plaintext into ciphertext|
||Decryption|Conversion of ciphertext back into plaintext|
||Confidentiality|Ensuring that information is only accessible to authorized parties|
||Symmetric Encryption|Encryption with a single secret key for both directions|
||Asymmetric Encryption|Encryption with a key pair (public + private)|
||Public Key|Key that can be freely shared to encrypt messages|
||Private Key|Secret key for decrypting messages, must remain secret|
||Hybrid Encryption|Combination of symmetric and asymmetric encryption|
||Key Distribution Problem|Challenge of sharing symmetric keys securely|
||Hashing|One-way function for creating a fingerprint of data|
||Hash Value/Digest|Fixed-length characters as the result of a hash function|
||Avalanche Effect|Small change in input leads to a completely different hash value|
||Data at Rest|Stored data on hard drives, USB sticks etc.|
||Data in Transit|Data being transmitted over networks|
||Authenticity|Confirmation of the genuineness of a message or identity|
||Integrity|Ensuring that data has not been altered|
||Digital Signature|Digital signature to confirm sender and unaltered state|
||Full-Disk Encryption|Complete encryption of all data on a storage medium|
||AES (Advanced Encryption Standard)|Modern, strong symmetric encryption algorithm|
||RSA|Widely used asymmetric encryption algorithm|
||ECC (Elliptic Curve Cryptography)|Modern asymmetric encryption with shorter keys|
||DES/3DES|Older, now insecure symmetric algorithms|
||SHA-256/SHA-3|Strong hash functions of the SHA family|
||MD5|Old, no longer secure hash function|
||Salting|Adding random data to passwords before hashing|
|**Key Vocabulary**|Scramble|Make data unreadable|
||Unscramble|Make data readable again|
||Secret code|Method for keeping messages confidential|
||Tamper-proof|Cannot be altered without detection|
||One-way|Process that is not reversible (in hashing)|
||Two-way|Process that is reversible (in encryption)|
||Fingerprint|Unique identifier for data (hash value)|
||Mailbox analogy|Illustration of asymmetric encryption|
||Padlock icon|Browser symbol for a secure HTTPS connection|
||Tunnel|Encrypted communication channel (in VPN)|
||Master password|Main password for unlocking a password manager|
||Intercept|Unauthorized reading of data during transmission|
||Caesar Cipher|Simple historical encryption method by shifting letters|
||Shift|Number of positions by which letters are shifted|
||Vault|Encrypted storage location for sensitive data|
||Download verification|Verification of the authenticity of downloaded files|