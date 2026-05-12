## **📊 Summary according to the 80/20 Principle**

**Text Editor – What is the Difference?**  
**Plain Text vs. Rich Text – The Critical Difference:**

* **Plain Text Editors** (Sublime Text, Notepad, Notepad++, VS Code): Only characters, no hidden formatting. **ALWAYS** use these for code, configuration files, scripts, and logs.

* **Word Processors** (Word, Google Docs): Formatting with fonts, colors, embedded objects. **NEVER** use for code — the hidden formatting will break your code and configuration files!

**Why Sublime Text? (Windows Alternatives)**  
Sublime Text is the course standard (free evaluation version with no time limit) because it:

* Is fast and stable
* Offers syntax highlighting (code is displayed in colors)
* Supports multi-cursor (write in multiple places at the same time)
* Is extensible (Package Control for plugins)

**Windows Alternatives:**

* **Notepad++**: Free, lightweight, great for beginners
* **VS Code**: Free, very powerful, from Microsoft, similar to Sublime Text

**CLI vs. GUI Editors**  
**CLI Editors** (Nano, Vim):

* Run in the terminal
* Keyboard-only control
* Essential for remote servers without a graphical interface
* **Nano**: Simple for beginners (commands shown at the bottom)
* **Vim**: Very powerful, but has a steep learning curve

**GUI Editors** (Sublime Text, Notepad++, VS Code):

* Graphical interface with menus
* Mouse and keyboard control
* Better for local work and beginners

**The 10 Most Important Keyboard Shortcuts for Windows**  
**Basic Editing (works almost everywhere):**

1. Ctrl + C – Copy
2. Ctrl + V – Paste
3. Ctrl + X – Cut
4. Ctrl + Z – Undo
5. Ctrl + S – Save

**Navigation & Efficiency:**
6. Ctrl + F – Search
7. Ctrl + A – Select All
8. Alt + Tab – Switch between programs
9. Ctrl + W – Close tab/window
10. Windows key – Open Start menu/Search

**Bonus for Text Editing:**

* Ctrl + Arrow keys – Jump word by word
* Home / End – Start/end of line
* Shift + Arrow keys – Select text while moving

**Sublime Text Installation (Windows)**

1. Go to: https://www.sublimetext.com/download
2. Download the Windows version (.exe Installer)
3. Run the installer (default settings are fine)
4. Start Sublime Text
5. (Optional) Right-click the icon in the taskbar → "Pin to taskbar"

**Practical Nano Test (Windows with WSL/Git Bash)**  
If you have WSL (Windows Subsystem for Linux) or Git Bash installed:

```bash
nano testfile.txt
# Write some text
# Ctrl + X to exit
# Y for Yes (save)
# Enter to confirm
type testfile.txt          # CMD
Get-Content testfile.txt   # PowerShell
del testfile.txt           # Delete (CMD)
```

**Without WSL:** Use Notepad or install Sublime Text immediately.

**Core Message**  
**The 3 decisive points:**

1. **Plain Text for Code**: Never use Word for code/configurations — always use Sublime Text, Notepad++, or VS Code.
2. **Keyboard Shortcuts = Speed**: The 10 basic shortcuts will save you hours every week.
3. **CLI Editor = Necessity**: Learn at least the basics of Nano — you will need them on servers.

**Windows-Specific:**

* Ctrl replaces Cmd (Mac)
* Alt replaces Option (Mac)
* Windows key replaces Cmd + Space (Mac Spotlight)

**Used Tools, Technical Terms and Important Vocabulary**

**Used Tools**

| Term | Meaning |
|------|--------|
| Text Editor | Program for editing pure text files without formatting |
| Sublime Text | Professional code editor (available for Windows, macOS, Linux) – main tool of the course |
| Nano | Simple CLI text editor for beginners (Windows alternative: nano in WSL or Git Bash) |
| Vim / Vi | Advanced modal CLI editor (available in WSL, Git Bash or as separate installation) |
| Notepad | Default text editor in Windows (simple, few features) |
| Notepad++ | Free enhanced text editor for Windows (alternative to Sublime Text) |
| VS Code | Free, popular code editor from Microsoft (alternative to Sublime Text) |
| Word Processor (Word, Google Docs) | Word processing program – **NOT** suitable for code/configuration files |

**Technical Terms**

| Technical Term | Meaning |
|----------------|--------|
| Plain Text | Pure text without formatting – only characters (.txt, .py, .conf, .log, .xml, .css, .js) |
| Rich Text | Formatted text with fonts, colors, images (.docx, .rtf) |
| CLI Editor | Text editor that runs in the terminal – keyboard control only |
| GUI Editor | Text editor with graphical interface – mouse and menu operation possible |
| Syntax Highlighting | Color highlighting of code elements (keywords, variables, strings) |
| Command Palette | Keyboard quick access to commands (in Sublime Text: Ctrl + Shift + P) |
| Multi-Cursor / Multi-Select | Simultaneous editing in multiple places in the text |
| Package Control | Extension manager for additional features in Sublime Text |
| Modal Editor | Editor with different modes (Vim: Normal mode, Insert mode, etc.) |
| Keyboard Shortcuts / Hotkeys | Keyboard combinations for fast command execution |

**Important File Formats**

| Format | Meaning |
|--------|--------|
| .txt | Simple text file |
| .py | Python program file |
| .sh | Shell script (Linux/Mac) / .bat or .ps1 (Windows scripts) |
| .conf / .ini | Configuration files |
| .log | Log files |
| .xml, .json, .yaml | Structured data files |
| .css, .js, .html | Web development files |

**Terminal Commands (Examples)**

| Command | Meaning |
|---------|--------|
| `nano file.txt` | Opens file in Nano editor (Windows: WSL/Git Bash or alternative editor) |
| `cat file.txt` | Displays file content (Windows CMD: `type file.txt`, PowerShell: `Get-Content file.txt`) |
| `rm file.txt` | Deletes file (Windows CMD: `del file.txt`, PowerShell: `Remove-Item file.txt`) |

**Windows 11 Keyboard Shortcuts (macOS Equivalents)**

| Function | macOS | Windows 11 |
|----------|-------|------------|
| Copy | Cmd + C | Ctrl + C |
| Cut | Cmd + X | Ctrl + X |
| Paste | Cmd + V | Ctrl + V |
| Undo | Cmd + Z | Ctrl + Z |
| Redo | Cmd + Shift + Z | Ctrl + Y or Ctrl + Shift + Z |
| Select All | Cmd + A | Ctrl + A |
| Save | Cmd + S | Ctrl + S |
| Search | Cmd + F | Ctrl + F |
| New Tab | Cmd + T | Ctrl + T |
| Close Tab/Window | Cmd + W | Ctrl + W or Ctrl + F4 |
| Close Application | Cmd + Q | Alt + F4 |
| Word left/right | Option + Arrow | Ctrl + Arrow |
| Start/End of Line | Cmd + Arrow | Home / End |
| Select Text | Shift + Arrow keys | Shift + Arrow keys |
| Select Word | Shift + Option + Arrow | Shift + Ctrl + Arrow |
| Switch Apps | Cmd + Tab | Alt + Tab |
| Open Search | Cmd + Space (Spotlight) | Windows key or Windows + S |
| Screenshot (full screen) | Cmd + Shift + 3 | Windows + Print or Print |
| Screenshot (selection) | Cmd + Shift + 4 | Windows + Shift + S (Snipping Tool) |
| Command Palette (Sublime Text) | Cmd + Shift + P | Ctrl + Shift + P |