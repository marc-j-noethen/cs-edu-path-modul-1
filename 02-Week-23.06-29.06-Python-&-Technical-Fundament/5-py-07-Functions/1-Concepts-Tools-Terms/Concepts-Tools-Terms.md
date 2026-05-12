## **📊 Summary according to the 80/20 Principle**

## **PART 1: WHAT ARE FUNCTIONS?**

### **1. The Problem Without Functions**

**Without a function (repetitive):**

```python
# Area of rectangle 1
length = 10
width = 5
area = length * width
print("Area:", area)

# Area of rectangle 2
length2 = 7
width2 = 3
area2 = length2 * width2
print("Area:", area2)

# Area of rectangle 3
length3 = 12
width3 = 8
area3 = length3 * width3
print("Area:", area3)
```

**With a function (elegant):**

```python
def calculate_area(length, width):
    area = length * width
    return area

# Multiple uses
print("Area:", calculate_area(10, 5))
print("Area:", calculate_area(7, 3))
print("Area:", calculate_area(12, 8))
```

**Function = reusable code building block**

---

## **PART 2: DEFINING FUNCTIONS**

### **2. Basic Structure of a Function**

```python
def function_name(parameter1, parameter2):
    """Optional docstring: explains what the function does."""
    # Code block (indented!)
    # ... statements ...
    return result  # Optional: returns a value
```

**Components:**

1. **`def`** = keyword to start
2. **`function_name`** = descriptive name in snake_case
3. **`(parameter1, parameter2)`** = inputs (can be 0 or more)
4. **`:`** = colon (required!)
5. **`"""Docstring"""`** = documentation (optional, but recommended)
6. **Indented code** = what the function does
7. **`return`** = returns a value (optional)

---

### **3. Simple Function Without Parameters**

```python
def greeting():
    """Prints a simple greeting."""
    print("Hello, welcome!")

# Call the function
greeting()
# Output: Hello, welcome!
```

**Important:**

- The definition alone does NOT execute the code
- Only the call `greeting()` executes the code

---

### **4. Function with Parameters**

```python
def greeting_with_name(name):
    """Greets a person by their name."""
    print(f"Hello, {name}!")

# Call the function with an argument
greeting_with_name("Alice")   # Output: Hello, Alice!
greeting_with_name("Bob")     # Output: Hello, Bob!
```

---

### **5. Function with Multiple Parameters**

```python
def add(number1, number2):
    """Adds two numbers."""
    total = number1 + number2
    return total

result = add(5, 3)
print(result)  # Output: 8

# Or print directly
print(add(10, 20))  # Output: 30
```

---

## **PART 3: PARAMETERS VS. ARGUMENTS**

### **6. The Difference**

```python
def multiply(x, y):  # x and y = PARAMETERS (placeholders)
    return x * y

result = multiply(4, 7)  # 4 and 7 = ARGUMENTS (actual values)
```

**Memory rule:**

- **Parameters** = placeholders in the **definition** (`def`)
- **Arguments** = values at the **call**

---

## **PART 4: THE `return` STATEMENT**

### **7. Function with a Return Value**

```python
def square(number):
    """Calculates the square of a number."""
    result = number ** 2
    return result

# Store return value in a variable
result = square(5)
print(result)  # Output: 25

# Or use directly
print(square(3) + square(4))  # Output: 9 + 16 = 25
```

---

### **8. `return` Ends the Function Immediately**

```python
def check_number(number):
    """Checks whether a number is positive, negative, or zero."""
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"
    print("This line is never reached!")  # Unreachable code

print(check_number(5))    # Output: Positive
print(check_number(-3))   # Output: Negative
print(check_number(0))    # Output: Zero
```

**Important:** Code after `return` is never executed!

---

### **9. Function Without `return` Returns `None`**

```python
def say_hello(name):
    """Prints a greeting but returns nothing."""
    print(f"Hello, {name}!")
    # No return statement

result = say_hello("Max")
print(result)

# Output:
# Hello, Max!
# None
```

---

### **10. Different Return Types**

```python
# Return integer
def get_age():
    return 25

# Return string
def get_name():
    return "Alice"

# Return boolean
def is_even(number):
    return number % 2 == 0

# Return list
def get_numbers():
    return [1, 2, 3, 4, 5]

print(get_age())        # Output: 25
print(get_name())       # Output: Alice
print(is_even(10))      # Output: True
print(get_numbers())    # Output: [1, 2, 3, 4, 5]
```

---

## **PART 5: WHY FUNCTIONS? (THE 4 ADVANTAGES)**

### **11. Organisation**

```python
# Without functions (cluttered)
# ... 100 lines of code for task 1 ...
# ... 150 lines of code for task 2 ...
# ... 80 lines of code for task 3 ...

# With functions (clean)
def task1():
    # ... code ...
    pass

def task2():
    # ... code ...
    pass

def task3():
    # ... code ...
    pass

# Main program
task1()
task2()
task3()
```

---

### **12. Reusability (DRY Principle)**

**DRY = "Don't Repeat Yourself"**

```python
# Without function: same code 3 times
password1 = "secret123"
if len(password1) >= 8 and any(c.isdigit() for c in password1):
    print("Password 1 is strong")

password2 = "test"
if len(password2) >= 8 and any(c.isdigit() for c in password2):
    print("Password 2 is strong")

# With function: write once, use multiple times
def is_password_strong(password):
    """Checks if password has at least 8 characters and one digit."""
    return len(password) >= 8 and any(c.isdigit() for c in password)

if is_password_strong("secret123"):
    print("Password 1 is strong")

if is_password_strong("test"):
    print("Password 2 is strong")
```

---

### **13. Maintainability**

```python
# Need to make a change? Only in ONE place!
def calculate_tax(amount):
    """Calculates tax on an amount."""
    tax_rate = 0.19  # Change here affects everything everywhere
    return amount * tax_rate

print(calculate_tax(100))
print(calculate_tax(250))
print(calculate_tax(500))
```

---

### **14. Abstraction**

```python
# You don't need to know HOW it works
# You only need to know WHAT it does

def encrypt_password(password):
    """Encrypts a password (complex logic internal)."""
    # Complex encryption algorithm here...
    # 50 lines of code...
    return encrypted

# The user only needs to know: returns an encrypted password
secure_pw = encrypt_password("myPassword123")
```

---

## **PART 6: SCOPE**

### **15. Local vs. Global Scope**

```python
# Global variable (outside of functions)
global_variable = "I am global"

def my_function():
    # Local variable (inside the function)
    local_variable = "I am local"
    
    print(local_variable)    # ✅ Works
    print(global_variable)   # ✅ Works (globally readable)

my_function()

print(global_variable)       # ✅ Works
# print(local_variable)      # ❌ NameError! Not accessible here
```

**Rule:**

- **Local variables** = only visible inside the function
- **Global variables** = visible everywhere (but changing inside a function requires `global`)

---

### **16. Parameters Are Local**

```python
def add(a, b):
    # a and b only exist inside this function
    total = a + b  # total is also local
    return total

result = add(5, 3)
# print(a)      # ❌ Error! a does not exist here
# print(b)      # ❌ Error! b does not exist here
# print(total)  # ❌ Error! total does not exist here
print(result)   # ✅ Works
```

---

## **PRACTICAL EXAMPLES**

### **17. Example 1: Temperature Converter**

```python
def celsius_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit."""
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

print(f"0°C = {celsius_to_fahrenheit(0)}°F")
print(f"25°C = {celsius_to_fahrenheit(25)}°F")
print(f"100°C = {celsius_to_fahrenheit(100)}°F")

# Output:
# 0°C = 32.0°F
# 25°C = 77.0°F
# 100°C = 212.0°F
```

---

### **18. Example 2: Even or Odd**

```python
def is_even(number):
    """Checks whether a number is even."""
    if number % 2 == 0:
        return True
    else:
        return False

# Or shorter:
def is_even(number):
    """Checks whether a number is even."""
    return number % 2 == 0

print(is_even(10))  # Output: True
print(is_even(7))   # Output: False
```

---

### **19. Example 3: Maximum of Three Numbers**

```python
def max_of_three(a, b, c):
    """Returns the largest of three numbers."""
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

print(max_of_three(5, 10, 3))   # Output: 10
print(max_of_three(15, 8, 12))  # Output: 15
```

---

### **20. Example 4: Processing a List**

```python
def double_list(numbers):
    """Doubles all numbers in a list."""
    doubled = []
    for number in numbers:
        doubled.append(number * 2)
    return doubled

original = [1, 2, 3, 4, 5]
result = double_list(original)

print(f"Original: {original}")
print(f"Doubled: {result}")

# Output:
# Original: [1, 2, 3, 4, 5]
# Doubled: [2, 4, 6, 8, 10]
```

---

## **QUICK REFERENCE**

### **Function Cheatsheet:**

```python
# Simple function
def say_hello():
    print("Hello!")

say_hello()

# With parameter
def greet(name):
    print(f"Hello, {name}!")

greet("Max")

# With return value
def add(a, b):
    return a + b

total = add(5, 3)

# With multiple parameters and return value
def calculate_area(length, width):
    """Calculates the area of a rectangle."""
    return length * width

area = calculate_area(10, 5)

# With docstring
def example_function(param):
    """
    Description of the function.
    
    Parameters:
        param: Description of the parameter
    
    Returns:
        Description of the return value
    """
    return param * 2
```

---

## **COMMON ERRORS AND SOLUTIONS**

❌ **Error 1: Function defined but not called**

```python
def say_hello():
    print("Hello!")

# Nothing happens because the function was not called
```

✅ **Solution:** Call the function

```python
def say_hello():
    print("Hello!")

say_hello()  # Now "Hello!" is printed
```

---

❌ **Error 2: Forgotten parentheses when calling**

```python
def calculate_sum(a, b):
    return a + b

print(calculate_sum)  # Prints the function object, not the result
```

✅ **Solution:** Add parentheses

```python
print(calculate_sum(5, 3))  # Output: 8
```

---

❌ **Error 3: Wrong number of arguments**

```python
def add(a, b):
    return a + b

# add(5)         # TypeError! Missing one argument
# add(5, 3, 7)   # TypeError! Too many arguments
```

✅ **Solution:** Pass the correct number

```python
add(5, 3)  # ✅ Works
```

---

❌ **Error 4: Return value not saved/used**

```python
def multiply(a, b):
    return a * b

multiply(5, 3)  # Result is lost
```

✅ **Solution:** Store or use the return value

```python
result = multiply(5, 3)
print(result)  # Output: 15
```

---

❌ **Error 5: Using a local variable outside the function**

```python
def calculate():
    total = 10 + 5
    return total

calculate()
# print(total)  # NameError! total only exists inside the function
```

✅ **Solution:** Use the return value

```python
result = calculate()
print(result)  # Output: 15
```

---

## **PRACTICE EXERCISES**

**Exercise 1:** Write a function `calculate_square(number)` that returns the square of a number.

**Exercise 2:** Write a function `is_adult(age)` that returns `True` if `age >= 18`, otherwise `False`.

**Exercise 3:** Write a function `sum_list(numbers)` that returns the sum of all numbers in a list.

**Exercise 4:** Write a function `reverse(text)` that returns a string backwards.

---

### **Memory Aids:**

🎯 **Definition ≠ Execution! Only a call with `()` executes the code** 🎯 **Parameters = placeholders at definition, arguments = values at call** 🎯 **`return` returns a value AND ends the function immediately** 🎯 **Without `return`, the function returns `None`** 🎯 **Local variables = only inside the function, global = visible everywhere** 🎯 **Functions = reusable, maintainable, organised (DRY principle!)**

---

## Categorization of Topics

|Category|Term|Meaning|
|---|---|---|
|**Tools Used**|Python Interpreter|For interactively testing functions|
||VS Code|Editor for writing Python scripts with functions|
||`print()` function|Output of values (itself a built-in function)|
||`def` keyword|Keyword for defining custom functions|
||`return` statement|Returns a value from a function|
|**Technical Terms**|Function|Reusable, named code block for a specific task|
||Function Definition|Creating a function with `def`|
||Function Call|Executing a function by using its name|
||Parameter|Placeholder variable in a function definition (e.g. `def func(parameter):`)|
||Argument|Actual value passed at the function call (e.g. `func(5)`)|
||Return Value|Value that the function returns with `return`|
||Docstring|Documentation string in triple quotes after the function header|
||Code Block|Indented code inside the function|
||Modularity|Breaking code into reusable units|
||Reusability|Using the same code multiple times without repetition|
||Abstraction|Using functions without knowing their internal workings|
||DRY Principle|"Don't Repeat Yourself" – avoiding code repetition|
||Scope|The area in which a variable is accessible|
||Local Scope|Variables inside the function (only accessible there)|
||Global Scope|Variables outside of functions (accessible everywhere)|
||Function Header|First line with `def`, name, parameters, and `:`|
||Function Body|Indented code that is executed|
||`None`|Special value returned by functions without `return`|
|**Important Vocabulary**|`def`|Keyword to start a function definition|
||`return`|Returns a value and ends the function|
||Function Name|Descriptive name in snake_case (e.g. `calculate_sum`)|
||Parentheses `()`|Round brackets for parameters at definition and arguments at call|
||Colon `:`|Colon at the end of the function header (required!)|
||Indentation|4 spaces for code inside the function|
||Triple Quotes `"""`|Triple quotation marks for docstrings|
||Calling|Executing a function with `function_name()`|
||Passing Arguments|Providing values when calling a function|
||Zero Parameters|Function without parameters: `def func():`|
||Multiple Parameters|Several parameters separated by commas: `def func(a, b, c):`|
||Unreachable Code|Code after `return` that is never executed|
||snake_case|Naming convention for functions: `my_function`|