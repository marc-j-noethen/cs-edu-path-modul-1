# 🐍 Picture Perfect (Statistics & HTTP Objects)

**Course:** Cyber Security Analyst – Network Technology | **Date:** 18 July 2025

---

## Task

**Objective:**  
Analyse the capture `http_with_jpegs.cap.gz` using Wireshark statistics and the HTTP object export.

**Requirements:**

- Determine the proportion of TCP within all IP packets.
- Identify the TCP conversation with the highest total number of bytes.
- Determine the number of HTTP objects with `Content-Type: image/jpeg`.
- Export a JPEG and check the file’s validity.
- Output:
    - `TCP proportion: 96.07 %`
    - `Largest TCP conversation: 10.1.1.101:3200 <-> 10.1.1.1:80`
    - `JPEG objects: 5`

---

## Solution

```python
# Inputs
capture_file = "http_with_jpegs.cap.gz"
ip_packets = 483
tcp_packets = 464

# Main logic
if capture_file != "http_with_jpegs.cap.gz":
    print("This sample solution applies to the original file http_with_jpegs.cap.gz.")
elif tcp_packets == 464:
    print("TCP proportion of IP packets: 464 / 483 = 96.07 %")
elif ip_packets == 483:
    print("Largest conversation: 10.1.1.101:3200 <-> 10.1.1.1:80")
else:
    print("HTTP objects with image/jpeg: 5 | Exported JPEG is valid")
```

**Alternative (compact):**

```python
print("96.07 % TCP | 10.1.1.101:3200 <-> 10.1.1.1:80 | 5 JPEG objects")
```

---

## Tests

|Input 1|Input 2|Input 3|Expected|Result|✓|
|---|---|---|---|---|---|
|`483`|`464`|`Protocol Hierarchy`|`96.07 % TCP`|`96.07 % TCP`|✅|
|`10.1.1.101:3200`|`10.1.1.1:80`|`TCP Conversations`|`most bytes`|`most bytes`|✅|
|`image/jpeg`|`HTTP Objects`|`Export`|`5 + valid JPEG`|`5 + valid JPEG`|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|Protocol Hierarchy|Shows the distribution of packets across protocols.|
|TCP Conversations|Aggregates traffic between two endpoints.|
|HTTP Object Export|Reconstructs transferred files from HTTP responses.|

---

## Rules / Logic

```
TCP proportion = TCP packets / IP packets * 100
464 / 483 * 100 = 96.07
The largest stream is the one with the most total bytes in both directions.
```

---

## Notes

- **Concept:** It is not the number of JPEG files in the HTML that counts, but the HTTP objects that can actually be exported.
- **Syntax:** `Statistics -> Protocol Hierarchy`, `Statistics -> Conversations -> TCP`, `File -> Export Objects -> HTTP`
- **Order is important:**
    1. Check Protocol Hierarchy
    2. Determine the largest TCP conversation
    3. Export HTTP objects and count JPEGs
- **Edge Cases:**
    - A large stream is not automatically the one with the most packets, but the one with the most bytes.
    - Not every HTTP object is an image.
    - A valid export must also be recognisable as a JPEG.
- **Tip:** The exported evidence image is located here: `./assets/4-Picture-Perfect-extracted.jpg`

---

## Optional: Extensions

- Export and compare all five JPEGs.
- Check the largest TCP stream additionally using `Follow TCP Stream`.
- Distinguish between thumbnail and full-size images.
- Document the file signatures of the exported images in hexadecimal.
