# 🖥️ Encoding Essentials - ASCII, UTF-8 & Base64

**Course:** Cyber Security Analyst - Technical Fundament Basics | **Date:** 27 June 2025

---

## Task

**Objective:** Practise ASCII/UTF-8 representation and Base64 encoding/decoding using standard tools

---

## Solution

### Environment
```
OS: Ubuntu
Shell: bash
Tools: echo, xxd, base64
```

### Procedure

**Step 1:** ASCII decimal value for 'A'
```bash
# Display ASCII table
man ascii

# Or direct method
printf "%d\n" "'A"
```
**Output:** `65`

**Answer:** The ASCII decimal value for 'A' is **65**

---

**Step 2:** UTF-8 bytes for the euro symbol '€'
```bash
# Display the euro symbol in hex bytes
echo -n '€' | xxd -p
```
**Output:** `e282ac`

**Analysis:**
- Hex bytes: `E2 82 AC`
- Number of bytes: **3 bytes**

**Why can’t 7-bit ASCII represent '€'?**
- Standard ASCII uses only 7 bits (0–127 decimal, 0x00–0x7F hex)
- The euro symbol € has the Unicode codepoint U+20AC
- U+20AC lies well outside the ASCII range (20AC hex = 8364 decimal)
- UTF-8 requires 3 bytes for encoding: `11100010 10000010 10101100`

---

**Step 3:** Base64 Encoding
```bash
# Encode the string "Cyber"
echo -n "Cyber" | base64
```
**Output:** `Q3liZXI=`

```bash
# Encode the string "Encoding is fun!"
echo -n "Encoding is fun!" | base64
```
**Output:** `RW5jb2RpbmcgaXMgZnVuIQ==`

---

**Step 4:** Base64 Decoding
```bash
# Decode Base64 string
echo "RGF0YSBFbmNvZGluZyBSb2NrcyE=" | base64 -d
```
**Output:** `Data Encoding Rocks!`

---

## Results

| Question | Answer |
|-------|---------|
| ASCII decimal for 'A' | `65` |
| UTF-8 hex bytes for '€' | `E2 82 AC` |
| Number of bytes for '€' | `3 bytes` |
| Why no ASCII for '€'? | ASCII is 7-bit (0-127), € is Unicode U+20AC (8364 decimal) – outside the ASCII range |
| Base64 of "Cyber" | `Q3liZXI=` |
| Base64 of "Encoding is fun!" | `RW5jb2RpbmcgaXMgZnVuIQ==` |
| Decoded "RGF0YSBFbmNvZGluZyBSb2NrcyE=" | `Data Encoding Rocks!` |

---

## Notes

- **Learnt:** ASCII vs UTF-8, multi-byte encodings, Base64 encoding/decoding
- **ASCII:** 7-bit (128 characters: 0-127), primarily English characters
- **UTF-8:** variable-length encoding (1-4 bytes)
  - 1 byte: ASCII-compatible (0x00–0x7F)
  - 2 bytes: Latin, Greek, Cyrillic
  - 3 bytes: € and most other characters
  - 4 bytes: Emojis, rare characters
- **Base64:** Convert binary data to ASCII text (6 bits → 1 ASCII character)
  - Alphabet: A-Z, a-z, 0-9, +, /
  - Padding: `=` for alignment to 4-character blocks
  - Purpose: Secure transmission of binary data via text protocols
- **xxd:** Hex dump tool, `-p` = plain hex output
- **echo -n:** `-n` prevents a newline at the end

