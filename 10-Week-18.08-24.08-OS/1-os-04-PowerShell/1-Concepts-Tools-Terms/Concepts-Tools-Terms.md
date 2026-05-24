## **PowerShell: The Essential 20% for 80% of Understanding**

### What is PowerShell?

PowerShell is Microsoft's modern automation solution for Windows 11 (and other platforms). The key difference from conventional shells: **PowerShell works with objects instead of plain text**. This enables significantly more elegant and powerful automation.

### The Most Important Concepts:

**1. Cmdlets (Verb-Noun Structure)**

- All commands follow the pattern: `Verb-Noun` (e.g. `Get-Process`, `Set-Location`)
- The most common verbs: `Get` (retrieve), `Set` (set), `Start`/`Stop` (start/stop), `New`/`Remove` (create/remove)

**2. Pipeline (`|`)**

- Connects commands and passes objects (not text!) between them
- Example: `Get-Process | Sort-Object CPU -Descending` sorts processes by CPU usage

**3. Objects Instead of Text**

- Every output is a structured object with properties and methods
- This eliminates tedious text parsing – you access properties directly

**4. Variables**

- Always start with `$` (e.g. `$processes = Get-Process`)
- Store values, objects, or entire collections for further use

### The 5 Most Important Cmdlets to Start With:

1. **`Get-Help`** – Your most important learning tool (parameters: `-Examples`, `-Detailed`, `-Online`)
2. **`Get-Command`** – Finds available commands
3. **`Get-Process`** – Shows running processes
4. **`Get-Service`** – Shows Windows services
5. **`Get-ChildItem`** – Lists files/folders (like `dir` or `ls`)

### Critical for Windows 11: Execution Policy

Before you can run scripts (`.ps1` files), you need to adjust the execution policy:

1. Open PowerShell **as Administrator**
2. Run the command: `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser`
3. Confirm with `Y`

**RemoteSigned** means: Your own scripts run, downloaded scripts must be signed – a good security compromise for learning.

### Why PowerShell Matters in Cybersecurity:

- **Incident Response**: Rapid data collection on compromised systems
- **Forensics**: Access to event logs, registry, services
- **Penetration Testing**: Attackers use PowerShell – you need to understand it in order to defend
- **Automation**: Security checks, compliance reports, remediation tasks

### Immediate Getting Started in the Console:

```
Get-Location              # Where am I?
Set-Location C:\          # Navigation
Get-ChildItem             # What's here?
Get-Process | Sort-Object CPU -Descending | Select-Object -First 10  # Top 10 processes
Get-Help Get-Process -Examples  # How does a command work?
```

**Key takeaway**: PowerShell = Objects + Pipeline + Verb-Noun + `Get-Help` is your friend!

## Categorisation of Topics

|**Category**|**Meaning**|
|---|---|
|**Tools Used**||
|PowerShell|Cross-platform automation solution with command-line shell, scripting language, and configuration framework by Microsoft|
|PowerShell ISE|Integrated scripting environment for Windows for writing and testing PowerShell scripts|
|Visual Studio Code|Modern code editor with excellent PowerShell support for development|
|Windows PowerShell|The version of PowerShell pre-installed on Windows (from Windows 7 SP1)|
|.NET Framework|Foundation of PowerShell, enables working with objects instead of plain text|
|**Technical Terms**||
|Cmdlets|Lightweight commands in PowerShell that perform a specific function (verb-noun syntax)|
|Pipeline (`\|`)|Mechanism for passing the output (objects) of one cmdlet as input to another|
|Objects|Structured data units with properties and methods, not just text|
|Parameters|Options that modify the behaviour of cmdlets (with `-` prefix)|
|Variables|Data storage in PowerShell, always start with `$` (e.g. `$myName`)|
|Execution Policy|Security feature that controls whether and which scripts can be executed|
|Aliases|Shorthand commands for frequently used cmdlets (e.g. `dir` for `Get-ChildItem`)|
|Properties|Characteristics/attributes of an object (e.g. ProcessName, CPU, Status)|
|Methods|Actions that an object can perform|
|`$_`|Special variable that refers to the current object in the pipeline|
|**Key Vocabulary (Verb-Noun Cmdlets)**||
|Get-Process|Retrieves a list of currently running processes|
|Get-Service|Retrieves information about Windows services|
|Get-Help|Displays help information about cmdlets and concepts|
|Get-Command|Lists all available commands|
|Get-ChildItem|Lists files and directories (alias: `dir`, `ls`)|
|Set-Location|Changes the current working directory (alias: `cd`)|
|Get-Location|Displays the current directory path (alias: `pwd`)|
|Sort-Object|Sorts objects by a specified property|
|Where-Object|Filters objects based on conditions|
|Select-Object|Selects specific properties from objects (alias: `select`)|
|Start-Service|Starts a specified service|
|Stop-Process|Terminates a running process|
|Clear-Host|Clears the screen content (alias: `cls`)|
|Update-Help|Updates the help files (requires administrator rights)|
|Get-ExecutionPolicy|Displays the current execution policy|
|Set-ExecutionPolicy|Changes the execution policy for scripts|
|Get-Alias|Shows what an alias stands for|
