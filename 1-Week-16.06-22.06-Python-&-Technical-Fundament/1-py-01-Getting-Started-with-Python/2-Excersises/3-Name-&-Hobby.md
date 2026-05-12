# 🐍 Name and Hobby (Multiple inputs)

**Course:** Cyber Security Analyst - Python Basics | **Date:** 16 June 2025

---

## Task

**Objective:** Prompt the user for two pieces of input and display them as a summary.

**Requirements:**
- Prompt 1: `First name:` (no space at the end)
- Prompt 2: `Favorite hobby:` (no space at the end)
- Output: `Summary: [Name]'s favourite hobby is [Hobby].`
- Use: String concatenation or f-strings

---

## Solution

```python
Name = input("First name: ")
Hobby = input("Favorite hobby: ")
print("Summary: " + Name + "'s favorite hobby is " + Hobby + ".")
```

**Alternative solutions:**
```python
# Using f-strings (recommended)
name = input("First name: ")
hobby = input("Favourite hobby: ")
print(f"Summary: {name}'s favourite hobby is {hobby}.")

# Using .format()
name = input("First name: ")
hobby = input("Favourite hobby: ")
print("Summary: {}'s favourite hobby is {}.".format(name, hobby))
```

---

## Tests

| Input | Expected | Result | ✓ |
|-------|----------|----------|---|
| `Max`, `Gaming` | `Summary: Max's favourite hobby is Gaming.` | `Summary: Max's favourite hobby is Gaming.` | ✅ |
| `Anna`, `Reading` | `Summary: Anna's favourite hobby is Reading.` | `Summary: Anna's favourite hobby is Reading.` | ✅ |

---

## Notes

- **Concept:** String concatenation using `+`
- **Important:** `+` does NOT automatically insert spaces
- **Apostrophe:** `'s` must be included manually in the string
- **Best practice:** Use lowercase for variable names (`name` instead of `Name`)
- **Tip:** f-strings are more readable than `+` concatenation

