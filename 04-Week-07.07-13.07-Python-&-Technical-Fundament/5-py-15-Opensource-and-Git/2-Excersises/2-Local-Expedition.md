# 🐍 Open-Source Explorer

**Course:** Cyber Security Analyst – Python Basics | **Date:** 11 July 2025

---

## Task

**Objective:** Explore a popular open-source Python project on GitHub, familiarise yourself with the contribution guidelines, and find out how changes are actually submitted and reviewed.

**Requirements:**
- Repository: [psf/requests](https://github.com/psf/requests)
- Tasks: Read the contribution guidelines, analyse issues, examine merged pull requests
- Output: Answers to 3 questions

---

## Solution

### Question 1: Preferred method for contributions

**Answer:** GitHub Issue Search

The contribution guidelines for the `requests` project primarily expect contributors to use the GitHub Issue Search to first check whether a problem has already been reported before creating new issues or pull requests.

---

### Question 2: Selected issue

**Title:** `builtin_str(method)` converts binary method names incorrectly

**Issue number:** #7152

**Description:** 
In this issue, a developer describes a problem with the `builtin_str` method in `requests/models.py`. The code `method = builtin_str(method)` causes errors when using binary method names, as the function should correctly decode bytes into strings.

---

### Question 3: Pull request analysed

**Title:** ValueError when calling requests.get on Windows systems

**Pull request number:** #6104

**Main purpose:** Workaround for a ValueError that occurred on Windows systems when calling `requests.get`.

**Files modified:**
- `utils.py`

---

## Tests

| Question | Status | ✓ |
|-------|--------|---|
| Question 1: Contribution method identified | GitHub issue search | ✅ |
| Question 2: Issue found and described | #7152 – builtin_str issue | ✅ |
| Question 3: Pull request analysed | #6104 – Windows ValueError fix | ✅ |

---

## Notes

- **Concept:** Open-source contribution workflow
- **Repository:** [psf/requests](https://github.com/psf/requests) – popular HTTP library for Python
- **Learning objective:** To understand how open-source projects are structured and how contributions work
- **Best practice:** Always search for existing issues first before creating new ones
