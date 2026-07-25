# PY 11 - Exercise 3: Weekday

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
import datetime
import calendar

def find_next_weekday(start_date_str, target_weekday_name):
    start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d").date()
    target_weekday_number = list(calendar.day_name).index(target_weekday_name)
    days_ahead = (target_weekday_number - start_date.weekday() + 7) % 7
    if days_ahead == 0:
        days_ahead = 7
    return (start_date + datetime.timedelta(days=days_ahead)).strftime("%Y-%m-%d")
```

## Result

All visible tests passed successfully. The screenshot shows the green Passed all tests! or Correct result.

## Evidence

![PY11 Exercise 3 passed tests](screenshots/py11-ex3-weekday.png)

## Evidence Assessment

The screenshot is sufficient evidence because it shows the passing test run, completed platform task, or relevant Git/GitHub state.

## Practical Value

Standard-library modules avoid unnecessary custom code and are an important part of maintainable Python solutions.
