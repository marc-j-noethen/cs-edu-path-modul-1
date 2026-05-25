# What is a File System?

A **file system** is the fundamental organisational structure that an operating system uses to manage data on storage media. It works like a librarian who catalogues all information and makes it findable.

### Main Functions:

- **Organisation**: Grouping into files and folders (hierarchical structure)
- **Naming**: Assigning meaningful names
- **Metadata management**: Storing size, date, permissions
- **Storage management**: Tracking free and occupied areas
- **Data retrieval**: Efficiently locating and accessing data
- **Integrity**: Protection against data loss through journaling

## The 3 Most Important File Systems for Windows

|File system|Usage|Key features|
|---|---|---|
|**NTFS**|Windows system drive (C:)|Journaling, permissions (ACLs), large files, encryption (EFS), MFT|
|**FAT32**|USB sticks, SD cards|Universal compatibility, **but**: max. 4GB file size|
|**exFAT**|Large USB drives, external HDDs|No size restrictions, good compatibility|

## Storage Technologies

### HDD vs. SSD

|Aspect|HDD (Hard Disk Drive)|SSD (Solid State Drive)|
|---|---|---|
|**Technology**|Mechanical, rotating magnetic platters|Electronic, flash memory (NAND)|
|**Speed**|Slower (seek time required)|Very fast (instant access)|
|**Lifespan**|Susceptible to mechanical damage|More durable, no moving parts|
|**Cost**|Cheaper per GB|More expensive per GB|
|**Fragmentation**|Problem (defragmentation required)|Not a problem (do not defragment!)|

## Windows Paths and Structure

- **Drive letters**: C: (system), D:, E:, etc.
- **Important system folders**:
    - `C:\Windows` – Operating system files
    - `C:\Program Files` – Installed applications
    - `C:\Users\[Name]` – User data
    - `C:\Users\[Name]\Documents` – Documents
    - `C:\temp` – Temporary files

### Path Examples:

- **Absolute**: `C:\Users\Max\Documents\report.docx`
- **Relative**: `Documents\report.docx` (when in C:\Users\Max)

## Data Protection: The 2 Pillars

### 1. Backups – Protection Against Data Loss

**Why important?**

- Hardware failures (hard drive crash)
- Accidental deletion
- Ransomware attacks
- Data corruption

**Backup strategies:**

1. **Full backup**
    
    - ✅ All data, simple recovery
    - ❌ Lots of storage space, time-consuming
2. **Incremental backup**
    
    - ✅ Only changes since last backup, space-saving
    - ❌ Complex recovery (requires all backups)
3. **Differential backup**
    
    - ✅ Changes since last full backup, faster recovery
    - ❌ Growing backup size until next full backup

**Windows tools:**

- **File History**: Automatic versioning of important folders
- **Backup and Restore**: System images and data backups

**Storage locations:**

- External hard drives/SSDs
- NAS (Network Attached Storage)
- Cloud (OneDrive, Google Drive, Backblaze)

### 2. Encryption – Protection Against Unauthorised Access

**Two encryption types:**

#### Full-Disk Encryption (FDE) – BitLocker

- Encrypts **entire drives**
- Automatic encryption/decryption on access
- Often uses TPM chip for security
- Ideal for: Laptops, portable devices
- ⚠️ Only available in Windows Pro/Enterprise

#### File/Folder Encryption – EFS

- Encrypts **individual files/folders** on NTFS
- Tied to user account
- Ideal for: Specific sensitive data, shared systems

**Why encryption?**

- ✅ Protection in case of theft/loss
- ✅ Compliance (GDPR, HIPAA)
- ✅ Minimises data breaches

## Understanding Formatting

**What happens during formatting?**

- File system structures are created
- (Optional) Existing data is deleted
- Drive is made usable

**Formatting types:**

- **Quick format**: File system structure only, data recoverable
- **Full format**: Overwrites data, more secure

**When to format?**

- Prepare new drives
- Switch file system (e.g. FAT32 → NTFS)
- Completely wipe a drive
- Fix file system errors

## Practical Windows Tools

### File Explorer

- Navigate the file system
- View file properties (right-click → Properties)
- Metadata in the "Details" tab
- Permissions in the "Security" tab (NTFS)

### Disk Management (diskmgmt.msc)

- View and manage partitions
- Format drives
- Change drive letters
- ⚠️ Caution: Incorrect use leads to data loss!

## Important Security Recommendations

1. **3-2-1 backup rule**:
    
    - 3 copies of the data
    - 2 different media types
    - 1 copy offsite (cloud/different location)
2. **Enable BitLocker** on laptops and portable devices
    
3. **Automate regular backups**
    
4. **Save the recovery key** when using encryption
    
5. **Securely wipe old drives** before disposal (full format or shredder software)
    

## Forensics Relevance

- **Deleted files**: Often recoverable, as only file system entries are removed
- **Formatting**: Standard format does not securely delete data
- **Metadata**: Important trace for digital forensics (timestamps, owner)
- **Fragmentation**: Can indicate HDD usage patterns

**Core message**: File systems organise data in a structured way, backups protect against loss, encryption protects against unauthorised access. Understanding file systems is fundamental for cybersecurity, forensics and system administration.

## Tools Used

|Tool/Application|Meaning|
|---|---|
|**File Explorer**|Main tool for navigating, viewing and managing files and folders in Windows|
|**Disk Management** (diskmgmt.msc)|Windows utility for viewing, creating, deleting, formatting and managing hard drives and partitions|
|**File History**|Automatic backup tool for files in libraries, desktop, contacts and favourites to external drives|
|**Backup and Restore**|Traditional Windows backup tool for system images and file/folder backups|
|**BitLocker Drive Encryption**|Microsoft's full encryption solution for entire drives and partitions (only in Pro/Enterprise versions)|
|**EFS (Encrypting File System)**|NTFS feature for encrypting individual files or folders, tied to user accounts|
|**Defragmentation**|Tool for reorganising fragmented files on HDDs for better performance|
|**Properties dialog**|Right-click → Properties shows metadata, permissions and details for files/folders|

## Technical Terms

|Term|Meaning|
|---|---|
|**File system**|Method and data structure for organising, storing and managing files on storage media|
|**NTFS (New Technology File System)**|Primary modern file system for Windows with journaling, ACLs, compression and encryption|
|**FAT32 (File Allocation Table 32)**|Older, simple file system with 4GB file size restriction, compatible with many operating systems|
|**exFAT (Extended FAT)**|Modern FAT32 successor without size restrictions, ideal for USB drives and SD cards|
|**Master File Table (MFT)**|Central data structure in NTFS that catalogues all files and directories|
|**Volume**|Single accessible storage area with its own file system, often represented as a drive letter (C:, D:)|
|**Partition**|Logical subdivision of a physical hard drive; each can be formatted with its own file system|
|**Formatting**|Preparation of a drive by deleting data and setting up a file system|
|**HDD (Hard Disk Drive)**|Mechanical hard drive with rotating magnetic platters, storage in sectors and tracks|
|**SSD (Solid State Drive)**|Flash-based storage medium without moving parts, faster and more durable than HDDs|
|**Fragmentation**|Distribution of file parts across non-contiguous blocks, slows down HDDs|
|**Journaling**|File system technique for logging changes before executing them for crash recovery|
|**ACL (Access Control List)**|List of permissions that defines which users/groups have which access rights to files|
|**Full-Disk Encryption (FDE)**|Encryption of an entire drive/volume for automatic protection of all data|
|**TPM (Trusted Platform Module)**|Security chip for storing cryptographic keys, often used for BitLocker|

## Key Vocabulary

|Vocabulary|Meaning|
|---|---|
|**File**|Named collection of related information on a storage medium|
|**Directory/Folder**|Container for files and other directories, enables hierarchical organisation|
|**Path**|String for uniquely specifying the storage location of a file in the file system|
|**Absolute path**|Complete path from the root of the file system (e.g. C:\Users\Name\Documents\file.txt)|
|**Relative path**|Path relative to the current working directory (e.g. Documents\file.txt)|
|**Metadata**|Information about files: name, size, type, timestamp, permissions, owner|
|**Drive letter**|Windows identifier for volumes (C: = system drive, D:, E: = additional drives)|
|**Backup**|Copy of data in another location for recovery after loss|
|**Full backup**|Backup of all selected data; simple recovery, high storage requirement|
|**Incremental backup**|Backup of only the data changed since the last backup; space-saving, complex recovery|
|**Differential backup**|Backup of all data changed since the last full backup; compromise between full and incremental|
|**Encryption**|Conversion of data into an unreadable format, only decryptable with a key|
|**NAS (Network Attached Storage)**|Central network storage for backups and shared file usage|
|**Cloud storage**|Online storage services such as OneDrive, Google Drive for external backups|
|**Sector**|Smallest physical storage unit on HDDs (typically 512 bytes or 4KB)|
|**Track**|Concentric circle on an HDD platter on which data is stored in sectors|
|**NAND flash**|Storage technology in SSDs, enables fast, non-volatile data access|
|**Quick format**|Formatting that only creates file system structures; data remains recoverable|
|**Full format**|Formatting with overwriting of all data; more secure, but slower|

---