# 🖥️ Base(ic) Training - Number System Conversions

**Course:** Cyber Security Analyst - Technical Fundament Basics | **Date:** 25 June 2025

---

## Task

**Objective:** To demonstrate basic number system conversions and binary operations

**Task:**
1. Decimal 99 → 8-bit Binary
2. Hexadecimal 0xE4 → Decimal
3. Binary 10100101 → Hexadecimal
4. Binary Addition: 11010011 + 01011101
5. Bitwise AND: 11110000 AND 10101010

---

## Solution

### Environment
```
Method: Manual calculation / Python (optional for verification)
Tools: Calculator, conversion tables
```

### Procedure

**Task 1:** Decimal 99 → 8-bit Binary

```
Method: Repeated division by 2
99 ÷ 2 = 49 Remainder 1  (LSB)
49 ÷ 2 = 24 Remainder 1
24 ÷ 2 = 12 Remainder 0
12 ÷ 2 = 6  Remainder 0
6  ÷ 2 = 3  Remainder 0
3  ÷ 2 = 1  Remainder 1
1  ÷ 2 = 0  remainder 1  (MSB)

Read from bottom to top: 1100011
With leading 0 for 8-bit: 01100011
```
**Result:** `01100011`

---

**Task 2:** Hexadecimal 0xE4 → Decimal

```
Method: Place-value method
0xE4 = E × 16¹ + 4 × 16⁰
     = 14 × 16 + 4 × 1
     = 224 + 4
     = 228
```
**Result:** `228`

---

**Task 3:** Binary 10100101 → Hexadecimal

```
Method: Grouping into 4-bit nibbles
10100101 → 1010 | 0101
           
1010 (binary) = 10 (decimal) = A (hex)
0101 (binary) = 5  (decimal) = 5 (hex)

Combined: A5
```
**Result:** `0xA5`

---

**Task 4:** Binary Addition: 11010011 + 01011101

```
Method: Columnar addition with carry

    1 1 1 1 1     (carry)
    1 1 0 1 0 0 1 1
  + 0 1 0 1 1 1 0 1
  -------------------
  1 0 0 1 1 0 0 0 0

Step by step:
Position 0: 1 + 1 = 10₂ → 0, carry 1
Position 1: 1 + 0 + 1 = 10₂ → 0, carry 1
Position 2: 0 + 1 + 1 = 10₂ → 0, carry 1
Position 3: 0 + 1 + 1 = 10₂ → 0, carry 1
Position 4: 1 + 1 + 1 = 11₂ → 1, carry 1
Position 5: 1 + 0 + 1 = 10₂ → 0, carry 1
Position 6: 1 + 1 + 1 = 11₂ → 1, carry 1
Position 7: 0 + 0 + 1 = 1₂ → 1, carry 0
```
**Result:** `100110000` (9-bit) or `00110000` (8-bit with overflow)

---

**Task 5:** Bitwise AND: 11110000 AND 10101010

```
Method: Bit-by-bit comparison (1 AND 1 = 1, otherwise 0)

  1 1 1 1 0 0 0 0
  1 0 1 0 1 0 1 0
  ---------------
  1 0 1 0 0 0 0 0

Bit by bit:
1 AND 1 = 1
1 AND 0 = 0
1 AND 1 = 1
1 AND 0 = 0
0 AND 1 = 0
0 AND 0 = 0
0 AND 1 = 0
0 AND 0 = 0
```
**Result:** `10100000`

---

## Results

| Task | Input | Result |
|---------|---------|----------|
| 1. Decimal → Binary | 99 | `01100011` |
| 2. Hex → Decimal | 0xE4 | `228` |
| 3. Binary → Hex | 10100101 | `0xA5` |
| 4. Binary Addition | 11010011 + 01011101 | `100110000` |
| 5. Bitwise AND | 11110000 AND 10101010 | `10100000` |

---

## Notes

- **Learned:** Number system conversions, binary addition, bitwise operations
- **Decimal → Binary:** Repeated division by 2, read remainders from bottom to top
- **Hex → Decimal:** E = 14, F = 15 in the hexadecimal system
- **Binary → Hex:** Always 4 bits = 1 hex digit (nibble)
- **Binary Addition:** Watch out for carry-overs! 1 + 1 = 10₂ (0 with a carry of 1)
- **AND operation:** Both bits must be 1 to give a result of 1
- **Tip:** Use Python for verification: `bin(99)`, `int('E4', 16)`, `hex(0b10100101)`

