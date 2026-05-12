## **📊 Summary according to the 80/20 Principle**

### Numeral Systems & Binary Operations

### 1. Place Value and Base Determine How Computers Understand Numbers

The 80/20 core is: every number depends on its base and the position of its digits. Humans mostly work with decimal numbers, computers internally with binary numbers, and in practice hexadecimal is the compact readable layer in between.

### 2. Step-by-Step Core Process

1. First determine the base: decimal works with 10, binary with 2, hexadecimal with 16 symbols.
2. Break the number down into place values based on powers of the respective base.
3. For human readability, binary numbers are often converted to hex, because 4 bits equal exactly 1 hex digit.
4. For bit operations, check each bit individually: AND masks, OR sets bits, XOR compares differences, shifts move values.

### 3. Interactive Mode / Tool Usage

The fastest way to learn this topic is to look at the same number in decimal, binary, and hex in parallel. Particularly useful are the calculator in Programmer mode and a Python REPL.

### 4. The Most Important Concepts with Code Examples

- **Bit, Byte, Nibble:** 1 bit is the smallest unit, 8 bits are 1 byte, 4 bits are 1 nibble.
- **MSB and LSB:** The leftmost bit carries the highest place value, the rightmost the lowest.
- **Hex as shorthand for binary:** Two hex digits cover exactly one byte.
- **Two's Complement:** This is how negative numbers are efficiently represented in the binary system.

```python
value = 42
print(bin(value))          # 0b101010
print(hex(value))          # 0x2a
print(int("101010", 2))    # 42
a = 0b1100   # 12
b = 0b1010   # 10
print(a & b)  # 8
print(a | b)  # 14
print(a ^ b)  # 6
print(a << 1) # 24
```

### 5. Comparison: Decimal vs. Binary vs. Hexadecimal

- Decimal is intuitive for humans because we use it every day.
- Binary is ideal for computers because hardware distinguishes between two states.
- Hex is the practical bridge because long bit sequences become short and easy to read.

### 6. Why This Matters / Advantages

This knowledge comes up everywhere: in memory values, network analysis, file formats, hashes, IPv6, MAC addresses, reverse engineering, and in any kind of low-level debugging.

**Quick-Start Checklist**

- ☐ I can explain what a base in a number system is.
- ☐ I can roughly convert a binary number to decimal.
- ☐ I understand why hexadecimal is so practical for binary data.
- ☐ I know the basic idea of AND, OR, XOR, and bit shifts.
- ☐ I know that negative numbers are often represented using Two's Complement.

**Memory Aid** Number systems are not fringe theory — they are the language in which computers actually express memory, networks, and machine instructions.

---

## Table 1: Tools Used

|Tool|Meaning|
|---|---|
|Programmer Calculator|Converts numbers directly between decimal, binary, and hex|
|Python REPL|Quickly tests conversions and bit operations via code|
|Online Converter|Helps cross-check calculation steps|
|Wireshark|Displays raw data and headers often in hexadecimal|

## Table 2: Technical Terms

|Term|Meaning|
|---|---|
|Numeral System|System for representing numbers with a fixed base|
|Bit|Smallest unit of digital information, with value 0 or 1|
|Byte|Group of 8 bits|
|Nibble|Group of 4 bits, corresponds to exactly one hex digit|
|MSB|Most Significant Bit with the highest place value|
|Two's Complement|Standard method for representing negative integers|

## Table 3: Important Vocabulary

|Vocabulary|Meaning|
|---|---|
|convert|to transform from one form to another|
|remainder|the amount left over after division|
|shift|to move bits left or right|
|mask|a bit pattern used to select specific bits|
|signed|includes a sign (positive or negative)|
|unsigned|no sign, positive values only|