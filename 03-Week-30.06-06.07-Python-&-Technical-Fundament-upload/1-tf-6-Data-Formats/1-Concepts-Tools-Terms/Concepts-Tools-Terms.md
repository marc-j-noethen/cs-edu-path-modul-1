## 📊 **Summary based on the 80/20 principle**

### Key concepts

**Serialisation and deserialisation** are the fundamental processes involved in data exchange:

- **Serialisation** converts data structures in memory into formats suitable for storage or transmission
- **Deserialisation** converts these formats back into usable data structures
- Analogy: packing (serialisation) and unpacking (deserialisation) data for transport

### The four most important data formats

**1. CSV (Comma-Separated Values)**

- Simplest format for tabular data
- Rows = records, commas separate values
- Ideal for spreadsheet-like data
- Limitation: Problematic with complex, nested structures

**2. JSON (JavaScript Object Notation)**

- Most popular format for web APIs and configuration
- Uses key-value pairs in `{}` and lists in `[]`
- Easily readable by both humans and machines
- Supports nested structures

**3. XML (eXtensible Markup Language)**

- Flexible format with user-defined tags `<tag>value</tag>`
- Supports attributes and nested elements
- More verbose than JSON, but highly structured
- Commonly found in older systems and complex data structures

**4. YAML (YAML Ain't Markup Language)**

- Minimalist and human-readable
- Uses indentation (spaces!) for structuring
- Popular for configuration files
- Caution: Indentation errors lead to parsing errors

### Relevance to cybersecurity (80% of practical applications)

1. **Configuration files** for security tools use JSON, XML or YAML
2. **API communication** with security services usually takes place via JSON
3. **Log analysis** benefits from structured formats (often JSON)
4. **Data export/import** between security tools uses CSV, XML or JSON
5. **Payload analysis** of network traffic requires deserialisation

### Practical skills

You do not need to be an expert in programming parsers, but you should:

- Be able to recognise formats at a glance
- Understand the basic structure
- Be able to read and adapt simple configurations
- Know when which format is suitable

---

## Tools used

|**Category**|**Term**|**Meaning**|
|---|---|---|
|**Tools used**|CSV editor (e.g. Excel, LibreOffice Calc)|Programmes for editing comma-separated values files|
||JSON parser (e.g. jq, Python json module)|Tools for processing and validating JSON data|
||XML parser (e.g. xmllint, Python xml module)|Tools for processing and validating XML documents|
||YAML parser (e.g. yamllint, Python yaml module)|Tools for processing and validating YAML files|
||Text editors (Notepad++, VS Code)|Editors for viewing and editing structured data files|

---

## Technical terms

| **Category**        | **Term**                                | **Meaning**                                                                                |
| ------------------- | --------------------------------------- | ------------------------------------------------------------------------------------------ |
| **Technical terms** | Serialisation                           | Conversion of data structures in memory into a format suitable for storage or transmission |
|                     | Deserialisation                         | Reconversion of serialised data into usable data structures in memory                      |
|                     | Structured data                         | Data that follows a consistent pattern or model                                            |
|                     | Key-value pair                          | A data pair consisting of a unique key and the corresponding value                         |
|                     | JSON object                             | A collection of key-value pairs enclosed in curly brackets {}                              |
|                     | JSON array                              | An ordered list of values enclosed in square brackets []                                   |
|                     | XML tag                                 | Markup element in angle brackets <> used to structure data                                 |
|                     | XML attribute                           | Additional information within an XML tag                                                   |
|                     | YAML mapping                            | Mapping of keys to values (equivalent to a JSON object)                                    |
|                     | YAML sequence                           | Ordered list of elements (equivalent to a JSON array)                                      |
|                     | API (Application Programming Interface) | Interface for data exchange between programmes                                             |
|                     | Delimiter                               | Character used to separate data values (e.g. comma in CSV)                                 |
|                     | Indentation                             | Use of spaces for structuring (important in YAML)                                          |
|                     | Parsing                                 | Analysing and processing structured data                                                   |
| **Key terms**       | Tabular data                            | Data organised into rows and columns                                                       |
|                     | Header row                              | First row containing column names                                                          |
|                     | Record                                  | A complete row containing related information                                              |
|                     | Nested                                  | Hierarchically organised data structures                                                   |
|                     | Portable                                | Transferable between different systems                                                     |
|                     | Persistent                              | Stored permanently (not temporarily)                                                       |
|                     | Human-readable                          | Formatted in a way that is understandable to humans                                        |
|                     | Machine-readable                        | Can be processed efficiently by computers                                                  |
|                     | Verbose                                 | Many characters used to represent the same information                                     |
|                     | Configuration file                      | File containing settings for programmes                                                    |
|                     | Payload                                 | Data being transmitted or processed                                                        |
|                     | Log file                                | File containing records of system events                                                   |

