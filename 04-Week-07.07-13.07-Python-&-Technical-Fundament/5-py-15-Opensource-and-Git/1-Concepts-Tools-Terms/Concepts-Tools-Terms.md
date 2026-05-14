# Python Lesson 15: Open Source, Git & GitHub

## Adjustments for Windows 11 (instead of macOS)

|macOS|Windows 11|
|---|---|
|**Open Terminal:** Applications > Utilities > Terminal|**CMD/PowerShell:** Windows key → type "cmd" or "powershell"|
|**Or:** Spotlight → "Terminal"|**Or:** Git Bash (recommended after Git installation)|
|**Install Git:** Command Line Developer Tools or git-scm.com|**Install Git:** https://git-scm.com/download/win|
|Check `git --version`|Check `git --version` (in CMD, PowerShell or Git Bash)|
|Terminal commands: Unix-based|**Git Bash:** Unix-like commands (recommended)|
||**CMD/PowerShell:** Windows commands (works, but Git Bash is better)|
|Path separator: `/`|Path separator: `\` (Git Bash accepts both)|

**Important for Windows:**

- **Install Git Bash:** Comes with Git for Windows (check "Git Bash Here" option during installation)
- **Use Git Bash:** Right-click in folder → "Git Bash Here"
- **Alternative:** Visual Studio Code integrated terminal (recommended!)

**Installation on Windows 11:**

1. Download: https://git-scm.com/download/win
2. Run installer
3. Important options:
    - Enable "Git Bash Here"
    - "Git from the command line and also from 3rd-party software"
    - Default editor of your choice (VS Code recommended)
4. After installation: Open Git Bash or VS Code terminal
5. Configuration as described in the text

---

## Summary Based on the 80/20 Principle

### The 20% core knowledge that covers 80% of practical application:

---

## **PART 1: OPEN SOURCE – THE PHILOSOPHY**

### **1. What is Open Source?**

**Definition:**

- **Source code is publicly** accessible
- Anyone can **view, modify, share** code
- Based on **transparency** and **community**

**Opposite: Proprietary (Closed)**

- Code is secret (e.g. Windows, Photoshop)
- Only the manufacturer can make changes
- "Black box" approach

---

**Well-known Open Source examples:**

- **Linux** (operating system)
- **Python** (programming language!)
- **Firefox** (browser)
- **Android** (mobile OS, based on Linux)
- **Nmap** (network scanner)
- **Wireshark** (packet analysis)
- **Metasploit** (penetration testing)

---

### **2. The 3 Freedoms of Open Source**

**1. Study**

```python
# You can see HOW a tool works
# Example: View Nmap source code on GitHub
# → Learn from the best!
```

**2. Modify**

```python
# Works almost, but not quite?
# → Change it yourself!
# Example: Adapt a security script for your network
```

**3. Share**

```python
# Made an improvement?
# → Share it with the community!
# → Others benefit, you build reputation
```

---

### **3. Why Open Source in Cybersecurity?**

**1. Trust through Transparency**

```
Closed Source: "Trust us, it's secure" 🤷
Open Source: "Here's the code, check it yourself" ✅
```

**2. Security through "Many Eyes"**

- Thousands of developers worldwide review code
- Bugs are found faster
- "Many eyes make all bugs shallow"

**3. Customisability**

- Tool almost does what you need?
- Modify it for your requirements

**4. Learning**

- Best learning resource: reading code from professionals
- Understand how real tools work

---

## **PART 2: VERSION CONTROL – THE PROBLEM**

### **4. The Chaos Without Version Control**

**Scenario 1: Solo Development**

```
project_final.py
project_final_v2.py
project_final_v2_truly_final.py
project_final_v2_truly_final_this_time_for_real.py
project_final_NEW.py
```

- Which version works?
- What was the difference?
- How to get back to the working version?

---

**Scenario 2: Team Work**

```
Alice: project_v1.py
  ↓ (email to Bob)
Bob: project_v2.py (changes function A)
  ↓ (email back)
Alice: project_v3.py (simultaneously changes function B)

How to combine? 😱
```

**Problems:**

- ❌ Changes get lost
- ❌ Conflicts when merging
- ❌ No tracking of who changed what
- ❌ No easy "undo" to the old version

---

## **PART 3: GIT – THE SOLUTION**

### **5. What is Git?**

**Git = Time machine for your code**

- Created by **Linus Torvalds** (creator of Linux)
- **Distributed** system (everyone has the complete history)
- Fast, flexible, powerful
- Industry standard

**Metaphor:**

- Git = Detailed lab notebook
- Every change is recorded
- Can scroll back at any time

---

### **6. Git Core Concepts**

**1. Repository (Repo)**

- Project folder with Git history
- Contains `.git` folder (hidden)

**2. Commit**

- Snapshot/photo of the entire project at a specific point in time
- With description: "What was changed?"

**3. Branch**

- Separate line of development
- `main` = main branch
- Feature branches for new features

**4. Merge**

- Combining branches

---

### **7. Git Workflow Visualised**

```
Working Directory     Staging Area         Repository
(Your files)          (Preparation)        (Commits)
     
     [file.py] -----> git add -----> [file.py] -----> git commit -----> [Commit]
                                                                          ↓
                                                                    History
```

**The 3 Areas:**

1. **Working Directory:** Where you work
2. **Staging Area:** Preparation for commit (what should be saved?)
3. **Repository:** Saved commits (history)

---

### **8. Basic Git Commands**

**Setup (one-time):**

```bash
# Set Git identity
git config --global user.name "Your Name"
git config --global user.email "your@email.com"

# Check version
git --version
```

**Create repository:**

```bash
# Initialise new Git repo
git init

# Show status
git status
```

**Save changes:**

```bash
# Add files to staging area
git add file.py           # Single file
git add .                 # All files

# Create commit
git commit -m "Description of the change"

# Show history
git log
git log --oneline         # Compact view
```

---

### **9. Practical Example: First Steps**

```bash
# 1. Create folder and navigate into it
mkdir my_project
cd my_project

# 2. Initialise Git
git init
# Output: Initialized empty Git repository in ...

# 3. Create file
echo "print('Hello World')" > hello.py

# 4. Check status
git status
# Output: Untracked files: hello.py

# 5. Add to staging area
git add hello.py

# 6. Check status again
git status
# Output: Changes to be committed: new file: hello.py

# 7. Create commit
git commit -m "First version: Hello World program"

# 8. View history
git log
# Shows: Commit ID, author, date, message
```

---

### **10. Branches – Parallel Development**

**Why Branches?**

- Experiment without risking the main code
- Work on features in isolation
- Multiple developers work in parallel

```bash
# Create new branch and switch to it
git checkout -b feature-login

# Make changes...
echo "def login(): pass" > login.py
git add login.py
git commit -m "Added login feature"

# Back to main
git checkout main

# Merge feature branch
git merge feature-login
```

**Visualisation:**

```
main:     [A] ──────────────── [D (merge)]
                    ↘              ↗
feature:              [B] ── [C]
```

---

## **PART 4: GITHUB – THE ONLINE PLATFORM**

### **11. What is GitHub?**

**GitHub = Social network for code**

- Online platform for Git repositories
- **Remote repository** (in the cloud)
- Collaboration features
- Portfolio for developers

**Main functions:**

1. **Host code** (backup + access anywhere)
2. **Collaborate** (pull requests, issues)
3. **Discover** (millions of open source projects)
4. **Learn** (view other people's code)
5. **Build a profile** (living portfolio)

---

### **12. GitHub Core Concepts**

**1. Remote Repository**

- Repository on GitHub servers
- Central location for collaboration

**2. Clone**

- Copies a remote repo to your local computer

```bash
git clone https://github.com/username/repository.git
```

**3. Push**

- Uploads local commits to GitHub

```bash
git push origin main
```

**4. Pull**

- Fetches changes from GitHub

```bash
git pull origin main
```

**5. Pull Request (PR)**

- Formal request: "I would like to contribute these changes"
- Code review possible
- Discussion about changes

**6. Issues**

- Bug tracking
- Feature requests
- Discussions

**7. Fork**

- Personal copy of someone else's repo
- Basis for your own changes

---

### **13. GitHub Workflow**

```
Local Computer                      GitHub (Remote)
     
[Local Repo] ────── git push ────→ [Remote Repo]
       ↑                                    ↓
       └──────────── git pull ──────────────┘
                                            
                                        [Fork]
                                            ↓
                                    [Pull Request]
```

**Typical process:**

1. Create repository on GitHub
2. Clone locally: `git clone`
3. Make changes and commit
4. Push to GitHub: `git push`
5. On GitHub: Create pull request (for team projects)

---

### **14. Creating a GitHub Account**

**Steps:**

1. Go to https://github.com
2. Click "Sign up"
3. **Username:** Choose professionally (will be publicly visible!)
4. **Email:** Use the same one as in `git config`
5. Verify email
6. Complete profile (optional but recommended)

**Profile tips:**

- ✅ Clear profile picture
- ✅ Bio with skills
- ✅ Link to portfolio/LinkedIn
- ✅ Pinned repositories (showcase best projects)

---

## **PART 5: GIT + GITHUB TOGETHER**

### **15. First Project on GitHub**

**Local project to GitHub:**

```bash
# 1. On GitHub: Create new repository
#    → "New" button
#    → Name: "my-first-project"
#    → Choose Public or Private
#    → Do NOT "Initialize with README" (already exists locally)

# 2. Locally: Add remote
git remote add origin https://github.com/username/my-first-project.git

# 3. First push (upload to GitHub)
git push -u origin main

# 4. Refresh on GitHub → Code is online! 🎉
```

**Future pushes:**

```bash
# Make changes
git add .
git commit -m "Added feature XYZ"
git push  # Short, because -u origin main is already set
```

---

### **16. Cloning and Contributing to Someone Else's Project**

**Workflow:**

```bash
# 1. On GitHub: Find an interesting project

# 2. Fork (create your own copy)
#    → "Fork" button on GitHub

# 3. Clone locally
git clone https://github.com/YOUR-USERNAME/project-name.git
cd project-name

# 4. Make changes
# ... edit code ...
git add .
git commit -m "Fixed bug in function X"

# 5. Push to your fork
git push origin main

# 6. On GitHub: Create pull request
#    → "New Pull Request"
#    → Description of the change
#    → Original author can review and merge
```

---

## **PRACTICAL EXAMPLES**

### **17. Example 1: Python Project with Git**

```bash
# Project setup
mkdir password-generator
cd password-generator
git init

# First version
cat > generator.py << 'EOF'
import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

if __name__ == "__main__":
    print(generate_password())
EOF

git add generator.py
git commit -m "Initial commit: Basic password generator"

# Add feature: special characters
cat > generator.py << 'EOF'
import random
import string

def generate_password(length=12, special_chars=True):
    characters = string.ascii_letters + string.digits
    if special_chars:
        characters += string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

if __name__ == "__main__":
    print(generate_password(16, True))
EOF

git add generator.py
git commit -m "Feature: Add special characters option"

# View history
git log --oneline
```

---

### **18. Example 2: Branch for Experimental Feature**

```bash
# Main code remains stable
git checkout -b experimental-encryption

# Experimental function
cat >> generator.py << 'EOF'

def encrypt_password(password, key):
    # Simple XOR encryption (demo only!)
    return ''.join(chr(ord(c) ^ key) for c in password)
EOF

git add generator.py
git commit -m "Experimental: Password encryption"

# Testing...
# If successful: Go back to main and merge
git checkout main
git merge experimental-encryption

# If not successful: Delete branch
# git branch -d experimental-encryption
```

---

### **19. Example 3: Using .gitignore**

```bash
# Exclude certain files from Git
cat > .gitignore << 'EOF'
# Python
__pycache__/
*.pyc
*.pyo
*.pyd

# Virtual Environment
venv/
env/

# IDE
.vscode/
.idea/

# OS
.DS_Store
Thumbs.db

# Secrets
.env
config.secret.json
EOF

git add .gitignore
git commit -m "Add .gitignore for Python project"
```

**Important:** Never commit passwords or API keys!

---

## **QUICK REFERENCE**

### **Git Cheatsheet:**

```bash
# Setup
git config --global user.name "Name"
git config --global user.email "email@example.com"

# Repository
git init                    # New repo
git clone <url>             # Clone remote

# Changes
git status                  # Show status
git add <file>              # Add file to staging area
git add .                   # All files
git commit -m "message"     # Create commit

# History
git log                     # Full history
git log --oneline           # Compact view

# Branches
git branch                  # Show branches
git checkout -b <name>      # Create new branch
git checkout <name>         # Switch branch
git merge <branch>          # Merge branch

# Remote (GitHub)
git remote add origin <url> # Add remote
git push origin main        # Push to GitHub
git pull origin main        # Pull from GitHub
```

### **GitHub Workflow:**

```
1. Fork → 2. Clone → 3. Branch → 4. Commit → 5. Push → 6. Pull Request
```

---

## **COMMON MISTAKES AND SOLUTIONS**

### **20. Mistake 1: Forgot Commit Message**

```bash
# ❌ Mistake
git commit
# Opens editor, confusing for beginners

# ✅ Solution: Use -m flag
git commit -m "Meaningful message"
```

---

### **21. Mistake 2: Wrong Email in git config**

```bash
# ❌ Problem: Email on GitHub differs from Git
# → Commits won't be linked to GitHub profile

# ✅ Solution: Check and correct
git config --global user.email
git config --global user.email "correct@email.com"
```

---

### **22. Mistake 3: Committed Sensitive Data**

```bash
# ❌ Committed passwords/API keys
git add config.py  # contains password!
git commit -m "Added config"

# ✅ Solution: Remove from history (complicated!)
# Better: Use .gitignore BEFOREHAND and never commit!

# If it already happened:
git rm --cached config.py
# Add to .gitignore
echo "config.py" >> .gitignore
git commit -m "Remove sensitive file"
```

**Important:** Once pushed = hard to undo!

---

## **EXERCISES**

**Exercise 1:** Create a local Git repository for a Python project. Make 3 commits with different changes.

**Exercise 2:** Create a GitHub account and push your local repository online.

**Exercise 3:** Find an open source Python project on GitHub (e.g. "requests" library). Clone it and view the commit history.

**Exercise 4:** Create a branch for a new feature in your project. Merge it back to main.

---

### **Key Takeaways:**

🎯 **Open Source = Transparency, Sharing, Community**  
🎯 **Git = Time machine for code (commits = snapshots)**  
🎯 **GitHub = Social network + cloud for Git projects**  
🎯 **Workflow: Add → Commit → Push**  
🎯 **Branches = safe experiments, Main = stable code**  
🎯 **Never commit passwords/API keys! (use .gitignore)**  
🎯 **Git email = GitHub email (for profile linking)**

---

## Tools Used

|Category|Term|Meaning|
|---|---|---|
|**Tools Used**|Git|Distributed version control system for code management|
||GitHub|Online platform for hosting and collaborating on Git projects|
||Terminal/Command Line|Command-line interface for Git commands (Windows: CMD, PowerShell, Git Bash)|
||Git Bash (Windows)|Unix-like command line for Git on Windows|
||Text Editor|For editing code and commit messages|
||Web Browser|For accessing GitHub.com|

---

## Technical Terms

|Category|Term|Meaning|
|---|---|---|
|**Technical Terms**|Open Source Software (OSS)|Software with publicly accessible source code|
||Proprietary Software|Closed software with secret source code|
||Source Code|Human-readable program code|
||Version Control System (VCS)|System for tracking code changes|
||Distributed VCS|Every developer has the complete project history|
||Repository (Repo)|Project folder with complete Git history|
||Remote Repository|Online-hosted repository (e.g. on GitHub)|
||Local Repository|Git repository on local computer|
||Commit|Saved snapshot of the project state|
||Branch|Separate line of development in the project|
||Main/Master Branch|Main development branch|
||Merge|Combining branches|
||Checkout|Switching to another branch or commit|
||Clone|Copying a remote repository to the local computer|
||Push|Uploading local commits to remote repository|
||Pull|Downloading changes from remote repository|
||Pull Request (PR)|Formal request to contribute changes to a project|
||Issue|Tracking bugs and feature requests|
||Fork|Personal copy of someone else's repository|
||License|Legal terms for use/distribution|
||Collaboration|Working together on projects|
||Code Review|Review of code by other developers|
||Transparency|Disclosure of source code|
||Community|Community of developers and users|
|**Key Vocabulary**|`git --version`|Shows installed Git version|
||`git config --global user.name`|Sets Git username|
||`git config --global user.email`|Sets Git email address|
||`git init`|Initialises new Git repository|
||`git status`|Shows status of working directory|
||`git add`|Adds files to staging area|
||`git commit`|Creates commit with snapshot|
||`git log`|Shows commit history|
||`git branch`|Manages branches|
||`git checkout`|Switches branch or restores old version|
||`git merge`|Merges branches together|
||`git clone`|Clones remote repository|
||`git push`|Uploads commits to remote|
||`git pull`|Fetches changes from remote|
||Commit Message|Description of changes in the commit|
||Working Directory|Current working folder with files|
||Staging Area|Intermediate area before commit|
||.git Folder|Hidden folder with Git data|
||README.md|Project description file (Markdown)|
||.gitignore|File listing files to be ignored|