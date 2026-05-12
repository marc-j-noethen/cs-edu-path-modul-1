## **📊 Summary according to the 80/20 Principle**

**The Terminal – What and Why?**  
The Terminal (Windows: Command Prompt/PowerShell) is a text-based alternative to the graphical interface. Instead of mouse clicks, you enter commands. It is faster, more powerful, and essential in cybersecurity because many tools only work here and you can automate processes.

**The 4 Most Important Navigation Commands (Windows Equivalents)**

1. **cd** (without parameters) or **pwd** → Shows where you are currently

   * Windows CMD: `cd`
   * Windows PowerShell: `pwd` or `Get-Location`

2. **dir** or **ls** → Shows files and folders in the current directory

   * Windows: `dir` (CMD) or `ls` (PowerShell)

3. **cd FolderName** → Changes into a folder

   * Example: `cd Documents`

4. **cd ..** → Goes one level up

   * Windows: identical

**Understanding Paths**

* **Absolute Path:** Full address starting from the hard drive  
  * Windows: `C:\Users\YourName\Documents\file.txt`

* **Relative Path:** From your current location  
  * `.\Documents` (current directory → Documents)  
  * `..\Pictures` (one level up → Pictures)

**Environment Variables – The Most Important**  
Environment variables are system settings that programs use. The most important one is **PATH** — it tells the system where to find programs.

**Display:**

* Windows CMD: `set`
* Windows PowerShell: `Get-ChildItem Env:` or `dir env:`
* Specific: `echo %PATH%` (CMD) or `$env:PATH` (PowerShell)

**Getting Help**

* Windows CMD: `command /?` (e.g. `dir /?`)
* Windows PowerShell: `Get-Help command` (e.g. `Get-Help Get-ChildItem`)

**Practical Tip for Windows**  
The Windows equivalent to the macOS Terminal is:

* **Command Prompt (CMD):** Classic, simpler
* **PowerShell:** More modern, more powerful, closer to Linux/Mac

**Open PowerShell:** Press Windows key → type “PowerShell” → Enter

**Key Takeaway:**  
The terminal feels unfamiliar at first, but it’s like learning to drive — complicated in the beginning, then indispensable. With these four basic commands (`cd`, `dir`/`ls`, `cd ..`, `cd Folder`) you can already master 80% of basic navigation.

**Used Tools, Technical Terms and Important Vocabulary**

**Used Tools**

| Term | Meaning |
|------|--------|
| Terminal / Command Prompt | Windows application for entering commands as text (Command Prompt or PowerShell) |
| GUI (Graphical User Interface) | Graphical user interface – operation via mouse clicks, icons and windows |
| CLI (Command-Line Interface) | Command-line interface – operation via text input |
| Shell (bash/zsh/PowerShell) | Program that interprets and executes commands (Windows uses PowerShell or CMD) |
| man / Get-Help | Help system for commands (Windows: `Get-Help` in PowerShell or `command /?` in CMD) |

**Technical Terms**

| Technical Term | Meaning |
|----------------|--------|
| Working Directory | Current working directory – the folder you are currently in |
| Root Directory | Root directory – top level of the file system (Windows: `C:\` instead of `/`) |
| Home Directory | User home directory (Windows: `C:\Users\Username`) |
| Absolute Path | Full path from the root (Windows: `C:\Users\Name\Documents\file.txt`) |
| Relative Path | Path relative to the current directory (`.\Documents\file.txt` or `..\Pictures`) |
| Environment Variables | System-wide settings and configurations |
| PATH Variable | List of directories where executable programs are searched for |
| Parent Directory | Parent directory – one level higher in the folder structure |
| Hidden Files | Hidden files – usually invisible system files |
| Script | Automated program consisting of multiple commands |

**Important Commands**

| Command | Meaning |
|---------|--------|
| `pwd` / `cd` (no parameters) | Shows current path (PowerShell: `Get-Location` or `pwd`, CMD: `cd`) |
| `ls` / `dir` | Lists files and folders (Windows: `dir` in CMD, `Get-ChildItem` or `ls` in PowerShell) |
| `cd <Folder>` | Changes to the specified folder (same in Windows) |
| `cd ..` | Moves one level up (same in Windows) |
| `cd \` | Changes to root directory (Windows: `cd C:\`) |
| `cd ~` / `cd %USERPROFILE%` | Changes to home directory (CMD: `cd %USERPROFILE%`, PowerShell: `cd ~`) |
| `printenv` / `env` | Shows environment variables (CMD: `set`, PowerShell: `Get-ChildItem Env:`) |
| `echo $VARIABLE` / `echo %VARIABLE%` | Shows value of a variable (CMD: `echo %VARIABLE%`, PowerShell: `$env:VARIABLE`) |
| `export` / `set` | Sets environment variable temporarily (CMD: `set VAR=value`, PowerShell: `$env:VAR="value"`) |