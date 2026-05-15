# 🌐 Global Ping Expedition

**Course:** Cyber Security Analyst – Network Technology | **Date:** 14 July 2025

---

## Task

**Objective:** To investigate the relationship between geographical distance, the number of network hops and latency using traceroute to various global locations.

---

## Environment

```
Location:       Germany (Halberstadt, Saxony-Anhalt)
Tool:           tracert (Windows Command Prompt)
ISP:            Tele Columbus AG
Local IP:      192.168.0.92
```

---

## Procedure

### Test 1: Europe – United Kingdom
**Target:** www.ox.ac.uk (University of Oxford)

```bash
tracert www.ox.ac.uk
```

**Output:**
```
Tracing route to www.ox.ac.uk.cdn.cloudflare.net [104.20.34.13]
via a maximum of 30 hops:

  1     9 ms     2 ms     1 ms  192.168.0.1
  2     *        *        *     Request timed out.
  3     9 ms     9 ms     9 ms  172.17.166.37
  4    15 ms     8 ms     9 ms  172.17.166.21
  5    18 ms     8 ms     9 ms  172.17.80.161
  6     9 ms     8 ms     8 ms  172.17.80.205
  7    11 ms     9 ms    10 ms  172.17.80.206
  8    22 ms    10 ms    10 ms  80.64.181.65
  9    22 ms    13 ms    14 ms  109.104.59.228
 10    24 ms    23 ms    34 ms  85.239.113.148
 11    14 ms    12 ms    21 ms  104.20.34.13
```

### Test 2: Europe – France
**Destination:** www.bnf.fr (Bibliothèque nationale de France)

```bash
tracert www.bnf.fr
```

**Output (abridged):**
```
Tracing route to www.bnf.fr [194.199.8.10]
via a maximum of 30 hops:

  1     1 ms     1 ms     1 ms  192.168.0.1
  [...]
  8     9 ms     8 ms     8 ms  80.64.181.65
  9    32 ms    13 ms    25 ms  109.104.60.32
 10    17 ms    14 ms    29 ms  gw2.dus2.dogado.net [212.162.17.137]
  [...]
 15    29 ms    28 ms    28 ms  be12265.ccr41.par01.atlas.cogentco.com
  [...]
 22    43 ms    43 ms    45 ms  rap-vl165-te0-1-0-8-ren-nr-jussieu-rtr-091.noc.renater.fr
 23-30 *        *        *     Timeout (destination reached, not responding)
```

### Test 3: North America – USA

**Destination:** www.mit.edu (Massachusetts Institute of Technology)

```bash
tracert www.mit.edu
```

**Output:**
```
Tracing route to e9566.dscb.akamaiedge.net [23.63.142.104]
over a maximum of 30 hops:

  1     1 ms     1 ms     1 ms  192.168.0.1
  [...]
  9    21 ms    13 ms    12 ms  109.104.61.181
 10     *        *        *     Request timed out.
 11    14 ms    24 ms    14 ms  lo1.r02.stem01.ber01.fab.netarch.akamai.com
 12    12 ms    14 ms    13 ms  lo1.r02.spine02.ber01.fab.netarch.akamai.com
 13    14 ms    23 ms    14 ms  lo1.r02.leaf01.ber01.fab.netarch.akamai.com
 14    13 ms    14 ms    14 ms  vlan100.r11.tor01.ber01.fab.netarch.akamai.com
 15    13 ms    14 ms    14 ms  a23-63-142-104.deploy.static.akamaitechnologies.com
```

### Test 4: East Asia – Japan
**Destination:** www.u-tokyo.ac.jp (University of Tokyo)

```bash
tracert www.u-tokyo.ac.jp
```

**Output:**
```
Tracing route to www.u-tokyo.ac.jp [210.152.243.234]
via a maximum of 30 hops:

  1     1 ms     1 ms     1 ms  192.168.0.1
  [...]
  9    25 ms    20 ms    16 ms  85.232.3.243
 10    29 ms    15 ms    28 ms  gw2.dus2.dogado.net [212.162.17.137]
 11   260 ms   260 ms   259 ms  ae2.3601.edge1.Osaka1.level3.net
 12   243 ms   247 ms   242 ms  8.245.34.46
 13   252 ms   243 ms   248 ms  163.139.136.67
 14   243 ms   244 ms   243 ms  202.79.80.158
 15-16 *        *        *     Request timed out.
 17   258 ms   259 ms   263 ms  158.205.121.24
```

### Test 5: East Asia – Japan (Alternative)
**Destination:** www.nii.ac.jp (National Institute of Informatics)

```bash
tracert www.nii.ac.jp
```

**Output:**
```
Tracing route to lb-nii-ssl-www-333134043.ap-northeast-1.elb.amazonaws.com [3.115.145.97]
via a maximum of 30 hops:

  1    11 ms     1 ms     1 ms  192.168.0.1
  [...]
  9    27 ms    18 ms    18 ms  BYMUC-MC01.hlkomm.net [109.104.60.129]
 10    20 ms    21 ms    20 ms  ae12-405.muc10.core-backbone.com
 11   177 ms   173 ms   173 ms  ae3-2090.sin10.core-backbone.com
```

---

## Analysis

### Summary of results

| Server | Region | GeoIP Location | Hops | Final Latency | Notes |
|--------|--------|----------------|------|---------------|--------------- -|
| www.ox.ac.uk | Europe (UK) | Cloudflare CDN (104.20.34.13) | 11 | ~16 ms | Via Cloudflare CDN |
| www.bnf.fr | Europe (FR) | Paris (194.199.8.10) | 22 | ~44 ms | Via Renater (FR Academic Network) |
| www.mit.edu | North America | Berlin - Akamai CDN (23.63.142.104) | 15 | ~14 ms | Cached locally in Berlin! |
| www.u-tokyo.ac.jp | East Asia (JP) | Tokyo (210.152.243.234) | 17+ | ~260 ms | Genuine Japanese server |
| www.nii.ac.jp | East Asia (JP) | Tokyo - AWS (3.115.145.97) | 11 | ~175 ms | Via Singapore to AWS Tokyo |

### GeoIP verification

**Oxford (www.ox.ac.uk):**
- **IP:** 104.20.34.13
- **Actual location:** Cloudflare CDN – likely Germany/Europe
- **Expected region:** UK ✗ (CDN has local edge server)

**BnF (www.bnf.fr):**
- **IP:** 194.199.8.10
- **Actual location:** Paris, France (Renater network)
- **Expected region:** France ✓

**MIT (www.mit.edu):**
- **IP:** 23.63.142.104
- **Actual location:** Berlin, Germany (Akamai CDN)
- **Expected region:** USA ✗ (Akamai Edge in Berlin)

**U-Tokyo (www.u-tokyo.ac.jp):**
- **IP:** 210.152.243.234
- **Actual location:** Tokyo, Japan (via Osaka Level3)
- **Expected region:** Japan ✓

**NII (www.nii.ac.jp):**
- **IP:** 3.115.145.97
- **Actual location:** Tokyo, Japan (AWS ap-northeast-1)
- **Expected region:** Japan ✓

---

## Report: Analysis of correlations

### 1. Latency and geographical distance

**Observations:**
- **Within Europe (UK/FR via CDN):** 14–44 ms
- **North America (via local CDN):** 14 ms (!)
- **East Asia (real server):** 175–260 ms

**Conclusion:** 
Latency does **not always** increase with geographical distance. CDNs (Content Delivery Networks) such as Cloudflare and Akamai have local edge servers in Germany that cache content. As a result, geographically distant websites (MIT in the USA) can be faster than closer locations without a CDN (BnF in France).

**For real servers without a CDN**, the correlation is clear:
- Paris (BnF): ~800 km → ~44 ms
- Tokyo (U-Tokyo): ~9000 km → ~260 ms

**Speed of light limit:** 
The theoretical minimum latency for 9,000 km is ~30 ms (round trip, 2/3 the speed of light in fibre optic cable). The actual 260 ms shows that routing delays and processing time contribute significantly to the overall latency.

### 2. Number of hops and distance

**Observations:**
- **Local CDN (MIT/Oxford):** 11–15 hops, but low latency
- **Paris without CDN (BnF):** 22 hops, moderate latency  
- **Japan (real servers):** 11–17 hops, very high latency

**Conclusion:**
The number of hops does **not necessarily** correlate with distance. What is more important is the **type of hops**:
- Many hops in well-connected regions (Europe) can be fast
- Few hops over long undersea cables (Germany → Japan) are slow

### 3. Stronger correlation: latency vs. hops or latency vs. distance?

**Answer: It is complex and mixed.**

**Main factors for latency:**

1. **Physical distance** (for physical servers):
   - Japan: 9,000 km → 260 ms
   - Paris: 800 km → 44 ms
   - Berlin (CDN): 200 km → 14 ms

2. **Network quality of the hops:**
   - Hop 11 (U-Tokyo): Germany → Japan jump = +230 ms (!)
   - Hops 1–10: Only ~30 ms cumulative

3. **CDN presence:**
   - MIT (USA) via Berlin CDN: 14 ms
   - BnF (Paris) without CDN: 44 ms

**Particularly noticeable with U-Tokyo:**
```
Hop 10: 29 ms (Germany, dogado)
Hop 11: 260 ms (Osaka, Level3) → +231 ms for a single hop!
```

This single hop via the undersea cable to Japan causes more latency than all previous hops combined.

### 4. Sources of delay in the network path

**Based on the tracert output:**

**a) Physical distance / cable length:**
- Largest single factor in intercontinental connections
- Example: Germany → Japan hop: +230 ms

**b) Router processing and queuing:**
- Each hop processes packets: typically 1–3 ms per hop
- 15 hops × 2 ms = 30 ms additional

**c) Backbone transitions:**
- Peering points between ISPs
- Example: Tele Columbus → Level3 → Cogent → Renater (BnF)

**d) Congestion:**
- Visible in fluctuating times
- Example BnF Hop 9: 32 ms, 13 ms, 25 ms (variance!)

**e) Continental crossings:**
- Submarine cables (Germany → Japan)
- Transatlantic would be similar (Germany → US East Coast)

**f) Non-responding hops (`* * *`):**
- Do not cause any additional latency for the traffic
- ICMP is simply not answered (firewall policy)

**Latency budget example (U-Tokyo):**
- Local hops 1–10: ~30 ms
- Germany → Japan cable: ~230 ms
- Processing in Japan: ~0 ms (already included in the total)
- **Total: ~260 ms**

---

## Answers

**1. Does latency increase with geographical distance?**

Yes, with real servers **without a CDN**, a clear correlation is visible:
- Paris: ~800 km → ~44 ms
- Tokyo: ~9000 km → ~260 ms

**However:** CDNs break this rule by caching content locally (MIT in Berlin with just 14 ms despite a US server).

**2. Does the number of hops increase with distance?**

**Not necessarily.** The number of hops depends more on the network topology:
- Japan (9,000 km): 11–17 hops
- Paris (800 km): 22 hops

Well-connected backbone providers (Level3, Cogent) enable few hops over long distances.

**3. Which has a stronger correlation: hops or distance?**

**Distance** has the greater influence on intercontinental connections. A single hop (Germany → Japan) causes more delay than 10 local hops.

**However:** In regions with good connectivity (Europe), a high number of hops can result in low latency if the hops use high-quality connections.

**4. What causes delays?**

Ranked by impact:
1. **Intercontinental cables** (+200+ ms)
2. **Physical distance** (speed of light: 3.3 µs/km in fibre optic cable)
3. **Router processing** (1–3 ms per hop)
4. **Network congestion** (variable, visible in fluctuations)
5. **Peering points** (ISP interconnections)

---

## Notes

### Key findings:

- **CDNs change everything:** MIT (USA) is faster than BnF (France) due to local caching
- **Submarine cables are slow:** One hop to Japan = +230 ms
- **`* * *` does not mean "blocked":** Packets get through, only ICMP replies are filtered
- **Number of hops ≠ distance:** Network topology is more important
- **Variation indicates congestion:** Fluctuating times (13 ms, 25 ms, 32 ms) indicate congestion

### Technical details:

- **Level3** (now Lumen/CenturyLink): Major international backbone provider
- **Cogent:** Budget backbone with a dense network in Europe
- **Renater:** French academic network (similar to DFN in Germany)
- **Akamai/Cloudflare:** CDN providers with edge servers worldwide

### Areas for improvement:

- In case of repeated timeouts: try alternative servers
- GeoIP tools can be inaccurate with anycast networks (CDNs)
- Multiple tests at different times of day reveal congestion patterns

