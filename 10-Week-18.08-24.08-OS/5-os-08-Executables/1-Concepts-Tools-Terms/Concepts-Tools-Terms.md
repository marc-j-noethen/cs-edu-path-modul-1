# Executables

### What are Executable Files?

An **executable file** (.exe) is a finished set of instructions for your computer. When you launch a program, the CPU reads these instructions and executes them. Under Windows 11, you recognise these files by the `.exe` extension (e.g. `notepad.exe`).

### From Code to Executable: The Journey in 3 Steps

**1. Compilation**

- Programmers write **source code** in languages such as C++ or Python
- A **compiler** translates this human-readable code into **machine code** (number sequences that the CPU understands)
- Intermediate stage: **Assembly language** (close to machine level, but still somewhat readable)

**2. Assembling**

- An **assembler** converts assembly code into actual machine code

**3. Linking**

- A **linker** combines all code parts and libraries into a finished `.exe` file
- Prepares the file for the operating system

### Internal Structure: PE Format (Portable Executable)

Windows executables have a structured organisation:

**Headers**

- Like a table of contents at the beginning
- Contain metadata: program type, memory requirements, entry point

**Sections**

- **Code Section**: Contains the machine instructions
- **Data Section**: Stores program data (texts, settings)
- **Import Table**: List of required external functions (from DLLs)

### The Loading Process: From Double-Click to Execution

When you launch an `.exe`, the **loader** (part of the operating system) carries out the following steps:

1. **Read file**: Analyse headers
2. **Prepare memory**: Reserve RAM area for the program
3. **Load code**: Copy instructions and data from the hard drive into memory
4. **Connect DLLs**: Find and link required external libraries (dynamic linking)
5. **Start program**: CPU begins execution at the entry point

### DLLs: Shared Code Libraries

**What are DLLs?**

- **Dynamic Link Libraries** = Collections of pre-compiled code
- Multiple programs can use the same DLL simultaneously
- Example: Many programs use the same DLL for drawing windows

**Advantages:**

- ✓ Smaller .exe files (no duplicated code)
- ✓ Memory savings (one DLL in RAM, shared by all)
- ✓ Easy updates (update DLL = all programs benefit)

**Disadvantages & Risks:**

- ✗ **DLL Hell**: Missing, corrupted or wrong DLL versions → program won't start
- ✗ **DLL Hijacking**: Attackers inject fake DLLs

**Where do you find DLLs?**

- Mainly in `C:\Windows\System32`
- Hundreds of DLLs providing Windows core services

### Relevance for Cybersecurity

**1. Malware Analysis**

- Malicious software is mostly distributed as `.exe` or `.dll`
- Analysts need to understand the structure in order to recognise damage potential

**2. Attack Vectors**

- Many attacks are based on tricking users into executing malicious executables
- DLL hijacking exploits the loading mechanisms of the system

**3. Digital Forensics**

- After a security incident, executables on compromised systems are examined
- PE analysis shows what the program does and how it works

### Practical Getting Started with CFF Explorer

**Setup for Windows 11 VM:**

1. Download from [ntcore.com/exsuite.php](http://www.ntcore.com/exsuite.php)
2. Extract zip to `C:\Tools\CFFExplorer`
3. Launch `CFF Explorer.exe`
4. Open sample file: `C:\Windows\System32\notepad.exe`

**What can you see?**

- PE header with meta information
- Code, data and import sections
- List of used DLLs and functions

### Quick Test in File Explorer:

```
1. Open: C:\Windows\System32
2. Observe: Hundreds of .dll files
3. Understand: These are the shared libraries of the system
```

**Key takeaway**: Executable = Machine code + PE structure + DLL dependencies. From human code to CPU instruction via Compiler → Assembler → Linker!

## Categorisation of Topics

|**Category**|**Meaning**|
|---|---|
|**Tools Used**||
|CFF Explorer|Forensic tool for analysing PE files (Portable Executable Format), allows inspection of the internal structure of .exe and .dll files|
|Explorer Suite|Software package from NTCore containing CFF Explorer and further analysis tools|
|File Explorer|Windows file manager for navigating and examining system files|
|Compiler|Program that translates human-readable source code (e.g. C++, C#) into machine code|
|Assembler|Tool that converts assembly language into actual machine code|
|Linker|Program that combines various code parts and libraries into an executable file|
|**Technical Terms**||
|Executable File|File with finished instructions for the computer that can be launched directly by the operating system|
|Source Code|Human-readable program code written by programmers (e.g. Python, C++, Java)|
|Machine Code|Sequences of numbers/binary code that the CPU understands and can execute directly|
|Assembly Language|Low-level programming language that is very close to the hardware but slightly more readable than pure machine code|
|Compilation|Process of translating source code into machine code by a compiler|
|PE Format (Portable Executable)|Standard file format for executable files under Windows (.exe, .dll, .sys)|
|Headers|Opening area of a PE file with meta information: program type, memory requirements, entry point of instructions|
|Sections|Organised areas within a PE file for different content (code, data, imports)|
|Loader|Operating system component that loads executable files into memory and prepares them for execution|
|DLL (Dynamic Link Library)|Library file with reusable, pre-compiled code that multiple programs can use simultaneously|
|Dynamic Linking|Process by which programs access external functions in DLLs at runtime|
|Static Linking|Opposite of dynamic linking: all required code is embedded directly in the .exe file|
|DLL Hell|Problem when required DLLs are missing, corrupted, or present in the wrong version|
|DLL Hijacking|Attack technique in which malicious programs attempt to trick programs into loading fake DLLs|
|Dependencies|External files (mostly DLLs) that a program requires in order to function|
|Memory Allocation|Assignment of working memory by the operating system for a running program|
|CPU (Central Processing Unit)|Main processor of the computer that executes machine instructions|
|**Key Vocabulary**||
|.exe|File extension for executable programs under Windows (e.g. notepad.exe)|
|.dll|File extension for Dynamic Link Libraries under Windows|
|notepad.exe|Windows Notepad as an example of a simple executable file|
|C:\Windows\System32|Main directory for Windows system files, contains many DLLs and executable files|
|Import Table|Area in a PE file that lists which external functions from DLLs are required|
|Code Section|Section in a PE file that contains the actual program instructions (machine code)|
|Data Section|Section that contains data used by the program (e.g. texts, settings)|
|Entry Point|Starting point in an executable file where the CPU begins execution|
|Malware|Malicious software (viruses, ransomware, spyware), often distributed as .exe or .dll|
|Malware Analysis|Analysis of malicious software to identify its functionality and damage potential|
|Digital Forensics|Examination of computer systems following security incidents|
|High-level Language|Programming languages such as Python, C++, Java – abstract and human-readable|
|Low-level Language|Machine-level languages such as Assembly – directly hardware-related|

---