# What is the Registry?

**Definition:** Hierarchical database that stores all configuration settings for Windows – from the operating system through hardware drivers to application settings.

**Historical context:**

- Introduced with Windows 3.1 as a replacement for numerous INI files
- Centralises all system configurations in one place

**Storage structure:**

- Consists of several "hives" (files on the hard drive)
- Loaded into memory at system startup
- Presents itself as a logical, hierarchical tree structure

### 2. The 5 Root Keys

**HKEY_LOCAL_MACHINE (HKLM):**

- Computer-specific configuration
- Hardware, drivers, system-wide software
- **Most important key for system administration**

**HKEY_CURRENT_USER (HKCU):**

- Settings of the logged-in user
- Desktop, screensaver, personal app settings
- Pointer to the corresponding SID in HKEY_USERS

**HKEY_USERS (HKU):**

- Contains all user profiles organised by SID
- HKCU links to this

**HKEY_CLASSES_ROOT (HKCR):**

- File associations (.txt → Notepad)
- COM objects and OLE data

**HKEY_CURRENT_CONFIG (HKCC):**

- Current hardware profile at startup

### 3. Registry Structure: Keys and Values

**Keys/Subkeys:** Containers like folders, forming a tree structure

**Values:** The actual configuration data with three components:

1. **Name:** e.g. "ScreenSaveTimeOut"
2. **Type:** REG_SZ (text), REG_DWORD (32-bit number), REG_BINARY (binary data)
3. **Data:** e.g. "600" (seconds), "C:\Program Files\App\app.exe"

### 4. Cybersecurity Relevance of the Registry

**Forensic investigations:**

- **Timestamps:** When were keys modified?
- **RunMRU:** List of recently executed programs
- **USB history:** All USB devices ever connected
- **Network connections:** Previous Wi-Fi and VPN connections
- **User activity:** TypedPaths shows entered paths

**Malware persistence:**

- **Run Keys:** Classic persistence mechanism
    - `HKLM\Software\Microsoft\Windows\CurrentVersion\Run` → All users
    - `HKCU\Software\Microsoft\Windows\CurrentVersion\Run` → Current user only
- Malware registers itself here for autostart at every boot/login

**Incident Response:**

- Identification of IOCs (Indicators of Compromise)
- Analysis of attacker TTPs
- Determining the scope of compromise

### 5. Practical Access: Registry Editor

**Opening:**

- Windows + R → type `regedit` → Enter
- Confirm UAC prompt with "Yes"

**Navigation:**

- Left pane: Tree structure of keys
- Right pane: Values of the selected key
- Example path: `HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\TypedPaths`

**CRITICAL WARNING:**

- Incorrect registry changes can render the system unusable
- Look only, do not modify (except with a backup and precise knowledge)
- In case of errors, Windows may no longer boot

### Practical Application in Windows 11

**For forensics:** The registry is the first port of call in investigations – it contains comprehensive traces of user activities and system events.

**For malware analysis:** Checking the Run Keys is a standard check for identifying persistence mechanisms.

**For system hardening:** Targeted registry changes disable insecure features and enforce security policies.

## Table: Tools, Technical Terms and Vocabulary

|Category|Term|Meaning|
|---|---|---|
|**Tools Used**|Registry Editor (regedit.exe)|Built-in Windows tool for viewing and editing the registry|
||Windows + R|Keyboard shortcut for opening the "Run" dialog|
||PowerShell|Scripting for registry queries and modifications|
||RegEdit Command Line|Command-line access to the registry for automated tasks|
||Registry Backup Tools|Tools for backing up registry hives before making changes|
||Forensic Registry Tools|Specialised software for analysing registry data in investigations|
|**Technical Terms**|Registry|Central hierarchical database for Windows configurations|
||Hives|Files containing registry data that are loaded into memory at boot|
||Root Keys|Top-level containers of the registry hierarchy (HKEY_*)|
||HKEY_CLASSES_ROOT (HKCR)|File associations, OLE data and COM object registrations|
||HKEY_CURRENT_USER (HKCU)|Settings of the currently logged-in user|
||HKEY_LOCAL_MACHINE (HKLM)|Computer-specific configuration independent of the user|
||HKEY_USERS (HKU)|Profiles of all users organised by their respective SIDs|
||HKEY_CURRENT_CONFIG (HKCC)|Current hardware profile at system startup|
||Keys|Container elements in the registry, comparable to folders|
||Subkeys|Nested keys within a parent key|
||Values|The actual configuration data within keys|
||REG_SZ|Registry data type: fixed-length text string|
||REG_EXPAND_SZ|Registry data type: expandable string with environment variables|
||REG_BINARY|Registry data type: raw binary data|
||REG_DWORD|Registry data type: 32-bit integer|
||REG_QWORD|Registry data type: 64-bit integer|
||REG_MULTI_SZ|Registry data type: multiple text entries in one value|
||SID (Security Identifier)|Unique security identifier for user accounts|
||Run Keys|Registry keys for automatic program startup at boot/login|
||Persistence|Ability of malware to survive restarts (via registry)|
||INI files|Outdated configuration system before the introduction of the registry|
|**Key Vocabulary**|Hierarchical structure|Tree-shaped organisation of keys and subkeys|
||OLE (Object Linking and Embedding)|Technology for embedding objects in documents|
||COM (Component Object Model)|Microsoft standard for software components|
||File association|Assignment of file types to applications|
||System hardening|Security measures to reduce attack surfaces|
||Malware persistence|Mechanisms by which malware remains permanently active|
||Forensic artefacts|Traces in the registry that are relevant in investigations|
||RunMRU|Registry entry containing a list of recently executed programs|
||TypedPaths|Registry location for file paths entered in Explorer|
||IOC (Indicators of Compromise)|Signs of system compromise in the registry|
||TTPs (Tactics, Techniques, Procedures)|Behaviours and methods of attackers|
||UAC (User Account Control)|Security prompt for administrative changes|
||Timestamp|Timestamp of registry changes for forensic analysis|
||USB device history|Information stored in the registry about connected devices|
||Network connection history|Registry entries about previous network connections|
||Autostart entries|Registry values for automatically starting programs|
||Registry permissions|Access rights to registry keys and values|

---