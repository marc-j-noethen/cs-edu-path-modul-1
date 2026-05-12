# 🖥️ Bitwise Combination Lock - Operation Sequencing

**Course:** Cyber Security Analyst - Technical Foundation Basics | **Date:** 25 June 2025

---

## Task

**Objective:** Determine the correct sequence of three bitwise operations to transform a starting value into a target value

**Task:**
- **Starting value:** `10110110` (Binary)
- **Target value:** `11100001` (Binary)
- **Available operations:**
  - Op 1: `XOR 11001100`
  - Op 2: `Right Shift >> 2` (logical, zeros from the left)
  - Op 3: `OR 00110011`
- Use each operation exactly once

---

## Solution

### Environment
```
Method: Systematic trial and error of all permutations
Number of possible sequences: 3! = 6
```

### Procedure

**Strategy:** Try out all 6 possible sequences

---

**Attempt 1: Op1 → Op2 → Op3**

```
Start:     10110110
Op1 (XOR): 10110110 XOR 11001100 = 01111010
Op2 (>>2): 01111010 >> 2         = 00011110
Op3 (OR):  00011110 OR 00110011  = 00111111
❌ Result: 00111111 ≠ 11100001
```

---

**Attempt 2: Op1 → Op3 → Op2**

```
Start:     10110110
Op1 (XOR): 10110110 XOR 11001100 = 01111010
Op3 (OR):  01111010 OR 00110011  = 01111011
Op2 (>>2): 01111011 >> 2         = 00011110
❌ Result: 00011110 ≠ 11100001
```

---

**Attempt 3: Op2 → Op1 → Op3**

```
Start:     10110110
Op2 (>>2): 10110110 >> 2         = 00101101
Op1 (XOR): 00101101 XOR 11001100 = 11100001
Op3 (OR):  11100001 OR 00110011  = 11110011
❌ Result: 11110011 ≠ 11100001
```

---

**Attempt 4: Op2 → Op3 → Op1** ✅

```
Start:     10110110

Op2 (Right Shift >> 2):
  10110110 >> 2
  Insert two zeros from the left
  = 00101101

Op3 (OR 00110011):
  0 0 1 0 1 1 0 1
  0 0 1 1 0 0 1 1
  ---------------
  0 0 1 1 1 1 1 1 = 00111111

Op1 (XOR 11001100):
  0 0 1 1 1 1 1 1
  1 1 0 0 1 1 0 0
  ---------------
  1 1 1 0 0 0 1 1 = 11100011

❌ Result: 11100011 ≠ 11100001
```

---

**Attempt 5: Op3 → Op1 → Op2**

```
Start:     10110110
Op3 (OR):  10110110 OR 00110011  = 10110111
Op1 (XOR): 10110111 XOR 11001100 = 01111011
Op2 (>>2): 01111011 >> 2         = 00011110
❌ Result: 00011110 ≠ 11100001
```

---

**Attempt 6: Op3 → Op2 → Op1** ✅

```
Start:     10110110

Op3 (OR 00110011):
  1 0 1 1 0 1 1 0
  0 0 1 1 0 0 1 1
  --- ------------
  1 0 1 1 0 1 1 1 = 10110111

Op2 (Right Shift >> 2):
  10110111 >> 2
  = 00101101

Op1 (XOR 11001100):
  0 0 1 0 1 1 0 1
  1 1 0 0 1 1 0 0
  ---------------
  1 1 1 0 0 0 0 1 = 11100001

✅ Result: 11100001 = Target value!
```

---

## Results

| Attempt | Sequence | Result | Status |
|---------|---------|----------|--------|
| 1 | Op1 → Op2 → Op3 | 00111111 | ❌ |
| 2 | Op1 → Op3 → Op2 | 00011110 | ❌ |
| 3 | Op2 → Op1 → Op3 | 11110011 | ❌ |
| 4 | Op2 → Op3 → Op1 | 11100011 | ❌ |
| 5 | Op3 → Op1 → Op2 | 00011110 | ❌ |
| 6 | Op3 → Op2 → Op1 | **11100001** | ✅ |

**Correct sequence:** **Operation 3, then Operation 2, then Operation 1**

Or: **OR 00110011, then Right Shift >> 2, then XOR 11001100**

---

## Notes

- **Learned:** The order of bitwise operations is crucial; systematic testing
- **Right Shift (>>):** Bits shift to the right, zeros fill in from the left
- **OR operation:** At least one bit must be 1 → Result 1
- **XOR operation:** Bits different → 1, same → 0
- **Methodology:** With 3 operations = 6 permutations (3! = 6)
- **Tip:** Work backwards from the target where possible (not trivial here due to the shift)
- **Python check:** `((0b10110110 | 0b00110011) >> 2) ^ 0b11001100`


