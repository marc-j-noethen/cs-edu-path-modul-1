# 🐍 Name Greeting - Formatting a greeting

**Course:** Cyber Security Analyst - Python Basics | **Date:** 3 July 2025

---

## Task

**Objective:** Read in a first name and surname, clean and format them, then output a greeting.

**Requirements:**
- Input: First name + Surname (with prompts)
- Processing: `.strip()` + `.title()`
- Output: `"Hello, [First name] [Surname]!"`

---

## Solution

```python
# Read in names
first_name = input("Enter first name: ")
last_name = input("Enter last name: ")

# Clean up and format
first_name = first_name.strip().title()
last_name = last_name.strip().title()

# Output
print(f"Hello, {first_name} {last_name}!")
```

**One-liner alternative:**
```python
print(f"Hello, {input('Enter first name: ').strip().title()} {input('Enter last name: ').strip().title()}!")
```

---

## Tests

| Input | Output | ✓ |
|-------|--------|---|
| `alice   ` / `sMitH` | `Hello, Alice Smith!` | ✅ |
| `bOB` / ` jones` | `Hello, Bob Jones!` | ✅ |
| `  JANE  ` / `DOE` | `Hello, Jane Doe!` | ✅ |

---

## Notes

- **`.strip()`:** Removes leading/trailing spaces
- **`.title()`:** Capitalises the first letter, lowercase the rest → `"jOHN"` → `"John"`
- **f-string:** `f"Text {variable}"` for formatted output

