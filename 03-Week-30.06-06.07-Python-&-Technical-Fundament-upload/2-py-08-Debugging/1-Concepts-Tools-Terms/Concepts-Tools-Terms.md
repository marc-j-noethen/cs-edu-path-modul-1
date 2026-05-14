## 📊 Summary Using the 80/20 Principle

---

### PART 1: WHAT ARE BUGS?

### **1. Definition: Bug**

**Bug = Error in code that leads to wrong or unexpected behavior**

```python
# Example: This code is supposed to print "Hello"
print("Helo")  # Typo = Bug!
```

**Debugging = Process of finding and fixing bugs**

**Historical Fact:** The term "bug" comes from real insects that used to crawl into computer hardware and cause errors! 🐛

---

## PART 2: THE 3 TYPES OF ERRORS

### **2. Syntax Errors – Code doesn't run at all**

**Definition:** Grammatical errors – Python cannot understand the code

**Most common causes:**

- Forgotten colon `:`
- Misspelled keywords
- Missing/wrong parentheses
- Missing indentation

**Examples:**

```python
# ❌ Error 1: Forgotten colon
if x > 5
    print("Large")
# SyntaxError: invalid syntax

# ✅ Correct:
if x > 5:
    print("Large")

# ❌ Error 2: Misspelled keyword
whlie count < 10:  # "whlie" instead of "while"
    print(count)
# SyntaxError: invalid syntax

# ✅ Correct:
while count < 10:
    print(count)

# ❌ Error 3: Mismatched parentheses
print("Hello"
# SyntaxError: unexpected EOF while parsing

# ✅ Correct:
print("Hello")
```

**Detection:** Python immediately shows an error message with the line number

---

### **3. Runtime Errors – Code crashes during execution**

**Definition:** Code starts, but something goes wrong during execution

**Most common causes:**

- Division by zero
- Accessing a non-existent list index
- Using an undefined variable
- Wrong data type

**Examples:**

```python
# ❌ Error 1: Division by zero
x = 10
y = 0
print(x / y)
# ZeroDivisionError: division by zero

# ✅ Solution: Check before dividing
if y != 0:
    print(x / y)
else:
    print("Division by zero not possible")

# ❌ Error 2: IndexError
list = [1, 2, 3]
print(list[5])
# IndexError: list index out of range

# ✅ Solution: Check index
if 5 < len(list):
    print(list[5])
else:
    print("Index does not exist")

# ❌ Error 3: NameError (undefined variable)
print(result)
# NameError: name 'result' is not defined

# ✅ Solution: Define variable first
result = 42
print(result)
```

**Detection:** Python shows a **Traceback** (error log) with:

- Error type (e.g. `IndexError`, `ZeroDivisionError`)
- Line number
- Error description

---

### **4. Logic Errors – Code runs, result is wrong**

**Definition:** No crash, but program doesn't do what it's supposed to

**Most common causes:**

- Wrong mathematical formula
- Wrong condition in `if`-statement
- Wrong operator (`>` instead of `>=`)
- Wrong initial value

**Examples:**

```python
# ❌ Error: Average calculated incorrectly
numbers = [10, 20, 30]
average = sum(numbers) / 2  # Should divide by 3!
print(average)  # Output: 30.0 (WRONG! Should be 20.0)

# ✅ Correct:
average = sum(numbers) / len(numbers)
print(average)  # Output: 20.0

# ❌ Error: Wrong condition
age = 18
if age > 18:  # Should be >=!
    print("Adult")
# Prints nothing, even though person is an adult at 18

# ✅ Correct:
if age >= 18:
    print("Adult")

# ❌ Error: Loop never runs
count = 0
while count > 5:  # Should be <!
    print(count)
    count += 1
# Prints nothing, because 0 is not > 5

# ✅ Correct:
count = 0
while count < 5:
    print(count)
    count += 1
```

**Detection:** The hardest! No error message, only wrong result

---

### PART 3: THE DEBUGGING PROCESS (4 STEPS)

### **5. Systematic Debugging**

**Step 1: Understand the problem**

- How do I reproduce the error?
- What is the **expected** output?
- What is the **actual** output?

**Step 2: Find the source of the error (isolate)**

- Where in the code does the error occur?
- Which variable has the wrong value?
- Which section of code is affected?

**Step 3: Fix the error**

- Correct the code

**Step 4: Test the fix**

- Run the code again
- Test edge cases
- Rule out new bugs

---

### PART 4: DEBUGGING WITH `print()` STATEMENTS

### **6. The simplest debugging method**

**Principle:** Insert `print()` at various places to:

- Check variable values
- Trace the execution flow
- Find out which part of the code is running

**Practical Example:**

```python
# ❌ Buggy Code: Sum is wrong
numbers = [1, 2, 3, 4, 5]
sum = 10  # Error: Should be 0!

for number in numbers:
    sum = sum + number

print(f"Final sum: {sum}")
# Output: Final sum: 25 (WRONG! Should be 15)

# ✅ Debugging with print()
numbers = [1, 2, 3, 4, 5]
sum = 10

print(f"Starting value sum: {sum}")  # Debug-Print

for number in numbers:
    print(f"Current number: {number}")  # Debug-Print
    sum = sum + number
    print(f"Sum after addition: {sum}")  # Debug-Print

print(f"Final sum: {sum}")

# Output:
# Starting value sum: 10  ← Here is the problem!
# Current number: 1
# Sum after addition: 11
# Current number: 2
# Sum after addition: 13
# ...
```

**After finding the error:** Remove or comment out `print()` statements

---

### **7. Using `print()` strategically**

```python
def calculate_discount(price, percent):
    """Calculates reduced price after discount."""
    print(f"DEBUG: Input price={price}, percent={percent}")  # Check input
    
    discount = price * percent
    print(f"DEBUG: Discount amount={discount}")  # Check intermediate value
    
    new_price = price - discount
    print(f"DEBUG: New price={new_price}")  # Check output
    
    return new_price

result = calculate_discount(100, 0.2)
print(f"Final price: {result}")
```

**Advantages:** ✅ Simple and fast ✅ Works everywhere ✅ No additional tools needed

**Disadvantages:** ❌ Must be inserted/removed manually ❌ Can make code messy ❌ Not ideal for large programs

---

### PART 5: VS CODE DEBUGGER (PROFESSIONAL DEBUGGING)

### **8. What is an IDE Debugger?**

**Debugger = Professional tool for stepping through code line by line**

**Advantages over `print()`:**

- ✅ Step through code line by line
- ✅ See all variables live
- ✅ No need to change the code
- ✅ Step through functions
- ✅ Pause and resume execution

---

### **9. Setting Breakpoints (Windows 11)**

**What is a Breakpoint?** A marker in the code where execution **pauses**

**How to set (VS Code):**

1. Open Python file in VS Code
2. Click to the left of the line number in the **Gutter** (gray area)
3. **Red dot** appears = Breakpoint set
4. Click again = Remove breakpoint

```python
def add(a, b):
    result = a + b      # ← Set breakpoint here (red dot)
    return result

x = 5
y = 10
sum = add(x, y)   # ← Set second breakpoint here
print(f"Sum: {sum}")
```

---

### **10. Starting the Debugger (Windows 11)**

**Step-by-step:**

1. **Open file:** Python file in VS Code
2. **Set breakpoint:** Place red dot next to line
3. **Open Run and Debug:**
    - Left sidebar → Icon with Play button + Bug icon
    - Or: `Ctrl + Shift + D`
4. **Start debugging:**
    - Click "Run and Debug" button
    - Choose configuration: "Python File"
5. **Program pauses** at first breakpoint

---

### **11. Debug Controls: The 4 Main Functions**

**Control elements (at the top of the debug window):**

|Symbol|Name|Keyboard Shortcut|Function|
|---|---|---|---|
|▶️|**Continue**|`F5`|Runs until the next breakpoint|
|⤵️|**Step Over**|`F10`|Executes next line (does NOT enter functions)|
|⬇️|**Step Into**|`F11`|Steps INTO a function|
|⬆️|**Step Out**|`Shift + F11`|Jumps OUT of current function|
|⏹️|**Stop**|`Shift + F5`|Stops debugging|

**Practical Example:**

```python
def multiply(a, b):
    result = a * b
    return result

x = 5
y = 3
result = multiply(x, y)  # ← Breakpoint here
print(result)
```

**Debugging workflow:**

1. Program pauses at `result = multiply(x, y)`
2. **Step Into (F11):** Jumps into `multiply()` function
3. **Step Over (F10):** Executes `result = a * b`
4. **Step Over (F10):** Executes `return result`
5. **Step Out (Shift+F11):** Jumps back to `print(result)`
6. **Continue (F5):** Runs to end (or next breakpoint)

---

### **12. Variables Panel – Observing variables live**

**Where to find (Windows 11):**

- Left sidebar during debugging
- Section "VARIABLES"

**What is visible:**

- **Locals:** Local variables (in current function)
- **Globals:** Global variables

**Practical Example:**

```python
def calculate(a, b):
    sum = a + b      # ← Breakpoint here
    product = a * b
    return sum, product

x = 10
y = 5
result = calculate(x, y)
```

**Variables Panel shows during pause:**

```
Locals:
  a = 10
  b = 5
  sum = 15
  product = (not yet calculated)

Globals:
  x = 10
  y = 5
  result = (not yet assigned)
```

---

### **13. Call Stack – Function call order**

**What is the Call Stack?** Shows the order of function calls up to the current position

**Example:**

```python
def function_a():
    function_b()

def function_b():
    function_c()

def function_c():
    x = 5 + 3  # ← Breakpoint here

function_a()
```

**Call Stack shows:**

```
function_c (current position)
  ↑ called by
function_b
  ↑ called by
function_a
  ↑ called by
<module> (main program)
```

---

### PART 6: DEBUGGER VS. PRINT() – WHEN TO USE WHICH?

### **14. Decision Guide**

|Situation|Method|Reason|
|---|---|---|
|Quick check|`print()`|Simple and fast|
|Small scripts|`print()`|No setup needed|
|Complex logic|Debugger|Step-by-step walkthrough|
|Checking many variables|Debugger|See all at once|
|Stepping through functions|Debugger|Step Into/Out|
|Production code|Debugger|No code changes needed|

---

## **QUICK REFERENCE**

### **Debugging Workflow:**

```
1. Identify the error
   ↓
2. Determine error type (Syntax/Runtime/Logic)
   ↓
3. Choose debugging method:
   - Simple: print()
   - Complex: Debugger
   ↓
4. Isolate the source of the error
   ↓
5. Correct the code
   ↓
6. Test (including edge cases!)
```

### **VS Code Debugger Cheatsheet (Windows 11):**

```
Set breakpoint:         Click to the left of line number
Start debugging:        Ctrl + Shift + D → "Run and Debug"
Continue:               F5
Step Over:              F10
Step Into:              F11
Step Out:               Shift + F11
Stop Debugging:         Shift + F5
```

---

## **COMMON ERRORS AND DEBUGGING STRATEGIES**

### **15. Common Error 1: Infinite Loop**

```python
# ❌ Problem
count = 0
while count < 10:
    print(count)
    # count is never incremented → Infinite loop!
```

**Debugging Strategy:**

1. Set breakpoint inside the loop
2. Check Variables Panel: Does `count` change?
3. If not: `count += 1` is missing

---

### **16. Common Error 2: Wrong Condition**

```python
# ❌ Problem
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    if number > 3:  # Should be >=
        print(number)
# Output: 4, 5 (WRONG! Should be 3, 4, 5)
```

**Debugging Strategy:**

1. Breakpoint in `if`-block
2. Variables Panel: Check value of `number`
3. Test condition manually: `3 > 3` = `False` → Error found!

---

### **17. Common Error 3: Off-by-One Error**

```python
# ❌ Problem
numbers = [10, 20, 30, 40, 50]
for i in range(len(numbers)):
    print(numbers[i+1])  # IndexError on last element!
```

**Debugging Strategy:**

1. Breakpoint inside the loop
2. Variables Panel: Watch `i` and `len(numbers)`
3. When `i = 4`: `numbers[5]` → IndexError!

---

## **PRACTICE TASKS**

**Task 1:** Find the error (logic error):

```python
def is_even(number):
    if number % 2 == 1:  # What is wrong here?
        return True
    else:
        return False
```

**Task 2:** Debug with `print()`:

```python
numbers = [1, 2, 3, 4, 5]
product = 0
for number in numbers:
    product = product * number
# Why is product always 0?
```

**Task 3:** Set breakpoints and step through:

```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))
# Step through with Step Into and observe the Call Stack
```

---

### **Key Takeaways:**

🎯 **3 Error types: Syntax (doesn't run), Runtime (crashes), Logic (wrong output)**  
🎯 **`print()` = quick & simple, Debugger = professional & powerful**  
🎯 **Breakpoint = red dot, code pauses here**  
🎯 **F10 = Step Over (next line), F11 = Step Into (into function)**  
🎯 **Variables Panel shows ALL values during pause**  
🎯 **Debugging is systematic: Understand → Isolate → Fix → Test**

---

## Categorization of Topics

|Category|Term|Meaning|
|---|---|---|
|**Tools Used**|Visual Studio Code (VS Code)|IDE with built-in debugger for Python|
||Python Extension|VS Code extension for Python debugging features|
||`print()` Function|Simplest debugging method for outputting values|
||Debugger (IDE Debugger)|Integrated tool for stepping through code line by line|
||Breakpoint|Marker at which code execution pauses|
||Run and Debug View|Area in VS Code for debugging functions (sidebar with Play+Bug icon)|
||Variables Panel|Window for displaying current variable values during debugging|
||Debug Controls|Control elements: Continue, Step Over, Step Into, Step Out|
||Watch Expressions|Monitoring specific variables/expressions during debugging|
||Call Stack View|Display of the function call order|
|**Technical Terms**|Bug (Error)|Error or defect in code that causes incorrect behavior|
||Debugging (Error search)|Process of finding and fixing bugs|
||Syntax Error|Grammatical error, Python cannot execute the code|
||Runtime Error|Error during execution (code starts, then crashes)|
||Logic Error|Code runs without errors, but result is wrong|
||Traceback|Error report from Python with information about the error location|
||Expected Output|What the program should do|
||Actual Output|What the program actually does|
||Reproduce|Consistently making an error reoccur|
||Isolate|Narrowing down the source of the error in the code|
||Edge Cases|Extreme values or special cases for testing|
||Breakpoint|Marker for pausing code execution|
||Step Over|Execute next line without entering functions|
||Step Into|Enter a function and step through it line by line|
||Step Out|Jump out of the current function|
||Continue|Continue execution until the next breakpoint|
||Execution Flow|Order in which code is executed|
||Inspect Variables|Examining variable values during a pause|
||Gutter|Area to the left of line numbers (for setting breakpoints)|
|**Important Vocabulary**|Syntax|Set of rules for how code must be written|
||Colon `:`|Colon (frequently forgotten with `if`, `for`, `def`)|
||Mismatched Parentheses|Unequal/missing brackets `()`, `[]`, `{}`|
||Divide by Zero|Division by zero (causes RuntimeError)|
||IndexError|Accessing a non-existent list index|
||NameError|Using an undefined variable|
||Crash|Program crash during execution|
||Red Dot|Red dot = set breakpoint in VS Code|
||Debug Console|Console during debugging for entering commands|
||Play Icon|Symbol for resuming execution (Continue)|
||Bug Icon|Symbol for debugging functions in VS Code|