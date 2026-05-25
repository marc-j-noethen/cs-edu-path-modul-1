# What are Windows Services?

**Windows services** are special background applications without a visible user interface that carry out essential system tasks. They are the "invisible workers" of the operating system.

### Key Characteristics of Services

1. **No UI**: Run invisibly in the background
2. **Own security context**: Run under specific user accounts
3. **Automatic/Manual start**: Can start at boot or on demand
4. **Dependencies**: May require other services in order to function

### Important Service Accounts

|Account|Permissions|Usage|
|---|---|---|
|**Local System**|Highest privileges, full system access|Critical system services|
|**Local Service**|Restricted local rights|Services with minimal requirements|
|**Network Service**|Network access, restricted local rights|Network-oriented services|

### Examples of Important Services

- **DHCP Client**: Network IP configuration
- **DNS Client**: Name resolution
- **Print Spooler**: Managing print jobs
- **Windows Update**: System updates
- **Windows Defender**: Virus protection

## The Windows Startup Process

### The 6 Main Phases

```
Power On → Firmware → Bootloader → Kernel → Services → Login → Desktop
```

#### 1. **Power-On & Hardware Check (Firmware Phase)**

- BIOS/UEFI starts
- **POST (Power-On Self Test)** checks hardware
- On error: Beep codes or error message
- Searches for operating system on storage device

#### 2. **Loading Windows (Bootloader Phase)**

- **Windows Boot Manager** takes over
- Reads boot configuration
- Finds Windows installation
- Loads OS components

#### 3. **Kernel Initialisation**

- Windows kernel is loaded into RAM
- Loads essential **drivers** for hardware
- Loads settings from the **Windows Registry**
- Initialises the base system

#### 4. **Preparing the System (Session Manager)**

- **Session Manager** starts
- Prepares user login
- Starts critical system processes

#### 5. **Starting Services & Preparing Login**

- **Service Control Manager (SCM)** starts
- SCM starts all "Automatic" services
- Login screen is prepared
- ⚠️ **Most important phase for services!**

#### 6. **User Login & Desktop**

- User authentication
- Personal settings are loaded
- **Autostart programs** are launched
- Desktop appears

### Difference: Services vs. Autostart Programs

|Aspect|Services|Autostart Programs|
|---|---|---|
|**Start time**|At system boot (before login)|At user login|
|**Management**|services.msc|Task Manager (Startup tab)|
|**User context**|System accounts|User account|
|**Visibility**|No UI (mostly)|Often visible applications|
|**Purpose**|System functions|User applications|

## Windows Management Tools

### 1. Services.msc (Services Console)

**Access**: Win+R → `services.msc`

**Functions**:

- Display list of all services
- Check status (Running/Stopped/Paused)
- Configure startup type
- Start/stop/restart services
- View properties & dependencies

**Startup types**:

- **Automatic**: Starts at boot
- **Automatic (Delayed Start)**: Starts with a delay after other services
- **Manual**: Must be started manually
- **Disabled**: Completely deactivated

### 2. Task Manager (Services & Startup)

**Access**: Ctrl+Shift+Esc

**Two important tabs**:

#### Services Tab

- Quick overview of running services
- Start/stop function
- Link to services.msc

#### Startup Tab

- Shows user autostart programs
- Status: Enabled/Disabled
- Startup impact (effect on boot time)
- Enable/disable programs

### 3. msconfig (System Configuration)

**Access**: Win+R → `msconfig`

**Functions**:

- Configure boot options (Safe Mode, etc.)
- View services (can hide Microsoft services)
- Startup → redirects to Task Manager

### 4. Autoruns (Sysinternals) ⭐

**Download**: Microsoft Sysinternals website

**Why important?**

- **Most comprehensive** view of all autostart mechanisms
- Shows hidden autostart entries
- Ideal for malware detection

**Tabs**:

- **Logon**: Autostart programs, Run Keys
- **Services**: All services (incl. third-party)
- **Scheduled Tasks**: Scheduled tasks
- **Drivers**: Drivers
- **KnownDLLs**: System libraries

**Information**:

- Entry name & description
- Publisher
- Image path (file path)
- Digital signature
- Timestamp

## Cybersecurity Relevance

### Why Services & Autostart Matter

#### 1. **Reducing the Attack Surface**

- Every running service = potential vulnerability
- Disabling unnecessary services = less risk

#### 2. **Detecting Malware Persistence**

Malware frequently uses:

- **Services**: For high privileges and early start
- **Autostart entries**: For persistence after reboot
- **Scheduled Tasks**: For time-controlled execution
- **Registry Run Keys**: For automatic startup

**Advantages of running as a service for malware**:

- ✅ Runs with high rights (Local System)
- ✅ Starts before user login
- ✅ Invisible (no UI)
- ✅ Recovery options (auto-restart)
- ✅ Harder to detect

#### 3. **Performance Optimisation**

- Too many autostart programs = slower boot
- Services consume CPU and RAM
- Regular review recommended

#### 4. **Forensic Analysis**

- Autostart entries = important trace in incidents
- Autoruns creates export for analysis
- Timestamps show when entries were created

## Practical Investigation of Suspicious Services

### Step-by-Step Approach

1. **Identification**
    
    - Unknown service in services.msc or Autoruns
2. **Check properties**
    
    - Name, description, display name
    - Executable path (file path)
    - Logon account
    - Dependencies
3. **Online research**
    
    - Google the service/file name
    - Is it a legitimate Windows/software component?
    - Known malware?
4. **Check digital signature**
    
    - Right-click on .exe → Properties → Digital Signatures
    - Microsoft/trusted publisher?
5. **Use Autoruns**
    
    - Collect detailed info
    - Mark unsigned entries (Options → Verify Code Signatures)
6. **If suspicious**
    
    - Stop & disable service (caution regarding impact!)
    - Scan with antivirus
    - Move file to quarantine
    - Carry out forensic analysis

## Best Practices

### Security

1. ✅ **Principle of minimal permission**
    
    - Run services with the lowest necessary rights
2. ✅ **Regular review**
    
    - Run Autoruns regularly
    - Investigate unknown entries
3. ✅ **Minimise autostart**
    
    - Only truly necessary programs in autostart
    - Improves performance and security
4. ✅ **Updates & patches**
    
    - Keep services up to date
    - Do not disable Windows Update

### Caution

⚠️ **Do NOT disable critical services** without knowledge!

- Windows Update
- Firewall
- DHCP Client
- DNS Client
- Cryptographic Services

⚠️ **Backup before making changes**

- Create a system restore point
- Document changes

## Summary of Core Concepts

**Services** are background applications that provide essential system functions. They start at boot through the **Service Control Manager** in the 5th phase of the Windows startup process.

**Autostart programs** are user applications that start at login and differ from services.

**Tools** such as services.msc, Task Manager and especially **Autoruns** enable management and security analysis.

**Cybersecurity**: Services & autostart are critical for reducing attack surfaces and detecting malware. Malware uses these mechanisms for persistence and privilege escalation.

**Core message**: Understanding and managing services and autostart mechanisms is fundamental for system security, performance optimisation and malware detection. Autoruns is the most powerful tool for comprehensive analysis.

## Tools Used

|Tool/Application|Meaning|
|---|---|
|**services.msc** (Services Console)|Main management tool for all Windows services; shows status, startup type, dependencies and enables start/stop|
|**Task Manager**|Shows running services in the "Services" tab and autostart applications in the "Startup" tab|
|**msconfig** (System Configuration)|Older tool for boot options and service management; often redirects to Task Manager for startup|
|**Autoruns (Sysinternals)**|Comprehensive tool for displaying all autostart entries: services, tasks, drivers, Run Keys, DLLs|
|**Windows Boot Manager**|Bootloader program that loads Windows and manages the startup configuration|
|**Service Control Manager (SCM)**|System process that manages all Windows services and coordinates their start/stop|
|**Session Manager**|System process that sets up the basic environment for Windows and starts critical processes|
|**Run Dialog** (Win+R)|Quick access to launch management tools by entering commands (services.msc, msconfig)|

## Technical Terms

|Term|Meaning|
|---|---|
|**Windows Service**|Background application without UI that runs independently of user login and performs system-relevant tasks|
|**Startup Type**|Configuration for how a service starts: Automatic, Automatic (Delayed), Manual, Disabled|
|**Service Dependencies**|Other services that must be running for a service to function|
|**Security Context**|User account under which a service runs (Local System, Local Service, Network Service, user account)|
|**Firmware**|Built-in system software (BIOS or UEFI) that initialises hardware|
|**POST (Power-On Self Test)**|Hardware self-test at system startup to check components|
|**Bootloader**|Software (Boot Manager) that loads the operating system|
|**Kernel Initialisation**|Start of the OS core, loading of drivers and registry settings|
|**Windows Registry**|Central database for system configuration and settings|
|**Driver**|Software that allows Windows to communicate with hardware|
|**Beep Code**|Acoustic signal during POST error for hardware diagnostics|
|**Safe Mode**|Diagnostic startup mode with minimal drivers and services|
|**Attack Surface**|Sum of all potentially exploitable points in the system|
|**Malware Persistence**|Ability of malware to remain active after a restart|
|**Digital Signature**|Cryptographic proof of the authenticity and integrity of a file|
|**Recovery Options**|Configuration for automatic restart in case of service failure|

## Key Vocabulary

|Vocabulary|Meaning|
|---|---|
|**Background Process**|Process that runs without a visible user interface|
|**User Interface (UI)**|Graphical or text-based interface for user interaction|
|**Automatic Startup**|Service starts automatically at Windows boot|
|**Manual Startup**|Service must be started manually or by other processes|
|**Disabled**|Service is completely switched off and cannot be started|
|**Status**|Current state of a service: Running, Stopped, Paused|
|**Local System**|Highest-privileged system account with full access to all resources|
|**Local Service**|Low-privileged account for local services with restricted access|
|**Network Service**|Account for services with network access but restricted local rights|
|**Boot Sequence**|Order of steps from power-on to desktop|
|**Logon Phase**|Phase in which user login is prepared and carried out|
|**Startup Programs**|Applications that start automatically at user login|
|**System Tray**|Area on the right of the taskbar with icons for background applications|
|**Executable Path**|Storage location of the program file (.exe) that runs a service|
|**Third-party Services**|Services from non-Microsoft software|
|**Scheduled Tasks**|Time-controlled or event-based automatic program executions|
|**Run Keys**|Registry entries that automatically execute programs at startup|
|**Known DLLs**|List of trusted system libraries that are loaded at startup|

---