# Python Lesson 16: Object-Oriented Programming (OOP)

## 📊 Summary Following the 80/20 Principle

### The 20% core knowledge that provides 80% of understanding:

---

### 1. Most Important Concept: What is OOP?

**Object-Oriented Programming** is a paradigm where code is structured around **objects** — not around procedures.

Each object has:

- **State:** Data/properties (e.g., name, IP address, timestamp)
- **Behavior:** Actions it can perform (e.g., bark(), parse(), filter())

**Comparison of Approaches:**

|Procedural|Object-Oriented|
|---|---|
|Focus on functions & procedures|Focus on objects & their interactions|
|Data and logic separated|Data and logic bundled in objects|
|Good for simple scripts|Good for complex, growing programs|

---

### 2. The 4 Core Building Blocks with Code Examples

#### 🔹 Class — the Blueprint

```python
class Dog:
    def __init__(self, name, breed):   # Constructor
        self.name = name               # Attribute
        self.breed = breed             # Attribute

    def bark(self):                    # Method
        print(f"{self.name} says Woof!")
```

#### 🔹 Object / Instance — the concrete example

```python
my_dog = Dog("Fido", "Golden Retriever")   # Create object
your_dog = Dog("Rex", "German Shepherd")   # Second object
```

#### 🔹 Attributes — the state

```python
print(my_dog.name)      # Output: Fido
print(your_dog.breed)   # Output: German Shepherd

my_dog.name = "Buddy"   # Modify attribute
print(my_dog.name)      # Output: Buddy
```

#### 🔹 Methods — the behavior

```python
my_dog.bark()    # Output: Buddy says Woof!
your_dog.bark()  # Output: Rex says Woof!
```

---

### 3. Understanding the `__init__` Constructor & `self`

```python
class Dog:
    def __init__(self, name, breed):
        # 'self' = the concrete object being created
        # 'name' and 'breed' = parameters passed during creation
        self.name = name
        self.breed = breed
```

**Memory Aid:**

- `__init__` is called **automatically** when an object is created
- `self` is always the **first parameter** of every method
- `self.name` stores the value **on the object** — not just locally in the function

```python
# Python passes 'self' automatically:
my_dog.bark()
# is the same as:
Dog.bark(my_dog)
```

---

### 4. Practical Example: LogEntry Class for Cybersecurity

```python
class LogEntry:
    def __init__(self, timestamp, source_ip, message, severity="INFO"):
        self.timestamp = timestamp
        self.source_ip = source_ip
        self.message = message
        self.severity = severity

    def is_error(self):
        return self.severity in ("ERROR", "CRITICAL")

    def display(self):
        print(f"[{self.severity}] {self.timestamp} | {self.source_ip} | {self.message}")


# Application
entry1 = LogEntry("2024-01-15 08:32:01", "192.168.1.105", "Login failed", "ERROR")
entry2 = LogEntry("2024-01-15 08:32:05", "10.0.0.1", "Service started")

entry1.display()     # [ERROR] 2024-01-15 08:32:01 | 192.168.1.105 | Login failed
entry2.display()     # [INFO] 2024-01-15 08:32:05 | 10.0.0.1 | Service started

print(entry1.is_error())   # True
print(entry2.is_error())   # False
```

---

### 5. Why OOP? — The Advantages

|Advantage|Explanation|Cybersecurity Example|
|---|---|---|
|**Organization**|Related data & functions bundled together|`Alert` class contains type, source, severity + actions|
|**Reusability**|Define blueprint once, use unlimited times|`NetworkPacket` class for every packet type|
|**Modularity**|Objects are self-contained|`Scanner` can be developed independently of `Logger`|
|**Modeling**|Map real-world concepts directly|`MalwareSample`, `SecurityAlert`, `UserSession`|

---

### ✅ Quick Start Checklist

☐ `class ClassName:` — Define class with capital letter  
☐ `def __init__(self, ...):` — Constructor with `self` as first parameter  
☐ `self.attribute = value` — Store attributes on the object  
☐ `def method(self):` — Always define methods with `self`  
☐ `object = ClassName(args)` — Create object/instance  
☐ `object.attribute` — Read or modify attribute  
☐ `object.method()` — Call method  
☐ Practice exercise: Type and run the `Dog` class from the material yourself

---

### 💡 Key Takeaway

> **A class is the blueprint, an object is the building — `self` is the address that tells each building where it stands.**

---

## Table 1: Tools Used

|Tool|Meaning|
|---|---|
|Python Interpreter|Direct execution of OOP code for testing|
|VS Code|IDE for writing and executing `.py` files|
|`.py` file|File format for Python scripts|

---

## Table 2: Technical Terms

|Term|Meaning|
|---|---|
|Object-Oriented Programming (OOP)|Programming paradigm that structures code around objects|
|Procedural Programming|Paradigm that structures code as a sequence of instructions/functions|
|Class|Blueprint/template for creating objects|
|Object / Instance|Concrete example created from a class|
|Attribute|Variable that belongs to an object and stores its state|
|Method|Function that belongs to a class and defines behavior|
|Constructor|Special method (`__init__`) called when creating an object|
|`self`|Reference to the concrete object within its own methods|
|State|Current condition of an object (stored in attributes)|
|Behavior|Actions an object can perform (defined in methods)|
|Dot Notation|Access to attributes/methods via `object.attribute` or `object.method()`|
|Instantiation|The process of creating an object from a class|
|Inheritance|A class inherits properties from another (advanced topic)|

---

## Table 3: Important Vocabulary

|Vocabulary|Meaning|
|---|---|
|`class`|Keyword for defining a class|
|`__init__`|Constructor method (double underscores = "dunder method")|
|`self`|First parameter of every instance method; refers to the object itself|
|`object.attribute`|Access to the state of an object|
|`object.method()`|Call a method on an object|
|Blueprint|Template/design — metaphor for a class|
|Instance|Concrete object created from a class|
|`def`|Keyword for defining a function or method|
|`print(f"...")`|F-string for formatted output|
|Dot Notation|Period notation for accessing members of an object|