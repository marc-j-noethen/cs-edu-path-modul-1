# Python Lesson 11: Modules

## Summary Using the 80/20 Principle

---

## **PART 1: WHAT ARE MODULES?**

### **1. Concept: Modules as Building Blocks**

**Metaphor: Building a house**

- Without modules: Build everything from scratch
- With modules: Use prefabricated parts (doors, windows, walls) **Python module:**
- Module = Python file (`.py`) with reusable code
- Contains: Functions, classes, variables
- Purpose: Organize and reuse code

```python
# Example: math_utils.py (a custom module)
def add(a, b):
    return a + b
def multiply(a, b):
    return a * b
PI = 3.14159
```

---

### **2. Why Use Modules? (5 Reasons)**

**1. Organization**

```python
# Instead of 1000 lines in one file:
# main.py (50 lines)
# database.py (200 lines)
# network.py (150 lines)
# ui.py (300 lines)
```

**2. Reusability (DRY)**

```python
# Write once
# math_utils.py
def calculate_area(radius):
    return 3.14 * radius ** 2
# Use in many projects
import math_utils
area = math_utils.calculate_area(5)
```

**3. Collaboration**

- Person A works on `database.py`
- Person B works on `ui.py`
- No conflicts! **4. Namespace Management (avoiding name conflicts)**

```python
# module_a.py
def calculate():
    return 10
# module_b.py
def calculate():
    return 20
# main.py
import module_a
import module_b
print(module_a.calculate())  # 10
print(module_b.calculate())  # 20
# No conflict!
```

**5. Using existing code**

- Python Standard Library: 200+ modules already available
- No need to reinvent the wheel!

---

## **PART 2: IMPORTING MODULES**

### **3. Method 1: `import module_name`**

**Syntax:**

```python
import module_name
```

**Usage with Dot Notation:**

```python
module_name.function()
module_name.variable
```

**Practical Example: `math` module**

```python
import math
# Calculate square root
number = 16
root = math.sqrt(number)
print(f"Square root of {number} = {root}")  # Output: Square root of 16 = 4.0
# Use Pi
radius = 5
area = math.pi * (radius ** 2)
print(f"Circle area: {area}")  # Output: Circle area: 78.53981633974483
# More useful functions
print(math.ceil(4.3))   # Output: 5 (round up)
print(math.floor(4.7))  # Output: 4 (round down)
print(math.pow(2, 3))   # Output: 8.0 (2^3)
```

**Advantages:**

- ✅ Clearly recognizable where functions come from
- ✅ No name conflicts
- ✅ Good readability

---

### **4. Method 2: `from module_name import item`**

**Syntax:**

```python
from module_name import function1, function2
```

**Usage directly without module name:**

```python
function1()  # Without "module_name." prefix
```

**Practical Example: `random` module**

```python
from random import randint, choice
# Direct use without "random." prefix
random_number = randint(1, 10)
print(f"Random number: {random_number}")
selection = choice(['Apple', 'Banana', 'Cherry'])
print(f"Random fruit: {selection}")
# ❌ Other functions from random are not available
# uniform(1, 10)  # NameError! Not imported
```

**Advantages:**

- ✅ Shorter code (no module name needed)
- ✅ Good for frequently used functions **Disadvantages:**
- ❌ Unclear where the function comes from
- ❌ Potential name conflicts

---

### **5. ⚠️ Method 3: `from module_name import *` (NOT RECOMMENDED!)**

**Syntax:**

```python
from math import *
```

**What happens:** All functions and variables from `math` are imported

```python
from math import *
# All functions directly usable
print(sqrt(16))  # 4.0
print(pi)        # 3.141592653589793
print(sin(0))    # 0.0
```

**⚠️ Why NOT recommended?**

```python
# Own variable
pi = 3.14
# Import overwrites own variable!
from math import *
print(pi)  # 3.141592653589793 (no longer 3.14!)
```

**Problems:**

- ❌ Namespace pollution
- ❌ Unclear origin of functions
- ❌ Accidentally overwrites own variables
- ❌ Hard to debug **Rule:** Never use `import *` in production code!

---

## **PART 3: PYTHON STANDARD LIBRARY**

### **6. The Most Important Standard Modules**

## **Python = "Batteries Included"** → Many useful modules already built in, no installation needed!

### **7. Module 1: `math` – Mathematical Functions**

```python
import math
# Basic functions
print(math.sqrt(25))        # 5.0 (square root)
print(math.pow(2, 3))       # 8.0 (power)
print(math.factorial(5))    # 120 (factorial: 5!)
# Rounding
print(math.ceil(4.3))       # 5 (round up)
print(math.floor(4.7))      # 4 (round down)
# Trigonometry
print(math.sin(math.pi/2))  # 1.0
print(math.cos(0))          # 1.0
# Constants
print(math.pi)              # 3.141592653589793
print(math.e)               # 2.718281828459045
```

## **Usage:** Scientific calculations, geometry, statistics

### **8. Module 2: `random` – Random Numbers**

```python
import random
# Random integer
roll = random.randint(1, 6)
print(f"Dice: {roll}")
# Random element from list
colors = ['red', 'green', 'blue', 'yellow']
color = random.choice(colors)
print(f"Random color: {color}")
# Random float
rand = random.random()  # 0.0 to 1.0
print(f"Random number: {rand}")
# Shuffle list
cards = ['Ace', 'King', 'Queen', 'Jack']
random.shuffle(cards)
print(f"Shuffled: {cards}")
# Multiple random elements
winners = random.sample(colors, 2)
print(f"2 Winners: {winners}")
```

## **Usage:** Games, simulations, sampling, tests

### **9. Module 3: `datetime` – Date and Time**

```python
import datetime
# Current date and time
now = datetime.datetime.now()
print(f"Now: {now}")
# Output: 2024-01-15 14:30:45.123456
# Date only
today = datetime.date.today()
print(f"Today: {today}")
# Output: 2024-01-15
# Formatted output
formatted = now.strftime("%d.%m.%Y %H:%M:%S")
print(f"Formatted: {formatted}")
# Output: 15.01.2024 14:30:45
# Create specific date
birthday = datetime.date(1990, 5, 15)
print(f"Birthday: {birthday}")
# Calculate time difference
age_days = (today - birthday).days
age_years = age_days // 365
print(f"Age: approx. {age_years} years")
```

## **Usage:** Timestamps, logs, scheduling, age calculation

### **10. Module 4: `os` – Operating System Interaction**

```python
import os
# Current working directory
directory = os.getcwd()
print(f"Current directory: {directory}")
# Windows: C:\Users\Username\Documents
# List files in directory
files = os.listdir('.')
print(f"Files: {files}")
# Check if file exists
if os.path.exists('test.txt'):
    print("File exists")
else:
    print("File does not exist")
# Create directory
# os.mkdir('new_folder')
# Build path (platform-independent!)
path = os.path.join('folder', 'file.txt')
print(f"Path: {path}")
# Windows: folder\file.txt
# Linux/Mac: folder/file.txt
```

## **Usage:** File/folder management, paths, environment variables

### **11. Module 5: `sys` – System Parameters**

```python
import sys
# Python version
print(f"Python version: {sys.version}")
# Platform (operating system)
print(f"Platform: {sys.platform}")
# Windows: 'win32'
# Linux: 'linux'
# Mac: 'darwin'
# Command line arguments
# When script is called: python script.py arg1 arg2
print(f"Arguments: {sys.argv}")
# Exit script
# sys.exit(0)
```

## **Usage:** System information, command line tools

### **12. Other Important Modules (Quick Overview)**

|Module|Purpose|Example|
|---|---|---|
|`json`|Process JSON data|`json.loads('{"name": "Alice"}')`|
|`re`|Regular Expressions|`re.search(r'\d+', 'abc123')`|
|`time`|Time functions|`time.sleep(1)` (wait 1 second)|
|`csv`|Read/write CSV files|`csv.reader(file)`|
|`pathlib`|Modern path management|`Path('file.txt').exists()`|
|**Full list:** https://docs.python.org/3/library/|||

---

## **PART 4: PRACTICAL EXAMPLES**

### **13. Example 1: Dice Game**

```python
import random
def roll_dice():
    """Rolls a 6-sided die."""
    return random.randint(1, 6)
# Game
print("Dice Game!")
player1 = roll_dice()
player2 = roll_dice()
print(f"Player 1: {player1}")
print(f"Player 2: {player2}")
if player1 > player2:
    print("Player 1 wins!")
elif player2 > player1:
    print("Player 2 wins!")
else:
    print("It's a tie!")
```

---

### **14. Example 2: Circle Calculation**

```python
import math
def calculate_circle(radius):
    """Calculates circumference and area of a circle."""
    circumference = 2 * math.pi * radius
    area = math.pi * radius ** 2
    return circumference, area
# Usage
r = 5
c, a = calculate_circle(r)
print(f"Radius: {r}")
print(f"Circumference: {c:.2f}")
print(f"Area: {a:.2f}")
# Output:
# Radius: 5
# Circumference: 31.42
# Area: 78.54
```

---

### **15. Example 3: Date Log**

```python
import datetime
def log_entry(message):
    """Creates a log entry with timestamp."""
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    return f"[{timestamp}] {message}"
# Usage
print(log_entry("Program started"))
print(log_entry("User logged in"))
print(log_entry("File saved"))
# Output:
# [2024-01-15 14:30:00] Program started
# [2024-01-15 14:30:01] User logged in
# [2024-01-15 14:30:02] File saved
```

---

## **QUICK REFERENCE**

### **Import Cheatsheet:**

```python
# Import entire module
import math
result = math.sqrt(16)
# Import specific elements
from random import randint, choice
number = randint(1, 10)
# Module with alias
import datetime as dt
now = dt.datetime.now()
# Multiple modules
import math, random, os
```

### **Important Standard Modules:**

```python
import math      # Mathematics
import random    # Random numbers
import datetime  # Date/time
import os        # Operating system
import sys       # System parameters
import json      # JSON data
import time      # Time functions
```

---

## **COMMON ERRORS AND SOLUTIONS**

### **16. Error 1: ModuleNotFoundError**

```python
# ❌ Problem
import non_existent_module
# ModuleNotFoundError: No module named 'non_existent_module'
```

**Causes:**

- Module not installed (for third-party)
- Typo in module name
- Wrong Python environment **✅ Solution:**

```python
# Check spelling
import math  # ✅ Correct (lowercase)
# For third-party: installation required
# pip install numpy (in terminal)
```

---

### **17. Error 2: Own Module Shadows Standard Module**

```python
# ❌ Problem: File is named "random.py"
# Attempt to import:
import random
# Imports own file instead of standard module!
```

## **✅ Solution:** Do NOT name your own files like standard modules

### **18. Error 3: Forgetting Dot Notation**

```python
import math
# ❌ Wrong
# print(sqrt(16))  # NameError: name 'sqrt' is not defined
# ✅ Correct
print(math.sqrt(16))  # 4.0
```

---

## **COMPARISON: IMPORT METHODS**

### **19. Which method when?**

|Method|When to use|Example|
|---|---|---|
|`import module`|Standard, always good|`import math`|
|`from module import item`|1-3 specific items|`from math import sqrt, pi`|
|`from module import *`|**NEVER!**|❌|
|`import module as alias`|Long module names|`import datetime as dt`|

---

## **CREATING YOUR OWN MODULES (PREVIEW)**

### **20. Simple custom module**

**File: `my_module.py`**

```python
def greeting(name):
    """Greets a person."""
    return f"Hello, {name}!"
def add(a, b):
    """Adds two numbers."""
    return a + b
PI = 3.14159
```

**File: `main.py`**

```python
import my_module
message = my_module.greeting("Alice")
print(message)  # Output: Hello, Alice!
total = my_module.add(5, 3)
print(total)  # Output: 8
print(my_module.PI)  # Output: 3.14159
```

---

## **PRACTICE TASKS**

## **Task 1:** Write a program using `random` that generates and prints 10 random numbers between 1 and 100. **Task 2:** Use `datetime` to calculate how many days are left until your next birthday. **Task 3:** Create a function using `math` that calculates the distance between two points (x1,y1) and (x2,y2). **Task 4:** Use `os` to list all `.txt` files in the current directory.

### **Key Takeaways:**

## 🎯 **Module = Python file with reusable code**  
🎯 **`import module` → Access with `module.function()`**  
🎯 **`from module import item` → Direct access to `item()`**  
🎯 **`from module import *` → NEVER use!**  
🎯 **Standard Library = 200+ modules, no installation needed**  
🎯 **Most important modules: `math`, `random`, `datetime`, `os`, `sys`**  
🎯 **Modules = DRY principle: write code once, use multiple times**

## Tools Used

|Category|Term|Meaning|
|---|---|---|
|**Tools Used**|Python Interpreter|For testing module imports|
||VS Code|Editor for writing Python scripts with modules|
||`.py` files|Python files that can act as modules|
||Standard Library|Built-in collection of Python modules|
||Third-party Modules|External modules from the community (not covered in this document)|

---

## Technical Terms

|Category|Term|Meaning|
|---|---|---|
|**Technical Terms**|Module|Python file with reusable code (functions, classes, variables)|
||Import|Including a module in the current code|
||`import` Statement|Command for importing a module|
||Dot Notation|Accessing module contents: `module.function()`|
||Namespace|Scope in which names (variables, functions) are defined|
||Namespace Management|Avoiding name conflicts through modules|
||Standard Library|Collection of built-in Python modules for common tasks|
||DRY Principle|"Don't Repeat Yourself" - reusability of code|
||Pre-fabricated Parts|Metaphor: modules as ready-made building blocks|
||Naming Conflict|Two functions/variables with the same name|
||Pollute Namespace|Overcrowding the namespace with many names (with `from ... import *`)|
||Reusability|Write code once, use it multiple times|
||Organization|Splitting code into logical modules|
||Collaboration|Multiple developers working on different modules|
|**Important Vocabulary**|`import module_name`|Imports entire module|
||`from module_name import item`|Imports specific element from module|
||`from module_name import *`|Imports everything from module (NOT recommended!)|
||`module_name.item_name`|Access to element in module (Dot Notation)|
||`math` Module|Standard module for mathematical functions|
||`random` Module|Standard module for random numbers|
||`os` Module|Standard module for operating system operations|
||`sys` Module|Standard module for system-specific parameters|
||`datetime` Module|Standard module for date and time|
||`json` Module|Standard module for JSON data|
||`re` Module|Standard module for Regular Expressions|
||`.sqrt()`|Square root function from `math`|
||`.pi`|Pi constant from `math`|
||`.randint()`|Random integer from `random`|
||`.now()`|Current time from `datetime`|
||`.strftime()`|Format time from `datetime`|
||File Extension `.py`|Python file extension|