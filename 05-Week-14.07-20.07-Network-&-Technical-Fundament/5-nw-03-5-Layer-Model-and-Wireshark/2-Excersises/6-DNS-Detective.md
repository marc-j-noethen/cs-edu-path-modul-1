# 🐍 DNS Detective (Remote Shell on Port 53)

**Course:** Cyber Security Analyst – Network Technology | **Date:** 18 July 2025

---

## Task

**Objective:**  
In `dns-remoteshell.pcap`, clearly explain what is actually happening and why the traffic does not match genuine DNS.

**Requirements:**

- Identify the suspicious stream on port 53.
- Demonstrate that the payload does not have a DNS structure.
- Explain the shell commands and responses from the stream.
- Explain why an attacker would specifically choose port 53 for this disguise.
- Output:
    - `Suspicious stream: 192.168.1.3:1396 -> 192.168.1.2:53`
    - `Content: Windows Remote Shell instead of DNS`
    - `Reason: Disguise / Firewall bypass`

---

## Solution

```python
# Inputs
service_port = 53
suspicious_payload = "Microsoft Windows XP ... C:\\>dir"
real_dns = False

# Main logic
if service_port != 53:
    print("This sample solution refers to the anomaly on TCP port 53.")
elif suspicious_payload.startswith("Microsoft Windows XP"):
    print("Port 53 is carrying an interactive Windows shell here, not DNS messages.")
elif real_dns:
    print("In that case, query/response fields, record types and DNS headers would be visible.")
else:
    print("The use of port 53 here is very likely intended for camouflage and to easily bypass firewalls.")
```

**Alternative (compact):**

```python
print("TCP/53 != DNS: visible shell commands such as dir/exit -> remote shell on port 53")
```

---

## Tests

|Input 1|Input 2|Input 3|Expected|Result|✓|
|---|---|---|---|---|---|
|`53`|`TCP`|`Payload`|`not DNS, but shell`|`not DNS, but shell`|✅|
|`dir`|`exit`|`Responses from the host`|`C:\\ directory listing`|`C:\\ directory listing`|✅|
|`23 and 80`|`same behaviour`|`Comparison`|`Port masquerading`|`Port masquerading`|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|DNS|Normal DNS communication consists of structured queries and responses, usually via UDP/53.|
|Remote Shell|Enables the execution of commands on a remote host.|
|Masquerading|Misuse of an expected port to make external traffic appear less conspicuous.|

---

## Rules / Logic

```
The port number alone does not prove the protocol.
If shell banners, `dir` and `exit` are visible on port 53, it is not DNS.
Suspicious traffic on permitted standard ports indicates masquerading.
```

---

## Notes

- **Concept:** DNS is not being "misused" here; rather, another service is simply masquerading using the same port number.
- **Syntax:** `tcp.port == 53`
- **Order is important:**
    1. Isolate port 53 traffic
    2. Check payload as plain text
    3. Interpret shell commands and responses
- **Edge Cases:**
    - TCP/53 can carry legitimate DNS traffic, e.g. zone transfers.
    - However, the DNS structure is completely missing from this capture.
    - Additionally, the same shell behaviour also appears on ports 23 and 80, which supports the disguise.
- **Tip:** The strongest piece of evidence is the Windows banner plus `C:\>dir` in the suspicious TCP/53 stream.

---

## Optional: Extensions

- Compare legitimate UDP DNS frames with the fake TCP/53 stream.
- Formulate an IDS rule for non-DNS payloads on port 53.
- Explain the role of egress filtering in such attacks.
- Collect similar tunnelling/masquerading techniques using other ports.

