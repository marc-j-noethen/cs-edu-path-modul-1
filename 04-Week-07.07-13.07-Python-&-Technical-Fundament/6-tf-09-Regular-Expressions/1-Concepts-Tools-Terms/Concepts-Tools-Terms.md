## 📊 Summary Following the 80/20 Principle

### What are Regular Expressions?

**Regular Expressions (Regex)** are sequences of characters that define search patterns — like a “Find & Replace” function on steroids. Instead of searching for fixed text, you can search for **patterns**.

**Examples**:

- All email addresses in a document
    
- All IP addresses in log files
    
- All phone numbers in the format XXX-XXX-XXXX
    
- Lines that begin with a specific word
    

---

### Why Regex in Cybersecurity?

**The 6 Main Applications**:

1. **Log Analysis**: Search millions of lines for suspicious patterns (e.g., failed login attempts)
    
2. **Intrusion Detection**: IDS/IPS systems use regex for malware signatures
    
3. **Data Validation**: Validate inputs (email, passwords) against attacks
    
4. **Forensics**: Extract evidence (emails, credit cards, URLs)
    
5. **Automation**: Scripts for parsing outputs and configuration files
    
6. **Malware Analysis**: Detect function calls, URLs, encryption keys
    

---

### Testing Tool: Regex101.com

**Recommended Tool**: [Regex101.com](https://regex101.com/?utm_source=chatgpt.com) (platform-independent, browser-based)

**Interface**:

- **REGULAR EXPRESSION** (top): Enter regex pattern
    
- **TEST STRING** (middle): Text for testing
    
- **EXPLANATION** (right): Automatic explanation of the pattern
    
- **MATCH INFORMATION**: Shows all matches
    
- **FLAVOR**: PCRE2 (similar to Python) as default
    

---

### The 6 Fundamental Regex Concepts

#### 1. Literal Characters

**Simplest form**: Characters match themselves

```regex
cat
```

Finds: “cat” in “The **cat** sat on the mat”

---

#### 2. Anchors - Position Markers

|Character|Meaning|Example|
|---|---|---|
|`^`|Beginning of line|`^Start` finds only at the beginning|
|`$`|End of line|`end$` finds only at the end|
|`\b`|Word boundary|`\bcat\b` finds “cat”, not “catalog”|
|`\B`|No word boundary|`\Bcat\B` finds “cat” in “concatenate”|

**Example**:

```regex
^\d{3}     # Finds 3 digits at the beginning of a line
log$       # Finds "log" at the end of a line
```

---

#### 3. Character Classes

|Character|Meaning|Example|
|---|---|---|
|`.`|Any character (except newline)|`a.c` → "abc", "a1c", "a@c"|
|`[abc]`|One of the specified characters|`[aeiou]` → vowels|
|`[a-z]`|Character range|`[0-9]` → digits|
|`[^abc]`|NOT one of these characters|`[^0-9]` → non-digits|

**Predefined Classes (Shortcuts)**:

```regex
\d    # Digit [0-9]
\D    # Non-digit [^0-9]
\w    # Word character [a-zA-Z0-9_]
\W    # Non-word character
\s    # Whitespace (space, tab, newline)
\S    # Non-whitespace
```

**Example**:

```regex
\d\d\d-\d\d\d-\d\d\d\d    # Phone number: 123-456-7890
[A-Z]\w+                   # Word starting with a capital letter
```

---

#### 4. Quantifiers - “How many times?”

|Character|Meaning|Example|
|---|---|---|
|`*`|0 or more|`ab*c` → "ac", "abc", "abbc"|
|`+`|1 or more|`ab+c` → "abc", "abbc" (NOT "ac")|
|`?`|0 or 1 (optional)|`colou?r` → "color", "colour"|
|`{n}`|Exactly n times|`\d{3}` → exactly 3 digits|
|`{n,}`|At least n times|`\d{2,}` → 2 or more digits|
|`{n,m}`|Between n and m times|`\d{2,4}` → 2 to 4 digits|

**Greedy vs. Non-Greedy**:

```regex
<div>.*</div>        # GREEDY: Matches entire string
<div>.*?</div>       # NON-GREEDY: Matches individual tags
```

**Memory Aid**: `?` after a quantifier makes it “lazy” (minimal matching)

---

#### 5. Grouping & Capturing

**Capturing Groups `()`**:

```regex
(\d{3})-(\d{3})-(\d{4})    # Phone number with 3 groups
```

- Group 1: "123"
    
- Group 2: "456"
    
- Group 3: "7890"
    

**Non-Capturing Groups `(?:...)`**:

```regex
(?:ab)+       # Groups "ab" for quantifier, but does not extract it
```

**Alternation (OR) `|`**:

```regex
cat|dog              # Finds "cat" OR "dog"
^(Error|Warning):    # Lines with "Error:" or "Warning:"
```

---

#### 6. Escaping

**Problem**: Matching metacharacters literally

```regex
\.        # Literal dot (not "any character")
\*        # Literal asterisk (not "0 or more")
\$        # Literal dollar sign (not "end of line")
\\        # Literal backslash
\(        # Literal parenthesis
```

**Example**:

```regex
main\.py           # Finds "main.py" (not "mainXpy")
5\*4               # Finds "5*4" literally
192\.168\.1\.1     # IP address with literal dots
```

---

### Practical Examples for Cybersecurity

#### 1. Find IP Address:

```regex
\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}
```

#### 2. Email Address (simple):

```regex
\w+@\w+\.\w+
```

#### 3. Failed Logins:

```regex
^.*Failed login.*from\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})
```

#### 4. Extract URL:

```regex
https?://[^\s]+
```

#### 5. Date in YYYY-MM-DD Format:

```regex
\d{4}-\d{2}-\d{2}
```

#### 6. Hash (MD5/SHA):

```regex
\b[a-fA-F0-9]{32}\b      # MD5
\b[a-fA-F0-9]{40}\b      # SHA1
```

---

### Regex in Python (`re` Module)

**Most Important Functions**:

```python
import re

text = "My phone is 123-456-7890"
pattern = r"\d{3}-\d{3}-\d{4}"    # Raw string r"" for regex!

# 1. Find first match
match = re.search(pattern, text)
if match:
    print(match.group(0))  # "123-456-7890"

# 2. Find all matches
matches = re.findall(r"\d+", "12 cats and 34 dogs")  # ['12', '34']

# 3. Replace
new_text = re.sub(r"\d+", "X", text)  # "My phone is X-X-X"

# 4. Match at beginning
if re.match(r"^My", text):
    print("Starts with 'My'")
```

---

### Cheat Sheet - Most Important Regex Elements

**Anchors**:

```regex
^     Beginning of line
$     End of line
\b    Word boundary
```

**Character Classes**:

```regex
.     Any character
\d    Digit
\w    Word character
\s    Whitespace
[abc] One of a, b, c
[^abc] Not a, b, or c
```

**Quantifiers**:

```regex
*     0 or more
+     1 or more
?     0 or 1
{n}   Exactly n
{n,m} n to m
```

**Groups**:

```regex
(...)    Capturing group
(?:...)  Non-capturing group
|        OR
```

**Escaping**:

```regex
\.  \*  \?  \+  \$  \^  \(  \)  \[  \]  \\
```

---

### Learning Strategy for Regex

**The 80/20 Approach**:

1. **Master these 5 patterns** (cover 80% of use cases):
    
    - `\d+` (one or more digits)
        
    - `\w+` (one or more word characters)
        
    - `.*` (any text)
        
    - `^...$` (entire line)
        
    - `(...|...)` (alternatives)
        
2. **Practice on Regex101.com**:
    
    - Enter patterns
        
    - Insert test text
        
    - Read the explanation panel
        
    - Experiment!
        
3. **Avoid common mistakes**:
    
    - `.` is NOT a literal dot (→ use `\.`)
        
    - `*` can match 0 occurrences (→ use `+` for at least 1)
        
    - Greedy matching can match too much (→ use `?` for lazy matching)
        
    - Forgetting to escape metacharacters
        

---

### Memory Aids

- **Literal = Itself**: `cat` finds “cat”
    
- **Metacharacters = Special meaning**: `. * + ? ^ $ [ ] ( ) | \`
    
- **Anchors match positions**, not characters
    
- **Quantifiers are greedy** (match maximum), unless used with `?`
    
- **Backslash escapes metacharacters**: `\.` = literal dot
    
- **Raw strings in Python**: `r"\d+"` prevents double escaping
    
- **Test, test, test**: Regex101.com is your best friend
    

---

### Typical Regex Tasks in Cybersecurity

|Task|Regex Example|
|---|---|
|Find IP address|`\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}`|
|Extract email|`[\w.-]+@[\w.-]+\.\w+`|
|Failed logins|`Failed.*\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}`|
|HTTP status codes|`HTTP/\d\.\d"\s+(\d{3})`|
|Malicious URLs|`https?://[a-z0-9.-]+.(ru|
|Credit card (PCI DSS)|`\b\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}\b`|
|Suspicious PowerShell|`-enc[oded]*\s+[A-Za-z0-9+/=]+`|

---

## Tools Used

|Category|Term|Meaning|
|---|---|---|
|Tools Used|Regex101.com|Online testing environment for creating, testing, and understanding regular expressions|
||Python `re` Module|Built-in Python module for using regex in scripts|
||Web Browser|Used to access online regex testers (Chrome, Firefox, Edge for Windows 11)|
||Text Editor with Regex Support|Editors like VS Code, Notepad++ (Windows 11) for text processing with regex|
||`grep` (Command Line)|Unix/Linux tool for searching files with regex patterns|
||`sed` (Stream Editor)|Tool for text manipulation with regex patterns|

---

## Technical Terms

|Category|Term|Meaning|
|---|---|---|
|Technical Terms|Regular Expression (Regex/Regexp)|Sequence of characters defining a search pattern for text processing|
||Pattern|Definition of what should be searched for in text|
||Metacharacter|Special character with special meaning in regex (e.g. ., *, +, ?)|
||Literal Character|Character that represents itself (e.g. 'a' finds 'a')|
||Anchor|Position in text (start/end), not actual characters (^, $, \b)|
||Character Class|Set of characters where one should be matched (e.g. [aeiou])|
||Predefined Character Class|Predefined shortcuts (\d, \w, \s, \D, \W, \S)|
||Quantifier|Specifies how often an element must occur (*, +, ?, {n}, {n,m})|
||Greedy Matching|Quantifier matches as much text as possible|
||Non-Greedy/Lazy Matching|Quantifier matches as little text as possible (with ? after quantifier)|
||Capturing Group|Grouping with parentheses () that extracts matched text|
||Non-Capturing Group|Grouping (?:...) without extraction, only for logic|
||Alternation (OR Logic)|Pipe symbol \| for “or” logic (e.g. cat\|dog)|
||Escaping|Backslash \ before metacharacters to match them literally|
||Word Boundary|Position between word and non-word characters (\b)|
||Regex Flavor|Variant of regex syntax (PCRE, POSIX BRE/ERE, Python)|
||Match|Successful match of a pattern against text|
||PCRE (Perl Compatible RE)|Widely used regex syntax similar to Python|
||Raw String (Python)|String with `r""` prefix, treats backslashes literally|

|Important Vocabulary|Meaning|
|---|---|
|Pattern matching|Finding text patterns|
|Search pattern|Pattern used for text searching|
|Text processing|Text processing and manipulation|
|Data extraction|Extraction of specific data from text|
|Log analysis|Analysis of log files|
|Intrusion Detection/Prevention (IDS/IPS)|Systems for detecting/preventing attacks|
|Data validation|Verification of correct input|
|Digital forensics|Digital forensics for evidence collection|
|Malware analysis|Analysis of malicious software|
|Signature|Detection pattern for malware or attacks|
|Whitespace|Spaces, tabs, line breaks|
|Newline|Line break (`\n`)|
|Alphanumeric|Letters and numbers|
|Delimiter|Separator character|
|Token|Individual element in a pattern|
|Modifier/Flag|Options that modify behavior (e.g. case-insensitive)|
|Non-overlapping|Non-overlapping matches|
|Iterator|Object for step-by-step processing of matches|