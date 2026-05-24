# Networking Modules (Imports)

**Course:** Cyber Security Analyst – OS Technology | **Date:** 22 August 2025

---

## Task

**Objective:**  
Identify and classify network-related import modules of `ping.exe`.

**Requirements:**

- Name two network-related DLLs.
- Briefly explain one function per DLL.
- Assess the consequences of a DLL failure or manipulation.

---

## Solution

```text
File:
C:\Windows\System32\ping.exe

Two relevant modules:
1. IPHLPAPI.DLL
   - Example function: IcmpSendEcho2Ex
   - Purpose: Sends ICMP echo requests and receives responses. This is exactly what `ping.exe` needs for its core functionality.

2. WS2_32.dll
   - Example function: GetAddrInfoW
   - Purpose: Resolves hostnames into addresses so that `ping` can process names such as `example.com` rather than just raw IPs.

What happens if a module cannot be loaded?
- Without IPHLPAPI.DLL, `ping` would be unable to send ICMP requests correctly.
- Without WS2_32.dll, name resolution and socket-related network functionality would be compromised.

What would be possible if an attacker were to manipulate it?
- Falsify or redirect responses
- Covertly swap targets
- Introduce network monitoring or backdoor behaviour into many programmes that use the same DLL
```

**Alternative (compact):**

```text
Imports reveal which external capabilities a programme requires at runtime.
```

---

## Tests

|Item|Expected|✓|
|---|---|---|
|DLL 1|network-related|✅|
|DLL 2|network-related|✅|
|Security assessment|Exploit identified|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|Import Table|List of external functions used by an EXE.|
|ICMP API|Required for ping functionality.|
|Name Resolution|Required for hostnames instead of bare IP addresses.|

---

## Rules / Logic

```text
If an import is missing or has been tampered with, the function that depends on it will be affected.
```

---

## Notes

- **Tip:** Network DLLs are often a quick indicator of an EXE’s behaviour.
- **Concept:** Supply chain and DLL hijacking risks stem precisely from this.

---

## Optional: Extensions

- Analyse further imports such as `FreeAddrInfoW` or `IcmpCreateFile`.
- Compare other network tools such as `tracert.exe`.

