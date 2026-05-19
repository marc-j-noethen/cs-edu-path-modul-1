# Picture Perfect (Advanced Wireshark)

**Course:** Cyber Security Analyst – Network Technology | **Date:** 19 July 2025

---

## Task

**Objective:**  
Work with Wireshark’s statistical functions and HTTP object export.

**Requirements:**

- Open `http_with_jpegs.cap.gz`.
- Analyse the Protocol Hierarchy and TCP Conversations.
- Export HTTP Objects.
- Identify JPEG files.

---

## Solution

```text
Procedure:
1. Unzip the capture and open it in Wireshark.
2. Go to Statistics -> Protocol Hierarchy -> Read the TCP percentage under IP.
3. Go to Statistics -> Conversations -> TCP -> Sort by bytes.
4. Go to File -> Export Objects -> HTTP -> Filter for `image/jpeg`.
5. Save a JPEG file and open it locally.
```

**Alternative (compact):**

```text
Three things are required:
- TCP percentage under IP
- Largest TCP conversation by bytes
- Number of exportable JPEG objects
```

---

## Tests

|Scenario|Expected|Result|✓|
|---|---|---|---|
|Protocol Hierarchy|TCP percentage visible|correct|✅|
|TCP Conversations|Largest connection by bytes identifiable|correct|✅|
|Export Objects -> HTTP|JPEGs visible and exportable|correct|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|Protocol Hierarchy|Shows the distribution of protocols in the capture.|
|Conversations|Groups traffic by endpoints.|
|HTTP Object Export|Extracts payload objects such as images from HTTP traffic.|

---

## Rules / Logic

```text
Statistics provide an aggregated view of the capture.
Sort conversations by bytes for the largest transfer.
HTTP objects show content, not just headers.
```

---

## Notes

- **Concept:** Wireshark is not just a packet list, but also a statistics and extraction tool.
- **Syntax:** Knowing the menu paths saves a lot of time.
- **Order is important:**
    1. Load capture
    2. Read statistics
    3. Export objects
- **Edge cases:**
    - Compressed or fragmented content.
    - Not every image is available in the HTTP Object Export in a clean format.
    - HTTPS cannot be exported without a key.
- **Tip:** When exporting objects, always sort by Content-Type.

---

## Optional: Extensions

- Compare multiple image types.
- View the largest conversation in more detail using Follow TCP Stream.
- Repeat the same process with other sample captures.

