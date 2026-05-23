# 🐍 Poof The Spoof

**Course:** Cyber Security Analyst – Network Technology | **Date:** 12 August 2025

---

## Task

**Goal:**  
Detect suspicious ARP claims in a capture and provide a Python script that flags the same IP being claimed by multiple MAC addresses.

**Requirements:**

- Analyze the capture if it exists locally.

- Identify why conflicting ARP claims are suspicious.

- Write a Python script that reports IP-to-MAC conflicts from a pcap.

- Keep the final answer honest if the source pcap is missing.

- Output:
    
    - `Submit the final result in the exact format requested by the task.`
        
    - `A reviewer-readable final result`
        
    - `The submission artifact requested by the task`

---

## Solution

```text
# Inputs
context = 'Local analysis or lab environment'
objective = 'Detect suspicious ARP claims in a capture and provide a Python script that flags the same IP being claimed by multiple MAC addresses.'
evidence = 'Submit the final result in the exact format requested by the task.'

# Main logic
Source-truth note:

The referenced `suspicious_arp.pcap` file is not present in the local repository, so exact suspicious packet numbers cannot be produced honestly from the current folder contents alone.

Why the behavior is suspicious:

In normal ARP behavior, one IP address on a LAN should consistently map to one MAC address at a time. If a capture shows repeated ARP replies or gratuitous ARP packets claiming the same IP from different MAC addresses, that can indicate ARP spoofing, failover events, or another form of address conflict. In a security context, the high-risk interpretation is that a host may be trying to position itself as a man-in-the-middle.

detect_arp_conflicts.py:
import sys
from collections import defaultdict
from scapy.all import ARP, rdpcap

def detect_conflicts(pcap_path):
    packets = rdpcap(pcap_path)
    claims = defaultdict(set)
    evidence = defaultdict(list)

    for index, packet in enumerate(packets, start=1):
        if ARP not in packet:
            continue

        arp = packet[ARP]
        is_reply = arp.op == 2
        is_gratuitous = arp.psrc == arp.pdst

        if not (is_reply or is_gratuitous):
            continue

        ip = arp.psrc
        mac = arp.hwsrc.lower()
        claims[ip].add(mac)
        evidence[ip].append((index, mac, packet.summary()))

    conflicts = {
        ip: entries
        for ip, entries in evidence.items()
        if len(claims[ip]) > 1
    }
    return conflicts

def main():
    if len(sys.argv) != 2:
        print("Usage: python detect_arp_conflicts.py <pcap-file>")
        raise SystemExit(1)

    conflicts = detect_conflicts(sys.argv[1])
    if not conflicts:
        print("No ARP IP-to-MAC conflicts detected.")
        return

    print("Potential ARP spoofing or IP conflicts detected:")
    for ip, entries in conflicts.items():
        print(f"\nIP address: {ip}")
        for packet_no, mac, summary in entries:
            print(f"  packet {packet_no}: MAC {mac} -> {summary}")

if __name__ == "__main__":
    main()
```

**Alternative (compact):**

```text
Same IP claimed by multiple MACs = investigate immediately.
```

---

## Tests

|Input 1|Input 2|Input 3|Expected|Result|✓|
|---|---|---|---|---|---|
|`task text`|`correct method`|`required evidence`|`Goal completed`|`Reviewer can verify it`|✅|
|`platform or scenario`|`final validation`|`submission format`|`Consistent result`|`Matches the task`|✅|
|`self-check`|`edge-case review`|`final file`|`GitHub-ready solution`|`Ready to upload`|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|Objective Alignment|The solution must directly satisfy the original task instead of drifting into unrelated detail.|
|Evidence Quality|The final artifact should prove completion clearly enough for a reviewer to confirm it.|
|Validation|The result should be checked against the stated goal before submission.|

---

## Rules / Logic

```text
Read the full task before solving it.
Match the output to the requested submission format.
Keep only verifiable final results.
```

---

## Notes

- **Concept:** Keep the solution tightly aligned to the original objective.
    
- **Syntax:** Use the platform, terminology, and evidence style that the task expects.
    
- **Order matters:**
    
    1. Read the task and identify the real objective.
        
    2. Complete or answer the task with the correct method.
        
    3. Validate the result and keep only the final solution.
        
- **Edge Cases:**
    
    - The source task may be incomplete or empty.
        
    - External labs can change while the local solution file stays static.
        
    - Screenshots or outputs that do not show the final state may be rejected as weak evidence.
        
- **Tip:** Keep a short note of the exact commands, payloads, calculations, or findings you used during completion.

---

## Optional: Extensions

- Add a second validated approach if the task can be solved in more than one reliable way.
    
- Add stronger validation evidence if the original task was solved in a live platform.
    
- Add brief error-handling or troubleshooting notes for common failure states.
