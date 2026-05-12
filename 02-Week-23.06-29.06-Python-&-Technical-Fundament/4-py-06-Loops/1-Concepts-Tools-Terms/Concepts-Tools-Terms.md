## **📊 Summary according to the 80/20 Principle**

## **PART 1: WHY LOOPS?**

### **1. The Problem Without Loops**

**Without a loop (cumbersome):**

```python
print(1)
print(2)
print(3)
print(4)
print(5)
# What if we need to count to 1000? 😱
```

**With a loop (elegant):**

```python
for i in range(1, 6):
    print(i)
# Same output, but flexible and maintainable!
```

**Loops = automation of repetition**

---

## **PART 2: THE `for` LOOP**

### **2. Basic Structure of the `for` Loop**

```python
for variable in sequence:
    # Code block (indented!)
    # Repeated for each element
```

**Components:**

- **`for`** = keyword to start
- **`variable`** = takes on each value from the sequence one at a time
- **`in`** = connects the variable to the sequence
- **`sequence`** = list, tuple, string, range() etc.
- **`:`** = colon (required!)
- **Indentation** = 4 spaces (defines what belongs to the loop)

---

### **3. `for` Loop with Lists**

```python
fruits = ["Apple", "Banana", "Cherry"]

for fruit in fruits:
    print(f"I like {fruit}")

# Output:
# I like Apple
# I like Banana
# I like Cherry
```

**What happens:**

1. First iteration: `fruit = "Apple"` → execute code
2. Second iteration: `fruit = "Banana"` → execute code
3. Third iteration: `fruit = "Cherry"` → execute code
4. List exhausted → loop stops

---

### **4. The `range()` Function: Generating Number Sequences**

**Three variants:**

**Variant 1: `range(stop)` – from 0 to stop-1**

```python
for i in range(5):
    print(i)
# Output: 0, 1, 2, 3, 4
```

**Variant 2: `range(start, stop)` – from start to stop-1**

```python
for i in range(3, 7):
    print(i)
# Output: 3, 4, 5, 6
```

**Variant 3: `range(start, stop, step)` – with step size**

```python
# Even numbers from 0 to 10
for i in range(0, 11, 2):
    print(i)
# Output: 0, 2, 4, 6, 8, 10

# Counting backwards
for i in range(10, 0, -1):
    print(i)
# Output: 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
```

**⚠️ Important:** `stop` is NEVER reached!

- `range(5)` → 0, 1, 2, 3, 4 (NOT 5!)
- `range(1, 4)` → 1, 2, 3 (NOT 4!)

---

### **5. Practical `for` Loop Examples**

**Example 1: Calculating square numbers**

```python
for number in range(1, 6):
    square = number ** 2
    print(f"{number} squared = {square}")

# Output:
# 1 squared = 1
# 2 squared = 4
# 3 squared = 9
# 4 squared = 16
# 5 squared = 25
```

**Example 2: Iterating over a string**

```python
word = "Python"
for letter in word:
    print(letter)

# Output:
# P
# y
# t
# h
# o
# n
```

**Example 3: Calculating a sum**

```python
numbers = [10, 20, 30, 40, 50]
total = 0

for number in numbers:
    total = total + number

print(f"Sum: {total}")  # Output: Sum: 150
```

---

## **PART 3: THE `while` LOOP**

### **6. Basic Structure of the `while` Loop**

```python
while condition:
    # Code block (indented!)
    # Runs as long as condition is True
```

**Difference from `for`:**

- `for` = "Repeat X times" or "for each element"
- `while` = "Repeat as long as condition is true"

---

### **7. `while` Loop Examples**

**Example 1: Countdown**

```python
count = 5

while count > 0:
    print(count)
    count = count - 1  # IMPORTANT: condition must eventually become False!

print("Go!")

# Output:
# 5
# 4
# 3
# 2
# 1
# Go!
```

**Example 2: User input**

```python
password = ""

while password != "secret":
    password = input("Enter password: ")

print("Access granted!")
```

**Example 3: Summing until a limit**

```python
total = 0
number = 1

while total < 50:
    total = total + number
    number = number + 1

print(f"Sum: {total}, Last number: {number-1}")
# Output: Sum: 55, Last number: 10
```

---

### **8. ⚠️ Avoiding Infinite Loops!**

**❌ WRONG (infinite loop):**

```python
count = 0
while count < 5:
    print(count)
    # count is never incremented → runs forever!
```

**✅ CORRECT:**

```python
count = 0
while count < 5:
    print(count)
    count = count + 1  # Condition will eventually become False
```

**How to recognize infinite loops:**

- Variable in condition is never changed
- Condition never becomes `False`

**Emergency stop:** `Ctrl + C` in the terminal stops a running program!

---

## **PART 4: FLOW CONTROL WITH `break` AND `continue`**

### **9. `break` – Exit the Loop Immediately**

**Syntax:**

```python
for item in sequence:
    if condition:
        break  # Loop ends immediately
    # Code here is skipped after break
```

**Practical example: Find the first match**

```python
numbers = [1, 2, 4, 3, 5, 6]

for number in numbers:
    print(f"Checking {number}...")
    if number % 3 == 0:  # Divisible by 3?
        print(f"Found: {number}")
        break  # End the loop

print("Done!")

# Output:
# Checking 1...
# Checking 2...
# Checking 4...
# Checking 3...
# Found: 3
# Done!
```

**When to use `break`:**

- Searched element has been found
- An error has occurred
- Condition is met, further iterations are unnecessary

---

### **10. `continue` – Skip the Current Iteration**

**Syntax:**

```python
for item in sequence:
    if condition:
        continue  # Jump to the next iteration
    # Code here is skipped when continue is executed
```

**Practical example: Print only even numbers**

```python
for number in range(1, 11):
    if number % 2 != 0:  # Odd number?
        continue  # Skip the rest, go to the next number
    print(number)  # Only executed for even numbers

# Output:
# 2
# 4
# 6
# 8
# 10
```

**When to use `continue`:**

- An element should be skipped
- A certain condition is not met
- Filter logic

---

### **11. `break` vs. `continue` – The Difference**

```python
# With break (stops at 5)
print("With break:")
for i in range(1, 11):
    if i == 5:
        break
    print(i)
# Output: 1, 2, 3, 4

print("\nWith continue:")
# With continue (skips 5)
for i in range(1, 11):
    if i == 5:
        continue
    print(i)
# Output: 1, 2, 3, 4, 6, 7, 8, 9, 10
```

**Memory aid:**

- **`break`** = "Stop, I'm done!" (loop ends)
- **`continue`** = "Skip this element, on to the next!" (loop continues)

---

## **PART 5: `for` VS. `while` – WHEN TO USE WHICH?**

### **12. Decision Guide**

|Situation|Use|Example|
|---|---|---|
|Number of iterations known|`for`|"Repeat 10 times"|
|Iterating over a list/sequence|`for`|"Process each element"|
|Number of iterations unknown|`while`|"Until user types 'quit'"|
|Condition-based|`while`|"As long as sum < 100"|
|Counter from X to Y|`for` with `range()`|"From 1 to 100"|

**Rule of thumb:**

- ✅ `for` = When you know HOW MANY TIMES or OVER WHAT
- ✅ `while` = When you know UNTIL WHEN (condition)

---

## **QUICK REFERENCE**

### **`for` Loop Cheatsheet:**

```python
# Over a list
for item in list:
    print(item)

# With range (0 to 4)
for i in range(5):
    print(i)

# With range (start, stop)
for i in range(2, 6):
    print(i)

# With step size
for i in range(0, 10, 2):
    print(i)

# With break
for i in range(10):
    if i == 5:
        break

# With continue
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
```

### **`while` Loop Cheatsheet:**

```python
# Simple while
count = 0
while count < 5:
    print(count)
    count += 1

# With break
while True:
    answer = input("Continue? (y/n): ")
    if answer == "n":
        break

# With continue
count = 0
while count < 10:
    count += 1
    if count % 2 == 0:
        continue
    print(count)
```

---

## **COMMON ERRORS AND SOLUTIONS**

❌ **Error 1: Missing colon**

```python
for i in range(5)  # SyntaxError!
    print(i)
```

✅ **Solution:** Add colon

```python
for i in range(5):
    print(i)
```

---

❌ **Error 2: Missing indentation**

```python
for i in range(5):
print(i)  # IndentationError!
```

✅ **Solution:** Indent the code

```python
for i in range(5):
    print(i)
```

---

❌ **Error 3: Infinite loop**

```python
x = 0
while x < 10:
    print(x)
    # x is never incremented!
```

✅ **Solution:** Change the variable

```python
x = 0
while x < 10:
    print(x)
    x += 1
```

---

❌ **Error 4: `range()` misunderstood**

```python
# Expected: 1, 2, 3, 4, 5
for i in range(1, 5):  # Only gives 1, 2, 3, 4
    print(i)
```

✅ **Solution:** Increase stop value by 1

```python
for i in range(1, 6):  # Gives 1, 2, 3, 4, 5
    print(i)
```

---

## **PRACTICE EXERCISES**

**Exercise 1:** Write a `for` loop that prints all numbers from 1 to 10.

**Exercise 2:** Write a `while` loop that counts backwards from 10 to 1.

**Exercise 3:** Write a loop that prints only the odd numbers from 1 to 20 (use `continue`).

**Exercise 4:** Write a loop that stops at the first number > 50:

```python
numbers = [10, 25, 30, 55, 60, 70]
```

---

### **Memory Aids:**

🎯 **`for` = "for each element", `while` = "as long as condition is true"** 🎯 **`range(stop)` goes from 0 to stop-1, NOT to stop!** 🎯 **`break` = exit the loop, `continue` = skip the iteration** 🎯 **Never forget the colon `:` and the indentation!** 🎯 **With `while`: the variable in the condition MUST change, otherwise infinite loop!**

---

## Categorization of Topics

|Category|Term|Meaning|
|---|---|---|
|**Tools Used**|Python Interpreter|For interactively testing loops|
||VS Code|Editor for writing Python scripts with loops|
||`print()` function|Output of values inside loops|
||`range()` function|Generates number sequences for `for` loops|
||`input()` function|User input in `while` loops (not in the document, but relevant)|
|**Technical Terms**|Loop|Repetition of a code block multiple times|
||`for` Loop|Loop that iterates over a sequence (list, tuple, string, etc.)|
||`while` Loop|Loop that runs as long as a condition is `True`|
||Iteration|A single pass through the loop|
||Iterate|To go through the elements of a sequence|
||Sequence|Ordered collection (list, tuple, string, range)|
||Iterable Object|An object that can be iterated over|
||Variable (loop variable)|Variable that takes on the next value in each iteration|
||Code Block|Indented code inside the loop|
||Indentation|Required indentation for code inside the loop (4 spaces)|
||Infinite Loop|A loop that never ends (condition remains `True`)|
||Condition|A boolean expression that is `True` or `False`|
||Increment|To increase a value (e.g. `count = count + 1` or `count += 1`)|
||Modulo Operator `%`|Remainder of a division (e.g. `7 % 3 = 1`)|
||Nested Loop|A loop inside another loop|
||Flow Control|Controlling program flow with `break` and `continue`|
|**Important Vocabulary**|`for` keyword|Starts a `for` loop|
||`while` keyword|Starts a `while` loop|
||`in` keyword|Connects loop variable to sequence (`for item in list`)|
||`range(stop)`|Generates numbers from 0 to `stop-1`|
||`range(start, stop)`|Generates numbers from `start` to `stop-1`|
||`range(start, stop, step)`|Generates numbers from `start` to `stop-1` with step size `step`|
||`break` statement|Ends the loop immediately and continues after it|
||`continue` statement|Skips the rest of the current iteration, moves to the next|
||Colon `:`|Colon at the end of the loop header (required!)|
||Loop Body|The indented code that is repeated|
||Start Value|First value in `range()`|
||Stop Value|Last value + 1 in `range()` (is NEVER reached)|
||Step Value|How much is incremented in `range()`|