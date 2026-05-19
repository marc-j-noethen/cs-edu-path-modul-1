# 🐍 Anarchy Reins (Advanced Wireshark)

**Course:** Cyber Security Analyst - Network Technology | **Date:** 19 July 2025

---

## Task

**Objective:**  
Fully reconstruct the IM and file transfer details from `anarchy.pcap` / `evidence01.pcap`.

**Requirements:**

- Identify the IM contact and the first message.
- Identify the file transfer.
- Specify the magic number and MD5 of the transferred document.
- State the content of the secret recipe from the extracted DOCX.

- Output:

    - six direct answers to the task’s questions
    - filename, magic number and MD5 of the transfer
    - Extracted recipe content

---

## Solution

```text
Answers:
1. Ann’s IM buddy: Sec558user1
2. Opening message:
   Here’s the secret recipe... I just downloaded it from the file server. Just copy it to a USB stick and you’re good to go >:-)
3. Name of the transferred file: recipe.docx
4. First four bytes / Magic Number of the actual file: 50 4B 03 04
5. MD5 of the extracted file: 8350582774e1d4dbe1d61d64c89e0ea1
6. Secret recipe:
   Recipe for Disaster:
   - 1 serving
   - Ingredients: 4 cups sugar, 2 cups water
   - In a medium saucepan, bring the water to the boil. Add sugar.
     Stir gently over a low heat until the sugar has completely dissolved.
     Remove the saucepan from the heat. Allow to cool completely.
     Pour into the petrol tank. Repeat as necessary.

Verification notes:
- The AIM message is visible directly in the OSCAR text.
- `recipe.docx` appears in the OFT2 / Cool FileXfer stream.
- The transferred DOCX can be carved from the stream; the file size is 12008 bytes.
- `word/document.xml` in the DOCX contains the recipe text.
```

**Alternative (compact):**

```text
The IM message reveals the leak, the OFT2 transfer reveals the file, and the recipe can be reconstructed directly from the DOCX.
```

---

## Tests

|Input 1|Input 2|Input 3|Expected|Result|✓|
|---|---|---|---|---|---|
|`OSCAR chat`|`Buddy name`|`first message`|`IM replies clear`|`yes`|✅|
|`OFT2`|`recipe.docx`|`PK0304`|`File transfer matches`|`yes`|✅|
|`DOCX carved`|`MD5`|`document.xml`|`Recipe content readable`|`yes`|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|OSCAR / AIM|AOL Instant Messenger transmits messages and file transfers using its own protocol components.|
|File Carving|Files are reconstructed from a data stream using signatures and structures.|
|OOXML / DOCX|DOCX is internally a ZIP archive; the actual text is stored, for example, in `word/document.xml`.|

---

## Rules / Logic

```text
Search terms such as `recipe`, `OFT2` and `PK\x03\x04` significantly speed up the analysis.
A file signature is more reliable than the file extension alone.
With OOXML files, it is always worth taking a look at `word/document.xml` after carving.
```

---

## Notes

- **Verified:** Buddy, message, filename, magic number, MD5 and recipe text were derived from the original PCAP or the DOCX file reconstructed directly from it.
- **Important:** The OFT2 signature belongs to the AIM file transfer container; the actual DOCX signature is only visible within the stream.
- **Tip:** After carving, it is worth hashing the file before opening it.

---

## Optional: Extensions

- Extract the entire file transfer automatically using a small parser.
- Correlate the exact stream and the roles of the two IP addresses in time once again.

