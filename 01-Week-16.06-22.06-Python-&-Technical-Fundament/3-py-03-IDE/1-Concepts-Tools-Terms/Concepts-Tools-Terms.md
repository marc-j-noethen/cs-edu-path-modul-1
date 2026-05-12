## **📊 Summary according to the 80/20 Principle**

**1. What is an IDE and why VS Code?**

* IDE = "Professional workbench" for programming with editor, terminal, debugger, and more all in one place
* VS Code = free, popular, powerful, and runs on Windows, macOS, and Linux
* Advantage: Faster workflow thanks to auto-completion, error detection, and everything in one window

**2. Installation on Windows 11 (3 Steps)**  
**Step 1:** Install VS Code

* Go to the website: https://code.visualstudio.com/download
* Download the Windows 64-bit User Installer
* Run the .exe file and follow the installation wizard
* Important: Check "Add to PATH" during installation (enables the `code` command in the terminal)

**Step 2:** Install the Python Extension

* Start VS Code
* Click the Extensions icon (4 squares) in the left sidebar
* Search for "Python"
* Install the **Python** extension by Microsoft (should be the first result)

**Step 3:** Done!

* VS Code is now ready for Python development

**3. Getting to Know the Most Important VS Code Areas**

```
┌─────────────────────────────────────────────────┐
│ Menu Bar (File, Edit, View, ...)                │
├───┬─────────────────────────────────────────────┤
│ A │                                             │
│ c │          Editor Group                       │
│ t │     (This is where you write code)          │
│ i │                                             │
│ v │                                             │
│ i │─────────────────────────────────────────────│
│ t │          Panel (Terminal, Debug, ...)       │
│ y │                                             │
│   ├─────────────────────────────────────────────┤
│ B │ Status Bar (Line, Python version, Errors)   │
│ a └─────────────────────────────────────────────┘
│ r
└───
```

* **Activity Bar (Left):** Icons for File Explorer, Search, Extensions, Debug
* **Editor Group (Center):** Main area for writing code – open multiple files in tabs
* **Panel (Bottom):** Show terminal with **Ctrl + `**
* **Status Bar (Very bottom):** Shows line number, Python interpreter, error count

**4. The 5 Most Important Features That Make Your Life Easier**  
✅ Syntax Highlighting → Code is colorful: keywords blue, strings green, etc.  
✅ Auto-completion → Type `pri` → VS Code suggests `print()`  
✅ Integrated Terminal → No more switching windows! **Ctrl + `**  
✅ Debugger → Step through code line by line and inspect variables  
✅ See errors immediately → Red squiggly lines show errors before you run the program

**5. Command Palette – The Magic Trick**

* Keyboard shortcut: **Ctrl + Shift + P** (Windows)
* Opens a search field for **ALL** VS Code commands
* Examples:
  * Python: Select Interpreter → Choose Python version
  * Format Document → Automatically format code
  * Terminal: Create New Terminal → Open new terminal

**6. Quick Start: First Steps After Installation**  
Create a Python file:

1. File → Create new folder (e.g. `my_python_project`)
2. File → New File → Save as `test.py`
3. Write code:

```python
name = "Max"
print(f"Hello {name}!")
```

4. Open Terminal (**Ctrl + `**)
5. Run the code: `python test.py`

**7. Common Beginner Questions**  
❓ Which Python version is VS Code using?  
→ The current Python version is shown in the bottom right of the Status Bar. Click it to select another one.  

❓ Why don’t I see colors in the code?  
→ The file must be saved with the `.py` extension **AND** the Python extension must be installed.  

❓ How do I open a folder?  
→ File → Open Folder or in terminal: `code my_folder`

**Key Takeaway:**  
**VS Code = Your new best friend for programming!**  
Instead of switching between editor, terminal, and browser, you now have everything in one window – faster, clearer, and more professional.

**Categorization of Topics**

**Used Tools**

| Tool                                      | Meaning |
|-------------------------------------------|--------|
| Visual Studio Code (VS Code)              | Free, open-source code editor from Microsoft for Windows, macOS, and Linux |
| Python Extension for VS Code              | Official Microsoft extension for Python support in VS Code |
| Integrated Terminal                       | Built-in command line in VS Code (saves switching to external terminal) |
| Command Palette                           | Quick access to all VS Code commands (Windows: Ctrl + Shift + P) |
| Debugger                                  | Tool for stepping through code and troubleshooting |
| Extensions Marketplace                    | Library for additional features and extensions |
| Git Integration                           | Built-in version control in VS Code |

**Technical Terms**

| Technical Term                    | Meaning |
|-----------------------------------|--------|
| IDE (Integrated Development Environment) | Complete software environment for programming |
| Syntax Highlighting               | Color coding of code elements (keywords, variables, strings) |
| Auto-completion / IntelliSense    | Automatic code completion while typing |
| Code Formatting                   | Automatic adjustment of code to style guidelines (e.g. PEP 8) |
| Breakpoint                        | Marker in code where execution pauses during debugging |
| Call Stack                        | Order of function calls during program execution |
| Build Automation Tools            | Tools for automating compilation and packaging |
| Source Control                    | Version control of code (e.g. with Git) |
| Activity Bar                      | Left sidebar in VS Code with main functions |
| Side Bar                          | Sidebar that displays content based on Activity Bar selection |
| Editor Group                      | Main area for writing code with tab support |
| Status Bar                        | Bottom status bar with information (line number, Python version, errors) |
| Panel                             | Bottom area for Terminal, Debug Console, Problems, Output |

**Important Vocabulary**

| Vocabulary                        | Meaning |
|-----------------------------------|--------|
| Download Page                     | https://code.visualstudio.com/download |
| Stable Build                      | Stable, tested version (not Beta) |
| Extension                         | Add-on module to extend functionality |
| File Explorer                     | File browser in the Activity Bar |
| Search                            | Search function in the Activity Bar |
| Run & Debug                       | Run and debug section in the Activity Bar |
| View Menu                         | Menu to show/hide panels |
| Terminal Toggle                   | Show/hide terminal (Windows: Ctrl + `) |
| Typo                              | Typing error, avoided by auto-completion |
| Dependencies                        | External libraries/modules required by a project |

**Windows 11 Adjustments (instead of macOS)**

| macOS Instruction                          | Windows 11 Equivalent |
|--------------------------------------------|-----------------------|
| Download: Mac Universal Stable Build       | Download: Windows 64-bit User Installer (or System Installer) |
| Extract .zip → Drag Visual Studio Code.app to Applications | Run .exe installer → Follow installation wizard |
| Start VS Code from Applications            | Start VS Code from Start menu or desktop shortcut |
| Command Palette: Shift + Command + P       | Command Palette: Ctrl + Shift + P |
| Open Terminal: Control + `                 | Open Terminal: Ctrl + ` |
| Shell Command: Install 'code' command in PATH | `code` command is added automatically (check "Add to PATH" option) |
| Enter administrator password               | Run installer as Administrator (right-click → "Run as administrator") |