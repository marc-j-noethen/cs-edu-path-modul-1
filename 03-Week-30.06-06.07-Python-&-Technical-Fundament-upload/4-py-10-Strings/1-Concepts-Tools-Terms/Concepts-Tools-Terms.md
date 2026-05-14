## 📊 Summary Using the 80/20 Principle

## **PART 1: WHAT ARE STRINGS?**

### **1. Definition: String**

**String = Ordered sequence of characters**

```python
# Different ways to create strings
message1 = 'Hello World!'
message2 = "This is also a string."
number_as_string = "12345"
empty = ""
print(message1)  # Output: Hello World!
```

**Characters can be:**

- Letters: `a-z`, `A-Z`
- Numbers: `0-9`
- Symbols: `!`, `@`, `#`, `$`, etc.
- Whitespace: spaces, tabs, line breaks

---

### **2. Single vs. Double vs. Triple Quotes**

```python
# Single Quotes
text1 = 'Hello'
# Double Quotes
text2 = "Hello"
# Triple Quotes (multi-line)
text3 = """This is
a multi-line
string."""
print(text3)
# Output:
# This is
# a multi-line
# string.
```

**When to use which?**

- **Single/Double:** For short, single-line strings (interchangeable)
- **Triple:** For multi-line strings or docstrings

---

## **PART 2: INDEXING – ACCESSING INDIVIDUAL CHARACTERS**

### **3. Positive Index (from the front)**

```python
text = "Python"
#       012345  (indices)
print(text[0])  # Output: P
print(text[1])  # Output: y
print(text[2])  # Output: t
print(text[5])  # Output: n
```

## **⚠️ Important:** Python starts at 0, not 1!

### **4. Negative Index (from the back)**

```python
text = "Python"
#       -6-5-4-3-2-1  (negative indices)
print(text[-1])  # Output: n (last character)
print(text[-2])  # Output: o (second to last character)
print(text[-6])  # Output: P (first character)
```

## **Practical use:** Last character without knowing the length: `text[-1]`

### **5. Avoiding IndexError**

```python
text = "Hello"
# ❌ Error
# print(text[10])  # IndexError: string index out of range
# ✅ Safe access
if 10 < len(text):
    print(text[10])
else:
    print("Index does not exist")
```

---

## **PART 3: SLICING – EXTRACTING SUBSTRINGS**

### **6. Slicing Syntax: `[start:stop:step]`**

```python
text = "Cybersecurity"
#       0123456789...
# [start:stop] - from start to stop (exclusive)
print(text[0:5])    # Output: Cyber
print(text[5:13])   # Output: security
# [:stop] - from the beginning to stop
print(text[:5])     # Output: Cyber
# [start:] - from start to the end
print(text[5:])     # Output: security
# [:] - complete string
print(text[:])      # Output: Cybersecurity
```

## **Important:** `stop` is **exclusive** (not included)

### **7. Slicing with Step**

```python
text = "Python"
# Every second character
print(text[::2])    # Output: Pto
# Every third letter
print(text[::3])    # Output: Ph
# Reverse string (negative step!)
print(text[::-1])   # Output: nohtyP
```

## **Trick:** `[::-1]` reverses a string!

### **8. Practical Slicing Examples**

```python
email = "user@example.com"
# Everything before @
username = email[:email.find('@')]
print(username)  # Output: user
# Everything after @
domain = email[email.find('@')+1:]
print(domain)  # Output: example.com
# Last 4 characters
filename = "document.txt"
extension = filename[-4:]
print(extension)  # Output: .txt
```

---

## **PART 4: STRING OPERATIONS**

### **9. Concatenation with `+` and Repetition with `*`**

```python
# Concatenation
firstname = "Max"
lastname = "Mustermann"
fullname = firstname + " " + lastname
print(fullname)  # Output: Max Mustermann
# Repetition
divider = "-" * 20
print(divider)  # Output: --------------------
greeting = "Hello! " * 3
print(greeting)  # Output: Hello! Hello! Hello!
```

---

### **10. Length with `len()`**

```python
text = "Python"
length = len(text)
print(length)  # Output: 6
# Useful for validation
password = "secret123"
if len(password) >= 8:
    print("Password is long enough")
else:
    print("Password too short")
```

---

## **PART 5: IMPORTANT STRING METHODS**

### **11. Changing Case**

```python
text = "PyThOn PrOgRaMmInG"
print(text.upper())      # Output: PYTHON PROGRAMMING
print(text.lower())      # Output: python programming
print(text.capitalize()) # Output: Python programming
print(text.title())      # Output: Python Programming
```

**Usage:**

- `.upper()` / `.lower()` → Comparisons (case-insensitive)
- `.title()` → Format headings
- `.capitalize()` → Start of sentence

---

### **12. Finding Substrings with `.find()` and `.index()`**

```python
text = "The quick brown fox jumps."
# .find() - returns -1 if not found
position1 = text.find("fox")
print(position1)  # Output: 16
position2 = text.find("cat")
print(position2)  # Output: -1
# .index() - ValueError if not found
position3 = text.index("fox")
print(position3)  # Output: 16
# position4 = text.index("cat")  # ValueError!
```

**Difference:**

- `.find()` → Returns `-1` (safer)
- `.index()` → Throws ValueError (only when certain)

---

### **13. Replacing Substrings with `.replace()`**

```python
text = "I like cats."
new_text = text.replace("cats", "dogs")
print(new_text)  # Output: I like dogs.
# Original remains unchanged (strings are immutable!)
print(text)  # Output: I like cats.
# Multiple replacements
numbers = "1-2-3-4-5"
without_hyphens = numbers.replace("-", "")
print(without_hyphens)  # Output: 12345
```

## **Important:** Strings are **immutable** → Methods return new strings!

### **14. Splitting Strings with `.split()`**

```python
# Split at whitespace (default)
sentence = "This is a sentence"
words = sentence.split()
print(words)  # Output: ['This', 'is', 'a', 'sentence']
# Split at specific delimiter
csv_line = "Name,Age,City"
columns = csv_line.split(',')
print(columns)  # Output: ['Name', 'Age', 'City']
# Parsing a log file
log = "ERROR:2024-01-15:File not found"
parts = log.split(':')
print(parts)  # Output: ['ERROR', '2024-01-15', 'File not found']
level = parts[0]
date = parts[1]
message = parts[2]
```

## **Useful for:** Parsing CSV files, logs, paths

### **15. Removing Whitespace with `.strip()`**

```python
# .strip() - removes leading AND trailing whitespace
username = "  admin  \n"
clean = username.strip()
print(f"'{clean}'")  # Output: 'admin'
# .lstrip() - only leading whitespace (left)
text = "  Hello"
print(f"'{text.lstrip()}'")  # Output: 'Hello'
# .rstrip() - only trailing whitespace (right)
text2 = "Hello  "
print(f"'{text2.rstrip()}'")  # Output: 'Hello'
```

## **Usage:** Cleaning user input, sanitizing file lines

### **16. Checking String Contents**

```python
# .startswith() - starts with?
filename = "report.txt"
print(filename.startswith("report"))  # Output: True
print(filename.startswith("data"))    # Output: False
# .endswith() - ends with?
print(filename.endswith(".txt"))    # Output: True
print(filename.endswith(".pdf"))    # Output: False
# .isdigit() - only digits?
pin = "1234"
print(pin.isdigit())  # Output: True
pin2 = "12a4"
print(pin2.isdigit())  # Output: False
# .isalpha() - only letters?
name = "Alice"
print(name.isalpha())  # Output: True
name2 = "Alice123"
print(name2.isalpha())  # Output: False
# .isalnum() - letters OR numbers?
username = "User123"
print(username.isalnum())  # Output: True
```

## **Useful for:** Validating input

## **PART 6: STRING FORMATTING**

### **17. f-Strings (RECOMMENDED – from Python 3.6)**

```python
name = "Alice"
age = 30
# Embedding variables
print(f"User {name} is {age} years old.")
# Output: User Alice is 30 years old.
# Expressions in {}
print(f"In 5 years, {name} will be {age + 5} years old.")
# Output: In 5 years, Alice will be 35 years old.
# Formatting
price = 19.99
print(f"Price: {price:.2f} EUR")
# Output: Price: 19.99 EUR
# Multiple variables
city = "Berlin"
country = "Germany"
print(f"{name} lives in {city}, {country}.")
# Output: Alice lives in Berlin, Germany.
```

## **Advantages:** Readable, precise, modern

### **18. Older Formatting Methods (for reference)**

```python
name = "Bob"
age = 25
# .format() method
print("User {} is {} years old.".format(name, age))
# Output: User Bob is 25 years old.
# %-formatting (outdated, but found in old code)
print("User %s is %d years old." % (name, age))
# Output: User Bob is 25 years old.
```

## **Recommendation:** Use f-strings for new code!

## **PART 7: ESCAPE CHARACTERS**

### **19. Special Characters with Backslash `\`**

```python
# \n - line break
print("Line 1\nLine 2")
# Output:
# Line 1
# Line 2
# \t - tab
print("Name:\tAlice")
# Output: Name:    Alice
# \\ - backslash
print("Path: C:\\Users\\Admin")
# Output: Path: C:\Users\Admin
# \' - single quote
print('It\'s a nice day.')
# Output: It's a nice day.
# \" - double quote
print("He said \"Hello\".")
# Output: He said "Hello".
```

---

### **20. Correctly Representing Windows Paths**

```python
# ❌ Wrong (interpreted as escape sequences)
# path = "C:\Users\Admin"  # SyntaxError or wrong output
# ✅ Correct: Double backslashes
path1 = "C:\\Users\\Admin"
print(path1)  # Output: C:\Users\Admin
# ✅ Or: Raw string (r before string)
path2 = r"C:\Users\Admin"
print(path2)  # Output: C:\Users\Admin
```

## **Windows 11:** Always use `\\` or `r"..."` for paths!

## **PRACTICAL EXAMPLES**

### **21. Example 1: Email Validation**

```python
def is_email_valid(email):
    """Simple email validation."""
    # Clean up
    email = email.strip().lower()
    
    # Contains @?
    if '@' not in email:
        return False
    
    # At least one dot after @?
    at_position = email.find('@')
    after_at = email[at_position+1:]
    if '.' not in after_at:
        return False
    
    return True
print(is_email_valid("user@example.com"))   # True
print(is_email_valid("invalid-email"))      # False
print(is_email_valid("  TEST@SITE.DE  "))  # True
```

---

### **22. Example 2: Checking Password Strength**

```python
def check_password(password):
    """Checks password strength."""
    if len(password) < 8:
        return "Too short (min. 8 characters)"
    
    has_digit = any(char.isdigit() for char in password)
    has_letter = any(char.isalpha() for char in password)
    
    if not has_digit:
        return "No digit included"
    
    if not has_letter:
        return "No letter included"
    
    return "Strong"
print(check_password("secret"))      # Too short
print(check_password("abcdefgh"))    # No digit
print(check_password("12345678"))    # No letter
print(check_password("secret123"))   # Strong
```

---

### **23. Example 3: Parsing a Log File**

```python
log_lines = [
    "2024-01-15 10:30:00 INFO User logged in",
    "2024-01-15 10:35:12 ERROR File not found",
    "2024-01-15 10:40:55 WARNING Memory almost full"
]
for line in log_lines:
    parts = line.split(' ', 3)  # Max. 4 parts
    date = parts[0]
    time = parts[1]
    level = parts[2]
    message = parts[3]
    
    print(f"[{level}] {date} {time}: {message}")
# Output:
# [INFO] 2024-01-15 10:30:00: User logged in
# [ERROR] 2024-01-15 10:35:12: File not found
# [WARNING] 2024-01-15 10:40:55: Memory almost full
```

---

## **QUICK REFERENCE**

### **String Cheatsheet:**

```python
# Create
s = "Hello"
s = 'Hello'
s = """Multi-line"""
# Access
s[0]        # First character
s[-1]       # Last character
s[1:4]      # Slice from index 1 to 3
s[::-1]     # Reverse string
# Operations
s1 + s2     # Concatenate
s * 3       # Repeat
len(s)      # Length
# Important methods
s.upper()              # UPPERCASE
s.lower()              # lowercase
s.strip()              # Remove whitespace
s.split(',')           # Split at ','
s.replace('old', 'new') # Replace
s.find('sub')          # Find substring
s.startswith('pre')    # Starts with?
s.endswith('suf')      # Ends with?
s.isdigit()            # Only digits?
# Formatting
f"{var}"               # f-string (recommended)
# Escape characters
\n  # Line break
\t  # Tab
\\  # Backslash
```

---

## **COMMON ERRORS AND SOLUTIONS**

### **24. Error 1: Strings are immutable**

```python
# ❌ Does not work
text = "Hello"
# text[0] = "h"  # TypeError: 'str' object does not support item assignment
# ✅ Solution: Create a new string
text = "h" + text[1:]
print(text)  # Output: hello
```

---

### **25. Error 2: IndexError with Slicing**

```python
text = "Python"
# ❌ IndexError
# print(text[10])  # IndexError
# ✅ Slicing does not throw an error
print(text[10:20])  # Output: '' (empty string)
```

---

### **26. Error 3: Confusing `.find()` and `.index()`**

```python
text = "Hello World"
# .find() - safe
pos1 = text.find("xyz")
print(pos1)  # Output: -1
# .index() - can crash
# pos2 = text.index("xyz")  # ValueError!
# ✅ Better: Check first
if "xyz" in text:
    pos = text.index("xyz")
else:
    print("Not found")
```

---

## **PRACTICE TASKS**

## **Task 1:** Write a function that reverses a string (without `[::-1]`). **Task 2:** Count how many times a specific letter appears in a string. **Task 3:** Extract the username and domain from an email address. **Task 4:** Format a phone number: `"1234567890"` → `"(123) 456-7890"`

### **Key Takeaways:**

## 🎯 **String = immutable! Methods return new strings**  
🎯 **Indexing: `[0]` = first, `[-1]` = last character**  
🎯 **Slicing: `[start:stop:step]`, stop is exclusive!**  
🎯 **`[::-1]` reverses a string (negative step)**  
🎯 **f-strings = best formatting: `f"{variable}"`**  
🎯 **`.strip()` = remove whitespace (very common with input!)**  
🎯 **`.split()` = split string into list (parsing!)**  
🎯 **Windows paths: `"C:\\Users"` or `r"C:\Users"`**

## Tools Used

|Category|Term|Meaning|
|---|---|---|
|**Tools Used**|Python Interpreter|For interactively testing string operations|
||VS Code|Editor for writing Python scripts with strings|
||`print()` Function|Output of strings and string operations|
||`len()` Function|Returns the length (number of characters) of a string|
||f-Strings|Modern method for string formatting (from Python 3.6)|

---

## Technical Terms

|Category|Term|Meaning|
|---|---|---|
|**Technical Terms**|String|Ordered sequence of characters|
||Character|Single element of a string (letter, number, symbol, space)|
||Index (Indexing)|Position of a character in the string (starts at 0)|
||Zero-based Indexing|First character has index 0, not 1|
||Negative Indexing|Access from the back: `-1` = last character|
||Slicing|Extracting a substring from a string|
||Substring|Part of a string|
||Concatenation|Joining strings with `+`|
||Repetition|Multiplying a string with `*`|
||Method|Function that belongs to a string object (called with `.`)|
||Immutable|Strings cannot be changed; methods return new strings|
||Delimiter|Character for splitting strings (e.g. with `.split()`)|
||Whitespace|Spaces, tabs, line breaks|
||Escape Character|Backslash `\` for special characters (e.g. `\n`, `\t`)|
||String Formatting|Embedding variables into strings|
||String Literal|String value directly in code (e.g. `"Hello"`)|
||Multi-line String|String spanning multiple lines (with `"""` or `'''`)|
||IndexError|Error when accessing a non-existent index|
||ValueError|Error with `.index()` when substring is not found|
|**Important Vocabulary**|`'...'` Single Quotes|Single quotation marks for strings|
||`"..."` Double Quotes|Double quotation marks for strings|
||`"""..."""` Triple Quotes|Triple quotation marks for multi-line strings|
||`[index]`|Access character at position|
||`[start:stop:step]`|Slicing syntax for extracting substrings|
||`+` Operator|Concatenation of strings|
||`*` Operator|Repetition of strings|
||`.upper()`|Converts to uppercase|
||`.lower()`|Converts to lowercase|
||`.capitalize()`|First letter uppercase|
||`.title()`|First letter of each word uppercase|
||`.find(substring)`|Returns index of first occurrence (-1 if not found)|
||`.index(substring)`|Like `.find()`, but ValueError if not found|
||`.replace(old, new)`|Replaces substring with another|
||`.split(delimiter)`|Splits string into a list|
||`.strip()`|Removes leading/trailing whitespace|
||`.lstrip()`|Removes leading whitespace (left)|
||`.rstrip()`|Removes trailing whitespace (right)|
||`.startswith(prefix)`|Checks if string starts with prefix|
||`.endswith(suffix)`|Checks if string ends with suffix|
||`.isdigit()`|Checks if all characters are digits|
||`.isalpha()`|Checks if all characters are letters|
||`.isalnum()`|Checks if all characters are alphanumeric|
||`f"..."`|f-string for formatting with variables in `{}`|
||`.format()`|Older formatting method|
||`\n`|Escape character for line break|
||`\t`|Escape character for tab|
||`\\`|Escape character for backslash|
||`\'`|Escape character for single quote|
||`\"`|Escape character for double quote|