## **📊 Summary according to the 80/20 Principle**

**1. Creating and Using Variables (5 Minutes of Practice)**

* Syntax: `variable_name = value`
* Example: `age = 25` or `name = "Max"`
* Variable names: Lowercase with underscores (`my_name`, not `MyName`)
* Output value: `print(age)` or simply type `age` in the interpreter

**2. Knowing the 4 Basic Data Types**

* `int` → Whole numbers: `5`, `100`, `-3`
* `float` → Decimal numbers: `3.14`, `2.0`
* `str` → Text in quotation marks: `"Hello"` or `'World'`
* `bool` → Boolean values: `True`, `False`

**3. Checking Data Types**

* `type(variable)` shows the data type
* Example: `type(25)` → `<class 'int'>`

**4. Basic Arithmetic Operations with Numbers**

* Addition: `10 + 5` → `15`
* Subtraction: `10 - 3` → `7`
* Multiplication: `4 * 5` → `20`
* Division: `10 / 3` → `3.333...` (always returns a float!)
* Floor Division: `10 // 3` → `3`
* Remainder (Modulo): `10 % 3` → `1`
* Exponent: `2 ** 3` → `8`

**5. Working with Text**

* Concatenation: `"Hello" + " " + "World"` → `"Hello World"`
* Repetition: `"Python " * 3` → `"Python Python Python "`
* Important: You cannot directly mix numbers and text! `5 + "Text"` → Error!

**6. Type Conversion for Errors**

* Number to text: `str(5)` → `"5"`
* Text to number: `int("100")` → `100`
* Practical: `"I am " + str(25) + " years old"` works!
* Even better: Use f-strings: `f"I am {25} years old"`

**7. Using the Python Interpreter (Windows 11)**

* Open Terminal/Command Prompt
* Type `python` or `python3`
* Test code line by line
* Exit with `exit()` or Ctrl + D (on some systems Ctrl + Z)

**Most Common Beginner Mistake:**  
❌ `"100" / 2` → TypeError (Text cannot be divided by a number)  
✅ `int("100") / 2` → `50.0` (convert to number first!)

**Key Takeaway:** Python is flexible with variables (dynamic typing), but strict when performing operations between different data types!

**Categorization of Topics**

**Used Tools**

| Tool                          | Meaning |
|-------------------------------|--------|
| Python Interpreter            | Interactive development environment for running Python code |
| Terminal / Command Prompt     | Command line to start the Python interpreter (Windows: `python` or `python3`) |
| `>>>` Prompt                  | Input prompt of the Python interpreter |
| `print()` Function            | Outputs values to the console |
| `type()` Function             | Shows the data type of a variable or value |
| `isinstance()` Function       | Checks if an object belongs to a specific data type |

**Technical Terms**

| Technical Term                | Meaning |
|-------------------------------|--------|
| Variable                      | Named storage location for data |
| Assignment Operator           | The equals sign `=` for assigning values |
| Data Type                     | The type of stored data (e.g. number, text) |
| Dynamic Typing                | The data type of a variable can change at runtime |
| snake_case                    | Naming convention with underscores (e.g. `my_name`) |
| PEP 8                         | Python Enhancement Proposal – Style guide for Python code |
| TypeError                     | Error message for incompatible data types |
| Concatenation                 | Joining strings with `+` |
| f-string (formatted string)   | Modern method for string formatting with `f"..."` |
| Floor Division                | Division with rounding down `//` |
| Modulo (Remainder)            | Remainder of a division `%` |

**Important Vocabulary**

| Vocabulary                    | Meaning |
|-------------------------------|--------|
| int (Integer)                 | Whole number without decimal places (e.g. 10, -3, 0) |
| float                         | Floating-point number with decimal places (e.g. 3.14, 2.0) |
| str (String)                  | Character string/text in quotation marks (e.g. "Hello") |
| bool (Boolean)                | Boolean value: True or False |
| Exponentiation                | Raising to a power with `**` (e.g. 2**3 = 8) |
| Type Conversion               | Conversion between data types: `int()`, `float()`, `str()` |
| Keyword                       | Reserved words in Python (e.g. `if`, `else`, `for`) |
| Case-sensitive                | Python distinguishes between uppercase and lowercase (e.g. `Variable` vs `variable`) |