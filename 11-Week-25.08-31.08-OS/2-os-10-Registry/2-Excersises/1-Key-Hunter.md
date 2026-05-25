# Key Hunter (Registry Basics)

**Course:** Cyber Security Analyst – OS Technology | **Date:** 26 August 2025

---

## Task

**Objective:**  
Read important Windows and user values directly from the registry.

**Requirements:**

- Find `ProductName` and `RegisteredOwner`.
- Read the screensaver timeout and wallpaper path.
- Document the registry paths.

---

## Solution

```text
Key 1:
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion

Values found:
- ProductName: Windows 10 Pro
- RegisteredOwner: lukasreinhardt1234@gmail.com

Key 2:
HKEY_CURRENT_USER\Control Panel\Desktop

Values found:
- ScreenSaveTimeOut: empty / not set on this system
- WallPaper: C:\Windows\Web\Wallpaper\Windows\img0.jpg
```

**Alternative (compact):**

```text
System identity is located under HKLM, user-specific desktop values under HKCU.
```

---

## Tests

|Item|Expected|✓|
|---|---|---|
|ProductName|Found|✅|
|RegisteredOwner|Found|✅|
|Wallpaper path|Found|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|HKLM|System-wide settings.|
|HKCU|Settings for the currently logged-in user.|
|Desktop key|Contains many interface and user values.|

---

## Rules / Logic

```text
System-wide data is usually located under HKLM.
User-specific interface values are often under HKCU.
```

---

## Notes

- **Important:** Values may vary significantly depending on the system.
- **Tip:** Always note down the exact path in Regedit.

---

## Optional: Extensions

- Check further desktop values such as `ScreenSaveActive`.
- Read the same data using PowerShell `Get-ItemProperty`.

