# 5-Layer Model and Wireshark

## 📊 Summary based on the 80/20 principle

### 1. The 5-layer model makes networks understandable and analysable
The essence of the 80/20 principle is that network communication is broken down into clearly distinct layers. This allows complex processes to be structured, devices from different manufacturers to be made interoperable, and faults to be systematically isolated.

### 2. Step-by-step core process
1. Data originates at the top in an application such as a browser, email programme or DNS client.
2. The transport layer adds information to ensure the data reaches the correct application on the target system.
3. The network layer adds IP information to the data to guide its path through various networks.
4. The data link layer handles local delivery within the current network segment.
5. The physical layer actually transmits the bits via cable or radio.
6. At the destination, the same process runs in reverse as decapsulation.

### 3. Interactive mode / Using the tool
Wireshark makes precisely these layers visible. The tool shows you, for a given packet, Ethernet, IP, TCP or UDP, and finally the application protocol, one after the other, so that you not only learn about encapsulation in theory, but see it in action.

### 4. Key concepts with code examples
- **Application Layer:** This is where protocols such as HTTP, DNS or SMTP operate.
- **Transport Layer:** TCP and UDP deliver data to the correct application.
- **Network Layer:** IP routes packets between different networks.
- **Data Link Layer:** Ethernet and Wi-Fi manage local transmission.
- **Physical Layer:** Here, bits are transmitted electrically, optically or via radio.

```text
Application  -> HTTP / DNS / SMTP
Transport    -> TCP / UDP
Network      -> IP / ICMP
Data Link    -> Ethernet / Wi-Fi / ARP
Physical     -> Cable / Fibre / Radio Signals
```

### 5. Comparison: OSI Model vs. 5-Layer TCP/IP Model
- The OSI model is more theoretical and is divided more finely into 7 layers.
- The 5-layer model is more practical and is more closely aligned with real-world internet communication.
- For day-to-day analysis and troubleshooting, the 5-layer model is often quicker to use.

### 6. Why is this important / Advantages
The layered model is the roadmap for every subsequent networking topic. Without this basic framework, protocol analysis, packet capture, troubleshooting and security assessment are significantly more difficult.

**Quick-start checklist**
- ☐ I know the five layers of the model in the correct order.
- ☐ I can explain encapsulation and decapsulation in broad terms.
- ☐ I know why layering facilitates interoperability and troubleshooting.
- ☐ I can classify Wireshark as a protocol analyser.
- ☐ I know that Wireshark displays headers and protocols layer by layer.

**Mnemonic**
If you want to understand network communication, you have to think in terms of layers, because that is exactly how data is constructed, transported and analysed.

---

## Table 1: Tools used
| Tool | Description |
|---|---|
| Wireshark | Network protocol analyser for capturing and examining packets |
| Browser | Generates typical application layer communication such as HTTP/HTTPS |
| Network Interface | Interface where Wireshark captures traffic |
| ChmodBPF | macOS component enabling Wireshark to perform live capture without root privileges |

## Table 2: Technical Terms
| Term | Meaning |
|---|---|
| Application Layer | Layer for application-oriented network protocols |
| Transport Layer | Layer for end-to-end communication between processes |
| Network Layer | Layer for logical addressing and routing |
| Data Link Layer | Layer for local delivery within a network segment |
| Physical Layer | Layer for the physical transmission of bits |
| Encapsulation | Adding headers and metadata per layer |

## Table 3: Key terms
| Term | Meaning |
|---|---|
| layer | Layer |
| packet | Packet |
| frame | Frame |
| header | Header |
| payload | Payload |
| capture | Capture |


