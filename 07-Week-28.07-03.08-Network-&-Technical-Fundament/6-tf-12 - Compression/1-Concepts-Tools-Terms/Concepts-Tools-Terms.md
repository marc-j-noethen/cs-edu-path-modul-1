## 📊 Summary based on the 80/20 principle

### What is data compression?

Data compression means representing information using fewer bits than the original. Like the abbreviation "LOL" instead of "Laugh Out Loud" – but for digital data.

**Two main reasons for compression:**

1. **Saving storage space**: Store more data on hard drives, SSDs or in the cloud
2. **Faster transmission**: Smaller files are transferred more quickly over the internet

**Cybersecurity relevance:**

- Log files are compressed to save space
- Malware can be compressed to make detection harder
- Compressed archives can contain malicious content

### The two main categories

#### 1. Lossless Compression

**Principle:** No data is lost – after decompression you get an exact copy of the original.

**Use cases:**

- Text documents and source code
- Executable programmes (.exe, .dll)
- Log files
- Certain image formats (PNG, GIF)

**Common formats:**

- ZIP (most widespread on Windows)
- Gzip (.gz)
- Bzip2 (.bz2)
- XZ (.xz)
- 7z (by 7-Zip)

#### 2. Lossy Compression

**Principle:** Unimportant data is permanently deleted to achieve much higher compression rates. The result is very similar to the original, but not identical.

**Use cases:**

- Images (JPEG/JPG)
- Audio (MP3, AAC)
- Video (MP4, AVI)

**How it works:** Algorithms remove information that humans find hard to perceive (e.g. colour gradations in images, inaudible frequencies in audio).

**Important for cybersecurity:** Lossy compression is unsuitable for data where every bit matters (programmes, logs, encryption keys)!

### How does lossless compression work?

Compression algorithms eliminate statistical redundancy (repetitions):

**1. Run-Length Encoding (RLE):**

```
Original:    ⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪
Compressed:  "20 × ⚪"
```

Repeated data is replaced by count + value.

**2. Dictionary Coding (LZ77/LZ78 – used in ZIP, Gzip):**

```
Original: "the quick fox jumps over the dog. the quick fox sleeps."
Step 1: Build dictionary
[1] = "the quick fox"
Step 2: Replace repetitions with references
Compressed: "[1] jumps over the dog. [1] sleeps."
```

### Archiving vs. Compression

**Difference:**

- **Archiving**: Bundling multiple files into a single file (e.g. with `tar`) – not necessarily compressed
- **Compression**: Reducing file size (e.g. with `gzip`)

**Common combination:**

- `.tar.gz`: First archived with `tar`, then compressed with `gzip`
- `.zip`: Combines both steps in one format

### Practical application in Windows 11

#### Method 1: Windows Explorer (GUI)

- **Compress**: Right-click on file/folder → "Send to" → "Compressed (zipped) folder"
- **Decompress**: Right-click on ZIP file → "Extract All..."

#### Method 2: PowerShell (command line)

**Create a test file:**

```powershell
"This is a test file. Repetition is the key to compression. Repetition is the key to compression. Repetition is the key to compression." | Out-File test.txt
```

**Check file size:**

```powershell
Get-Item test.txt | Select-Object Name, Length
```

**Compress:**

```powershell
Compress-Archive -Path test.txt -DestinationPath test.zip
```

**Check size of compressed file:**

```powershell
Get-Item test.zip | Select-Object Name, Length
```

**Decompress:**

```powershell
Expand-Archive -Path test.zip -DestinationPath extracted
```

**Verify contents:**

```powershell
Get-Content extracted\test.txt
```

#### Method 3: 7-Zip (recommended for advanced users)

- Download for free from [7-zip.org](https://www.7-zip.org/)
- Supports more formats (.7z, .tar, .gz, .bz2, .xz, .rar)
- Higher compression rates than standard ZIP
- Right-click integration in Windows Explorer

### Key points

✅ **Lossless compression**: For programmes, code, documents, logs – everything where accuracy matters ✅ **Lossy compression**: For multimedia (images, audio, video) – where minor quality loss is acceptable ✅ **ZIP is the standard**: Most widespread on Windows, combines archiving and compression ✅ **PowerShell for automation**: `Compress-Archive` and `Expand-Archive` for scripts ✅ **7-Zip for flexibility**: Supports more formats and better compression

---

## Overview of elements used

|Category|Terms/Tools|
|---|---|
|**Tools used (Windows 11)**|Windows PowerShell/Command Prompt, 7-Zip, WinRAR, Windows built-in ZIP compression, tar (in PowerShell from Windows 10 onwards), Compress-Archive (PowerShell cmdlet), Expand-Archive (PowerShell cmdlet)|
|**Technical terms**|Data compression, lossless compression, lossy compression, Run-Length Encoding (RLE), dictionary coding, LZ77/LZ78 algorithms, compression ratio, archiving, codec, redundancy, bit encoding|
|**Key vocabulary**|Compress, decompress, archive, storage space, bandwidth, data transfer, algorithm, original data, recovery, payload, log files, malware|

## Definitions

|Term|Definition|
|---|---|
|**Tools used (Windows 11)**||
|Windows PowerShell/Command Prompt|Command-line interfaces in Windows for executing compression commands|
|7-Zip|Free open-source compression programme for Windows (supports .7z, .zip, .gz, .tar, etc.)|
|WinRAR|Commercial compression programme for Windows (supports .rar, .zip and other formats)|
|Windows built-in ZIP compression|Function integrated into Windows Explorer for creating and opening ZIP archives (right-click → "Send to" → "Compressed (zipped) folder")|
|tar (PowerShell)|Unix archiving tool, available in PowerShell since Windows 10|
|Compress-Archive|PowerShell command for creating ZIP archives: `Compress-Archive -Path file.txt -DestinationPath archive.zip`|
|Expand-Archive|PowerShell command for extracting ZIP archives: `Expand-Archive -Path archive.zip -DestinationPath targetfolder`|
|**Technical terms**||
|Data compression|Process of encoding information using fewer bits than in the original representation|
|Lossless compression|No original data is lost – perfect recovery is possible|
|Lossy compression|Some data is permanently discarded to achieve higher compression rates|
|Run-Length Encoding (RLE)|Simple compression method that replaces repeated data sequences with count + value|
|Dictionary coding|Compression technique that creates a "dictionary" of frequent sequences and replaces them with short references|
|LZ77/LZ78 algorithms|Dictionary-based compression algorithms used in ZIP and Gzip|
|Compression ratio|Ratio between compressed and original file size (e.g. 50% means half the size)|
|Archiving|Bundling multiple files and directories into a single file (not necessarily compressed)|
|Codec|Technology for encoding/decoding data (especially for audio/video)|
|Redundancy|Superfluous or repeated information in data that can be compressed|
|Bit encoding|Representation of information in binary form (0 and 1)|
|**Key vocabulary**||
|Compress|Reduce data by applying a compression algorithm|
|Decompress|Convert compressed data back to its original or similar form|
|Archive|A single file containing multiple files and folders (e.g. .zip, .tar)|
|Storage space|Available space on a hard drive, SSD or in the cloud for storing data|
|Bandwidth|Data transfer capacity of a network connection|
|Data transfer|Sending data over networks (internet, LAN)|
|Algorithm|Step-by-step instructions for solving a problem (here: for compression)|
|Original data|Unchanged, uncompressed source data|
|Recovery|Retrieving the original data after decompression|
|Payload|The actual content of a file or message (sometimes malicious)|
|Log files|Protocol files that record system events|
|Malware|Malicious software (viruses, trojans, etc.)|