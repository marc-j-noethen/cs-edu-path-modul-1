# 🐍 Firewall Fortress (Windows Firewall)

**Course:** Cyber Security Analyst - OS Technology | **Date:** 29 August 2025

---

## Task

**Objective:**  
Set up a web service on port 8888 and use Windows Defender Firewall to first block access and then allow it only for a single host.

**Requirements:**

- Start a local web service on TCP/8888.
- Completely block inbound access to port 8888.
- Then allow only the host IP as an authorised source.
- Explain the different outcome from the host’s perspective.

- Output:

    - Method for the web service on port 8888
    - Block-all rule and expected test result
    - Allow-from-host rule and reasoned result

---

## Solution

```text
Web service:
python -m http.server 8888

Test 1 - Block completely:
- Create an inbound rule for TCP port 8888 in `wf.msc`
- Action: Block the connection
- Scope: Any source

Expected result:
- `http://localhost:8888` can still be accessed quickly locally in the VM’s browser.
- Access from the host via `http://<VM-IP>:8888` fails because the incoming connection is rejected by the firewall rules.

Test 2 – Allow only host IP:
- Remove or disable the block rule
- Create a new inbound allow rule for TCP/8888
- Restrict the remote IP address to exactly the host IP (e.g. 192.168.1.177)

Expected result:
- Access from the specified host to `http://<VM-IP>:8888` works.
- Other systems remain blocked because their source IP is not included in the allow rule.

Important:
Stop the Python web server again after the exercise.
```

**Alternative (compact):**

```text
Firewall rules do not have to be simply 'on or off' – scoping by source IP is often the decisive level of hardening.
```

---

## Tests

|Input 1|Input 2|Input 3|Expected|Result|✓|
|---|---|---|---|---|---|
|`python -m http.server 8888`|`VM local`|`browser`|`service up`|`expected`|✅|
|`block inbound 8888`|`host -> VM`|`HTTP`|`blocked`|`expected`|✅|
|`allow only host IP`|`host -> VM`|`HTTP`|`allowed`|`expected`|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|Inbound Rule|Rule for incoming connections to the protected system.|
|Scope Restriction|Firewall rules can be restricted to specific source IP addresses.|
|Least Privilege Network Access|Only the exact sources and ports required are permitted.|

---

## Rules / Logic

```text
First verify the service, then block it, then permit it selectively.
An enabled port does not mean it is 'open to everyone'.
Firewall scopes are a key hardening tool.
```

---

## Notes

- **Important:** The task tests from the host’s perspective via the VM IP, not just via `localhost`.
- **Tip:** Screenshots of the rule should clearly show the port, action and remote IP scope.
- **Observation:** The very transition from globally blocked to selectively allowed is the core learning point here.

---

## Optional: Extensions

- Create the same rule once via `netsh advfirewall` or PowerShell.
- Additional exercise: allow only a specific interface profile (Private/Domain).


