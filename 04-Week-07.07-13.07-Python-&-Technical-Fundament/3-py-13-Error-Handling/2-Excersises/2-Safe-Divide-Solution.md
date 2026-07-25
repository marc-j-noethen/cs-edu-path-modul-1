# PY 13 - Exercise 2: Safe Divide

## Task

This exercise covered Python error handling. The goal was to catch expected exceptions with 	ry/xcept and return predictable results.

## Execution Environment

- Browser: Cybersteps / Moodle CodeRunner
- Language: Python 3
- Module 1: no TryHackMe

## Approach

1. The function requirements and tests were reviewed.
2. The solution was implemented in Python and checked against the visible test cases.
3. The passing test run was documented with a screenshot.

## Code Used

```python
def safe_divide(numerator_str, denominator_str):
    try:
        numerator = float(numerator_str)
        denominator = float(denominator_str)
    except ValueError:
        return "Invalid number format"
    else:
        try:
            return numerator / denominator
        except ZeroDivisionError:
            return "Cannot divide by zero"
```

## Result

All visible tests passed successfully. The screenshot shows the green Passed all tests! or Correct result.

## Evidence

![PY13 Exercise 2 passed tests](screenshots/py13-ex2-safe-divide.png)

## Evidence Assessment

The screenshot is sufficient evidence because it shows the passing test run, completed platform task, or relevant Git/GitHub state.

## Practical Value

Error handling makes programs more robust and predictable, especially when inputs, files, or external data sources can be invalid.
