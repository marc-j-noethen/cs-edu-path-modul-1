# 🐍 Selective Sight

**Course:** Cyber Security Analyst - Python Basics | **Date:** 11 July 2025

---

## Task

**Objective:** Understand the purpose of a `.gitignore` file and practise using it to prevent Git from tracking specific files or patterns.

**Requirements:**
- Create a dummy file: `my_secret_api_key.txt`
- Create a `.gitignore` file
- Compare Git status before and after `.gitignore`
- Output: 3 screenshots (status before, .gitignore contents, status after)

---

## Solution

**Steps taken:**

1. **Secret file created:**
```bash
touch my_secret_api_key.txt
```

2. **Status before .gitignore:**
```bash
git status
```
**Output:** `my_secret_api_key.txt` appears under "Untracked files"

3. **.gitignore created and edited:**
```bash
# .gitignore file created
echo "my_secret_api_key.txt" > .gitignore
```

**Contents of .gitignore:**
```
my_secret_api_key.txt
```

4. **Status after .gitignore:**
```bash
git status
```
**Output:** 
- `my_secret_api_key.txt` is NO LONGER listed
- `.gitignore` appears as an untracked file

5. **.gitignore added to the repository:**
```bash
git add .gitignore
git commit -m "Add .gitignore to exclude secret key file"
```

6. **Pushed to GitHub:**
```bash
git push origin main
```

---

## Tests

| Step | Expected | Result | ✓ |
|---------|----------|----------|---|
| Secret file created | `my_secret_api_key.txt` | ✅ Present | ✅ |
| Status (before ignore) | File untracked | ✅ Visible | ✅ |
| .gitignore created | File exists | ✅ Created | ✅ |
| .gitignore content | `my_secret_api_key.txt` | ✅ Added | ✅ |
| Status (after ignore) | Secret not listed | ✅ Ignored | ✅ |
| .gitignore committed | In repository | ✅ Committed | ✅ |
| Push to GitHub | Remote updated | ✅ Pushed | ✅ |

---

## Notes

- **Concept:** `.gitignore` protects sensitive data from accidental commits
- **Important:** `.gitignore` itself should ALWAYS be committed
- **Patterns:** Supports wildcards (*.log, *.env, /temp/*)
- **Use Cases:** 
  - API keys and secrets
  - Build artefacts (dist/, build/)
  - Dependencies (node_modules/)
  - IDE configurations (.vscode/, .idea/)
  - OS files (.DS_Store, Thumbs.db)
- **Best practice:** Create early in the project to avoid errors
- **Template:** GitHub provides .gitignore templates for various languages

