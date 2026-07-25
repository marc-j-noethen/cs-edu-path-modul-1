# PY 11 - Exercise 2: Dates

## Task

This exercise covered Python modules. The goal was to import the right standard-library module and implement the requested function so that all provided tests pass.

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
from datetime import datetime

def days_between_dates(date_str1, date_str2):
    try:
        date1 = datetime.strptime(date_str1, "%Y-%m-%d").date()
        date2 = datetime.strptime(date_str2, "%Y-%m-%d").date()
        return abs((date2 - date1).days)
    except ValueError:
        return None
```

## Result

All visible tests passed successfully. The screenshot shows the green Passed all tests! or Correct result.

## Evidence

![PY11 Exercise 2 passed tests](screenshots/py11-ex2-dates.png)

## Evidence Assessment

The screenshot is sufficient evidence because it shows the passing test run, completed platform task, or relevant Git/GitHub state.

## Practical Value

Standard-library modules avoid unnecessary custom code and are an important part of maintainable Python solutions.
