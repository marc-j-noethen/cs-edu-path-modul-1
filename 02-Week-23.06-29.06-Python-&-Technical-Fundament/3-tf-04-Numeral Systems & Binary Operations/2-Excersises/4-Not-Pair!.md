# 🖥️ Not Pair! - Parity Checking

**Course:** Cyber Security Analyst - Technical Fundament Basics | **Date:** 25 June 2025

---

## Task

**Objective:** Understand and implement parity checking for error detection

**Task:**
- **Part 1:* * Manually verify 4 packets with even parity
- **Part 2:** Write the Python function `has_even_parity()`
- **Part 3:** Write the Python function `generate_even_parity_bit()`

**Concept:** Even parity = total number of 1s is even (including parity bit)

---

## Solution

### Environment
```
Method: Manual counting + Python implementation
Tools: Binary counting, Python 3.x
```

### Procedure

---

## Part 1: Manual Verification

**Packet 1: `11010110`**
```
Count the 1s: 1,1,0,1,0,1,1,0
Total: 1+1+0+1+0+1+1+0 = 5
5 is odd → Even Parity INCORRECT
```
**Status:** ❌ **Incorrect**

---

**Packet 2: `00111001`**
```
Count the 1s: 0,0,1,1,1,0,0,1
Total: 0+0+1+1+1+0+0+1 = 4
4 is even → Even Parity CORRECT
```
**Status:** ✅ **Correct**

---

**Packet 3: `10101011`**
```
Count the 1s: 1,0,1,0,1,0,1,1
Total: 1+0+1+0+1+0+1+1 = 5
5 is odd → Even Parity INCORRECT
```
**Status:** ❌ **Incorrect**

---

**Packet 4: `01100011`**
```
Count the 1s: 0,1,1,0,0,0,1,1
Total: 0+1+1+0+0+0+1+1 = 4
4 is even → Even Parity CORRECT
```
**Status:** ✅ **Correct**

---

## Part 2: Python - Parity Checker

**Function:** Checks whether an 8-bit packet has even parity

```python
def has_even_parity(packet_string):
    """
    Checks whether a binary string has even parity.
    
    Args:
        packet_string: 8-bit binary string (e.g. "11010110")
    
    Returns:
        True if the number of 1s is even, otherwise False
    """
    # Count the number of '1's in the string
    count_ones = packet_string.count('1')
    
    # Check if even (modulo 2 is 0)
    return count_ones % 2 == 0


# Tests
print(has_even_parity("11010110"))  # False (5 ones)
print(has_even_parity("00111001"))  # True  (4 ones)
print(has_even_parity("10101011"))  # False (5 ones)
print(has_even_parity("01100011"))  # True  (4 ones)
```

---

## Part 3: Python - Parity Bit Generator

**Function:** Generates the parity bit for 7-bit data

```python
def generate_even_parity_bit(data_bits_string):
    """
    Generates the even parity bit for 7-bit data.
    
    Args:
        data_bits_string: 7-bit binary data string (e.g. "1101011")
    
    Returns:
        Parity bit as a string: "0" or "1"
    """
    # Count the number of '1's in the data bits
    count_ones = data_bits_string.count('1')
    
    # If the number is odd: Parity bit = 1 (makes the total even)
    # If the number is even: Parity bit = 0 (keeps the total even)
    if count_ones % 2 == 0:
        return "0"
    else:
        return "1"


# Tests
print(generate_even_parity_bit("1101011"))  # "0" (4 ones → even)
print(generate_even_parity_bit("0011100"))  # "1" (3 ones → odd)
print(generate_even_parity_bit("1010101"))  # "0" (4 ones → even)
print(generate_even_parity_bit("0000000"))  # "0" (0 ones → even)
```

---

## Results

### Part 1: Manual Verification

| Packet | Binary | Number of 1s | Status |
|--------|--------|------------|--------|
| 1 | `11010110` | 5 (odd) | ❌ **Incorrect** |
| 2 | `00111001` | 4 (even) | ✅ **Correct** |
| 3 | `10101011` | 5 (odd) | ❌ **Incorrect** |
| 4 | `01100011` | 4 (even) | ✅ **Correct** |

### Part 2: Python Code
```python
def has_even_parity(packet_string):
    count_ones = packet_string.count('1')
    return count_ones % 2 == 0
```

### Part 3: Python Code
```python
def generate_even_parity_bit(data_bits_string):
    count_ones = data_bits_string.count('1')
    return "0" if count_ones % 2 == 0 else "1"
```

---

## Notes

- **Learnt:** Parity checking for error detection, even vs odd parity
- **Even parity:** The total number of 1s must be even (0, 2, 4, 6, 8)
- **Odd Parity:** The total number of 1s must be odd (1, 3, 5, 7)
- **Limitation:** Parity detects single-bit errors, but not when 2 or more bits flip
- **Application:** Serial communication (UART), RAM (ECC), data transmission
- **Modulo trick:** `count % 2 == 0` checks for an even number
- **Alternative:** XOR of all bits yields the parity bit (XOR chain)
- **Tip:** `str.count('1')` is efficient for parity calculation in Python


