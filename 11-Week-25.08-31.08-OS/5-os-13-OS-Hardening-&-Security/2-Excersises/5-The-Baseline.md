# 🐍 The Baseline (Security Baselines)

**Course:** Cyber Security Analyst - OS Technology | **Date:** 29 August 2025

---

## Task

**Objective:**  
Select two different hardening recommendations from an official Windows security baseline, explain them and describe how to implement them.

**Requirements:**

- Cover two different security areas.
- Explain each recommendation in terms of risk/benefit, implementation and verification.
- Use an official baseline as a reference framework.
- Formulate the answer as an actionable sample submission.

- Output:

    - two specific hardening recommendations
    - implementation steps
    - verification ideas and expected impact

---

## Solution

```text
Framework used:
Microsoft Security Baseline for Windows 11

Recommendation 1:
- Title: Apply UAC restrictions to local accounts on network logons
- Recommended state: Enabled
- Benefit:
  Local administrator accounts should not operate with full admin rights unfiltered when accessing the network.
  This reduces the risk of lateral movement and remote abuse of local accounts.
- Implementation:
  Local Security Policy / Group Policy ->
  Security Options ->
  `User Account Control: Apply UAC restrictions to local accounts on network logons` -> Enabled
- Verification:
  Check the policy in Local Security Policy or confirm via Registry/GPO status.
  Expected effect: Network logons with local admin accounts will have more restrictive token handling.

Recommendation 2:
- Title: Configure SMB v1 client driver
- Recommended state: Disable driver
- Benefit:
  SMBv1 is obsolete and has historically been associated with serious security issues.
  Disabling it reduces the attack surface for old, insecure file-sharing protocols.
- Implementation:
  Windows Features or PowerShell:
  `Disable-WindowsOptionalFeature -Online -FeatureName SMB1Protocol -NoRestart`
  or corresponding baseline/GPO setting for the SMBv1 client driver
- Verification:
  `Get-WindowsOptionalFeature -Online -FeatureName SMB1Protocol`
  or GUI check in Windows Features.
  Expected outcome: The system no longer offers the old SMBv1 client path.
```

**Alternative (compact):**

```text
A good baseline does not merely reduce ‘some sort of risk’, but specifically targets attack vectors such as insecure network logins and outdated protocols.
```

---

## Tests

|Input 1|Input 2|Input 3|Expected|Result|✓|
|---|---|---|---|---|---|
|`UAC network logons`|`Enabled`|`policy review`|`hardened`|`yes`|✅|
|`SMBv1`|`disabled`|`feature status`|`hardened`|`yes`|✅|
|`implementation`|`verification`|`expected impact`|`all covered`|`yes`|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|Security Baseline|A pre-checked set of recommended security settings for an operating system.|
|Attack Surface Reduction|Measures that disable unnecessary or obsolete attack vectors.|
|Verification|Hardening is only complete once the setting has been verifiably applied.|

---

## Rules / Logic

```text
Hardening recommendations should always consider risk, implementation and verification together.
Different security areas provide a stronger overall baseline than two variants of the same idea.
Outdated protocols and overly privileged network logins are classic, worthwhile hardening targets.
```

---

## Notes

- **Important:** The task explicitly allows the use of Microsoft’s own security baselines as well as CIS.
- **Tip:** For each recommendation, always consider: Where is it applied, how is it verified, and what specific improvements does it bring?
- **Observation:** Good baseline work is much closer to real-world system hardening than to purely theoretical learning.

---

## Optional: Extensions

- Additionally, include an audit policy recommendation from the same baseline.
- Automatically check both settings later using a PowerShell script.

