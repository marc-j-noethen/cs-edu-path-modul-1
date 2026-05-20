# 🐍 Router Rendezvous

**Course:** Cyber Security Analyst – Network Technology | **Date:** 04 August 2025

---

## Task

**Goal:**  
Configure Kali as a two-legged router between the host network and an internal Windows subnet, then explain why the host still needs a route to the internal network.

**Requirements:**

- Assign Kali one IP in `192.168.56.0/24` and one in `192.168.1.0/24`.

- Configure Windows with `192.168.1.10/24` and gateway `192.168.1.1`.

- Enable IPv4 forwarding on Kali.

- Add a host-side static route for the internal subnet via Kali.

- Output:
    
    - `Submit the final result in the exact format requested by the task.`
        
    - `A reviewer-readable final result`
        
    - `The submission artifact requested by the task`

---

## Solution

```text
# Inputs
context = 'Local analysis or lab environment'
objective = 'Configure Kali as a two-legged router between the host network and an internal Windows subnet, then explain why the host still needs a route to the internal network.'
evidence = 'Submit the final result in the exact format requested by the task.'

# Main logic
Example Kali configuration:

sudo ip addr add 192.168.56.1/24 dev eth0
sudo ip addr add 192.168.1.1/24 dev eth1
sudo ip link set eth0 up
sudo ip link set eth1 up
sudo sysctl -w net.ipv4.ip_forward=1

Windows internal settings:

IP address: 192.168.1.10
Mask:       255.255.255.0
Gateway:    192.168.1.1

Host-side static route (replace `<HOST_GATEWAY_INTERFACE_IP>` only if your host needs the explicit next hop syntax):

route add 192.168.1.0 mask 255.255.255.0 192.168.56.1

Direct answer:

Kali already knows both directly connected networks, but the host does not. The host only knows its own local subnet (`192.168.56.0/24`) and its default routes. Without a specific route for `192.168.1.0/24`, the host has no instruction that packets for the Windows subnet should be sent to Kali, so the traffic would never reach the internal network correctly.
```

**Alternative (compact):**

```text
A router can connect two networks only if each endpoint knows that the router is the next hop for the non-local subnet.
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
