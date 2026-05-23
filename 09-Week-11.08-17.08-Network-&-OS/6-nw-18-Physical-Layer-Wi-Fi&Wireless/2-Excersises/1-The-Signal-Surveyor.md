# The Signal Surveyor (Wi-Fi)

**Course:** Cyber Security Analyst – Network Technology | **Date:** 15 August 2025

---

## Task

**Objective:**  
Compare Wi-Fi metrics in Windows 11 using the GUI and CLI, and understand how they relate to the environment.

**Requirements:**

- Record the SSID, wireless type, signal strength, transmission/reception rate and channel.
- Compare four locations.
- Compare the GUI and `netsh wlan show interfaces`.

---

## Solution

```powershell
netsh wlan show interfaces
```

```text
Sample analysis:
- GUI and CLI values for SSID, wireless type, channel and signal strength should be very similar.
- Signal strength often drops significantly with greater distance or more obstacles.
- If signal quality drops, transmission and reception rates often fall as well.
- The GUI is useful for a quick check.
- For reproducible measurements, the CLI on Windows is more helpful.
```

**Important note:**

```text
The built-in Windows 11 tools usually display signal quality as a percentage,
not always RSSI or noise in dBm.
If an adapter or manufacturer’s tool displays additional dBm values, these can be added.
```

---

## Tests

|Item|Expected|✓|
|---|---|---|
|GUI vs. CLI|Values similar|✅|
|Greater distance|Signal strength worse|✅|
|Rate|Roughly correlates with signal quality|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|Signal strength|Quality of the wireless connection. Higher percentage = usually better.|
|Wireless type / PHY|e.g. 802.11n, 802.11ac, 802.11ax.|
|Tx/Rx Rate|Current transmission rate of the link.|

---

## Rules / Logic

```text
Greater distance and more obstacles degrade the signal.
A poorer signal often reduces the usable data rate.
```

---

## Notes

- **Important:** Specific measured values depend on the property, the device and the time.
- **Tip:** Always record values in quick succession at the same location via the GUI and CLI.

