# Unix & Linux Basics

### What is Linux?

**Linux** is a **Unix-like, open-source operating system** consisting of two main components:

1. **Linux Kernel** (developed by Linus Torvalds in 1991) – The core
2. **GNU software** + additional tools – The surrounding tools

**Correct name:** GNU/Linux

### Core Features of Linux

|Feature|Meaning|Advantage|
|---|---|---|
|**Open Source**|Source code freely available|Free, customisable, transparent|
|**Stability**|Servers often run for years without restarting|Reliable for critical systems|
|**Security**|Strong permissions model|Less susceptible to malware|
|**Flexibility**|Runs on all devices|Smartphones to supercomputers|
|**CLI-focused**|Powerful command line|Efficient system management|

### The Unix/Linux Philosophy (3 Core Principles)

1. **Programs do one thing – and do it well**
    
    - Every tool has a focused purpose
    - Example: `ls` only lists files, `grep` only filters text
2. **Programs work together**
    
    - Output of one program = input for another
    - Connected via pipes (`|`): `ls | grep document`
3. **Text is the universal interface**
    
    - Programs communicate via text streams
    - Enables flexible combination of different tools

### Linux Distributions: The Most Important

A **distribution** = Linux kernel + pre-installed software + configuration

|Distribution|Target audience|Feature|
|---|---|---|
|**Ubuntu**|Beginners, desktop|User-friendly, large community|
|**Debian**|Advanced users, servers|Very stable, basis for Ubuntu/Kali|
|**Kali Linux**|Cybersecurity|Pre-installed hacking tools|
|**Fedora**|Developers|Latest software versions|
|**CentOS/Rocky/Alma**|Enterprise servers|Long-term support, Red Hat-compatible|

**For this course:** Kali Linux (Debian-based)

### File System Hierarchy: The 10 Most Important Directories

Linux follows the **File System Hierarchy Standard (FHS)** – everything starts at `/` (root)

|Directory|Content|Example|
|---|---|---|
|**/**|Root – top level|Starting point of all paths|
|**/home**|User directories|`/home/max` (equivalent to `C:\Users\Max` in Windows)|
|**/etc**|System configuration files|Network configs, service settings|
|**/bin**|Essential user programs|`ls`, `cp`, `mv`, `cat`|
|**/usr/bin**|Additional user programs|Installed applications|
|**/var**|Variable data|`/var/log` (logs), mailboxes|
|**/tmp**|Temporary files|Deleted at restart|
|**/dev**|Device files|Hardware representations|
|**/proc**|Virtual process file system|Running processes, kernel info|
|**/lib**|System libraries|Shared libraries for programs|

**Navigation:**

- `cd /` → Root directory
- `cd ~` or `cd` → Your own home directory
- `pwd` → Show current path
- `ls /etc` → Show contents of /etc

### The Shell: Your Command Centre

**What is a shell?**

- Command-line interpreter between you and the kernel
- You type commands, the shell executes them

**The two most important shells:**

- **Bash** – Standard on many Linux systems, Ubuntu (formerly)
- **Zsh** – Modern, default on macOS and Kali Linux

**Check shell:** `echo $SHELL` **Check version:** `zsh --version` or `bash --version`

### Package Management with APT (Debian/Kali/Ubuntu)

**What is a package?** Software + all dependencies + metadata in one archive

**The 6 most important APT commands:**

|Command|Function|When to use|
|---|---|---|
|`sudo apt update`|Update package lists|**ALWAYS before installing/upgrading**|
|`sudo apt upgrade`|Update all packages|Regularly for updates|
|`sudo apt install <package>`|Install software|Add new programs|
|`sudo apt remove <package>`|Uninstall software|Programs no longer needed|
|`sudo apt autoremove`|Remove orphaned dependencies|After uninstalling|
|`apt search <search term>`|Search for packages|Research before installing|

**Typical workflow:**

```bash
sudo apt update              # Update lists
apt search vim               # Search
sudo apt install vim         # Install
sudo apt remove vim          # Uninstall
sudo apt autoremove          # Clean up
```

**Windows equivalent:** Microsoft Store, winget or manual downloads

### Users, Groups and Permissions

**Linux is multi-user:**

- Multiple users can be logged in simultaneously
- Each has their own area (`/home/username`)
- Permissions protect data from each other

**The permissions scheme: rwx for ugo**

|Who?|What?|Meaning|
|---|---|---|
|**u** (User/Owner)|**r** (Read)|Read file / list directory|
|**g** (Group)|**w** (Write)|Modify file / create/delete in directory|
|**o** (Others)|**x** (Execute)|Execute file / enter directory|

**Example:** `-rw-r--r--`

- `-` = regular file (would be `d` for directory)
- `rw-` = Owner can read and write
- `r--` = Group can only read
- `r--` = Others can only read

**Important commands:**

- `ls -l` → Show permissions
- `chmod 755 file.sh` → Change permissions (Owner: rwx, Group: rx, Others: rx)
- `chown user:group file` → Change owner

**The Root User (Superuser):**

- Has **all rights** on the system
- Equivalent to Administrator in Windows
- **DO NOT log in as root!** Instead: use `sudo`

**`sudo` (Superuser Do):**

- Executes a single command with root rights
- Safer than permanent root login
- Example: `sudo apt install firefox`

**Important system files:**

- `/etc/passwd` – User information (UID, home, shell)
- `/etc/group` – Group information
- `/etc/shadow` – Encrypted passwords (only readable by root)

**Show your own info:** `id`

### Managing Services (Daemons) with systemd

**What is a daemon?** Background process that provides services (web server, SSH, database)

**systemd** is the modern service manager in Linux

**The 5 most important systemctl commands:**

|Command|Function|
|---|---|
|`systemctl status <service>`|Check status (is it running?)|
|`sudo systemctl start <service>`|Start service|
|`sudo systemctl stop <service>`|Stop service|
|`sudo systemctl enable <service>`|Enable autostart at boot|
|`sudo systemctl disable <service>`|Disable autostart|

**Example – SSH server:**

```bash
systemctl status ssh         # Is SSH running?
sudo systemctl start ssh     # Start SSH
sudo systemctl enable ssh    # Start automatically at boot
```

### Scheduled Tasks with cron

**cron** automatically executes commands at set times

**Edit your own crontab:** `crontab -e`

**Format:** `Minute Hour Day Month Weekday Command`

**Examples:**

```bash
0 2 * * * /home/user/backup.sh          # Daily at 2:00 AM
*/15 * * * * /usr/bin/check-server.sh   # Every 15 minutes
0 0 * * 0 /home/user/weekly-report.sh   # Every Sunday at midnight
```

### Remote Access with SSH

**SSH (Secure Shell)** = encrypted remote access to the command line

**Why SSH?**

- Secure (encrypted)
- Standard for Linux server management
- Enables remote administration

**Basic SSH commands:**

```bash
ssh user@192.168.1.100        # Log in to remote system
scp file.txt user@server:~/   # Copy file
sftp user@server              # Interactive file transfer
```

**Windows equivalent:** PuTTY, Windows Terminal with OpenSSH

### Kali Linux Setup (for the Course)

**Virtualisation on Mac:**

1. Install **VMware Fusion Player** (free personal licence)
    
2. Download **Kali Linux ARM64 ISO** ([kali.org](https://cdimage.kali.org/))
    
3. Create VM, select "Debian 12" as operating system
    
4. Install Kali
    
5. Install **VMware Tools**:
    
    ```bash
    sudo apt update && sudo apt install open-vm-tools-desktop
    sudo reboot
    ```
    

**On Windows 11:**

- Use VMware Workstation Player or VirtualBox
- Download Kali Linux x64 ISO (not ARM)
- Otherwise identical process

### The Most Important Basic Commands (Quick Reference)

|Command|Function|Example|
|---|---|---|
|`pwd`|Show current directory|`pwd`|
|`ls`|List files|`ls -la` (all details)|
|`cd`|Change directory|`cd /home/user/Documents`|
|`mkdir`|Create directory|`mkdir myfolder`|
|`touch`|Create empty file|`touch file.txt`|
|`cp`|Copy|`cp source.txt dest.txt`|
|`mv`|Move/rename|`mv old.txt new.txt`|
|`rm`|Delete (permanent!)|`rm file.txt`|
|`cat`|Show file content|`cat config.txt`|
|`less`|Show file page by page|`less logfile.log`|
|`head`|Show first lines|`head -n 10 file.txt`|
|`tail`|Show last lines|`tail -f /var/log/syslog`|
|`grep`|Filter text|`ps aux \| grep firefox`|
|`\|` (Pipe)|Redirect output|`ls \| grep .txt`|
|`>`|Output to file (overwrite)|`echo "Test" > file.txt`|
|`>>`|Append output|`echo "More" >> file.txt`|

### Practical Examples of Command Combinations

**1. Find all .txt files in the current directory:**

```bash
ls | grep .txt
```

**2. Show the 10 largest files:**

```bash
ls -lhS | head -n 11
```

**3. Show active network connections:**

```bash
ss -tuln
```

**4. Follow system logs in real time:**

```bash
sudo tail -f /var/log/syslog
```

**5. Search for a running process:**

```bash
ps aux | grep firefox
```

### The Most Important Takeaways

✅ **Linux is open source, stable, secure and flexible** ✅ **Everything is a file – hierarchy starts at `/`** ✅ **The shell is powerful – Unix philosophy: combine small tools** ✅ **APT manages software: update → search → install → remove → autoremove** ✅ **Permissions: rwx for User/Group/Others protect data** ✅ **`sudo` for admin tasks instead of root login** ✅ **systemd manages services (start/stop/enable/disable)** ✅ **SSH for secure remote access to servers** ✅ **Install Kali Linux for cybersecurity tasks in a VM** ✅ **Pipe (`|`) and redirection (`>`, `>>`) are essential for efficient working**

## Tools Used

|Tool|Meaning|
|---|---|
|**Bash (Bourne Again Shell)**|Widely used shell and command-line interpreter, default on many Linux distributions|
|**Zsh (Z Shell)**|Modern, powerful shell, default on macOS and Kali Linux|
|**Terminal / Terminal Emulator**|Application for interacting with the shell via command line|
|**APT (Advanced Package Tool)**|Package management system for Debian-based systems such as Kali Linux and Ubuntu|
|**systemd**|Modern init system and service manager for Linux distributions|
|**systemctl**|Command for managing systemd services (start, stop, status, enable/disable)|
|**cron**|Time-based job scheduler for recurring tasks|
|**SSH (Secure Shell)**|Encrypted protocol for secure remote access to the command line|
|**scp (Secure Copy)**|Tool for secure file transfer over SSH|
|**sftp (SSH File Transfer Protocol)**|Secure file transfer protocol over SSH|
|**VMware Fusion Player**|Virtualisation software for macOS (on Windows: VMware Workstation or VirtualBox)|
|**chmod**|Command for changing file permissions|
|**chown**|Command for changing ownership|
|**id**|Shows user ID (UID), group ID (GID) and group memberships|
|**tree**|Shows directory structures in tree view|

## Technical Terms

|Term|Meaning|
|---|---|
|**Unix**|Family of multitasking operating systems from the 1960s/70s, foundation of modern systems|
|**Linux Kernel**|Core of the operating system, manages hardware, processes and system calls|
|**GNU/Linux**|Correct name for "Linux": Linux kernel + GNU software collection|
|**Open Source**|Source code is freely available, can be used, modified and distributed|
|**Distribution (Distro)**|Complete operating system consisting of Linux kernel plus additional software and tools|
|**CLI (Command-Line Interface)**|Text-based user interface for controlling the system via commands|
|**Shell**|Command-line interpreter, interface between user and kernel|
|**File System Hierarchy Standard (FHS)**|Standard directory structure in Linux systems|
|**Root (/)**|Top level of the file system, starting point of the directory hierarchy|
|**Root User (Superuser)**|Administrator account with full system privileges|
|**sudo (Superuser Do)**|Command for temporarily executing commands with root rights|
|**Package**|Archive with all files of a software plus metadata (version, dependencies)|
|**Repository (Repo)**|Server that provides software packages for download|
|**Dependencies**|Other packages required for a software to function|
|**Daemon**|Background process that provides system services (e.g. web server, SSH server)|
|**Init System**|First process started, manages all other processes and services|
|**Crontab**|Configuration file for time-controlled, recurring tasks|
|**UID (User ID)**|Unique numeric identifier of a user|
|**GID (Group ID)**|Unique numeric identifier of a group|
|**Pipe (\|)**|Mechanism for passing the output of one program as input to another|
|**Redirection (>, >>, <)**|Redirecting input/output to/from files|
|**ISO Image**|Image file of a CD/DVD, used for installing operating systems|

## Key Vocabulary

|Vocabulary|Meaning|
|---|---|
|**Owner**|User to whom a file or directory belongs|
|**Group**|Collection of users for simplified rights management|
|**Others**|All users except owner and group members|
|**Read (r)**|Permission to view file contents or directory listings|
|**Write (w)**|Permission to modify files or create/delete within directories|
|**Execute (x)**|Permission to execute files or enter directories|
|**Permissions**|Access rights for files and directories (rwx for u/g/o)|
|**Virtual Machine (VM)**|Simulated computer environment within a host system|
|**Hierarchical File System**|Tree-structure file system with root (/) as starting point|
|**Portable**|Software that can run on different systems|
|**Modular**|Built from independent, interchangeable components|
|**Text Streams**|Text-based data flows between programs|
|**Binary Compatible**|Software runs without changes on different systems of the same architecture|
|**Kernel Space / User Space**|Separation between kernel area (privileged) and user area|
|**Home Directory**|Personal directory of a user (e.g. /home/username)|
|**Configuration Files (Configs)**|Settings files for system configuration (mostly in /etc)|
|**Log Files**|Log files with system messages and events (mostly in /var/log)|

---