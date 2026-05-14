# The Gitting Tree (Open Source & Git)

**Course:** Cyber Security Analyst - Python Basics | **Date:** 11 July 2025

---

## Task

**Objective:**  
Practise the basic concepts of Git in Learn Git Branching: commits, branches, merges and rebases.

**Requirements:**

- Open Learn Git Branching and complete several levels.
- Apply the most important Git commands in practice.
- Briefly note down what has been learnt in each section.
- Document your progress with a screenshot.

---

## Solution

```bash
# typical commands found in the first core levels

git commit
git branch bugFix
git checkout bugFix
git checkout -b feature
git merge bugFix
git rebase main
git checkout main
git merge feature
```

**Alternative (compact):**

```text
Commit = Snapshot
Branch = movable pointer to commits
Merge = merging two development branches
Rebase = repositioning commits on a new basis
```

---

## Tests

|Scenario|Expected|Result|✓|
|---|---|---|---|
|First commit|New snapshot appears in the graph|Commit creates a new node|✅|
|Create branch|New pointer to current commit|`bugFix` points to the same commit|✅|
|Merge or Rebase|History is extended appropriately|Graph shows merge or new base|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|Commit|Saves a state of the project as a snapshot.|
|Branch|Enables parallel work on different ideas.|
|Merge vs. Rebase|Merge keeps branches visible, Rebase rewrites the basis of the commits.|

---

## Rules / Logic

```text
Commit small, meaningful changes.
Use branches for separate work steps.
Merge for a traceable history, Rebase for a linear history.
```

---

## Notes

- **Concept:** Git stores snapshots, not just file differences in the user’s head.
- **Syntax:** `git branch`, `git checkout`, `git merge`, `git rebase`.
- **Order is important:**
    1. Create a commit base
    2. Create and switch to a branch
    3. Integrate changes
- **Edge cases:**
    - Rebase can cause conflicts.
    - Merge can create a merge commit.
    - Branches without a checkout are easily confused.
- **Tip:** In Learn Git Branching, it helps to briefly visualise the expected graph in your mind before each command.

---

## Optional: Extensions

- Try `git log --oneline --graph --all` locally.
- Recreate your own mini-repo with merge and rebase.
- Add cherry-pick and reset as the next topics.

