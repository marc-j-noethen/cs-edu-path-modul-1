## **📊 Summary according to the 80/20 Principle**

### The Core Problem: Computers Only Understand Numbers

**Computer = binary machines**: Everything (texts, images, videos, programs) must be stored as 0s and 1s.

**Encoding = translation rule**: How do we convert letters into numbers?

**Example:**

- Letter 'A' → number 65 → binary 01000001
- Without a standard: chaos! (Computer A says 65='A', Computer B says 65='Z')

### The 3 Most Important Encodings

#### 1. **ASCII - The Ancestor (1963)**

**What it is:**

- Standard for English characters
- Uses **7 bits** = 2⁷ = **128 characters** (0–127)
- Defines the mapping: number ↔ character

**What it contains:**

- Uppercase letters: A–Z (65–90)
- Lowercase letters: a–z (97–122)
- Digits: 0–9 (48–57)
- Punctuation: !, @, #, $, etc.
- Control characters: Newline, Tab, Backspace (invisible)

**Most important ASCII values to memorize:**

```
'A' = 65    'a' = 97    '0' = 48
'Z' = 90    'z' = 122   '9' = 57
Space = 32  Newline = 10  Tab = 9
```

**Memory aid:** Lowercase letters = uppercase letters + 32

- 'A' (65) + 32 = 'a' (97)
- 'B' (66) + 32 = 'b' (98)

**Limitation:** English only! No ä, é, ñ, 猫, 😀

#### 2. **Unicode & UTF-8 - The Modern Solution**

**Unicode:**

- Universal system with over 149,000 characters
- Every character = unique number (code point)
- Example: 'A' = U+0041, '猫' = U+732B, '😀' = U+1F600

**UTF-8 (the most important Unicode encoding):**

- **Variable width**: 1–4 bytes per character

|Character Type|Bytes|Examples|
|---|---|---|
|ASCII (0–127)|1 byte|A, B, 5, !, Space|
|Extended Latin|2 bytes|ä, ö, ü, é, ñ|
|Asian/Symbols|3 bytes|猫, €, ™|
|Emojis/Rare|4 bytes|😀, 🚀, 🎉|

**Killer feature: ASCII compatibility**

- ASCII characters (0–127) are **identical** in UTF-8
- Old ASCII files = valid UTF-8 files
- Smooth transition with no breaking changes

**Why UTF-8 dominates:**

1. Supports ALL languages worldwide
2. 100% backward compatible with ASCII
3. Efficient: English only needs 1 byte/character
4. Web standard (>98% of all websites)

#### 3. **Base64 - Binary Data as Text**

**Problem:**

- Email systems expect only text (ASCII)
- Images/PDFs are binary data (contain all 256 byte values)
- Binary data could contain control characters → corruption!

**Solution: Base64**

- Converts **arbitrary binary data** into **printable ASCII characters**
- Uses only 64 "safe" characters: `A–Z`, `a–z`, `0–9`, `+`, `/`

**How it works (simplified):**

```
Input:  3 bytes (24 bits) of binary data
↓
Split: 4 × 6-bit blocks
↓
Mapping: each 6-bit block → one Base64 character (0–63)
↓
Output: 4 ASCII characters
```

**Example: encoding "Man"**

```
Text:    M        a        n
ASCII:   77       97       110
Binary:  01001101 01100001 01101110  (24 bits)

Group into 6 bits:
         010011   010110   000101   101110
Decimal: 19       22       5        46
Base64:  T        W        F        u

Result: "TWFu"
```

**Padding rule:**

- If input is not a multiple of 3 bytes → pad with `=`
- Example: "A" → `QQ==` (2× padding)

**CRITICAL: Base64 is NOT encryption!**

- ❌ Offers ZERO security
- ❌ Anyone can decode it
- ✅ Only for safe transmission, not secrecy
- Comparison: like translating from German to English (no secret)

**Where you see Base64:**

- Email attachments (MIME)
- Images in HTML: `<img src="data:image/png;base64,iVBORw0K...">`
- JWT tokens (authentication)
- SSL certificates (.pem files)
- API keys

### ASCII vs UTF-8 vs Base64: When to Use Which?

||ASCII|UTF-8|Base64|
|---|---|---|---|
|**Purpose**|English characters|All languages|Binary data as text|
|**Characters**|128 (0–127)|149,000+|Not for characters|
|**Bytes/character**|1|1–4|1.33× input|
|**Contains**|A–Z, 0–9, basic|A–Z + ä, é, 猫, 😀|Only A–Z, a–z, 0–9, +, /|
|**Usage**|Legacy systems|Modern text|Email, data URLs|
|**Compatible with**|–|ASCII (0–127)|ASCII output|

### Common Problems & Solutions

#### **Problem 1: Mojibake (Garbled Text)**

```
File contains:  "Hällö" (UTF-8)
Read as:        "HÃ¤llÃ¶" (ASCII/Latin-1)
```

**Cause:** Wrong encoding used when opening **Solution:** Specify the correct encoding (UTF-8 is the standard)

#### **Problem 2: Confusing Base64 with Encryption**

```
Secret password:  "admin123"
Base64:           "YWRtaW4xMjM="
```

**WRONG:** "Now it's secure!" ❌ **CORRECT:** Anyone can decode it with `base64 -d`!

#### **Problem 3: Sending Binary Data Directly**

```
Image file → Email → Corrupted!
```

**Cause:** Email system interprets bytes as text **Solution:** Base64-encode before sending

### Windows Tools: Quick Reference

**Character Map:**

1. `Windows key` → "charmap"
2. Search for character → view code point
3. Copy → paste

**PowerShell for ASCII:**

```powershell
# Character → code
[int][char]'A'      # → 65

# Code → character
[char]65            # → A

# String → bytes
[System.Text.Encoding]::UTF8.GetBytes("Hello")
```

**Python (if installed):**

```python
# Start: python in CMD
ord('A')                # ASCII value
chr(65)                 # Character
'Hello'.encode('utf-8') # UTF-8 bytes

# Base64
import base64
base64.b64encode(b'Hello World!')
```

### Practical Exercises

**Exercise 1: Exploring ASCII**

```
Find the ASCII value for:
1. Your initial (e.g. 'J')
2. The $ symbol
3. The digit 0 (not the null byte!)

Calculate: 'J' (74) + 32 = ? → 'j' (106)
```

**Exercise 2: Decoding Base64**

```
Given: "SGVsbG8gV29ybGQh"
Tool: https://www.base64decode.org/
Result: ?
```

**Exercise 3: Understanding Mojibake**

```
Text: "café"
UTF-8 hex: 63 61 66 C3 A9
Read as ASCII: c a f ? ?  (? ?)
```

### The 5 Most Important Insights

1. **ASCII is dead, long live UTF-8!**
    
    - ASCII only for legacy systems
    - UTF-8 is the modern standard
    - Always choose UTF-8 for new projects
2. **Base64 ≠ Encryption**
    
    - Just encoding, no security
    - In cybersecurity: attackers decode Base64 instantly
    - Never "protect" secrets with Base64 alone
3. **Encoding mismatch = garbled text**
    
    - Sender: UTF-8, receiver: ASCII → Mojibake
    - Always agree on the same encoding
    - UTF-8 is the safest choice (universal)
4. **1 hex digit = 1 Base64 character? NO!**
    
    - Base64: 3 bytes → 4 characters
    - Expansion of ~33%
    - Hex: 1 byte → 2 characters (100% expansion)
5. **Binary → Text: use Base64**
    
    - Images, PDFs, archives in email
    - Data in JSON/XML
    - API communication

### Core Message

**The Encoding Pyramid:**

```
     Application
         ↓
    UTF-8 (Text)
         ↓
   Base64 (Transport)
         ↓
    Binary (0 & 1)
         ↓
     Hardware
```

**Memory aids:**

- **ASCII** = Ancient System Comes from International Institute (English only)
- **UTF-8** = Universal Text Format – 8 bits (but variable!)
- **Base64** = Base with 64 characters (A–Z, a–z, 0–9, +, /)

**Practical tip for cybersecurity:**

- Base64 in suspicious scripts? → Decode immediately!
- Attackers often hide malware in Base64
- Tools: `base64 -d` (Linux/Mac) or CyberChef (web)

---

## Tools Used, Technical Terms, and Important Vocabulary

|Term|Meaning|
|---|---|
|**Tools Used (macOS → Windows)**||
|`man ascii` (Terminal)|Display ASCII table in terminal (Windows CMD: not available; use an online ASCII table or PowerShell: `[char]65` shows 'A')|
|Terminal / Command Prompt|Command line for displaying character tables (Windows: CMD or PowerShell)|
|Online Base64 Encoder/Decoder|Web tools for Base64 encoding/decoding (platform-independent)|
|Text Editor (Plain Text Mode)|Simple text editor for viewing encodings (Windows: Notepad, Notepad++)|
|Character Map|Character map tool (Windows: `charmap.exe` via Start search)|
|Python|Programming language for encoding experiments (`encode()`, `decode()`) – identical on Windows|
|**Core Concepts**||
|Data Encoding|Conversion of information into a specific format (usually binary)|
|Decoding|Reverse conversion back into a readable/usable form|
|Character Encoding|Mapping of characters to binary numbers|
|Binary Data|Raw data in 0s and 1s (e.g. images, programs)|
|Text Data|Human-readable characters and symbols|
|Bit|Binary digit – smallest unit of data (0 or 1)|
|Byte|8 bits together – standard unit of storage|
|Pattern|Specific bit arrangement used to represent information|
|**ASCII (American Standard Code for Information Interchange)**||
|ASCII|Oldest standard for character encoding (7 bit = 128 characters)|
|7-bit Encoding|7-bit encoding – 2⁷ = 128 different characters possible|
|ASCII Table|Mapping of numbers (0–127) to characters|
|Code Point|Numeric value of a character in an encoding|
|Control Characters|Invisible characters that control text processing (Newline, Tab, Backspace)|
|Printable Characters|Visible characters (letters, numbers, symbols)|
|Uppercase Letters|Capital letters A–Z (ASCII 65–90)|
|Lowercase Letters|Small letters a–z (ASCII 97–122)|
|Digits|Digits 0–9 (ASCII 48–57)|
|Punctuation|Punctuation marks and symbols (!, @, #, $, etc.)|
|**ASCII Examples**||
|'A' = 65 = 0x41 = 01000001|Uppercase letter A|
|'a' = 97 = 0x61 = 01100001|Lowercase letter a|
|'0' = 48 = 0x30 = 00110000|Digit zero (not the null byte!)|
|Space = 32 = 0x20 = 00100000|Space character|
|'!' = 33 = 0x21 = 00100001|Exclamation mark|
|Newline (LF) = 10 = 0x0A|Line break (Line Feed)|
|Tab = 9 = 0x09|Tab character|
|**ASCII Limitations**||
|English-Only|English alphabet only – no umlauts, accents, or other alphabets|
|No Accents|No accent characters (é, à, ñ, etc.)|
|No Umlauts|No German umlauts (ä, ö, ü, ß)|
|No International Characters|No international characters (Cyrillic, Greek, Chinese, etc.)|
|**Unicode & UTF-8**||
|Unicode|Universal character set – over 149,000 characters from all languages + emojis|
|Code Point|Unicode code point – unique number for each character (e.g. U+0041 for 'A')|
|Character Set|Collection of all defined characters|
|UTF-8|Unicode Transformation Format 8-bit – most common Unicode encoding|
|Variable-Width Encoding|Uses 1–4 bytes per character depending on need|
|Backward Compatible|ASCII characters (0–127) are identical in UTF-8|
|Multi-Byte Character|Characters outside ASCII require 2–4 bytes|
|**UTF-8 Byte Structure**||
|1 Byte (ASCII range)|ASCII-compatible: 0–127 (0xxxxxxx)|
|2 Bytes|Extended Latin, Greek, Cyrillic characters (110xxxxx 10xxxxxx)|
|3 Bytes|Asian characters, symbols (1110xxxx 10xxxxxx 10xxxxxx)|
|4 Bytes|Rare characters, emojis (11110xxx 10xxxxxx 10xxxxxx 10xxxxxx)|
|**Unicode Examples**||
|'€' (Euro)|U+20AC – 3 bytes in UTF-8|
|'ä' (Umlaut)|U+00E4 – 2 bytes in UTF-8|
|'猫' (cat, Chinese)|U+732B – 3 bytes in UTF-8|
|'😀' (Emoji)|U+1F600 – 4 bytes in UTF-8|
|**Base64 Encoding**||
|Base64|Encoding of binary data as printable ASCII characters (64 different ones)|
|Binary-to-Text Encoding|Makes binary data text-safe|
|6-bit Chunks|Base64 works with 6-bit groups|
|Padding|`=` characters at the end for incomplete groups|
|Base64 Alphabet|64 characters: A–Z, a–z, 0–9, +, /|
|**Base64 Structure**||
|Input: 3 bytes (24 bits)|Input is processed in 3-byte blocks|
|Output: 4 characters|Output is 4 printable characters|
|Expansion|Size increase of ~33% (3 bytes → 4 characters)|
|Reversible|Easily decodable|
|NOT Encryption|NOT encryption – offers no security!|
|**Base64 Padding Rules**||
|No padding|Input is a multiple of 3 bytes → no `=`|
|One `=`|2 bytes remaining → one `=` at the end|
|Two `==`|1 byte remaining → two `==` at the end|
|**Use Cases**||
|Email Attachments|Base64 for binary files in emails (MIME)|
|Data URLs|Embedded images in HTML/CSS (`data:image/png;base64,...`)|
|Authentication Tokens|API keys, JWT tokens often in Base64|
|Binary in JSON/XML|Binary data in text-based formats|
|Certificate Files|SSL/TLS certificates (.pem, .crt files)|
|**Encoding vs Encryption**||
|Encoding|Format conversion, no secrecy (reversible by anyone)|
|Encryption|Secrecy – requires a key to decrypt|
|Obfuscation|Making something harder to read, but not secure|
|**Problems & Errors**||
|Mojibake|Garbled text – wrong decoding (e.g. UTF-8 read as ASCII)|
|Character Corruption|Character distortion due to wrong encoding|
|Data Corruption|Binary data damaged by a text-based system|
|Encoding Mismatch|Sender and receiver use different encodings|
|**Important Commands/Syntax**||
|Python: `str.encode('utf-8')`|Encode string to bytes using UTF-8|
|Python: `bytes.decode('utf-8')`|Decode bytes to string using UTF-8|
|Python: `base64.b64encode()`|Base64 encoding|
|Python: `base64.b64decode()`|Base64 decoding|
|Python: `ord('A')`|Returns ASCII/Unicode code point (65)|
|Python: `chr(65)`|Converts code point to character ('A')|

---

## Windows 11: Exploring Character Encoding

|Function|Instructions|
|---|---|
|**Open Character Map**|`Windows key` → type "charmap" → Enter (shows all Unicode characters)|
|**Display ASCII values**|In Character Map: select character → bottom right shows "U+0041" (hex code point)|
|**PowerShell: Character → Code**|`[int][char]'A'` returns `65`|
|**PowerShell: Code → Character**|`[char]65` returns `A`|
|**Notepad encoding**|Save As → dropdown "Encoding": UTF-8, ANSI, Unicode (UTF-16)|
|**Python for encoding**|Install Python → in CMD/PowerShell: `python`|

**Python examples (Windows CMD/PowerShell):**

```python
# Start Python
python

# ASCII/Unicode values
ord('A')           # → 65
chr(65)            # → 'A'
ord('€')           # → 8364 (U+20AC)

# UTF-8 encoding
'Hello'.encode('utf-8')      # → b'Hello'
'Hällö'.encode('utf-8')      # → b'H\xc3\xa4ll\xc3\xb6'

# Base64
import base64
base64.b64encode(b'Hello World!')          # → b'SGVsbG8gV29ybGQh'
base64.b64decode(b'SGVsbG8gV29ybGQh')     # → b'Hello World!'
```