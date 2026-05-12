## **📊 Summary according to the 80/20 Principle**

**1. What are Conditions?**

* Conditions = Questions that the program asks
* The answer is always **True** (true) or **False** (false)
* Purpose: Code reacts differently to different situations
* Example: Is the user over 18? → Yes/No → Grant/Deny access

**2. Boolean Values: The Foundation**

* Only two possible values: `True` and `False`
* Important: Pay attention to capitalization! `true` does **NOT** work

```python
is_adult = True
is_child = False
print(type(is_adult))  # <class 'bool'>
```

**3. Comparison Operators: Asking Questions**

| Operator | Meaning              | Example     | Result |
|----------|----------------------|-------------|--------|
| ==       | Equal to             | 5 == 5      | True   |
| !=       | Not equal to         | 5 != 6      | True   |
| >        | Greater than         | 10 > 5      | True   |
| <        | Less than            | 3 < 8       | True   |
| >=       | Greater than or equal| 7 >= 7      | True   |
| <=       | Less than or equal   | 4 <= 3      | False  |

⚠️ Most Common Mistake:

* `=` is **Assignment** → `x = 5` (stores 5 in x)
* `==` is **Comparison** → `x == 5` (checks if x is equal to 5)

**4. The if-Statement: Simple Decision**

**Structure:**

```python
if condition:
    # Code is ONLY executed if condition is True
    # MUST be indented (4 spaces)
    print("Condition is true!")
```

**Practical Example:**

```python
temperature = 32
if temperature > 30:
    print("It's hot!")     # This will be executed
print("Have a nice day!")  # This is ALWAYS executed (not indented)
```

**5. The else-Statement: The Alternative**

**Structure:**

```python
if condition:
    # Code if True
else:
    # Code if False
```

**Practical Example:**

```python
age = 17
if age >= 18:
    print("Access granted")
else:
    print("Access denied")   # This will be executed
```

**6. The elif-Statement: Multiple Options**

**Structure:**

```python
if condition1:
    # Code if condition1 is True
elif condition2:
    # Code if condition1 is False BUT condition2 is True
elif condition3:
    # Code if condition1 and condition2 are False BUT condition3 is True
else:
    # Code if ALL conditions are False
```

**Practical Example (Grading System):**

```python
points = 75

if points >= 90:
    print("Grade: Excellent")
elif points >= 80:
    print("Grade: Good")
elif points >= 70:
    print("Grade: Satisfactory")   # This will be executed
elif points >= 60:
    print("Grade: Sufficient")
else:
    print("Grade: Fail")
```

**Important:** Python checks from top to bottom and stops at the first `True`!

**7. Logical Operators: Combining Conditions**

**and** – AND (BOTH must be True):

```python
age = 25
has_ticket = True

if age >= 18 and has_ticket:
    print("Entry allowed")   # Both conditions are True → executed
```

**or** – OR (AT LEAST ONE must be True):

```python
is_weekend = False
has_vacation = True

if is_weekend or has_vacation:
    print("Free!")   # One condition is True → executed
```

**not** – NOT (reverses the value):

```python
raining = False

if not raining:
    print("No umbrella needed")   # not False = True → executed
```

**Truth Table for and and or:**

```
True and True   = True
True and False  = False
False and False = False

True or True    = True
True or False   = True
False or False  = False
```

**8. Important Syntax Rules (Avoid Common Mistakes!)**

✅ Correct:

```python
if age >= 18:
    print("Adult")
```

❌ Wrong (missing colon):

```python
if age >= 18
    print("Adult")
```

❌ Wrong (missing indentation):

```python
if age >= 18:
print("Adult")
```

❌ Wrong (wrong capitalization):

```python
if age >= 18:
    print(true)   # Must be True!
```

**9. Practical Example: Complete Decision Logic**

```python
# Club entry control
age = 22
has_id = True
is_guest = False

if age >= 21 and has_id:
    print("Welcome!")
elif is_guest:
    print("Guests must go to reception")
else:
    print("No entry possible")
```

**Step-by-step logic:**

1. Check: `age >= 21` → True AND `has_id` → True = True and True = True
2. First condition is True → "Welcome!" is printed
3. All further conditions (`elif`, `else`) are skipped

**10. Quick Test: Do You Understand It?**

**Task:** What does this code output?

```python
x = 10
y = 5

if x > y:
    print("A")
elif x < y:
    print("B")
else:
    print("C")
```

**Answer:** A (because 10 > 5 is True)

**Task:** What does this code output?

```python
is_sunny = True
temperature = 20

if is_sunny and temperature > 25:
    print("Perfect beach day!")
elif is_sunny:
    print("Nice day for a walk")
else:
    print("Maybe better stay inside")
```

**Answer:** Nice day for a walk  
(First condition False because 20 is not > 25, second condition True because `is_sunny = True`)

**Key Takeaways:**
🎯 `=` stores, `==` compares  
🎯 Indentation is mandatory, not optional!  
🎯 `and` = both must be true, `or` = one is enough  
🎯 Never forget the colon `:` at the end of the condition line!  
🎯 Python checks conditions from top to bottom and stops at the first `True`

**Categorization of Topics**

**Used Tools**

| Tool                | Meaning |
|---------------------|--------|
| Python Interpreter  | Interactive environment for testing conditions |
| VS Code             | Code editor for writing and running Python scripts (.py files) |
| `print()` Function  | Output of values and results to check conditions |

**Technical Terms**

| Technical Term              | Meaning |
|-----------------------------|--------|
| Condition                   | Expression that evaluates to True or False |
| Boolean Value               | Truth value: either True or False |
| Comparison Operator         | Operators for comparing values (==, !=, >, <, >=, <=) |
| Logical Operator            | Operators for combining conditions (and, or, not) |
| Assignment Operator         | The `=` sign for assigning values (x = 5) |
| Equality Operator           | The `==` sign for comparing values (x == 5) |
| Indentation                 | Required indentation in Python (4 spaces) to define code blocks |
| Code Block                  | Related lines grouped by indentation |
| Control Flow                | Control of which code is executed based on conditions |
| Case-sensitive              | True/False must be capitalized, not true/false |
| Expression                  | Code that is evaluated to a value (e.g. 5 > 3 → True) |
| Dynamic Execution           | Code reacts differently based on conditions |

**Important Vocabulary**

| Vocabulary               | Meaning |
|--------------------------|--------|
| if Statement             | Executes code if condition is True |
| else Statement           | Executes code if the previous if condition is False |
| elif Statement           | "else if" – checks additional condition if previous was False |
| == (Equal to)            | Equal (e.g. 5 == 5 → True) |
| != (Not equal to)        | Not equal (e.g. 5 != 6 → True) |
| > (Greater than)         | Greater than (e.g. 10 > 5 → True) |
| < (Less than)            | Less than (e.g. 3 < 8 → True) |
| >= (Greater than or equal) | Greater than or equal (e.g. 7 >= 7 → True) |
| <= (Less than or equal)  | Less than or equal (e.g. 4 <= 3 → False) |
| and                      | AND – both conditions must be True |
| or                       | OR – at least one condition must be True |
| not                      | NOT – reverses the truth value (not True → False) |
| Colon `:`                | Colon at the end of every condition line (required!) |
| Catch-all else           | Block executed if no condition is met |