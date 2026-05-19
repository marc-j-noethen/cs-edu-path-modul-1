## 📊 Summary based on the 80/20 principle

### **What is DNS? The internet phone book**

DNS (Domain Name System) translates **human-readable domain names** (such as `google.com`) into **machine-readable IP addresses** (such as `142.250.180.142`) . Without DNS, we would all have to memorise IP addresses – practically impossible!

**Analogy**: DNS is like a telephone directory – you look up a name and get the telephone number (IP address).

### **The DNS hierarchy: An inverted tree**

DNS is organised hierarchically, from top to bottom:

1. **Root Zone (.)** – The root of the system (hundreds of servers worldwide)
2. **TLDs (Top-Level Domains)** – Extensions such as `.com`, `.org`, `.de`
3. **SLDs (Second-Level Domains)** – Your registered domain, such as `google` in `google.com`
4. **Subdomains** – Further subdivisions such as `mail.google.com`

**Example**: `www.google.com.` = Subdomain (www) + SLD (google) + TLD (com) + Root (.)

**Important**: This structure makes DNS scalable – no single instance needs to know everything!

### **How does a DNS query work? The 8-step process**

When you enter `www.example.com`:

1. **Local cache** – Computer checks its own memory
2. **Recursive resolver** – Your ISP or public DNS (8.8.8.8, 1.1.1.1) takes over
3. **Root Server** – “Where can I find .com?”
4. **TLD Server** – “The .com server knows where example.com is”
5. **Authoritative Server** – “example.com’s server knows www.example.com”
6. **Final response** – IP address is returned
7. **Caching** – Result is stored (note TTL)
8. **Connection** – Browser connects to the IP address

**Time taken**: Usually just milliseconds!

### **The most important DNS record types**

|Record type|Meaning|Example|
|---|---|---|
|**A**|IPv4 address|`google.com` → `142.250.180.142`|
|**AAAA**|IPv6 address|`google.com` → `2a00:1450:4005:80a::200e`|
|**CNAME**|Alias/Reference|`www.example.com` → `example.com`|
|**MX**|Mail server|Priority email delivery|
|**NS**|Name server|Delegation to responsible servers|
|**TXT**|Text information|Domain verification, email security|

**Note**: **A** and **AAAA** are the cornerstones – they provide the actual IP addresses!

### **DNS caching and TTL: Speed vs. timeliness**

**Caching** temporarily stores DNS responses (in the browser, operating system, resolver) to speed up repeated queries.

**TTL (Time-To-Live)** determines how long an entry may be cached:

- **Short TTL** (60–300 sec.) → Changes visible quickly, but increased server load
- **Long TTL** (86,400 sec. = 24h) → Less load, but changes take longer

**Finding the right balance**: Stable domains → long TTL; frequent changes → short TTL

### **Practical test (Windows configuration)**

Open the **Command Prompt** or **PowerShell**:

```cmd
ping -n 1 google.com
```

→ Displays the resolved IP address

```cmd
ping -n 1 heise.de
```

→ Different domain, different IP

```cmd
ping -n 1 non-existent-domain-12345.com
```

→ Error: "Ping request could not find host" = DNS resolution failed

**Additional tools for Windows**:

```cmd
nslookup google.com
```

→ Displays detailed DNS information

### **Public DNS resolvers: Alternative to ISP DNS**

Instead of your internet service provider’s DNS server, you can use public resolvers:

- **Google**: `8.8.8.8` and `8.8.4.4`
- **Cloudflare**: `1.1.1.1` and `1.0.0.1`

**Advantages**: Often faster, more privacy, more reliable

**Disadvantages**: External provider sees your DNS queries

### **Key message**

DNS is the **invisible backbone of the internet** – a distributed, hierarchical system that translates human-friendly names into machine-readable addresses in milliseconds. Without DNS, the modern internet would be practically unusable!

**Recursive** (your resolver does the work) and **iterative** (resolver queries step by step) work together to answer every query in a fraction of a second.

---

## Summary table

| **Category**        | **Details**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Tools used**      | • **Terminal**: Command-line tool (macOS: Terminal; Windows: Command Prompt, PowerShell, Windows Terminal)<br>• **ping**: Network diagnostic tool for testing connections (available on both systems)<br>• **nslookup**: DNS lookup tool (Windows & macOS)<br>• **dig**: Advanced DNS query (pre-installed on macOS; Windows: via BIND installation)<br>• **hosts file**: Local name resolution (macOS: `/etc/hosts`; Windows: `C:\Windows\System32\drivers\etc\hosts`)<br>• **Spotlight**: Search function (macOS: Cmd+Space; Windows: Windows key for search)<br>• **Public DNS resolvers**: Google DNS (8.8.8.8), Cloudflare (1.1.1.1)<br>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **Technical terms** | • **DNS** (Domain Name System): Internet domain name resolution system<br>• **IP address**: Numerical network address (IPv4: e.g. 142.250.180.142; IPv6: e.g. 2a00:1450:4005:80a::200e)<br>• **Root Zone**: Top level of the DNS hierarchy<br>• **TLD** (Top-Level Domain): Domain extensions such as .com, .org, .de<br>• **SLD** (Second-Level Domain): Registered domain such as "google" in google.com<br>• **Subdomain**: Sub-section of a domain (e.g. mail.google.com)<br>• **FQDN** (Fully Qualified Domain Name): Full domain name ending with a full stop<br>• **Recursive Resolver**: DNS server that processes complete queries<br>• **Authoritative Name Server**: DNS server containing official domain information<br>• **Recursive Query**: A query in which the resolver handles the full resolution<br>• **Iterative Query**: A step-by-step query through various DNS server levels<br>• **DNS Cache**: Temporary storage for DNS queries<br>• **TTL** (Time-To-Live): Validity period of DNS entries in seconds<br>• **DNS Records**: Records stored on DNS servers<br>• **Reverse DNS Lookup**: Reverse resolution from IP address to hostname<br> |
| **Key vocabulary**  | • **Name resolution**: The process of translating domain names into IP addresses<br>• **Hierarchy**: The tree structure of the DNS system<br>• **Delegation**: The transfer of authority to subordinate servers<br>• **Scalability**: The system’s ability to grow<br>• **Resilience**: Reliability and robustness<br>• **Propagation**: Dissemination of DNS changes across the internet<br>• **A Record**: IPv4 address mapping<br>• **AAAA Record** (Quad-A): IPv6 address mapping<br>• **CNAME Record**: Alias name for a domain<br>• **MX Record**: Mail server mapping<br>• **NS Record**: Name server delegation<br>• **TXT Record**: Text information (SPF, DKIM, DMARC)<br>• **PTR Record**: Pointer for reverse DNS<br>• **ISP** (Internet Service Provider): Internet service provider<br>• **Milliseconds**: Unit of time for DNS queries<br>• **Priority value**: Order of precedence for MX records<br>• **Domain registration**: Registration of a domain<br>• **Hosts file**: Local manual name resolution<br>                                                                                                                                          |
