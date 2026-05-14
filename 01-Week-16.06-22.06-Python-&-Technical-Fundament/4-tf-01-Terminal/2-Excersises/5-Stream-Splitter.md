# 🖥️ Stream Splitter

**Course:** Cyber Security Analyst - Technical Fundament Basics | **Date:** 19 June 2025

---

## Task

**Objective:** Run a command that generates both stdout and stderr, and redirect both streams to separate files.

---

## Solution

### Environment
```
OS: Win11 (WSL/Ubuntu)
Shell: bash
```

### Procedure

**Step 1:** Navigate to the TF1_Exercises directory and create a test file
```bash
cd ~/TF1_Exercises
touch my_commands.txt
```

**Step 2:** Test the command (generates stdout and stderr)
```bash
ls my_commands.txt non_existent_file.txt
```
**Output:**
```
ls: cannot access 'non_existent_file.txt': No such file or directory
my_commands.txt
```
- Line 1 = stderr (error message)
- Line 2 = stdout (normal output)

**Step 3:** Redirect both streams to separate files
```bash
ls my_commands.txt non_existent_file.txt > stdout.log 2> stderr.log
```
**Explanation:**
- `> stdout.log` = Redirects stdout (file descriptor 1) to stdout.log
- `2> stderr.log` = Redirects stderr (file descriptor 2) to stderr.log

**Step 4:** Check the result
```bash
cat stdout.log
```
**Output:** `my_commands.txt`

```bash
cat stderr.log
```
**Output:** `ls: cannot access 'non_existent_file.txt': No such file or directory`

---

## Results

| Step | Command |
|---------|--------|
| Step 3 (Redirect both streams) | `ls my_commands.txt non_existent_file.txt > stdout.log 2> stderr.log` |

---

## Notes

- **File Descriptors:**
  - `0` = stdin (Standard Input)
  - `1` = stdout (Standard Output) – implicit with `>`
  - `2` = stderr (Standard Error)

- **Redirection syntax:**
  - `> file` = stdout to file (overwrite)
  - `>> file` = stdout to file (append)
  - `2> file` = stderr to file
  - `2>> file` = stderr to file (append)
  - `&> file` = stdout AND stderr to file
  - `2>&1` = redirect stderr to stdout

- **Tip:** The order of the redirections is important!
- **Learned:** stdout and stderr are separate channels that can be redirected independently
