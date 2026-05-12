## **📊 Summary according to the 80/20 Principle**

## **PART 1: LISTS**

### **1. What is a List?**

- **List = container for multiple elements in one variable**
- Syntax: Square brackets `[]` separated by commas
- **3 main properties:**
    - ✅ **Ordered** (order is preserved)
    - ✅ **Mutable** (can be changed after creation)
    - ✅ **Allows duplicates** (same values can appear multiple times)

```python
# Different list types
numbers = [1, 2, 3, 4, 5]
fruits = ["Apple", "Banana", "Cherry"]
mixed = ["Hello", 100, True, 3.14]
empty = []
```

---

### **2. Indexing: Accessing Elements**

**Positive index (from the front):**

```python
fruits = ["Apple", "Banana", "Cherry"]
#          Index:    0         1         2

print(fruits[0])   # Output: Apple
print(fruits[1])   # Output: Banana
print(fruits[2])   # Output: Cherry
```

**Negative index (from the back):**

```python
fruits = ["Apple", "Banana", "Cherry"]
#          Index:   -3        -2        -1

print(fruits[-1])  # Output: Cherry (last element)
print(fruits[-2])  # Output: Banana (second to last)
```

**⚠️ Important:** Python starts at 0, not 1!

**❌ Avoiding errors:**

```python
fruits = ["Apple", "Banana", "Cherry"]
# print(fruits[3])  # IndexError! Only indices 0, 1, 2 exist
```

---

### **3. Modifying Lists (Mutable)**

**Changing an element:**

```python
colors = ["red", "green", "blue"]
colors[1] = "yellow"
print(colors)  # Output: ['red', 'yellow', 'blue']
```

**Adding an element with `.append()`:**

```python
tasks = ["Read email", "Go shopping"]
tasks.append("Exercise")
print(tasks)  # Output: ['Read email', 'Go shopping', 'Exercise']
```

---

### **4. Length of a List with `len()`**

```python
fruits = ["Apple", "Banana", "Cherry"]
count = len(fruits)
print(count)  # Output: 3

empty_list = []
print(len(empty_list))  # Output: 0
```

**Important rule:**

- A list of length 5 has indices: `0, 1, 2, 3, 4`
- The last index is always `len(list) - 1`

---

### **5. Checking for an Element with `in`**

```python
fruits = ["Apple", "Banana", "Cherry"]

if "Banana" in fruits:
    print("Yes, Banana is in the list!")
    
if "Strawberry" not in fruits:
    print("Strawberry is not in the list!")
```

---

### **6. The Most Important List Methods**

|Method|Description|Example|
|---|---|---|
|`.append(item)`|Adds element at the end|`list.append(5)`|
|`.remove(item)`|Removes first occurrence|`list.remove("Apple")`|
|`.sort()`|Sorts the list|`numbers.sort()`|
|`.count(item)`|Counts occurrences|`list.count("Apple")`|
|`.index(item)`|Returns the index|`list.index("Banana")`|

```python
numbers = [3, 1, 4, 1, 5, 9]

numbers.append(2)
print(numbers)  # Output: [3, 1, 4, 1, 5, 9, 2]

numbers.sort()
print(numbers)  # Output: [1, 1, 2, 3, 4, 5, 9]

print(numbers.count(1))  # Output: 2 (1 appears twice)
```

---

## **PART 2: TUPLES**

### **7. What is a Tuple?**

- **Tuple = immutable list**
- Syntax: Round brackets `()` instead of square brackets `[]`
- CANNOT be changed after creation

```python
coordinates = (10.0, 20.0)
person = ("Alice", 30, "Engineer")
colors = ("red", "green", "blue")
```

**⚠️ Special case with a single element:**

```python
# WRONG:
single = ("Hello")  # This is a string, not a tuple!

# CORRECT:
single = ("Hello",)  # Comma is required for single-element tuples!
```

---

### **8. Tuple vs. List: The Key Difference**

|Property|List `[]`|Tuple `()`|
|---|---|---|
|**Mutable?**|✅ Yes|❌ No|
|**Add elements?**|✅ `.append()`|❌ Not possible|
|**Change elements?**|✅ `list[0] = new`|❌ Error!|
|**Speed**|Slower|Faster|
|**Use case**|Data that changes|Data that stays constant|

```python
# List (mutable)
list = [1, 2, 3]
list[0] = 10
list.append(4)
print(list)  # Output: [10, 2, 3, 4]

# Tuple (immutable)
tuple = (1, 2, 3)
# tuple[0] = 10  # TypeError! Not allowed
# tuple.append(4)  # AttributeError! Method does not exist
```

---

### **9. Accessing Tuples (same as lists)**

```python
person = ("Alice", 30, "Engineer")

print(person[0])   # Output: Alice
print(person[-1])  # Output: Engineer
print(len(person)) # Output: 3
```

---

### **10. Tuple Unpacking: The Secret Trick!**

**Assigning multiple variables at once:**

```python
person = ("Alice", 30, "Engineer")

name, age, job = person

print(name)  # Output: Alice
print(age)   # Output: 30
print(job)   # Output: Engineer
```

**Swapping values without a temporary variable:**

```python
x = 10
y = 20

x, y = y, x  # Swap!

print(x)  # Output: 20
print(y)  # Output: 10
```

**Function with multiple return values:**

```python
def get_coordinates():
    return (100, 200)

x, y = get_coordinates()
print(f"X: {x}, Y: {y}")  # Output: X: 100, Y: 200
```

---

### **11. When to Use a Tuple, When a List?**

**Use TUPLES when:**

- ✅ Data should NOT change (e.g. days of the week, GPS coordinates)
- ✅ As a dictionary key (lists cannot do this!)
- ✅ Returning multiple values from a function
- ✅ Performance matters (tuples are faster)

**Use LISTS when:**

- ✅ Data needs to be able to change
- ✅ Adding/removing elements
- ✅ Sorting or modifying

```python
# Good: Tuple for fixed values
DAYS_OF_WEEK = ("Monday", "Tuesday", "Wednesday", "Thursday", 
                "Friday", "Saturday", "Sunday")

# Good: List for mutable data
shopping_list = ["Milk", "Eggs"]
shopping_list.append("Bread")
```

---

## **QUICK REFERENCE**

### **List Cheatsheet:**

```python
# Create
list = [1, 2, 3]

# Access
list[0]      # First element
list[-1]     # Last element

# Modify
list[0] = 10

# Add
list.append(4)

# Length
len(list)

# Check
if 2 in list:
    print("Found!")
```

### **Tuple Cheatsheet:**

```python
# Create
tuple = (1, 2, 3)

# Access (same as list)
tuple[0]      # First element
tuple[-1]     # Last element

# Unpacking
a, b, c = tuple

# Length
len(tuple)

# NOT possible:
# tuple[0] = 10    # Error!
# tuple.append(4)  # Error!
```

---

## **COMMON ERRORS AND SOLUTIONS**

❌ **Error 1: Index out of range**

```python
fruits = ["Apple", "Banana"]
# print(fruits[2])  # IndexError!
```

✅ **Solution:** Check length with `len()` or use `-1` for the last element

---

❌ **Error 2: Tuple without comma for a single element**

```python
wrong = ("Hello")   # This is a string!
```

✅ **Solution:** Add a comma:

```python
correct = ("Hello",)
```

---

❌ **Error 3: Trying to modify a tuple**

```python
tuple = (1, 2, 3)
# tuple[0] = 10  # TypeError!
```

✅ **Solution:** Use a list instead of a tuple, or create a new tuple

---

### **Memory Aids:**

🎯 **Lists = mutable `[]`, Tuples = immutable `()`** 🎯 **Python counts from 0, not 1!** 🎯 **Index `-1` = last element** 🎯 **Tuple with 1 element: `(item,)` – don't forget the comma!** 🎯 **Tuple unpacking saves code: `x, y = (10, 20)`**

---

## Categorization of Topics

|Category|Term|Meaning|
|---|---|---|
|**Tools Used**|Python Interpreter|For interactively testing list operations|
||VS Code|Editor for writing Python scripts with lists|
||`print()` function|Output of lists and their contents|
||`len()` function|Returns the number of elements in a list/tuple|
||`type()` function|Shows the data type (list or tuple)|
|**Technical Terms**|List|Mutable collection of elements in square brackets `[]`|
||Tuple|Immutable collection of elements in round brackets `()`|
||Index (Indexing)|Position of an element in a list (starts at 0)|
||Zero-based Indexing|First element has index 0, not 1|
||Negative Indexing|Access from the back: `-1` = last element, `-2` = second to last|
||Mutable|Contents can be changed after creation (lists)|
||Immutable|Contents CANNOT be changed after creation (tuples)|
||Ordered|Elements retain their order|
||Duplicates|Same elements can appear multiple times|
||IndexError|Error when accessing a non-existent index|
||Method|Function that belongs to an object (called with `.`)|
||Dot Notation|Calling methods: `list.append()`|
||Mixed Data Types|List/tuple with different data types (int, str, bool, etc.)|
||Tuple Unpacking|Assigning multiple values from a tuple to separate variables|
||Hashable|Can be used as a dictionary key (tuples yes, lists no)|
||Iteration|Going through all elements of a list/tuple with a loop|
|**Important Vocabulary**|`[]` Square Brackets|Square brackets for creating lists|
||`()` Parentheses|Round brackets for creating tuples|
||`.append(item)`|Adds element at the end of the list|
||`.count(value)`|Counts how often a value appears (list & tuple)|
||`.index(value)`|Returns the index of the first occurrence (list & tuple)|
||`.remove(item)`|Removes the first occurrence of an element (list only)|
||`.sort()`|Sorts the list (list only, not tuple)|
||`in` operator|Checks whether an element exists in a list/tuple|
||Concatenation|Joining lists/tuples with `+`|
||Length|Number of elements (with `len()`)|
||First Item|Index `0` or `list[0]`|
||Last Item|Index `-1` or `list[-1]`|
||Empty List|`[]` with no elements|
||Single Item Tuple|Tuple with one element: `(item,)` – comma is required!|