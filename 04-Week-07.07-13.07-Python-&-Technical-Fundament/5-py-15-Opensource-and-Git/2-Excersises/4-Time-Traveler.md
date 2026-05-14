# 🐍 Time Traveller

**Course:** Cyber Security Analyst – Python Basics | **Date:** 11 July 2025

---

## Task

**Objective:** Practise navigating your project’s history using `git log` to find past commits, and `git checkout` to view the project status at that point in time.

**Requirements:**
- Create two new commits
- Check the Git history using `git log`
- Switch to an older commit using `git checkout`
- Output: Screenshots and commit hash

---

## Solution

**Steps taken:**

1. **First change:**
```bash
# Edited README.md: “Add another line for the history”
git add README.md
git commit -m “Add history line”
```

2. **Second change:**
```bash
# Edited README.md: “Final line for log test”
git add README.md
git commit -m “Add final line”
```

3. **Checked history:**
```bash
git log
```

**Commit identified:**
- **Hash:** `9afa096bdbdeabcfc1692e4285c29b5213fe6731`
- **Message:** “Add history line”

4. **Time travel performed:**
```bash
git checkout 9afa096bdbdeabcfc1692e4285c29b5213fe6731
# HEAD detached at 9afa096
```

5. **Past state verified:**
   - README.md contains: “Add another line for the history”
   - README.md does NOT contain: “Final line for log test”

6. **Back to the present:**
```bash
git checkout main
```

---

## Tests

| Step | Expected | Result | ✓ |
|---------|----------|--------- -|---|
| Commit 1 created | “Add history line” | ✅ Committed | ✅ |
| Commit 2 created | “Add final line” | ✅ Committed | ✅ |
| Git log executed | Commits visible | ✅ History displayed | ✅ |
| Checkout to old commit | Detached HEAD | ✅ Switched | ✅ |
| README in old state | Only first line | ✅ Correct | ✅ |
| Back to main | Both lines | ✅ Back | ✅ |

---

## Notes

- **Concept:** Git history navigation and detached HEAD state
- **Commit hash:** `9afa096bdbdeabcfc1692e4285c29b5213fe6731`
- **Detached HEAD:** Temporary state for reviewing past versions
- **Warning:** Changes made in Detached HEAD are lost without a branch
- **Alternative:** `git log --oneline` for a compact view
- **Useful:** Helpful for debugging and tracking changes

