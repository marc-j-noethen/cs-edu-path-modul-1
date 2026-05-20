# 📊 Summary based on the 80/20 principle

### What is an operating system?

An **operating system** is the central software that coordinates all hardware and software resources of a computer. It serves two main goals: **user-friendliness** by simplifying complex hardware operations, and **efficient resource management** of CPU, memory and devices.

### Core components

The most important components are:

1. **Kernel** - The "heart" of the OS, manages CPU, memory and hardware directly
2. **Shell/Terminal** - Command-line interface for advanced control
3. **GUI** - Graphical interface with windows and icons (Windows: File Explorer instead of Finder)
4. **File system** - Organises data on hard drives (Windows uses NTFS instead of APFS)

### Windows 11 specifics

- **Kernel**: NT kernel (instead of XNU)
- **Shell**: PowerShell and Command Prompt (instead of Zsh)
- **File manager**: File Explorer (instead of Finder)
- **Settings**: Windows Settings (instead of System Preferences)
- **Encryption**: BitLocker (instead of FileVault)
- **Security**: Windows Defender, SmartScreen (instead of Gatekeeper/XProtect)

### Why operating systems matter for cybersecurity

Operating systems are the **primary target of attacks**, since vulnerabilities in the OS can enable complete system control. Important aspects:

- **Attack target**: Vulnerabilities in kernel, system services and drivers
- **Security tools**: Antivirus software, firewalls, EDR solutions operate at OS level
- **Forensics**: Analysis of logs, processes and file system artefacts after incidents
- **System hardening**: Disabling unnecessary services, applying patches, strong permissions

### Most important security measures (Windows 11)

1. Enable **BitLocker** for disk encryption
2. Keep **Windows Defender Firewall** switched on
3. Install **updates** regularly
4. Use **SmartScreen** for download protection
5. Work with **user accounts** with restricted permissions
6. Review **privacy settings** in Windows Settings

### Practical tools (Windows 11)

- **Task Manager** (Ctrl+Shift+Esc): Monitor processes and resource usage
- **PowerShell**: Commands such as `Get-Process`, `Get-Service` for system analysis
- **Disk Management**: Format and partition hard drives
- **Event Viewer**: System logs for troubleshooting and security analysis

**Core message**: The operating system is the fundamental security layer – whoever controls the OS controls the entire system. Deep OS understanding is therefore indispensable for cybersecurity.

---

## Tools Used

|Tool/Application|Meaning|
|---|---|
|**Activity Monitor** (Win: Task Manager)|Shows running processes and system resource usage (CPU, RAM, disk, network)|
|**Terminal** (Win: Command Prompt/PowerShell)|Command-line interface for text-based system commands|
|**Finder** (Win: File Explorer)|Graphical file manager for browsing and managing files and folders|
|**System Preferences** (Win: Settings)|Central application for configuring system settings|
|**Disk Utility** (Win: Disk Management)|Tool for formatting, partitioning and repairing hard drives|
|**Spotlight** (Win: Windows Search)|System-wide search function for files, programmes and content|
|**Gatekeeper** (Win: SmartScreen)|Security mechanism that blocks downloads from untrusted sources|
|**FileVault** (Win: BitLocker)|Full disk encryption to protect data|

---

## Technical Terms

|Term|Meaning|
|---|---|
|**Kernel**|Core of the operating system that manages fundamental system operations and has privileged hardware access|
|**XNU** (Win: NT kernel)|Hybrid kernel of macOS, combines Mach microkernel and BSD Unix components|
|**Shell**|Command-line interface for interacting with the operating system (e.g. Zsh on macOS, PowerShell on Windows)|
|**GUI (Graphical User Interface)**|Visual interface with windows, icons and menus for controlling the computer|
|**CLI (Command-Line Interface)**|Text-based interface for entering commands|
|**Device driver**|Specialised software for communication between operating system and hardware|
|**System call**|Interface through which programmes request services from the kernel|
|**APFS** (Win: NTFS)|Apple File System – modern file system for SSDs with encryption and snapshots|
|**Process**|A programme in execution, managed by the operating system|
|**Multitasking**|Simultaneous execution of multiple programmes through rapid CPU switching|
|**SIP (System Integrity Protection)** (Win: similar: protected system files)|Protection mechanism that shields critical system files from modification|
|**Sandboxing**|Execution of programmes in an isolated environment with restricted access|
|**Root/Administrator**|User with full system privileges|
|**Virtual memory**|Use of disk storage as an extension of RAM|

---

## Important Vocabulary

|Vocabulary|Meaning|
|---|---|
|**Operating system (OS)**|Central software that coordinates and manages hardware and software resources|
|**Abstraction**|Simplification of complex processes by hiding technical details|
|**Resource management**|Allocation and control of CPU, memory, disk and I/O devices|
|**File system**|Structured organisation and management of data on storage devices|
|**Permissions**|Access rights that define who may do what with files and folders|
|**Encryption**|Conversion of data into an unreadable format to protect against unauthorised access|
|**Malware**|Malicious software such as viruses, worms, trojans, ransomware|
|**Vulnerability**|Security flaw in software that can be exploited by attackers|
|**System hardening**|Security measures to reduce the attack surface of a system|
|**Attack surface**|Sum of all points at which a system can be attacked|
|**Privilege escalation**|Gaining higher access rights by exploiting vulnerabilities|
|**Forensic analysis**|Examination of systems after security incidents for evidence gathering|
|**Patch**|Software update to fix security vulnerabilities or bugs|
|**Firewall**|Security system for controlling network traffic|