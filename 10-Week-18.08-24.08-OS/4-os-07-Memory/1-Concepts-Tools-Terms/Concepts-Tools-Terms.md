# Windows Tools & Troubleshooting 

### The Basic Principle of Troubleshooting

**Troubleshooting** is a systematic, step-by-step process for solving problems. The most important steps are:

1. **Identify the problem** – What exactly is not working? When did it occur?
2. **Gather information** – Error messages, system logs, recent changes
3. **Establish a theory** – Hypothetically define possible causes (start with the simplest)
4. **Test the theory** – Make controlled changes, only change one variable at a time
5. **Implement the solution** – Fix the problem based on the confirmed cause
6. **Verify functionality** – Ensure everything is working again
7. **Document** – Record for future reference

**Why systematic?** A methodical approach prevents making the problem worse, destroying important forensic evidence, or introducing new problems.

### The 5 Most Critical Windows Tools

**1. Task Manager**

- **Access:** `Ctrl + Shift + Esc`
- **Main function:** Shows running programs, processes and resource usage
- **Typical use:** Terminate non-responsive programs, check system load, manage startup programs

**2. Event Viewer**

- **Access:** Type `eventvwr.msc` into the search bar
- **Main function:** Logs errors, warnings and system events
- **Typical use:** Find the cause of crashes, track security events
- **Important areas:** Application, Security, System

**3. Device Manager**

- **Access:** Type `devmgmt.msc` into the search bar
- **Main function:** Manages hardware and drivers
- **Typical use:** Update drivers, identify faulty hardware (yellow exclamation mark)

**4. Command Line Tools (ipconfig & ping)**

- **ipconfig:** Shows network configuration (IP address, gateway, DNS)
    - `ipconfig /all` for details
    - `ipconfig /flushdns` to clear the DNS cache
- **ping:** Tests network connection to a target
    - `ping 8.8.8.8` tests internet connection
    - `ping www.google.com` tests DNS resolution

**5. Safe Mode**

- **Access:** Via `msconfig` → Boot tab or advanced startup options
- **Main function:** Starts Windows with minimal drivers
- **Typical use:** Isolate problems caused by third-party software or faulty drivers

### Most Common Problem Sources (in order)

1. **Driver problems** – Outdated, missing or incompatible drivers
2. **Startup programs** – Too many automatically starting programs slow down the system
3. **Network configuration** – Incorrect IP, DNS or gateway settings
4. **Software conflicts** – Incompatible programs or services
5. **Hardware faults** – Defective components (identifiable in Device Manager)

### Sysinternals Suite – The Professional Tools

For advanced diagnostics, Microsoft offers free tools:

- **Process Explorer:** Detailed process view with hierarchy
- **Autoruns:** Shows ALL autostart entries (more than msconfig)
- **Process Monitor:** Monitors file and registry access in real time
- **TCPView:** Shows all network connections with associated processes

**Access:** Download from Microsoft Learn or directly via `\\live.sysinternals.com\tools\`

### Golden Rules

✅ **Always make only one change at a time** ✅ **Undo changes if they don't help** ✅ **Document everything – for yourself and others** ✅ **When in doubt, run with administrator rights** ✅ **For network problems: Test physical connection → IP → Gateway → DNS → Internet**

These 20% of the material cover the most common troubleshooting scenarios and form the foundation for effective problem solving in Windows 11.

## Tools Used

|Tool|Meaning|
|---|---|
|**Task Manager**|Shows running applications, processes and system resources (CPU, RAM, disk, network) in real time. Access via `Ctrl + Shift + Esc`|
|**System Information (msinfo32)**|Provides a comprehensive overview of hardware configuration, system components and software environment|
|**Device Manager**|Manages hardware devices and their drivers, displays problematic devices with a yellow exclamation mark|
|**Event Viewer**|Logs system events, errors, warnings and security-relevant activities|
|**Resource Monitor**|Shows detailed real-time information about resource usage of individual processes|
|**Reliability Monitor**|Displays system stability on a timeline with a stability index of 1–10|
|**System Configuration (msconfig)**|Manages startup processes, boot options and system services for diagnostic purposes|
|**Command Prompt/PowerShell**|Command-line interface for advanced system management and network diagnostics|
|**Process Explorer (Sysinternals)**|Advanced Task Manager with hierarchical process view and detailed information|
|**Autoruns (Sysinternals)**|Shows all programs that are automatically loaded at system startup|
|**Process Monitor (ProcMon)**|Monitors file system, registry and process activity in real time|
|**TCPView (Sysinternals)**|Lists all TCP and UDP connections with associated processes|

## Technical Terms

|Term|Meaning|
|---|---|
|**Process**|A running instance of an executable program in working memory|
|**Service**|Background programs that provide core functions of the operating system|
|**Device Driver**|Software that enables communication between Windows and hardware components|
|**Administrative Privileges**|Elevated permissions for accessing protected system areas|
|**Safe Mode**|Diagnostic startup mode with minimal drivers and services|
|**Event ID**|Unique number for identifying specific system events|
|**PID (Process ID)**|Unique number for identifying a running process|
|**TCP/UDP Endpoints**|Network connection points with IP address and port number|
|**Registry**|Central Windows database for system configuration and settings|
|**DLL (Dynamic Link Library)**|Shared program library with reusable functions|
|**IRQ (Interrupt Request)**|Hardware signal for communication with the processor|
|**DNS (Domain Name System)**|Translates domain names into IP addresses|
|**DHCP (Dynamic Host Configuration Protocol)**|Automatically assigns IP addresses in the network|

## Key Vocabulary

|Vocabulary|Meaning|
|---|---|
|**Troubleshooting**|Systematic process for diagnosing and resolving computer problems|
|**Bottleneck**|Component that limits the overall performance of the system|
|**Root cause**|The original, underlying cause of a problem|
|**Symptoms**|Observable signs of a problem|
|**Theory of probable cause**|Reasoned assumption about the likely cause|
|**Diagnostic startup**|Start with minimal configuration for problem diagnosis|
|**Clean boot**|Windows startup with minimal drivers and startup programs|
|**Rollback**|Undoing changes, e.g. with drivers|
|**Forensic evidence**|Digital evidence for security-relevant investigations|
|**Persistence mechanisms**|Methods used by malware to remain active after a restart|
|**Image signature**|Digital signature for verifying the authenticity of files|
|**Code signing**|Process of digitally signing software|

---