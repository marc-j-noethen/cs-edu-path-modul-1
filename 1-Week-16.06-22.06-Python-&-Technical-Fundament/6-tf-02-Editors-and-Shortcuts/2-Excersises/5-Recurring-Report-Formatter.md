# 🖥️ Recurring Report Formatter (Macro Transformation)

**Course:** Cyber Security Analyst - Technical Foundation Basics | **Date:** 20 June 2025

---

## Task

**Objective:** Build a repeatable Windows-friendly workflow in Sublime Text to transform semicolon-separated data into the target report format.

---

## Solution

### Environment
```text
OS: Windows 11
Editor: Sublime Text
```

### Format X (Input)
```text
Hardware;Laptop;Operational
Software;Antivirus;Needs Update
Network;Firewall;Configured
Access;VPN;Enabled
Hardware;Monitor;Operational
Software;OS;Patched
```

### Format Y (Target)
```text
* **Hardware:** Laptop (Status: Operational)
* **Software:** Antivirus (Status: Needs Update)
* **Network:** Firewall (Status: Configured)
* **Access:** VPN (Status: Enabled)
* **Hardware:** Monitor (Status: Operational)
* **Software:** OS (Status: Patched)
```

---

## Recommended Method: Regex Find & Replace

### Procedure

```text
1. Ctrl+H
2. Alt+R
3. Find:    ^(.+);(.+);(.+)$
4. Replace: * **$1:** $2 (Status: $3)
5. Replace All
```

### Regex explained

| Pattern | Meaning |
|---------|-----------|
| `^` | Start of line |
| `(.+)` | One or more characters, captured as a group |
| `;` | Literal semicolon separator |
| `$` | End of line |
| `$1`, `$2`, `$3` | Backreferences to the captured groups |

**Transformation:**
```text
Hardware;Laptop;Operational
   $1      $2       $3

-> * **$1:** $2 (Status: $3)
-> * **Hardware:** Laptop (Status: Operational)
```

---

## Optional Method: Record as a macro

```text
1. Ctrl+Q                  -> Start recording
2. Perform the regex replacement workflow once
3. Ctrl+Q                  -> Stop recording
4. Ctrl+Shift+Q            -> Play macro
```

---

## Result

### Before (Format X)
```text
Hardware;Laptop;Operational
Software;Antivirus;Needs Update
Network;Firewall;Configured
Access;VPN;Enabled
Hardware;Monitor;Operational
Software;OS;Patched
```

### After (Format Y)
```text
* **Hardware:** Laptop (Status: Operational)
* **Software:** Antivirus (Status: Needs Update)
* **Network:** Firewall (Status: Configured)
* **Access:** VPN (Status: Enabled)
* **Hardware:** Monitor (Status: Operational)
* **Software:** OS (Status: Patched)
```

---

## Shortcut overview

| Shortcut | Action |
|----------|--------|
| `Ctrl+Q` | Start / stop macro recording |
| `Ctrl+Shift+Q` | Play macro |
| `Ctrl+H` | Find & Replace |
| `Alt+R` | Regex toggle |

---

## Notes

- **Learned:** Regex Find & Replace, capture groups, and reusable editing workflows.
- **Best practice:** Regex is the most truthful and reproducible solution for this exact input pattern.
- **Important:** The transformed output above is deterministic and uses a Windows-friendly workflow.
