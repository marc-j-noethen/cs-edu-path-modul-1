# 🐍 Log Lurker (Windows Event Logs)

**Course:** Cyber Security Analyst - OS Technology | **Date:** 29 August 2025

---

## Task

**Objective:**  
Explain how to locate and filter failed and successful logins in Windows security logs.

**Requirements:**

- Identify 4625 for failed logins and 4624 for successful logins.
- Highlight useful fields such as Account Name and Logon Type.
- Name a useful filtering method in Event Viewer.
- Formulate the result as a brief forensic observation.

- Output:

    - Key details of the 4625 and 4624 events
    - Method for quickly filtering failed logins
    - Brief forensic assessment

---

## Solution

```text
Relevant events:
- Event ID 4625 = failed logon (Audit Failure)
- Event ID 4624 = successful logon (Audit Success)

Useful fields:
- Account Name / TargetUserName
- Logon Type
- Failure Reason or Status/Substatus for 4625
- Workstation / Source Network Address, if available

What makes this forensically interesting?
4625 indicates that a login attempt took place but failed – including user details and often the reason.
4624, on the other hand, confirms a successful login and helps with the temporal correlation of legitimate user activity.

Quick filtering method:
In Event Viewer -> Windows Logs -> Security -> `Filter Current Log...`
and enter, for example, `4625` as the Event ID.
For successful logins, use `4624` accordingly.
Alternatively, a custom view can be created for both IDs.
```

**Alternative (compact):**

```text
4625 answers 'who was denied access?', 4624 answers 'who successfully logged in?'.
```

---

## Tests

|Input 1|Input 2|Input 3|Expected|Result|✓|
|---|---|---|---|---|---|
|`4625`|`Security log`|`Filter`|`failed logins only`|`expected`|✅|
|`4624`|`Security log`|`Filter`|`successful logins only`|`expected`|✅|
|`Account/Reason`|`event details`|`review`|`useful context`|`yes`|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|Audit Failure|Security event for failed authentication-related actions.|
|Audit Success|Security event for successfully completed actions.|
|Event Filtering|Targeted reduction of large logs to relevant event IDs or time windows.|

---

## Rules / Logic

```text
Without filters, the security log quickly becomes confusing.
Event ID plus time plus username usually provides the most useful starting point.
Failure and success events belong together for a good timeline.
```

---

## Notes

- **Important:** 4625 and 4624 are standard anchors for login analysis in Windows.
- **Tip:** View Failed and Success events within the same timeline, not in isolation.
- **Observation:** Status/substatus for 4625 in particular often provide the real added value.

---

## Optional: Extensions

- Addition: Include 4634 (Logoff) and 4648 (Explicit Credentials) in the same analysis.
- Automate Event Viewer filters later via PowerShell (`Get-WinEvent`).
