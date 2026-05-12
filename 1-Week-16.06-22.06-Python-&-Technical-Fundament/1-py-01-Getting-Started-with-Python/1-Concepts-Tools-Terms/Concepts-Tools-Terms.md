## **📊 Summary according to the 80/20 Principle**

**1. What is Python?**  
Python is a beginner-friendly programming language that:

- Is written in a readable way, like normal English
- Is versatile and used in many areas (Web, AI, Cybersecurity, Automation)
- Is interpreted (code is executed directly, no compilation required)
- Has a huge community and many ready-made libraries

**Why Python in Cybersecurity?**

- Automation of security tests
- Development of security tools
- Malware analysis
- Network analysis

**2. Check Python Installation (Windows 11)**  
**Step 1:** Open PowerShell

```
Windows key + R → cmd or powershell
```

**Step 2:** Check Python version

```powershell
python --version
```

Expected output: Python 3.x.y (e.g. Python 3.11.5)  

If not installed:

1. Download from python.org/downloads
2. Important: Check "Add Python to PATH" during installation!
3. Restart PowerShell after installation
4. Test `python --version` again

Alternative commands (if `python` doesn't work):

```powershell
python3 --version
py --version
```

**3. The Python REPL (Interactive Mode)**  
Start REPL:

```powershell
python
```

What happens:

```
Python 3.11.5 (...)
>>>
```

The `>>>` prompt means: Python is waiting for your commands!  

**REPL = Read-Eval-Print Loop:**

1. Read: Reads your command
2. Eval: Executes it
3. Print: Shows the result
4. Loop: Waits for the next command

**Examples to try:**

```python
>>> 2 + 2
4

>>> print("Hello Cybersecurity!")
Hello Cybersecurity!

>>> 10 * 5
50
```

**Exit REPL:**

```python
>>> exit()
```

or Ctrl + Z → Enter (Windows)

**4. The Most Important Concepts**  
**Functions:**

```python
print("Text")  # Outputs text
```

- `print()` is a function
- Text must be in quotation marks ("..." or '...')

**Strings (Text):**

```python
"This is a string"
'This one too'
```

**Mathematics:**

```python
2 + 2        # Addition
10 * 5       # Multiplication
100 / 4      # Division
2 ** 3       # Exponent (2³ = 8)
```

**5. Windows 11 vs. macOS – The Differences**

| Task                    | macOS                          | Windows 11                     |
|-------------------------|--------------------------------|--------------------------------|
| Open Terminal           | Cmd + Space → "Terminal"       | Win + R → cmd or powershell    |
| Start Python            | python3                        | python or py                   |
| Check version           | python3 --version              | python --version               |
| Exit REPL               | Ctrl + D or exit()             | Ctrl + Z → Enter or exit()     |
| Download link           | python.org/downloads/macos     | python.org/downloads/windows   |

**6. Why Python is Ideal for Beginners**  
✅ Simple syntax – almost like normal English  
✅ Instant feedback – REPL shows results immediately  
✅ Versatile – everything from web to cybersecurity is possible  
✅ Huge community – lots of help and tutorials available  
✅ Many libraries – ready-made code for almost everything  

**Quick Start Checklist:**

```
☐ Open PowerShell (Win + R → powershell)
☐ Run python --version
☐ If not installed: Install from python.org
☐ Type python → Start REPL
☐ Test print("Hello World!")
☐ Calculate 2 + 2
☐ Use exit() to quit
```

**Key Takeaway:** Python is a beginner-friendly, interpreted language. You start the interpreter with `python`, you see the REPL mode with `>>>`, and you output text with `print()`. Everything runs directly in PowerShell (Windows) or Terminal (Mac).

**Table 1: Tools Used**

| Tool (Windows 11)       | Meaning |
|-------------------------|--------|
| PowerShell / CMD        | Command line in Windows (replaces Terminal on macOS) |
| Python Interpreter      | Program that executes Python code |
| REPL (Read-Eval-Print Loop) | Interactive Python mode for testing code directly |
| Python IDLE             | Pre-installed Python development environment (optional) |
| VS Code                 | Code editor for writing Python programs |
| python.org              | Official website for downloading Python |

**Table 2: Technical Terms**

| Technical Term          | Meaning |
|-------------------------|--------|
| Programming Language    | Language for communication between human and computer |
| Syntax                  | Grammar/rules of a programming language |
| Interpreter             | Program that executes code line by line (unlike compiler) |
| Compiled Language       | Language where code is fully translated first (e.g. C++, Java) |
| Interpreted Language    | Language where code is executed directly line by line (e.g. Python) |
| Library / Module        | Pre-made collection of code for specific tasks |
| REPL                    | Read-Eval-Print Loop – interactive interpreter mode |
| Function                | Reusable block of code (e.g. print()) |
| String                  | Text data in quotation marks ("Text" or 'Text') |
| Command Line / CLI      | Text-based user interface (PowerShell/CMD in Windows) |
| Version                 | Specific release of the software (e.g. Python 3.12.3) |
| Stable Release          | Officially released, tested version |
| Pre-release             | Pre-version, still in development |

**Table 3: Important Vocabulary**

| Vocabulary              | Meaning |
|-------------------------|--------|
| Versatile               | Usable for many purposes |
| Automation              | Automating repetitive tasks |
| Execute / Run           | Run code |
| Output                  | Output of a program |
| Prompt                  | Input prompt (e.g. >>> in Python or PS C:\> in PowerShell) |
| Command                 | Instruction that is executed |
| Error Message           | Error notification when problems occur |
| Install                 | Install/set up software |
| Verify                  | Check whether something works |
| Download                | Download files |