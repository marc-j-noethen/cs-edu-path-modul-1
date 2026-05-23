# Windows Tools & Troubleshooting - Categorisation

### Basic principle of troubleshooting

**Troubleshooting** is a systematic, step-by-step process for solving problems. The most important steps are:

1. **Identify the problem** - What exactly is not working? When did it occur?
2. **Gather information** - Error messages, system logs, recent changes
3. **Establish a theory** - Hypothetically determine possible causes (start with the simplest)
4. **Test the theory** - Make controlled changes, only change one variable at a time
5. **Implement a solution** - Fix the problem based on confirmed cause
6. **Verify functionality** - Make sure everything is working again
7. **Document** - Record for future reference

**Why systematic?** A structured approach prevents making the problem worse, destroying important forensic evidence, or introducing new problems.

### The 5 most critical Windows tools

**1. Task Manager**

- **Access:** `Ctrl + Shift + Esc`
- **Main function:** Shows running programmes, processes and resource usage
- **Typical use:** End non-responding programmes, check system load, manage startup programmes

**2. Event Viewer**

- **Access:** Type `eventvwr.msc` into search
- **Main function:** Logs errors, warnings and system events
- **Typical use:** Find the cause of crashes, track security events
- **Important areas:** Application, Security, System

**3. Device Manager**

- **Access:** Type `devmgmt.msc` into search
- **Main function:** Manages hardware and drivers
- **Typical use:** Update drivers, identify defective hardware (yellow exclamation mark)

**4. Command Line Tools (ipconfig & ping)**

- **ipconfig:** Shows network configuration (IP address, gateway, DNS)
    - `ipconfig /all` for details
    - `ipconfig /flushdns` to clear the DNS cache
- **ping:** Tests network connection to a destination
    - `ping 8.8.8.8` tests internet connection
    - `ping www.google.com` tests DNS resolution

**5. Safe Mode**

- **Access:** Via `msconfig` → Boot tab or advanced startup options
- **Main function:** Starts Windows with minimal drivers
- **Typical use:** Isolate problems caused by third-party software or faulty drivers

### Most common problem sources (in order)

1. **Driver problems** - Outdated, missing or incompatible drivers
2. **Startup programmes** - Too many automatically starting programmes slow down the system
3. **Network configuration** - Incorrect IP, DNS or gateway settings
4. **Software conflicts** - Incompatible programmes or services
5. **Hardware failures** - Defective components (visible in Device Manager)

### Sysinternals Suite - The professional tools

For advanced diagnostics, Microsoft offers free tools:

- **Process Explorer:** Detailed process view with hierarchy
- **Autoruns:** Shows ALL autostart entries (more than msconfig)
- **Process Monitor:** Monitors file and registry access in real time
- **TCPView:** Shows all network connections with associated processes

**Access:** Download from Microsoft Learn or directly via `\\live.sysinternals.com\tools\`

### Golden rules

✅ **Always make only one change at a time** ✅ **Undo changes if they don't help** ✅ **Document everything - for yourself and others** ✅ **When in doubt, run with administrator privileges** ✅ **For network problems: Test physical connection → IP → gateway → DNS → internet**

These 20% of the material cover the most common troubleshooting scenarios and form the foundation for effective problem solving in Windows 11.

## Tools Used

|Tool|Meaning|
|---|---|
|**Task Manager**|Shows running applications, processes and system resources (CPU, RAM, disk, network) in real time. Access via `Ctrl + Shift + Esc`|
|**System Information (msinfo32)**|Provides a comprehensive overview of hardware configuration, system components and software environment|
|**Device Manager**|Manages hardware devices and their drivers, shows problematic devices with a yellow exclamation mark|
|**Event Viewer**|Logs system events, errors, warnings and security-related activities|
|**Resource Monitor**|Shows detailed real-time information about resource usage of individual processes|
|**Reliability Monitor**|Displays system stability on a timeline with a stability index from 1–10|
|**System Configuration (msconfig)**|Manages startup processes, boot options and system services for diagnostic purposes|
|**Command Prompt/PowerShell**|Command-line interface for advanced system management and network diagnostics|
|**Process Explorer (Sysinternals)**|Advanced Task Manager with hierarchical process view and detailed information|
|**Autoruns (Sysinternals)**|Shows all programmes that are automatically loaded at system startup|
|**Process Monitor (ProcMon)**|Monitors file system, registry and process activities in real time|
|**TCPView (Sysinternals)**|Lists all TCP and UDP connections with associated processes|

## Technical Terms

|Term|Meaning|
|---|---|
|**Process**|A running instance of an executable programme in memory|
|**Service**|Background programmes that provide core functions of the operating system|
|**Device driver**|Software that enables communication between Windows and hardware components|
|**Administrative privileges**|Elevated permissions to access protected system areas|
|**Safe Mode**|Diagnostic startup mode with minimal drivers and services|
|**Event ID**|Unique number for identifying specific system events|
|**PID (Process ID)**|Unique number for identifying a running process|
|**TCP/UDP endpoints**|Network connection points with IP address and port number|
|**Registry**|Central Windows database for system configuration and settings|
|**DLL (Dynamic Link Library)**|Shared programme library with reusable functions|
|**IRQ (Interrupt Request)**|Hardware signal for communicating with the processor|
|**DNS (Domain Name System)**|Translates domain names into IP addresses|
|**DHCP (Dynamic Host Configuration Protocol)**|Automatically assigns IP addresses in the network|

## Important Vocabulary

|Vocabulary|Meaning|
|---|---|
|**Troubleshooting**|Systematic process for diagnosing and solving computer problems|
|**Bottleneck**|Component that limits the overall performance of the system|
|**Root cause**|The original, underlying cause of a problem|
|**Symptoms**|Observable signs of a problem|
|**Theory of probable cause**|Reasoned assumption about the most likely cause|
|**Diagnostic startup**|Starting with minimal configuration for problem diagnosis|
|**Clean boot**|Windows startup with minimal drivers and startup programmes|
|**Rollback**|Undoing changes, e.g. for drivers|
|**Forensic evidence**|Digital evidence for security-related investigations|
|**Persistence mechanisms**|Methods used by malware to remain active after a restart|
|**Image signature**|Digital signature to verify the authenticity of files|
|**Code signing**|Process of digitally signing software|