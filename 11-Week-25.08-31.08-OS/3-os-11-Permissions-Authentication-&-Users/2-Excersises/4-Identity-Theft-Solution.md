# 🐍 Identity Theft (Alternate Credentials)

**Course:** Cyber Security Analyst - OS Technology | **Date:** 27 August 2025

---

## Task

**Objective:**  
Execute a command under the security context of another user whilst still saving the output to an admin folder.

**Requirements:**

- Log in non-interactively as `TargetUserTom`.
- Run `whoami` in the context of this user.
- Write the output to `C:\Evidence\ImpersonationProof.txt`, even though the target user has no permissions there.
- Clearly explain the method.

- Output:

    - Clean impersonation method
    - Explanation of why the file still ends up in the Evidence folder
    - Reference to the target user’s lack of direct write permissions

---

## Solution

```text
Appropriate method:
A PowerShell/NET process is launched using alternative credentials,
but the standard output is not written to `C:\Evidence` by the target user;
instead, it is intercepted by the already privileged parent process and stored there.

Example approach in PowerShell / .NET:
- `ProcessStartInfo` with `UserName = "TargetUserTom"`, password as a secure string and `UseShellExecute = $false`
- `RedirectStandardOutput = $true`
- Target command: `whoami`
- Parent process reads the output and then writes it itself as an administrator to:
  `C:\Evidence\ImpersonationProof.txt`

Why is this important?
If `TargetUserTom` were required to write directly to `C:\Evidence` themselves,
the process would fail due to the intentionally revoked permissions.
By using Redirect + Parent-Save, the identity of the executed command remains correct,
whilst the file is created within the authorised context.

Expected file content:
<Computername>\TargetUserTom
```

**Alternative (compact):**

```text
The trick is not 'more rights for Tom', but to capture the stdout from Tom's process and save it as an admin.
```

---

## Tests

|Input 1|Input 2|Input 3|Expected|Result|✓|
|---|---|---|---|---|---|
|`alternate credentials`|`whoami`|`stdout`|`shows TargetUserTom`|`expected`|✅|
|`TargetUserTom`|`Evidence folder`|`direct write`|`denied`|`expected`|✅|
|`parent admin`|`redirected output`|`save file`|`success`|`expected`|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|Alternate Credentials|A process can be started with different user credentials without the need for interactive re-login.|
|Stdout Redirection|The output of a process running in a different context can be intercepted by the parent.|
|Permission Boundary|The target user retains no write permissions to the evidence folder.|

---

## Rules / Logic

```text
The identity of the process and the write context of the evidence file must be considered separately.
Direct file operations by the target user fail due to intentionally missing permissions.
Redirected output is the cleanest way to provide evidence here.
```

---

## Notes

- **Important:** The task explicitly does not require interactive login as the target user.
- **Tip:** In Process Explorer or Task Manager, you can also view the user context of the launched process.
- **Observation:** This task is excellent for practising the difference between 'who is executing' and 'who is writing the file'.

---

## Optional: Extensions

- Conceptually compare the same approach with `runas`, scheduled tasks or PsExec.
- Additional: in addition to `whoami`, also capture `whoami /groups`.

