# Follow the Path (DNS Trace)

**Course:** Cyber Security Analyst – Network Technology | **Date:** 29 July 2025

---

## Task

**Objective:**  
To understand the iterative DNS path from the root through the TLD to the authoritative nameserver.

**Requirements:**

- Analyse `dig +trace heise.de`.
- Name the root server, TLD server and authoritative server.
- Explain the result logically.

---

## Solution

```text
Important note:
With `dig +trace`, the specific root and TLD servers may vary depending on the run.
Therefore, the structure is more important than a single fixed hostname.

Valid sample answer:
- Root server: e.g. `a.root-servers.net`
- TLD server for `.de`: e.g. `f.nic.de`
- Authoritative name server for `heise.de`: e.g. `ns.heise.de`

The key points are:
1. The root server only provides the path to the `.de` zone.
2. A `.de` name server provides the delegation for `heise.de`.
3. An authoritative server for `heise.de` provides the final A record.
```

**Alternative (compact):**

```text
Root -> TLD -> authoritative.
This is how iterative DNS resolution works.
```

---

## Tests

|Level|Expected|✓|
|---|---|---|
|Root|Reference to `.de`|✅|
|TLD|Reference to `heise.de` NS|✅|
|Authoritative|Provides final record|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|Root Server|Does not know the destination IP, but the path to the TLD.|
|TLD Server|Points to the domain’s authoritative servers.|
|Authoritative|Holds the final zone information.|

---

## Rules / Logic

```text
`+trace` does not show recursion through the local resolver,
but rather the iterative path through the DNS hierarchy.
```

---

## Notes

- **Important:** Specific root and TLD servers may change between runs.
- **Tip:** Authoritative servers are the actual source of the response.

---

## Optional: Extensions

- Repeat the same process for another TLD such as `.org` or `.com`.
- Include TTL and glue records in the analysis.

