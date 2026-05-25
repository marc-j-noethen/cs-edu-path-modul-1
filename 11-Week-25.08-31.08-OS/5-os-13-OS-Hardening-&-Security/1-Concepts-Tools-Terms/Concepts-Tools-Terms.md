# What is OS Hardening?

**Definition:** Process of securely configuring an operating system to minimise vulnerabilities and attack points.

**Core concept:** Like fortifying a castle – reduce entry points, strengthen defences, make attack attempts detectable.

**Philosophy:**

- **Proactive** rather than reactive: make the system hard to compromise before attacks occur
- **Defense in Depth**: implement multiple layers of security
- **Attack Surface Reduction**: remove or disable everything unnecessary

### 2. The 5 Core Principles of Hardening

**1. Principle of Least Privilege:**

- Users/processes receive only the minimum necessary rights
- Compromised accounts with few rights = minimal damage
- Example: Regular user account for daily use, admin only when necessary

**2. Attack Surface Reduction:**

- Remove unnecessary software, services, accounts, network ports
- Every active component = potential attack point
- If not needed → disable or delete

**3. Secure Configuration:**

- Default settings are often insecure
- Adjust configurations according to best practices
- Use security baselines (CIS Benchmarks, Microsoft Security Baselines)

**4. Patch Management:**

- Systematic identification, testing and installation of updates
- Closes known security vulnerabilities
- Timely installation is critical (attackers analyse patches)

**5. Logging and Monitoring:**

- Comprehensive logging of system events
- Enables detection of suspicious activity
- Foundation for incident investigation

### 3. Practical Hardening Areas in Windows 11

**User Account Management:**

- **Strong password policies**: Complexity, length, regular changes
- **Secure default accounts**: Rename Administrator, disable Guest
- **Keep UAC enabled**: Prevents unauthorised administrative changes
- **Account Lockout Policy**: Protection against brute-force attacks

**Software Management:**

- Uninstall unnecessary applications
- Keep all software up to date (not just the OS)
- Application control: Whitelisting of permitted programs

**Service Management:**

- Disable unnecessary background services
- Example: Print Spooler on non-print servers
- **Caution**: Observe service dependencies

**Patch Management – The Critical Process:**

1. **Identification**: Which systems/software are affected?
2. **Acquisition**: Download patches from the manufacturer
3. **Testing**: Check on test systems first
4. **Deployment**: Roll out (manually or automated via WSUS)
5. **Verification**: Confirm installation

**Patch Tuesday**: Second Tuesday of the month = regular Microsoft update day

### 4. Network and File System Security

**Network Security:**

- **Windows Defender Firewall**: Only allow necessary connections
- Configure firewall rules (e.g. web server: Port 80/443 open)
- Disable outdated network protocols

**File System Security:**

- **NTFS permissions**: Least privilege at file/folder level
- **BitLocker**: Full disk encryption (protection in case of theft)
- **EFS**: Encryption of individual files/folders per user

### 5. Security Policies & Logging (Windows 11)

**Local Security Policy (secpol.msc):**

- Password Policy: Define password requirements
- Account Lockout Policy: e.g. lock after 5 failed attempts
- Audit Policy: Which events are logged?

**Event Viewer (eventvwr.msc) – Three Critical Logs:**

- **Security Log**: Login attempts, file access, audit events
- **System Log**: OS events, services, drivers
- **Application Log**: Application events

**Important Event IDs:**

- **4624**: Successful login
- **4625**: Failed login (possible attack)

### 6. Tools and Standards

**Built-in Windows Tools:**

- Local Security Policy, Services, Event Viewer
- Windows Defender Firewall, BitLocker
- Programs and Features (software uninstallation)

**Security Baselines:**

- **Microsoft Security Baselines**: Official recommendations
- **CIS Benchmarks**: Industry standard, consensus-based, detailed

**Why use baselines?**

- Proven configurations
- Bundled expert knowledge
- Meet compliance requirements

### Critical Success Factors

**Testing before deployment:**

- Patches can cause problems
- Test on non-critical systems first
- Then roll out to production

**Finding the balance:**

- Too little hardening = vulnerable
- Too much hardening = system unusable
- Goal: Maximum security with acceptable usability

**Time-critical patching:**

- Attackers reverse-engineer patches → find the vulnerability
- Exploit unpatched systems
- Fast patching = less time window for attackers

## Table: Tools, Technical Terms and Vocabulary

|Category|Term|Meaning|
|---|---|---|
|**Tools Used**|Local Security Policy (secpol.msc)|Windows tool for configuring security policies on the local computer|
||Event Viewer (eventvwr.msc)|Display and analysis of system, security and application logs|
||Services (services.msc)|Management console for Windows background services|
||Windows Defender Firewall|Integrated host-based firewall for controlling network traffic|
||BitLocker Drive Encryption|Full disk encryption for Windows|
||EFS (Encrypting File System)|File system encryption at file and folder level|
||Programs and Features|Windows tool for uninstalling software|
||WSUS (Windows Server Update Services)|Centralised update distribution in enterprise environments|
||Microsoft Endpoint Configuration Manager|Enterprise tool for patch management and system configuration|
||Group Policy Editor|Centralised management of security configurations in domains|
||PowerShell|Automation of hardening tasks and security audits|
|**Technical Terms**|OS Hardening|Process of securely configuring an OS to reduce vulnerabilities|
||Attack Surface|Sum of all potential vulnerabilities that attackers can exploit|
||Principle of Least Privilege|Minimal principle: grant only necessary access rights|
||Defense in Depth|Multi-layered security architecture with redundant controls|
||Patch Management|Systematic process for identifying, testing and installing updates|
||Patch Tuesday|Second Tuesday of the month on which Microsoft regularly releases updates|
||Out-of-Band Patch|Unscheduled critical security update outside the regular cycle|
||UAC (User Account Control)|Security feature for confirming administrative changes|
||NTFS Permissions|File system permissions for access control on files/folders|
||Host-Based Firewall|Firewall on the individual system (not a network firewall)|
||Security Baseline|Documented recommendations for secure system configurations|
||CIS Benchmarks|Consensus-based hardening guidelines from the Center for Internet Security|
||Microsoft Security Baselines|Official Microsoft recommendations for secure configurations|
||Whitelisting|Only explicitly permitted applications may be executed|
||Blacklisting|Explicitly prohibited applications are blocked|
||Account Lockout|Account lock after multiple failed login attempts|
||Audit Policy|Policy for defining which events are logged|
||Event ID|Unique identifier for specific system events in logs|
||Reverse Engineering|Analysis of patches to identify the resolved vulnerability|
|**Key Vocabulary**|Vulnerability|Security gap that can be exploited by attackers|
||Exploit|Exploitation of a vulnerability for attacks|
||Default Configuration|Standard configuration, often not security-optimised|
||Secure Configuration|Security-oriented adjustment of system settings|
||Service Dependencies|Dependencies between Windows services|
||Password Complexity|Requirements for password structure (length, characters, complexity)|
||Password Reuse Prevention|Prevention of reusing old passwords|
||Default Account|Pre-configured system accounts such as Administrator or Guest|
||Elevated Privileges|Increased permissions for administrative tasks|
||Brute-Force Attack|Attack by systematically trying out passwords|
||Security Log|Log file for security-relevant events|
||System Log|Log file for operating system events|
||Application Log|Log file for application events|
||Event ID 4624|Event code for successful login|
||Event ID 4625|Event code for failed login|
||Logging Noise|Excessive logging of unimportant events|
||Attack Vector|Path or method through which an attack is carried out|
||Proactive Security|Preventive security measures before an attack|
||Reactive Security|Reactive measures after detected attacks|
||Compliance|Adherence to security policies and standards|
||Network Protocol|Communication standard for network connections|
||Firewall Rules|Rule set for controlling incoming and outgoing network traffic|
||Port|Network endpoint for specific services (e.g. Port 80 for HTTP)|

---