# 🐍 Full Name Greeting (First Name and Surname)

**Course:** Cyber Security Analyst - Python Basics | **Date:** 17 June 2025

---

## Task

**Objective:** Read in the first name and surname and display a personalised greeting.

**Requirements:**
- Prompt 1: `Enter your first name: `
- Prompt 2: `Enter your last name: `
- Output: `Hello, [first_name] [last_name]!`
- Ensure there is a space between the first name and surname

---

## Solution

```python
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
greets = f"Hello, {first_name} {last_name}!"
print(greets)
```

**Alternative solutions:**
```python
# Using string concatenation
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print("Hello, " + first_name + " " + last_name + "!")

# Compact with f-strings
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print(f"Hello, {first_name} {last_name}!")

# Using .format()
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print("Hello, {} {}!".format(first_name, last_name))
```

---

## Tests

| First Name | Last Name | Expected | Result | ✓ |
|------------|-----------|----------|----------|---|
| `Max` | `Mustermann` | `Hello, Max Mustermann!` | `Hello, Max Mustermann!` | ✅ |
| `Anna` | `Schmidt` | `Hello, Anna Schmidt!` | `Hello, Anna Schmidt!` | ✅ |
| `John` | `Doe` | `Hello, John Doe!` | `Hello, John Doe!` | ✅ |

---

## Notes

- **Concept:** Combining multiple inputs with f-strings
- **Important:** Space in the f-string between `{first_name}` and `{last_name}`
- **Best practice:** Choose descriptive variable names (`first_name` instead of `fn`)
- **Tip:** f-strings also allow expressions: `f"{name.upper()}"`

