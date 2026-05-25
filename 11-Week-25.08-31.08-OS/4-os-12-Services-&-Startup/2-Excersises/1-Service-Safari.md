# Service Safari (Windows Services)

**Course:** Cyber Security Analyst – OS Technology | **Date:** 28 August 2025

---

## Task

**Objective:**  
Read the status, startup type, account and dependencies of typical Windows services.

**Requirements:**

- Examine four services.
- Document the status, startup type and logon account.
- Identify dependencies and dependent services.

---

## Solution

```text
Spooler:
- Status: Running
- Startup type: Automatic
- Account: LocalSystem
- Dependency: RPCSS (also listed as `http`)
- Dependent service: none obviously listed on this system

Audiosrv:
- Status: Running
- Startup type: Automatic
- Account: NT AUTHORITY\LocalService
- Dependency: AudioEndpointBuilder (also RpcSs)
- Dependent service: e.g. RtkAudioUniversalService

BITS:
- Status: Stopped
- Startup type: Manual
- Account: LocalSystem
- Dependency: RpcSs
- Dependent service: none obviously listed on this system

WSearch:
- Status: Running
- Startup type: Automatic (Delayed)
- Account: LocalSystem
- Dependency: RPCSS (also BrokerInfrastructure)
- Dependent service: e.g. WMPNetworkSvc
```

**Alternative (compact):**

```text
Services never run in isolation – dependencies explain the sequence and consequences of failure.
```

---

## Tests

|Service|Expected|✓|
|---|---|---|
|Spooler|Status/Start/Account documented|✅|
|Audiosrv|Dependency found|✅|
|WSearch|Dependent service found|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|Startup type|Determines when a service starts.|
|Service account|The security context under which the service runs.|
|Dependencies|Which services must be available first.|

---

## Rules / Logic

```text
A service may be correctly configured but still fail to run
if a necessary dependency is missing.
```

---

## Notes

- **Important:** Dependent services may vary between systems.
- **Tip:** `sc qc <service>` and `Get-Service` complement each other well.

---

## Optional: Extensions

- Track service start via Event Viewer.
- Mark third-party services separately.


