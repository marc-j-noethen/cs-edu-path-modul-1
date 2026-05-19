# Mission Telnet (Telnet)

**Course:** Cyber Security Analyst – Network Technology | **Date:** 28 July 2025

---

## Task

**Objective:**  
Read Telnet traffic in Wireshark and understand plain text and control sequences.

**Requirements:**

- Connect to `telehack.com`.
- Enter commands and monitor the TCP stream.
- Identify plain text and IAC control sequences.

---

## Solution

```text
Answer 1:
Yes. User input and server output were readable as plain text in the TCP stream.
This is precisely the main reason why Telnet is considered insecure today.

Answer 2:
Telnet control sequences with IAC (`Interpret As Command`, byte 0xFF) are not used for the payload,
but for protocol control, e.g. for option negotiation, interrupts or special keys.
In the stream, they typically appear as short non-printable sequences.
They separate control information from normal user data.
```

**Alternative (compact):**

```text
Telnet transmits content in a readable format.
IAC controls the protocol itself.
```

---

## Tests

|Item|Expected|✓|
|---|---|---|
|Plain text visible|Commands and responses readable|✅|
|Control bytes visible|Short special sequences present|✅|
|Security rating|Telnet is insecure|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|Plaintext protocol|No encryption, everything is directly readable.|
|IAC|Controls option negotiation and signals.|
|TCP stream|Shows the reconstructed data stream of a connection.|

---

## Rules / Logic

```text
Payload = readable text.
Control data = IAC-based commands.
No encryption -> high risk of interception.
```

---

## Notes

- **Concept:** Telnet is good for teaching purposes, but practically obsolete.
- **Tip:** In Wireshark, `Follow TCP Stream` is the quickest way.

---

## Optional: Extensions

- Compare Telnet directly with SSH.
- Read up on IAC commands from RFC 854 in more detail.

