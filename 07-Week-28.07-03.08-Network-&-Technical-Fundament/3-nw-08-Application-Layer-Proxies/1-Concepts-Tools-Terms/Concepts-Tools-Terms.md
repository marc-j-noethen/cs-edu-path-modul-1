# Application Layer Proxies

## 📊 Summary based on the 80/20 principle

### 1. A proxy acts as an intermediary between the client and the server
The essence of the 80/20 principle is this: a proxy does not merely pass on requests, but can also check, filter, cache, anonymise or distribute them to other systems. The crucial factor is whose side it is on and what purpose it serves.

### 2. Step-by-step core process
1. A client sends its request not directly to the target server, but to the proxy.
2. The proxy evaluates or modifies the request according to a set of rules.
3. The proxy then forwards the request to the actual server.
4. The response travels back along the same route via the proxy to the client.
5. Depending on the type of proxy, IP information may be hidden, disclosed, cached or redistributed in the process.

### 3. Interactive mode / Tool usage
In practice, you often encounter proxies without realising it: in school or company networks, in web filters, in front of web servers, or in your system’s network settings as HTTP, HTTPS or SOCKS proxies.

### 4. Key concepts with code examples
- **Forward proxy:** Operates on behalf of multiple clients and controls their external access.
- **Reverse proxy:** Acts on behalf of servers and protects or distributes incoming traffic.
- **Transparent proxy:** Intercepts traffic without the client having to configure anything.
- **Anonymity levels:** Determine whether a proxy reveals its own identity and the client’s real IP address.

```text
Client -> Forward Proxy -> Server
Client <- Forward Proxy <- Server

Internet User -> Reverse Proxy -> Backend Server
```

### 5. Comparison: Forward Proxy vs. Reverse Proxy
- A **Forward Proxy** sits in front of clients and controls outgoing traffic.
- A **reverse proxy** sits in front of servers and protects or distributes incoming requests.
- Both mediate traffic, but they address different security and architectural issues.

### 6. Why is this important / Benefits
Proxies are central to cybersecurity and infrastructure because they can visibly control access paths, distribute load, cache content and shield systems from direct exposure.

**Quick Start Checklist**
- ☐ I can explain why a proxy acts as an intermediary.
- ☐ I know the typical reasons for using proxies: security, filtering, caching, anonymity and load balancing.
- ☐ I understand the difference between a forward and a reverse proxy.
- ☐ I know that not every proxy automatically offers true anonymity.
- ☐ I can broadly distinguish between HTTP/HTTPS proxies and SOCKS proxies.

**Key point**
A proxy is not simply a detour, but a control point where network traffic can be protected, filtered, concealed or distributed.

---

## Table 1: Tools used
| Tool | Meaning |
|---|---|
| HTTP Proxy | Mediates and controls web traffic |
| HTTPS Proxy | Mediates encrypted web traffic, often via a tunnel |
| SOCKS Proxy | More general-purpose proxy for various protocol types |
| System Proxy Settings | Location for configuring proxy usage on the device |

## Table 2: Technical Terms
| Term | Meaning |
|---|---|
| Proxy Server | Intermediate station for network traffic between client and server |
| Forward Proxy | Client-side proxy for outgoing requests |
| Reverse Proxy | Proxy on the server side for incoming requests |
| Transparent Proxy | Proxy that intercepts traffic without active client configuration |
| Caching | Caching of frequently requested content |
| Load Balancing | Distribution of incoming requests across multiple servers |

## Table 3: Key terms
| Term | Meaning |
|---|---|
| intermediary | intermediary |
| filtering | filtering |
| caching | caching |
| anonymity | anonymity |
| bypass | bypass |
| destination server | destination server |


