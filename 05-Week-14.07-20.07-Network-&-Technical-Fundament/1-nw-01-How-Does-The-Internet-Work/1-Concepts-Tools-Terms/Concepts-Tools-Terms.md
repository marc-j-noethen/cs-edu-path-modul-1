# How Does the Internet Work

## 📊 Summary based on the 80/20 principle

### 1. The Internet is a network of networks
The core of the 80/20 principle is this: devices do not simply communicate directly with one another, but via clearly defined roles and intermediate stations. Key elements here are the client-server model, IP addresses, routers and the ISP as the gateway to the global network.

### 2. Step-by-step core process
1. A client, such as your browser, wants to request a resource.
2. The destination address is assigned to a server that provides the service.
3. The request is sent via the local network to the router.
4. The router forwards the traffic via the ISP and other routers to the internet.
5. The server responds, and the response packets find their way back to your device.

### 3. Interactive Mode / Using Tools
With two simple terminal commands, you can put the theory into practice straight away: `ping` checks reachability and approximate latency, `ifconfig` shows you your device’s local network configuration.

### 4. Key concepts with code examples
- **Network:** Two or more connected devices share data or resources.
- **Internet:** Many individual networks are linked to form a global network.
- **Client and server:** The client makes a request; the server provides the service or data.
- **IP Address:** It identifies and locates a device on the network.
- **Router:** It decides where data is forwarded to next.

```bash
ping www.google.com
ifconfig
```

### 5. Comparison: Local network vs. Internet
- A local network connects devices in a limited location such as at home or in the office.
- The Internet connects a vast number of such local and organisational networks with one another.
- On a home network, you often see private IP addresses such as `192.168.x.x` or `10.x.x.x`; on the Internet, communication takes place via public addresses.

### 6. Why is this important / Benefits
Once you have grasped these basics, you will be able to understand later topics such as DNS, HTTP, firewalls, routing, proxies and packet analysis much more quickly.

**Quick Start Checklist**
- ☐ I can explain the difference between a network and the Internet.
- ☐ I understand the roles of client and server.
- ☐ I know what an IP address is used for.
- ☐ I can roughly explain what routers and ISPs do.
- ☐ I am familiar with `ping` and `ifconfig` as basic network tools.

**Key point**
The Internet works because many individual networks are connected via addresses, routers and common protocols to form a global communication system.

---

## Table 1: Tools used
| Tool | Meaning |
|---|---|
| Terminal | Starting point for simple network diagnostics |
| ping | Checks whether a destination is reachable and how long responses take |
| ifconfig | Displays network interfaces and local IP configuration |
| Browser | Typical client for web requests to servers |

## Table 2: Technical Terms
| Term | Meaning |
|---|---|
| Network | A group of devices connected for communication |
| Internet | A global network comprising many subnetworks |
| Client | A device or programme that requests a service |
| Server | A device or programme that provides a service |
| IP Address | A unique logical address of a device on the network |
| Router | Device for forwarding traffic between networks |

## Table 3: Key vocabulary
| Term | Meaning |
|---|---|
| request | Request |
| response | Response |
| route | Path / forward |
| reachable | Accessible |
| local network | Local network |
| provider | Provider |


