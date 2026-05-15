# Advanced Wireshark

## 📊 Summary based on the 80/20 principle

### 1. Effective analysis comes from filtering, reconstructing and summarising
The essence of the 80/20 principle is this: large packet captures only become useful once you’ve filtered out the irrelevant data, reassembled individual conversations and used statistics to gain a quick overview.

### 2. Step-by-step core process
1. Start with a display filter to reduce the data volume to the relevant packets.
2. Use `Find Packet` if you are searching specifically for strings, hex values or fields.
3. Use `Follow Stream` to reconstruct the actual application communication.
4. Use `Endpoints`, `Conversations` and `Protocol Hierarchy` to check who communicated with whom and how much.
5. If necessary, use `Export Objects` to extract transferred files from the traffic.

### 3. Interactive mode / Using the tool
Advanced Wireshark is all about asking questions rather than reading packet by packet. Which IP is of interest, which stream contains the login, which protocols dominate, where are the peaks or errors?

### 4. Key concepts with code examples
- **Combined filters:** Link conditions using `&&`, `||` and `!`.
- **Find Packet:** Jumps directly to content rather than just visible fields.
- **Follow Stream:** Reconstructs a comprehensible conversation history from multiple packets.
- **Statistics:** Provides an overview of endpoints, conversations, protocols and time series.

```text
ip.addr == 8.8.8.8 || ip.addr == 1.1.1.1
ip.src == 192.168.1.50 && tcp.dstport == 80
frame.len > 1000
tcp.flags.reset == 1
http.request.method == "POST"
dns.flags.rcode != 0
```

### 5. Comparison: Display Filter vs. Find Packet vs. Statistics
- **Display Filter** logically shows or hides packets.
- **Find Packet** searches specifically for a value or string within the displayed data.
- **Statistics** provides a bird’s-eye view before or after you have examined the details.

### 6. Why is this important / Benefits
These tools save a huge amount of time during incident response, malware analysis, troubleshooting and when learning about protocols, because you can move more quickly from raw traffic to the actual message.

**Quick Start Checklist**
- ☐ I can logically combine multiple filter conditions.
- ☐ I know when `Find Packet` is more helpful than simply scrolling.
- ☐ I understand what `Follow Stream` is used for.
- ☐ I am familiar with the most important statistics views in Wireshark.
- ☐ I know that files can often be exported from unencrypted traffic.

**Key point**
Wireshark only becomes truly powerful when you don’t just view traffic, but systematically filter it, reconstruct it coherently and evaluate it statistically.

---

## Table 1: Tools used
| Tool | Description |
|---|---|
| Display Filter Bar | Filters displayed packets according to rules |
| Find Packet | Searches for filters, strings or hex values |
| Follow Stream | Reconstructs complete TCP, UDP or HTTP conversations |
| Statistics Menu | Provides overviews of endpoints, protocols and traffic patterns |
| Export Objects | Extracts transferred files from the capture |

## Table 2: Technical terms
| Term | Meaning |
|---|---|
| Display Filter | Expression used to narrow down visible packets |
| Conversation | Communication between two endpoints |
| Endpoint | Device, port or address object involved in the capture |
| Protocol Hierarchy | Distribution of protocols within a capture |
| IO Graph | Temporal visualisation of traffic volumes |
| Object Export | Extraction of files from log data |

## Table 3: Key terms
| Term | Meaning |
|---|---|
| refine | refine |
| stream | data stream |
| endpoint | endpoint |
| hierarchy | hierarchy |
| extract | extract |
| sample capture | sample capture |



