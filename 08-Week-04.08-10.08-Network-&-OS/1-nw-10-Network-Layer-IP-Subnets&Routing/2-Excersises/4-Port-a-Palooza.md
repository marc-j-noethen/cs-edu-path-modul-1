# 🐍 Port-a-Palooza 

**Course:** Cyber Security Analyst – Network Technology | **Date:** 04 August 2025

---

## Task

**Goal:**  
Use Kali as a Linux NAT router so an internal Windows VM reaches a host-side web server, then explain why the host sees Kali’s IP instead of the Windows address.

**Requirements:**

- Configure the internal `10.10.10.0/24` network and the external `192.168.56.0/24` network.

- Enable IP forwarding on Kali.

- Apply MASQUERADE/PAT on the external interface.

- Explain the translated source IP and the reason port translation is still useful for one client.

- Output:
    
    - `Submit the final result in the exact format requested by the task.`
        
    - `A reviewer-readable final result`
        
    - `The submission artifact requested by the task`

---

## Solution

```text
# Inputs
context = 'Local analysis or lab environment'
objective = 'Use Kali as a Linux NAT router so an internal Windows VM reaches a host-side web server, then explain why the host sees Kali’s IP instead of the Windows address.'
evidence = 'Submit the final result in the exact format requested by the task.'

# Main logic
Example Kali setup:

sudo ip addr add 10.10.10.1/24 dev eth0
sudo ip addr add 192.168.56.1/24 dev eth1
sudo ip link set eth0 up
sudo ip link set eth1 up
sudo sysctl -w net.ipv4.ip_forward=1

sudo iptables -t nat -A POSTROUTING -o eth1 -j MASQUERADE
sudo iptables -A FORWARD -i eth0 -o eth1 -j ACCEPT
sudo iptables -A FORWARD -i eth1 -o eth0 -m state --state ESTABLISHED,RELATED -j ACCEPT

Direct answers:

1. Source IP seen by the host web server: Kali’s external address on `192.168.56.0/24`, typically `192.168.56.1`.
2. PAT is still useful with only one internal client because that client can open multiple simultaneous connections. Source-port rewriting keeps those flows distinct on the shared translated IP.
3. PAT hides the private address `10.10.10.10` from the external side while preserving enough uniqueness to map replies back to the correct internal session.
```

**Alternative (compact):**

```text
The host sees the router’s outside IP, not the inside client’s private IP.
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
