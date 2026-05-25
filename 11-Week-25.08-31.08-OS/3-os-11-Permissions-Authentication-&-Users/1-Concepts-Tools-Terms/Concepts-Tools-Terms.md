# Permissions, Authentication & Users in Windows – Categorisation

### Three Pillars of Access Security

Windows security is based on three fundamental concepts:

1. **Users** – Who are you?
2. **Authentication** – Can you prove who you are?
3. **Permissions** – What are you allowed to do?

### User Accounts: The Two Most Important Types

**1. Administrator Account**

- **Rights:** Full control over the system
- **Can:** Install software, change system settings, access all files, manage other accounts
- **Risk:** Malware with admin rights has full system control
- **Recommendation:** Do NOT use for daily tasks

**2. Standard User Account**

- **Rights:** Restricted privileges
- **Can:** Run programs, manage own files, change personal settings
- **Cannot:** Make system-wide changes, install software (without admin password)
- **Recommendation:** For daily use (internet, email, office)

**Important system accounts:**

- `SYSTEM` – Highest privileges for Windows services
- `Local Service` / `Network Service` – For background services

### User Groups: Efficient Rights Management

**Why groups?** Instead of assigning rights to each user individually, you assign rights to a group and add users to it.

**The 5 most important default groups:**

|Group|Permissions|Typical use|
|---|---|---|
|**Administrators**|Full access to everything|IT administrators|
|**Users**|Standard permissions|Regular employees|
|**Guests**|Very restricted (often disabled)|Temporary visitors|
|**Backup Operators**|Data backup despite missing file permissions|Backup software|
|**Remote Desktop Users**|Remote access to computers|External employees|

**Access:** `Win + R` → `compmgmt.msc` → System Tools → Local Users and Groups → Groups

### Authentication: Proving Identity

**The 5 main methods:**

1. **Password** – Something you **know**
    
    - Most commonly used
    - Should be long, complex and unique
2. **PIN** – Something you **know** (device-bound)
    
    - Shorter than a password
    - Tied to a specific device
3. **Biometrics** – Something you **are**
    
    - Fingerprint, facial recognition (Windows Hello)
    - Unique physical characteristics
4. **Smart Card/Security Key** – Something you **have**
    
    - Physical device for authentication
    - Often used in enterprises
5. **Multi-Factor Authentication (MFA)** – Combination
    
    - At least 2 different factors
    - Example: Password + code from smartphone
    - **Significantly more secure** than a single method

**Technical background:**

- Local login: Comparison with **SAM database** (Security Account Manager)
- Network login: Comparison with **Active Directory**

### NTFS Permissions: Control Over Files and Folders

**The 6 standard permissions (sorted by scope):**

|Permission|What is allowed|
|---|---|
|**Full Control**|Everything: read, write, modify, delete, change permissions, take ownership|
|**Modify**|Read, write, modify, execute, delete|
|**Read & Execute**|View, read, execute programs|
|**List Folder Contents**|Only view file/folder names (not open)|
|**Read**|Open files and view properties|
|**Write**|Create new files and write to existing ones|

**Checking permissions:**

1. Right-click on file/folder → Properties
2. "Security" tab
3. Select user/group → view permissions

**CRITICAL RULE: Deny overrides Allow**

- If a user has "Allow" in Group A and "Deny" in Group B → **Access denied**
- Important for troubleshooting access problems

### Ownership: The Ultimate Trump Card

**What is ownership?**

- Every file/folder has an owner (normally the creator)
- The owner can **ALWAYS** change the permissions
- Even if all other rights have been denied

**Taking ownership:**

- Administrative right
- Enables access to other users' files in case of permission problems
- Found under: Properties → Security → Advanced → Owner

### The Principle of Least Privilege

**Core statement:** Grant only the **minimum necessary** permissions.

**Examples:**

- ❌ WRONG: All employees as administrators
    
- ✅ RIGHT: Standard accounts + admin password when needed
    
- ❌ WRONG: Intern with full access to the finance folder
    
- ✅ RIGHT: Intern with read access to relevant documents
    

**Advantages:**

- Less damage from compromised accounts
- Protection against accidental changes
- Better compliance and traceability

### User Account Control (UAC): The Guardian Angel

**What does UAC do?**

- Dims the screen and asks for confirmation on administrative actions
- Prevents programs from secretly obtaining admin rights
- Applies to administrator accounts too (!)

**How does it work?**

1. Administrator logs in
2. Programs run with **standard rights** (filtered token)
3. On admin action → UAC prompt
4. After confirmation → Temporary **elevation**

**Typical UAC triggers:**

- Software installation
- Changing system settings
- Installing drivers
- Modifying files in system folders

### Practical Use Cases

**Scenario 1: Installing software as a standard user**

1. Double-click the installation file
2. UAC requests administrator password
3. Enter admin password
4. Installation runs with admin rights

**Scenario 2: Access to shared folder denied**

1. Check Properties → Security
2. Is the user/group listed?
3. Is there a "Deny"? (overrides "Allow"!)
4. Adjust permissions accordingly

**Scenario 3: Setting up MFA for critical systems**

1. Password (knowledge) alone is not secure enough
2. Additionally: Authenticator app (possession) or biometrics (inherence)
3. Significantly higher protection against hacking

### The Most Important Takeaways

✅ **Standard accounts for everyday use, administrator only when needed** ✅ **Use groups instead of individual user permissions** ✅ **Enable MFA for sensitive accounts (email, banking)** ✅ **Principle of Least Privilege: as few rights as possible** ✅ **Deny overrides Allow – important when troubleshooting** ✅ **Do not ignore UAC – it protects against malware** ✅ **The owner can always change permissions**

These 20% of the knowledge cover the most important concepts needed for 80% of daily tasks and security decisions in Windows.

## Tools Used

|Tool|Meaning|
|---|---|
|**Computer Management (compmgmt.msc)**|Central management console for local users, groups, services and system resources|
|**Local Users and Groups**|Management of user accounts and groups on a local Windows system|
|**File Explorer Security Tab**|Displays and manages NTFS permissions for files and folders|
|**User Account Control (UAC)**|Security feature that protects administrative actions through confirmation|
|**Windows Hello**|Microsoft's biometric authentication system (facial recognition, fingerprint)|
|**Security Account Manager (SAM)**|Database that stores local user accounts and passwords|
|**Active Directory**|Central directory for managing users and resources in network environments|
|**Properties Dialog**|Window for viewing and editing file/folder attributes and permissions|
|**Advanced Security Settings**|Detailed view of permissions, inheritance and ownership|

## Technical Terms

|Term|Meaning|
|---|---|
|**User Account**|Collection of information defining the identity, permissions and settings of a user|
|**Administrator Account**|User account with full control over the system and all resources|
|**Standard User Account**|User account with restricted rights that cannot make system-wide changes|
|**User Groups**|Collection of user accounts for simplified rights management|
|**Authentication**|Process of verifying the identity of a user, process or device|
|**Authorization**|Determination of which actions an authenticated user is permitted to perform|
|**Permissions**|Rules that define which actions on resources are allowed or prohibited|
|**NTFS Permissions**|File system permissions of the NT File System for granular access control|
|**Allow/Deny**|Permission types, where "Deny" normally overrides "Allow"|
|**Ownership**|The owner of a resource can always change its permissions|
|**Principle of Least Privilege**|Security principle: users receive only the minimum necessary access rights|
|**Multi-Factor Authentication (MFA)**|Authentication using two or more different factors (knowledge, possession, biometrics)|
|**Inheritance**|Passing of permissions from parent to child objects|
|**Token (Access Token)**|Data structure containing user identity and permissions for access decisions|
|**Elevation**|Temporary increase of permissions for administrative tasks|
|**SYSTEM Account**|Internal Windows account with the highest privileges for system services|

## Key Vocabulary

|Vocabulary|Meaning|
|---|---|
|**Full Control**|Highest permission level with all rights including deletion and taking ownership|
|**Modify**|Permission to read, write, modify, execute and delete|
|**Read & Execute**|Permission to view and execute files|
|**List Folder Contents**|Permission to view file and folder names without access to contents|
|**Read**|Permission to open and view files and attributes|
|**Write**|Permission to create new files and write to existing ones|
|**Credentials**|Username and password or other authentication information|
|**Biometrics**|Authentication through unique physical characteristics (fingerprint, face)|
|**PIN (Personal Identification Number)**|Short numeric identifier for device-bound authentication|
|**Smart Card**|Physical device for secure authentication|
|**Taking Ownership**|Administrative right to take ownership of a resource|
|**Filtered Token**|Restricted access token for administrators in standard mode|
|**Security Principal**|Entity (user, group, computer) to which permissions can be assigned|
|**Remote Desktop**|Remote access to a Windows computer over a network|
|**Backup Operators**|Group with rights to back up and restore files|

---