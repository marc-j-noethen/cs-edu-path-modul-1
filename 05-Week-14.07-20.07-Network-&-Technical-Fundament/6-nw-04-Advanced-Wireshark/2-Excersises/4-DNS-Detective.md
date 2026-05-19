# 🐍 DNS Detective (Advanced Wireshark)

**Course:** Cyber Security Analyst - Network Technology | **Date:** 19 July 2025

---

## Task

**Objective:**  
Explain what is actually happening in `dns-remoteshell.pcap` and why it was implemented in this way.

**Requirements:**

- Identify the clues from the filename and port usage.
- Distinguish normal DNS from the actual payload.
- Describe the suspicious protocol behaviour.
- Explain the purpose of the obfuscation.

- Output:

    - what is actually being transmitted in the capture
    - why port 53 was deliberately used
    - why this is not normal DNS

---

## Solution

```text
Findings:
The capture does not show a regular DNS dialogue as the actual main content,
but rather an interactive remote shell that was tunnelled via TCP port 53.

Why is this suspicious?
- In practice, DNS primarily uses UDP/53; TCP/53 is only used for special cases such as large responses or zone transfers.
- A complete Windows command-line dialogue appears in the payload:
  `Microsoft Windows XP [Version 5.1.2600]` followed by `C:\>`.
- The dominant connection is `192.168.1.3:1396 -> 192.168.1.2:53`, i.e. shell traffic on a port where an analyst would initially expect DNS.

Why was this done?
This is classic camouflage or firewall bypass.
Many environments allow outbound DNS traffic quite liberally.
An attacker can therefore run a backdoor or remote shell over port 53 to masquerade as legitimate DNS traffic and be less likely to attract attention.

In short:
`dns-remoteshell.pcap` is not a "broken DNS", but a remote shell channel deliberately disguised on port 53.
```

**Alternative (compact):**

```text
The filename pretty much says it all: a remote shell that merely pretends to be DNS.
```

---

## Tests

|Input 1|Input 2|Input 3|Expected|Result|✓|
|---|---|---|---|---|---|
|`Port 53`|`TCP session`|`Payload`|`atypical for DNS`|`suspicious`|✅|
|`Windows XP Banner`|`C:\>`|`interactive`|`shell detectable`|`yes`|✅|
|`UDP/53`|`genuine DNS packets`|`comparison`|`distinguishable from normal DNS`|`yes`|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|Tunneling|Another protocol or shell traffic is hidden within a permitted channel.|
|Evasion|Attackers disguise traffic via commonly permitted ports to bypass security controls.|
|Protocol Misuse|A port is used even though the actual payload does not match the expected protocol.|

---

## Rules / Logic

```text
Port numbers alone do not prove a protocol.
If the payload does not look like DNS, the assumption 'Port 53 = DNS' must be questioned.
Interactive banners and prompts are strong indicators of shell access.
```

---

## Notes

- **Important:** The capture also contains genuine DNS traffic; however, the conspicuous main session is TCP/53 with shell content.
- **Observation:** The Windows XP banner in the payload is the key clue.
- **Tip:** In Wireshark, first look for `tcp.port == 53` and then check the ASCII payload.

---

## Optional: Extensions

- Reconstruct the session packet by packet as a pseudo-terminal.
- Compare what a DNS tunnel for file exfiltration would look like instead of an interactive shell.

