# 🐍 Switch Up (Ethernet Switching)

**Course:** Cyber Security Analyst – Network Technology | **Date:** 11 August 2025

---

## Task

**Objective:**  
Simulate the core logic of a Layer 2 switch for MAC learning and forward/flood decisions in Python.

**Requirements:**

- Maintain a MAC address table learned from the source MAC and ingress port.
- Flood unknown or broadcast destinations.
- Forward known destinations to exactly one port.
- Visibly process the given 6-port test sequence.

- Output:

    - Complete Python script
    - Visible decision logic per frame
    - Continuously updated MAC table

---

## Solution

```python
frames = [
    {'in_port': 1, 'src_mac': 'AA:AA:AA: AA:AA:AA', 'dest_mac': 'BB:BB:BB:BB:BB:BB'},
    {'in_port': 2, 'src_mac': 'BB:BB:BB:BB:BB:BB', 'dest_mac': 'AA:AA:AA:AA:AA:AA'},
    {'in_port': 1, 'src_mac': 'AA:AA:AA:AA:AA:AA', 'dest_mac': 'CC:CC:CC:CC:CC:CC'},
    {'in_port': 3, 'src_mac': 'CC:CC:CC:CC:CC:CC', 'dest_mac': 'AA:AA: AA:AA:AA:AA'},
    {'in_port': 2, 'src_mac': 'BB:BB:BB:BB:BB:BB', 'dest_mac': 'CC:CC:CC:CC:CC:CC'},
    {'in_port': 4, 'src_mac': 'DD:DD:DD: DD:DD:DD', 'dest_mac': 'AA:AA:AA:AA:AA:AA'},
    {'in_port': 1, 'src_mac': 'AA:AA:AA:AA:AA:AA', 'dest_mac': 'FF:FF:FF:FF:FF:FF'},
    {'in_port': 3, 'src_mac': 'CC:CC:CC:CC:CC:CC', 'dest_mac': 'EE:EE:EE:EE:EE:EE'},
    {'in_port': 5, 'src_mac': 'AA:AA:AA:AA:AA:AA', 'dest_mac': 'BB:BB: BB:BB:BB:BB'},
    {'in_port': 2, 'src_mac': 'BB:BB:BB:BB:BB:BB', 'dest_mac': 'AA:AA:AA:AA:AA:AA'},
    {'in_port': 4, 'src_mac': 'DD:DD:DD: DD:DD:DD', 'dest_mac': 'AA:AA:AA:AA:AA:AA'},
    {'in_port': 6, 'src_mac': 'FF:FF:FF:FF:FF:FF', 'dest_mac': 'DD:DD:DD:DD:DD:DD'},
]

num_ports = 6


def process_frames(frame_list, port_count):
    mac_table = {}
    all_ports = list(range(1, port_count + 1))

    for index, frame in enumerate(frame_list, start=1):
        in_port = frame["in_port"]
        src_mac = frame["src_mac"]
        dest_mac = frame["dest_mac"]

        mac_table[src_mac] = in_port

        if dest_mac == "FF:FF:FF:FF:FF:FF" or dest_mac not in mac_table:
            out_ports = [port for port in all_ports if port != in_port]
            decision = f"Flood -> {out_ports}"
        else:
            out_port = mac_table[dest_mac]
            if out_port == in_port:
                decision = f"Filter (destination already on incoming port {in_port})"
            else:
                decision = f"Forward -> port {out_port}"

        print(f"Frame {index}: in_port={in_port}, src={src_mac}, dest={dest_mac}")
        print(f"Decision: {decision}")
        print("MAC table:")
        for learned_mac in sorted(mac_table):
            print(f"  {learned_mac} -> port {mac_table[learned_mac]}")
        print("-" * 50)


process_frames(frames, num_ports)
```

**Alternative (compact):**

```text
A switch always learns the source MAC first; only then does it decide between targeted forwarding and flooding.
```

---

## Tests

|Input 1|Input 2|Input 3|Expected|Result|✓|
|---|---|---|---|---|---|
|`unknown dest`|`frame 1`|`6 ports`|`Flood`|`yes`|✅|
|`learned dest`|`frame 2+`|`MAC table`|`Forward`|`yes`|✅|
|`broadcast`|`FF:FF:FF:FF:FF:FF`|`frame 7`|`Flood`|`yes`|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|MAC Learning|Source MAC addresses are assigned to the incoming port.|
|Flooding|Unknown or broadcast destinations are sent to all other ports.|
|Forwarding|Known destination MACs are sent only to the appropriate port.|

---

## Rules / Logic

```text
First learn the source, then decide on the destination.
Broadcast and unknown destinations are flooded.
A switch does not send a frame back to the same port on which it arrived.
```

---

## Notes

- **Important:** The script deliberately simulates only the core logic, not timeouts or STP.
- **Observation:** As soon as `AA` moves from Port 1 to Port 5, the entry in the table is updated.
- **Tip:** This exact MAC move behaviour is a good self-test for the implementation.

---

## Optional: Extensions

- Implement an ageing timer for old MAC entries.
- Model ports as access/trunk ports and extend them to be VLAN-aware.

