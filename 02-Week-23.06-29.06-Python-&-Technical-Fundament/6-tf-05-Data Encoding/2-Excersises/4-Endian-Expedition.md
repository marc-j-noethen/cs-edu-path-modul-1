# 🖥️ Endian Expedition - Byte Order Analysis

**Course:** Cyber Security Analyst - Python Basics | **Date:** 27 June 2025

---

## Task

**Objective:** Interpret multi-byte values taking endianness into account and extract data from a hexadecimal data stream

---

## Solution

### Environment
```
Language: Python 3.x
Modules: struct
Concept: Big-Endian vs Little-Endian
```

### Implementation

**Given hex data:** `01 F4 00 0A 1B CD 4F 4B 00`

**Data structure:**
- Message ID: 16-bit unsigned int (2 bytes) - **Big-Endian**
- Timestamp: 32-bit unsigned int (4 bytes) - **Big-Endian**
- Status Message: ASCII string, null-terminated

---

**Step 1: Identify fields**

```
Hex Data: 01 F4 00 0A 1B CD 4F 4B 00
          │────│ │──────────│ │────│ │
          │    │ │          │ │    │ └─ Null terminator
          │    │ │          │ └────┴─── ASCII string
          │    │ └──────────┴────────── Timestamp (4 bytes)
          └────┴────────────────────── Message ID (2 bytes)

Breakdown:
- Bytes 0-1:   01 F4        → Message ID
- Bytes 2-5:   00 0A 1B CD  → Timestamp
- Bytes 6-8:   4F 4B 00     → Status Message + Null
```

---

**Step 2: Endian Conversion**

**Message ID: `01 F4` (Big-Endian)**

```
Manual calculation:
Big-Endian: Most Significant Byte (MSB) first
  01 F4
  │  └─── Least Significant Byte (LSB)
  └────── Most Significant Byte (MSB)

Decimal Value:
  01 × 256 + F4 × 1
  = 1 × 256 + 244 × 1
  = 256 + 244
  = 500

Answer: 500 (decimal)
```

**Timestamp: `00 0A 1B CD` (Big-Endian)**

```
Manual calculation:
Big-Endian: Bytes from left to right, MSB first
  00    0A    1B    CD
  MSB               LSB

Decimal Value:
  00 × 256³ + 0A × 256² + 1B × 256¹ + CD × 256⁰
  = 0 × 16777216 + 10 × 65536 + 27 × 256 + 205 × 1
  = 0 + 655360 + 6912 + 205
  = 662477

Answer: 662477 (decimal)
```

---

**Step 3: Extract ASCII string**

**Bytes: `4F 4B 00`**

```
ASCII Conversion:
  4F (hex) = 79 (dec) = 'O'
  4B (hex) = 75 (dec) = 'K'
  00 (hex) = 0  (dec) = null terminator (not visible)

String: "OK"
```

---

**Python Implementation:**

```python
import struct

# Hex data as bytes
hex_data = "01 F4 00 0A 1B CD 4F 4B 00"
data_bytes = bytes.fromhex(hex_data)

print(f"Raw Bytes: {data_bytes.hex(' ')}")
print(f"Total Length: {len(data_bytes)} bytes")
print()

# Message ID: 2 bytes, Big-Endian unsigned short
message_id_bytes = data_bytes[0:2]
message_id = struct.unpack('>H', message_id_bytes)[0]  # >H = Big-Endian unsigned short
print(f"Message ID (bytes): {message_id_bytes.hex(' ').upper()}")
print(f"Message ID (value): {message_id}")
print()

# Timestamp: 4 bytes, Big-Endian unsigned int
timestamp_bytes = data_bytes[2:6]
timestamp = struct.unpack('>I', timestamp_bytes)[0]  # >I = Big-Endian unsigned int
print(f"Timestamp (bytes): {timestamp_bytes.hex(' ').upper()}")
print(f"Timestamp (value): {timestamp}")
print()

# Status Message: ASCII string until null terminator
status_bytes = data_bytes[6:9]
status_message = status_bytes.decode('ascii').rstrip('\x00')  # Remove null terminator
print(f"Status Message (bytes): {status_bytes.hex(' ').upper()}")
print(f"Status Message (string): '{status_message}'")
print()

# Summary
print("=" * 50)
print("SUMMARY")
print("=" * 50)
print(f"Message ID:      {message_id}")
print(f"Timestamp:       {timestamp}")
print(f"Status Message:  '{status_message}'")
```

**Output:**
```
Raw Bytes: 01 f4 00 0a 1b cd 4f 4b 00
Total Length: 9 bytes

Message ID (bytes): 01 F4
Message ID (value): 500

Timestamp (bytes): 00 0A 1B CD
Timestamp (value): 662477

Status Message (bytes): 4F 4B 00
Status Message (string): 'OK'

==================================================
SUMMARY
==================================================
Message ID:      500
Timestamp:       662477
Status Message:  'OK'
```

---

## Results

| Field | Bytes | Big-Endian Value |
|------|-------|------------------|
| **Message ID** | `01 F4` | **500** (decimal) |
| **Timestamp** | `00 0A 1B CD` | **662477** (decimal) |
| **Status Message** | `4F 4B 00` | **"OK"** |

---

## Notes

- **Learned:** Big-Endian vs Little-Endian, Multi-Byte Integer Interpretation, struct module
- **Endianness:**
  - **Big-Endian:** MSB first (Network Byte Order)
    - Example: 0x01F4 → `01 F4` (human-readable)
  - **Little-Endian:** LSB first (Intel x86/x64)
    - Example: 0x01F4 → `F4 01` (stored in reverse)
- **struct format strings:**
  - `>` = Big-Endian
  - `<` = Little-Endian
  - `H` = unsigned short (2 bytes)
  - `I` = unsigned int (4 bytes)
  - `B` = unsigned char (1 byte)
- **Network protocols:** Typically use big-endian (RFC 1700)
- **Why is this important?** Same bytes, different interpretation depending on endianness
  - `01 F4` → Big-endian: 500, Little-endian: 62721
- **Python bytes.fromhex():** Converts a hex string to bytes
- **ASCII null terminator:** `\x00` or `0x00` marks the end of the string (C-style)
- **Tip:** Always document endianness for network data!

