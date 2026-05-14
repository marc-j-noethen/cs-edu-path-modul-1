## 📊 Summary Using the 80/20 Principle

## **PART 1: WHAT ARE ERRORS?**

### **1. The Two Main Categories**

**1. Syntax Errors**

- **When:** Detected before program execution
- **Cause:** Errors in code grammar
- **Python says:** "I don't understand this code"

```python
# ❌ Syntax error: Missing colon
if x > 5
    print("Large")
# SyntaxError: invalid syntax

# ❌ Syntax error: Misspelled keyword
whlie count < 10:
    print(count)
# SyntaxError: invalid syntax

# ❌ Syntax error: Unmatched parentheses
print("Hello"
# SyntaxError: unexpected EOF
```

**Solution:** Fix code, then program runs

---

**2. Exceptions (Runtime Errors)**

- **When:** During program execution
- **Cause:** Unexpected situation at runtime
- **Python says:** "Code is correct, but I cannot perform this action"

```python
# ✅ Syntax correct, but...

# ❌ TypeError at runtime
result = "Hello" + 5
# TypeError: can only concatenate str (not "int") to str

# ❌ ZeroDivisionError at runtime
result = 10 / 0
# ZeroDivisionError: division by zero

# ❌ IndexError at runtime
list = [1, 2, 3]
print(list[10])
# IndexError: list index out of range
```

**This lesson focuses on Exceptions!**

---

### **2. What Happens Without Error Handling?**

```python
# Program starts
print("Program started")

# Error occurs
result = 10 / 0  # ZeroDivisionError!

# Program stops here (crash)
print("This line will NEVER be reached")
```

**Output:**

```
Program started
Traceback (most recent call last):
  File "test.py", line 4, in <module>
    result = 10 / 0
ZeroDivisionError: division by zero
```

**Problem:** Program crashes, user sees cryptic error message

---

## **PART 2: WHY ERROR HANDLING?**

### **3. The 5 Main Reasons**

**1. Prevent Crashes**

```python
# ❌ Without handling: Crash
age = int(input("Age: "))  # User enters "abc" → Crash!

# ✅ With handling: No crash
try:
    age = int(input("Age: "))
except ValueError:
    print("Please enter a number!")
    age = 0
```

**2. User-Friendly Messages**

```python
# ❌ Without handling
with open("config.txt", "r") as file:
    config = file.read()
# FileNotFoundError: [Errno 2] No such file or directory: 'config.txt'
# → User understands nothing!

# ✅ With handling
try:
    with open("config.txt", "r") as file:
        config = file.read()
except FileNotFoundError:
    print("Configuration file not found. Using default settings.")
    config = "default"
```

**3. Clean Up Resources**

```python
try:
    file = open("data.txt", "w")
    file.write("Important data")
    # ... error here ...
finally:
    file.close()  # ALWAYS executed
```

**4. Enable Recovery**

```python
try:
    connect_to_server()
except ConnectionError:
    print("Connection failed, trying backup server...")
    connect_to_backup_server()
```

**5. Log Errors**

```python
try:
    critical_operation()
except Exception as e:
    log_error(f"Error in critical operation: {e}")
```

---

## **PART 3: THE TRY-EXCEPT STRUCTURE**

### **4. Basic Structure**

```python
try:
    # Code that could cause an error
    risky_operation()
except ExceptionType:
    # Code that runs when error occurs
    error_handling()
```

---

### **5. Simple Example: Division**

```python
# Without error handling
num1 = 10
num2 = 0
result = num1 / num2  # Crash!
print(result)

# With error handling
num1 = 10
num2 = 0

try:
    result = num1 / num2
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed!")
    result = None

print("Program continues running...")
```

**Output:**

```
Error: Division by zero is not allowed!
Program continues running...
```

---

### **6. Catching Multiple Exception Types**

```python
def process_input(input):
    try:
        # Could cause ValueError (with "abc")
        number = int(input)
        
        # Could cause ZeroDivisionError (with 0)
        result = 100 / number
        
        print(f"Result: {result}")
        
    except ValueError:
        print("Error: Please enter a valid number!")
        
    except ZeroDivisionError:
        print("Error: Division by zero!")
        
    print("Function completed.")

# Tests
process_input("20")    # Works
process_input("abc")   # ValueError
process_input("0")     # ZeroDivisionError
```

**Output:**

```
Result: 5.0
Function completed.
Error: Please enter a valid number!
Function completed.
Error: Division by zero!
Function completed.
```

---

### **7. Accessing the Exception Object with `as`**

```python
try:
    file = open("not_existing.txt", "r")
except FileNotFoundError as error:
    print(f"File error occurred: {error}")
    print(f"Error type: {type(error).__name__}")

# Output:
# File error occurred: [Errno 2] No such file or directory: 'not_existing.txt'
# Error type: FileNotFoundError
```

**Advantage:** Access to error details for logging/debugging

---

## **PART 4: THE `finally` STATEMENT**

### **8. What is `finally`?**

**`finally` = Code that ALWAYS runs**

- Regardless of whether an error occurs or not
- Regardless of whether the exception is caught or not
- Perfect for cleanup (closing files, disconnecting connections)

---

### **9. Example: File Cleanup**

```python
file = None
try:
    print("1. Opening file...")
    file = open("data.txt", "w")
    
    print("2. Writing data...")
    file.write("Important information")
    
    # Simulate error
    print("3. Executing risky operation...")
    x = 1 / 0  # ZeroDivisionError!
    
    print("4. This line will never be reached")
    
except ZeroDivisionError:
    print("5. Error caught!")
    
finally:
    print("6. Cleanup: Closing file...")
    if file:
        file.close()
    print("7. File closed!")

print("8. Program continues running")
```

**Output:**

```
1. Opening file...
2. Writing data...
3. Executing risky operation...
4. Error caught!
5. Cleanup: Closing file...
6. File closed!
7. Program continues running
```

**Important:** Line 4 is skipped, but `finally` runs anyway!

---

### **10. `finally` Without `except`**

```python
try:
    print("Attempting operation...")
    risky_operation()
finally:
    print("Cleanup always runs")
    cleanup()
# Exception is passed on after finally (if not caught)
```

**Use case:** When cleanup is important but the exception should not be handled

---

## **PART 5: COMMON EXCEPTIONS**

### **11. The 10 Most Important Exception Types**

**1. `TypeError` – Wrong Data Type Operation**

```python
try:
    result = "Text" + 5
except TypeError:
    print("Error: Cannot add string and integer")
```

**2. `ValueError` – Wrong Value**

```python
try:
    age = int("not-a-number")
except ValueError:
    print("Error: Not a valid number")
```

**3. `ZeroDivisionError` – Division by Zero**

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero")
```

**4. `IndexError` – Index Out of Range**

```python
try:
    list = [1, 2, 3]
    print(list[10])
except IndexError:
    print("Error: Index does not exist")
```

**5. `KeyError` – Dictionary Key Not Found**

```python
try:
    person = {"name": "Alice"}
    print(person["age"])
except KeyError:
    print("Error: Key 'age' not found")
```

**6. `FileNotFoundError` – File Not Found**

```python
try:
    with open("not_there.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("Error: File does not exist")
```

**7. `NameError` – Variable Not Defined**

```python
try:
    print(undefined_variable)
except NameError:
    print("Error: Variable does not exist")
```

**8. `AttributeError` – Attribute/Method Does Not Exist**

```python
try:
    list = [1, 2, 3]
    list.appeend(4)  # Typo
except AttributeError:
    print("Error: Method does not exist")
```

**9. `ImportError` – Module Not Found**

```python
try:
    import non_existing_module
except ImportError:
    print("Error: Module cannot be imported")
```

**10. `Exception` – General Exception (Base Class)**

```python
try:
    something_risky()
except Exception as e:
    print(f"An error occurred: {e}")
```

---

## **PART 6: BEST PRACTICES**

### **12. Specific Rather Than General**

```python
# ❌ Too general (catches EVERYTHING)
try:
    file = open("config.txt", "r")
    age = int(input)
    result = 10 / number
except:  # Also catches syntax errors, keyboard interrupts, etc.!
    print("Some error")

# ✅ Specific (only expected errors)
try:
    file = open("config.txt", "r")
    age = int(input)
    result = 10 / number
except FileNotFoundError:
    print("File not found")
except ValueError:
    print("Invalid number")
except ZeroDivisionError:
    print("Division by zero")
```

**Why?**

- Unexpected errors are not accidentally "swallowed"
- Better debugging
- Clearer code

---

### **13. Generic Exception as Fallback**

```python
try:
    complex_operation()
except ValueError:
    print("Value error")
except TypeError:
    print("Type error")
except Exception as e:  # Catches all other exceptions
    print(f"Unexpected error: {e}")
```

**Rule:** Specific exceptions first, then `Exception` as fallback

---

### **14. Multiple Exceptions at Once**

```python
# Method 1: Tuple of exceptions
try:
    risk()
except (ValueError, TypeError) as e:
    print(f"Input error: {e}")

# Method 2: Separate except blocks (when different handling needed)
try:
    risk()
except ValueError:
    print("Value is wrong")
except TypeError:
    print("Type is wrong")
```

---

## **PART 7: LBYL VS. EAFP**

### **15. Two Philosophies**

**LBYL (Look Before You Leap)**

```python
# Check beforehand
if 'key' in my_dict:
    value = my_dict['key']
else:
    value = 'default'

# Check data type
if isinstance(age, int):
    print(age)
```

**Advantages:**

- Explicit and predictable
- Good when checking is cheap

**Disadvantages:**

- More code
- Race conditions possible
- Not always possible to check

---

**EAFP (Easier to Ask Forgiveness than Permission)**

```python
# Just try it
try:
    value = my_dict['key']
except KeyError:
    value = 'default'

# Try conversion
try:
    number = int(input)
except ValueError:
    number = 0
```

**Advantages:**

- Pythonic (idiomatic)
- More efficient (for rare errors)
- Works in unpredictable situations

**Disadvantages:**

- Can cost performance (with frequent errors)

---

### **16. When to Use Which?**

|Situation|Method|Example|
|---|---|---|
|Check is cheap and clear|LBYL|`if x != 0: y = 10/x`|
|Error is rare|EAFP|`try: value = dict[key]`|
|Cannot check beforehand|EAFP|Import errors, network errors|
|Performance-critical (many errors)|LBYL|Loop over many items|

**Python preference:** EAFP is more idiomatic

---

## **PRACTICAL EXAMPLES**

### **17. Example 1: Safe User Input**

```python
def get_positive_number():
    """Prompts user to enter a positive number."""
    while True:
        try:
            input_val = input("Enter positive number: ")
            number = float(input_val)
            
            if number <= 0:
                print("Error: Number must be positive!")
                continue
            
            return number
            
        except ValueError:
            print("Error: Please enter a valid number!")
        except KeyboardInterrupt:
            print("\nProgram aborted")
            return None

# Usage
number = get_positive_number()
if number:
    print(f"Thank you! You entered {number}.")
```

---

### **18. Example 2: Load Configuration File**

```python
def load_config(filename="config.txt"):
    """Loads configuration, uses defaults on error."""
    default_config = {
        "theme": "light",
        "font_size": 12,
        "language": "en"
    }
    
    try:
        with open(filename, "r") as file:
            # Assumed: Each line is "key=value"
            config = {}
            for line in file:
                line = line.strip()
                if '=' in line:
                    key, value = line.split('=', 1)
                    config[key] = value
            
            print(f"Configuration loaded from {filename}")
            return config
            
    except FileNotFoundError:
        print(f"Warning: {filename} not found. Using default values.")
        return default_config
        
    except Exception as e:
        print(f"Error while loading: {e}. Using default values.")
        return default_config

# Usage
config = load_config()
print(f"Theme: {config.get('theme', 'light')}")
```

---

### **19. Example 3: Database Operation with Cleanup**

```python
def save_to_database(data):
    """Simulates database operation with cleanup."""
    connection = None
    try:
        print("1. Connecting to database...")
        connection = connect_database()
        
        print("2. Starting transaction...")
        connection.start_transaction()
        
        print("3. Saving data...")
        connection.save(data)
        
        print("4. Committing transaction...")
        connection.commit()
        
        print("Successfully saved!")
        return True
        
    except ConnectionError:
        print("Error: No connection to database")
        if connection:
            connection.rollback()
        return False
        
    except DataError as e:
        print(f"Error: Invalid data - {e}")
        if connection:
            connection.rollback()
        return False
        
    finally:
        print("5. Cleanup: Closing connection...")
        if connection:
            connection.close()
        print("Connection closed")
```

---

## **QUICK REFERENCE**

### **Try-Except-Finally Cheatsheet:**

```python
# Simple try-except
try:
    risk()
except ValueError:
    handling()

# Multiple exceptions
try:
    risk()
except ValueError:
    print("Value error")
except TypeError:
    print("Type error")

# Access exception object
try:
    risk()
except Exception as e:
    print(f"Error: {e}")

# With finally
try:
    risk()
except Exception:
    handling()
finally:
    cleanup()

# Multiple exceptions together
try:
    risk()
except (ValueError, TypeError):
    handling()

# Generic fallback
try:
    risk()
except ValueError:
    specific()
except Exception as e:
    general(e)
```

---

## **COMMON ERRORS AND SOLUTIONS**

### **20. Error 1: Too General `except:`**

```python
# ❌ Catches EVERYTHING (even Ctrl+C!)
try:
    operation()
except:
    print("Error")

# ✅ Specific
try:
    operation()
except ValueError:
    print("Value error")
except Exception as e:
    print(f"Other error: {e}")
```

---

### **21. Error 2: Forgotten `finally` for Cleanup**

```python
# ❌ File is not closed on error
try:
    file = open("data.txt", "w")
    file.write(risky_data())
    file.close()  # Not reached on error!
except Exception:
    print("Error")

# ✅ With finally
try:
    file = open("data.txt", "w")
    file.write(risky_data())
except Exception:
    print("Error")
finally:
    file.close()  # ALWAYS executed

# ✅✅ Or better: with 'with'
try:
    with open("data.txt", "w") as file:
        file.write(risky_data())
except Exception:
    print("Error")
```

---

### **22. Error 3: Wrong Order**

```python
# ❌ Generic exception first (catches everything!)
try:
    operation()
except Exception:  # Also catches ValueError!
    print("General")
except ValueError:  # NEVER reached!
    print("Value error")

# ✅ Specific first, generic last
try:
    operation()
except ValueError:
    print("Value error")
except Exception:
    print("General")
```

---

## **PRACTICE EXERCISES**

**Exercise 1:** Write a function `safe_division(a, b)` that performs division and catches all possible errors.

**Exercise 2:** Create a program that asks the user for a filename, opens the file, counts the lines. Handle FileNotFoundError.

**Exercise 3:** Write a function that converts a list of strings to integers. Skip invalid values.

**Exercise 4:** Simulate a network request with random errors. Use try-except-finally for cleanup.

---

### **Mnemonics:**

🎯 **Exceptions = runtime errors, Syntax Errors = pre-runtime errors**  
🎯 **`try` = attempt, `except` = on error, `finally` = always**  
🎯 **`finally` runs ALWAYS (perfect for cleanup!)**  
🎯 **Specific exceptions first, `Exception` as fallback last**  
🎯 **EAFP = Pythonic, LBYL = explicit (both have their place)**  
🎯 **Never use `except:` without exception type (catches too much!)**  
🎯 **Error handling = prevent crashes + user-friendliness**

---

## Tools Used

|Category|Term|Meaning|
|---|---|---|
|**Tools Used**|Python Interpreter|For testing exception handling|
||VS Code|Editor for writing Python scripts with error handling|
||Traceback|Python error report with details about the error origin|
||`try` Statement|Block for potentially error-prone code|
||`except` Statement|Block for handling exceptions|
||`finally` Statement|Block that always runs (for cleanup)|

---

## Technical Terms

|Category|Term|Meaning|
|---|---|---|
|**Technical Terms**|Error|Situation in which code cannot be executed as expected|
||Exception|Runtime error that occurs during program execution|
||Syntax Error|Error in code structure/grammar (detected before execution)|
||Runtime Error|Error during program execution (= Exception)|
||Exception Handling|Mechanism for catching and processing errors|
||Traceback|Error log with call history and error position|
||Crash|Program stops abruptly due to unhandled error|
||Graceful Handling|Catching errors without program crash|
||Cleanup|Releasing resources (files, connections)|
||Recovery|Correcting error or trying an alternative|
||Logging|Recording errors for debugging|
||User Feedback|User-friendly error message|
||Unhandled Exception|Uncaught exception (leads to crash)|
||Re-raise|Passing exception to outer try block|
||Matching|Finding the right `except` for an exception type|
||Base Class|Superclass from which other exceptions inherit|
||LBYL|"Look Before You Leap" - check before action|
||EAFP|"Easier to Ask Forgiveness than Permission" - try first, then handle errors|
|**Important Vocabulary**|`try:`|Starts block with potentially error-prone code|
||`except ExceptionType:`|Catches specific exception type|
||`except Exception as e:`|Catches exception and stores in variable `e`|
||`finally:`|Block that always runs (cleanup)|
||`Exception`|Base class for most exceptions|
||`SyntaxError`|Error in code syntax (cannot be caught by try-except)|
||`TypeError`|Wrong data type operation (e.g. `"text" + 5`)|
||`ValueError`|Correct type, wrong value (e.g. `int("abc")`)|
||`NameError`|Variable not defined|
||`IndexError`|Index outside list/sequence|
||`KeyError`|Dictionary key not found|
||`FileNotFoundError`|File does not exist|
||`ZeroDivisionError`|Division by zero|
||`ImportError`|Module cannot be imported|
||`AttributeError`|Attribute/method does not exist (e.g. typo)|
||`IOError`|Input/output error|
||`raise`|Manually raising an exception (not covered in detail)|