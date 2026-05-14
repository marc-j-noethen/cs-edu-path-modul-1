## 📊 Summary Using the 80/20 Principle

**Dictionaries** are a fundamental Python data structure that stores data as **key-value pairs**. Unlike lists, where elements are accessed via indices, dictionaries use unique keys for data access. **Core Concepts:**

- **Creation**: `my_dict = {"key": "value"}` or `dict(key=value)`
- **Keys**: Must be immutable (strings, numbers, tuples) - no lists or dictionaries
- **Values**: Can be any data type (strings, numbers, lists, other dictionaries, etc.)
- **Access**: `my_dict["key"]` (throws KeyError for missing key) or `my_dict.get("key", default)` (safer)
- **Adding/Updating**: `my_dict["new_key"] = value`
- **Deleting**: `del my_dict["key"]`, `my_dict.pop("key")`, or `my_dict.popitem()`
- **Checking**: `"key" in my_dict`
- **Important Methods**: `.keys()`, `.values()`, `.items()` return view objects **Main Advantage**: Fast data access via unique identifiers instead of position numbers - ideal for contact lists, configurations, database-like structures.

---

## Tools

|Tool/Utility/Program|Meaning/Function|
|---|---|
|Python|Programming language in which dictionaries are available as a built-in data structure|
|VS Code|Code editor/IDE for experimenting with Python code|

---

## Technical Terms

|Technical Term|Meaning/Explanation|
|---|---|
|Dictionary|Python data structure for storing key-value pairs; unordered, but fast access via keys|
|Key|Unique identifier for looking up data in a dictionary; must be immutable|
|Value|The data associated with a key; can be any data type|
|Key-Value Pair|A combination of a key and its associated value in a dictionary|
|Immutable|Data types that cannot be changed after their creation (strings, numbers, tuples)|
|Mutable|Data types that can be changed after their creation (lists, dictionaries)|
|List|Ordered sequence of elements; access via index|
|Tuple|Immutable, ordered sequence of elements|
|String|Sequence of characters; immutable data type|
|Integer|Whole number data type without decimal places|
|Float|Numeric data type with decimal places|
|Boolean|Data type with two values: True or False|
|View Object|Dynamic object that shows the current keys, values, or pairs of a dictionary|
|KeyError|Error type that occurs when accessing a non-existent key|
|Method|Function that belongs to an object and is executed on it|
|Constructor|Special function for creating new objects (e.g. `dict()`)|
