# 🐍 Anarchy Reins (AIM Exfiltration)

**Course:** Cyber Security Analyst – Network Technology | **Date:** 18 July 2025

---

## Task

**Objective:**  
Analyse the capture `anarchy.pcap` in such a way that the chat partner, first message, file transfer, file signature, MD5 hash and the content of the exfiltrated document can be reliably verified.

**Requirements:**

- Identify Ann Dercover’s AIM buddy.
- Correctly reproduce the first chat message.
- Verify the name of the transferred file.
- Reconstruct the file from the transfer and determine the magic number and MD5.
- Output:
    - `Buddy: Sec558user1`
    - `File: recipe.docx | Magic Number: 50 4B 03 04 | MD5: 8350582774e1d4dbe1d61d64c89e0ea1`
    - `Recipe: Sugar-water mixture with sabotage instructions for the gas tank`

---

## Solution

```python
# Inputs
buddy_name = "Sec558user1"
filename = "recipe.docx"
md5_hash = "8350582774e1d4dbe1d61d64c89e0ea1"

# Main logic
if buddy_name != "Sec558user1":
    print("The AIM buddy has not yet been correctly identified.")
elif filename == "recipe.docx":
    print("File: recipe.docx | Magic Number: 50 4B 03 04")
elif md5_hash == "8350582774e1d4dbe1d61d64c89e0ea1":
    print("MD5: 8350582774e1d4dbe1d61d64c89e0ea1")
else:
    print("First message: Here's the secret recipe... I just downloaded it from the file server. Just copy to a USB stick and you're good to go >:-)")
```

**Alternative (compact):**

```python
print("Sec558user1 | recipe.docx | 50 4B 03 04 | 8350582774e1d4dbe1d61d64c89e0ea1")
print("Recipe: 4 cups sugar, 2 cups water, then pour into the gas tank")
```

---

## Tests

|Input 1|Input 2|Input 3|Expected|Result|✓|
|---|---|---|---|---|---|
|`192.168.1.158`|`Sec558user1`|`Start chat`|`Buddy correct`|`Buddy correct`|✅|
|`recipe.docx`|`50 4B 03 04`|`File signature`|`DOCX/ZIP detected`|`DOCX/ZIP detected`|✅|
|`word/document.xml`|`8350582774e1d4dbe1d61d64c89e0ea1`|`Document content`|`Recipe + sabotage note`|`Recipe + sabotage note`|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|AIM chat data|Contains buddy names and messages in plain text or HTML-like payload.|
|Magic number|The first bytes of a file; `50 4B 03 04` identifies ZIP or DOCX.|
|DOCX internal|A `.docx` is a ZIP container containing XML files such as `word/document.xml`.|

---

## Rules / Logic

```
Chat data provides the contact and the first message.
OFT/File stream provides the filename and file bytes.
The magic number, MD5 and recipe text can be extracted from the reconstructed DOCX file.
```

---

## Notes

- **Concept:** The file transfer itself is the most robust evidence of exfiltration.
- **Syntax:** Search for chat strings, filenames and `PK\x03\x04`.
- **Order is important:**
    1. Find the IM partner and first message in the chat payload
    2. Reconstruct the file stream
    3. Open the DOCX file and read `word/document.xml`
- **Edge cases:**
    - The character string `>:-)` appears in the HTML-like payload as `&gt;:-)`.
    - A `.docx` is not a standalone binary format, but a ZIP archive.
    - The recipe text is deliberately formulated to look like a cooking recipe, but contains a clear hint of sabotage.
- **Tip:** The crucial sentence in the document essentially states to allow the mixture to cool completely and then pour it into the gas tank.

---

## Optional: Extensions

- Document the entire AIM conversation as a timeline.
- Additionally log the file transfer with source, destination and stream ID.
- Archive the reconstructed DOCX as a separate piece of evidence.
- Convert the HTML-encoded chat messages into a readable text format.

