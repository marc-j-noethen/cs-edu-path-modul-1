# 🐍 Local Expedition

**Course:** Cyber Security Analyst – Python Basics | **Date:** 11 July 2025

---

## Task

**Objective:** To practise the basic local Git workflow: cloning a remote repository, making local changes, committing these changes and pushing them back to GitHub.

**Requirements:**
- Clone repository: `hello-world`
- Local change: Edit README.md
- Commands: `git status`, `git add`, `git commit`, `git push`
- Result: Screenshots of `git log` and GitHub repository

---

## Solution

**Steps taken:**

1. **Cloned repository:**
```bash
git clone <repository-url>
cd hello-world
```

2. **Edited README.md locally:**
   - Added line: “Local change made!”

3. **Checked status:**
```bash
git status
# Output: Modified README.md detected
```

4. **Staged change:**
```bash
git add README.md
```

5. **Commit made:**
```bash
git commit -m "Update README from local machine"
```

6. **Pushed to GitHub:**
```bash
git push origin main
```

7. **Verified on GitHub:**
   - Repository shows updated README.md with local change

**Evidence:** 
- Screenshot 1: Terminal with `git log` output
- Screenshot 2: GitHub repository with updated README.md

---

## Tests

| Step | Command | Result | ✓ |
|---------|----------|----------|---|
| Clone repository | `git clone` | ✅ Successful | ✅ |
| Make change | Edit README.md | ✅ ‘Local change’ added | ✅ |
| Check status | `git status` | ✅ 'Modified' displayed | ✅ |
| Staging | `git add README.md` | ✅ File staged | ✅ |
| Commit | `git commit -m "..."` | ✅ Commit created | ✅ |
| Push | `git push origin main` | ✅ Pushed to GitHub | ✅ |
| Verification | GitHub check | ✅ Change visible | ✅ |

---

## Notes

- **Concept:** Clone → Edit → Add → Commit → Push workflow
- **Important:** HTTPS vs. SSH for authentication
- **Git log:** Displays the commit history with hashes, author, date and message
- **Best practice:** Use meaningful commit messages
