# 🐍 Sensible Intelligence (IntelliSense & Debugger)

**Course:** Cyber Security Analyst - Python Basics | **Date:** 18 June 2025

---

## Task

**Objective:** Observe VS Code IntelliSense and syntax highlighting, and set a breakpoint in the debugger.

**Requirements:**
- Create `clues.py` using the provided code
- Observe colouring and IntelliSense
- Set a breakpoint and start the debugger

---

## Solution

### Code for `clues.py`

```python
# Observe the colour of this comment line
investigator_name = "Sherlock Coder"
clue_count = 0

print("Investigator:", investigator_name)

def find_clue(clue_number):
    # Observe the colour of the 'def' keyword above
    location = "Study" # Observe the colour of this text string
    global clue_count
    clue_count = clue_count + 1
    print(f"Found clue {clue_number} in the {location}. Total clues: {clue_count}") # Breakpoint goes here!

# Start typing 'find' below this line. Does VS Code suggest 'find_clue'?
find_clue (1)

# Now start typing 'inv'. Does VS Code suggest 'investigator_name'?
print("Checking investigator:", investigator_name)

# Hover your mouse cursor over the function name 'find_clue' on the line above.
# Hover your mouse cursor over the built-in function name 'print'.
```

---

## Answers to the questions

### Question 4a: Colour of the comment line
**Answer:** Comments are typically displayed in **green** or **grey** and appear lighter/more muted than the executable code. They stand out clearly from the rest of the code.

### Question 4b: Colour of the `def` keyword
**Answer:** The `def` keyword is typically displayed in **blue** or **purple/magenta** (depending on the colour scheme).

### Question 4c: IntelliSense for `find`
**Answer:** **Yes** – VS Code displays a suggestion for `find_clue`.

### Question 4d: IntelliSense for `inv`
**Answer:** **Yes** – VS Code displays a suggestion for `investigator_name`.

### Question 4e: Hover over `print`
**Answer:** A pop-up appears with the **function signature** and a **description** of the `print()` function. Typically, the following is displayed:
- Function name and parameters
- A brief description of what the function does
- Parameter types and return value

---

## Debugger guide

### Setting a breakpoint
1. Click to the left of the line number at `print(f"Found clue...")`
2. A **red dot** appears

### Starting the debugger
1. Click the **Run and Debug** icon (play button with a bug)
2. Click **"Run and Debug"** (green button)
3. Select **"Python File"** when prompted
4. Execution stops at the breakpoint line (highlighted in yellow)

---

## Screenshot checklist

For submission, the screenshot must show:
- [ ] `clues.py` open in VS Code
- [ ] Breakpoint (red dot) visible
- [ ] Line is highlighted in yellow (execution paused)
- [ ] Debug toolbar visible (Continue, Step Over, etc.)

---

## Notes

- **IntelliSense:** Automatic code completion
- **Syntax highlighting:** Colour-coding of code elements
- **Breakpoint:** Stop point for the debugger
- **Debugger shortcuts:**
  - `F5` = Start/resume debugger
  - `F10` = Step Over (next line)
  - `F11` = Step Into (jump into function)
  - `Shift+F5` = Stop debugger

**Typical colour scheme (Dark Theme):**
| Element | Colour |
|---------|-------|
| Comments | Green/Grey |
| Keywords (`def`, `if`) | Blue/Purple |
| Strings | Orange/Yellow |
| Function names | Yellow |
| Variables | White/Light blue |

