# 🐍 Compression Olympics (Compression)

**Course:** Cyber Security Analyst - Network Technology | **Date:** 1 August 2025

---

## Task

**Objective:**  
Compare the compression size and runtime of `gzip`, `bzip2` and `xz` for the same text file.

**Requirements:**

- Use a large text file as a basis for comparison.
- Record the compression sizes for `gzip`, `bzip2` and `xz`.
- Compare compression and decompression times.
- Justify the choice of each tool based on the situation.

- Output:

    - Smallest resulting file
    - Fastest tool for compression and decompression
    - Practical tool selection

---

## Solution

```text
Test data:
- File: Alice's Adventures in Wonderland (`alice.txt`)
- Original size: 151,191 bytes

Measured results:
- gzip  -> 53,357 bytes, compression approx. 18,750 ms, decompression approx. 0.886 ms
- bzip2 -> 42,743 bytes, compression approx. 15,909 ms, decompression approx. 4,761 ms
- xz    -> 47,636 bytes, compression approx. 54.353 ms, decompression approx. 2.646 ms

Answers:
1. Smallest file in this run: bzip2
2. Fastest compression in this run: bzip2
3. Fastest decompression in this run: gzip
4. Choice depending on the situation:
   - gzip: when very fast decompression and wide availability are important
   - bzip2: when better compression is more important than decompression speed for text data
   - xz: when maximum or very good compression is more important than compression time

Note:
Exact millisecond values depend on the CPU, implementation and tool version.
The relative observation – the trade-off between size and speed – remains technically the same.
```

**Alternative (compact):**

```text
Compression is always a trade-off between file size, CPU time and decompression speed.
```

---

## Tests

|Input 1|Input 2|Input 3|Expected|Result|✓|
|---|---|---|---|---|---|
|`alice.txt`|`3 algorithms`|`size`|`comparable`|`yes`|✅|
|`compress time`|`decompress time`|`same source`|`fair comparison`|`yes`|✅|
|`Tool selection`|`Practical case`|`Trade-off`|`Justifiable`|`yes`|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|Compression Ratio|Ratio between the original and target file sizes.|
|Throughput|How quickly a tool compresses or decompresses.|
|Workload Dependence|Depending on the data type, the results between algorithms can vary significantly.|

---

## Rules / Logic

```text
The smallest archive is not automatically the best choice.
Always benchmark the same input under conditions that are as consistent as possible.
Tool selection depends on the objective: archive size, CPU time or decompression speed.
```

---

## Notes

- **Verified:** The figures above are taken from a real run on the same text file.
- **Important:** Different Linux distributions or preset levels may slightly alter the order.
- **Tip:** `gzip` often wins for deployments and logs, whilst `xz` or `bzip2` are frequently better for archiving.

---

## Optional: Extensions

- Additionally, compare `xz -0` to `xz -9`.
- Test the same algorithms on binary data and on files that are already compressed.

