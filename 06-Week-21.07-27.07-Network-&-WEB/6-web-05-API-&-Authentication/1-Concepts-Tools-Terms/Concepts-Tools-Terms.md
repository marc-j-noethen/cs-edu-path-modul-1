## 📊 Summary based on the 80/20 principle

### What is an API?

An **API (Application Programming Interface)** is an interface that enables different software systems to communicate with one another. It works like a waiter in a restaurant: the customer (client) places an order via the waiter (API) with the chef (server), without going into the kitchen themselves.

### The most important 20% – REST APIs

**REST** is the most commonly used architectural style for web APIs, with the following core principles:

- **Resources** are identified by URLs (e.g. `/users/123`)
- **HTTP methods** define actions:
    - `GET` = Retrieve
    - `POST` = Create
    - `PUT/PATCH` = Update
    - `DELETE` = Delete
- **JSON** is the standard data format for exchange
- **Statelessness**: Every request contains all necessary information

### Security: Authentication vs. Authorisation

**Authentication** (“Who are you?”) verifies identity, **authorisation** (“What are you allowed to do?”) checks permissions.

**The three most common authentication methods:**

1. **API Keys**: Simple unique string, but long-lived and less secure
2. **HTTP Basic Auth**: Username:Password in Base64, secure only with HTTPS
3. **Bearer Tokens** (OAuth 2.0/JWT): Modern standard with short validity and specific permissions

**Key security rule**: Always use HTTPS so that login credentials cannot be intercepted.

### Practical benefits of APIs

APIs enable **modularity** (independent services), **reusability** (same functionality for multiple apps), **integration** (connecting different systems) and **abstraction** (complexity is hidden).

**Everyday example**: A weather app on a smartphone retrieves temperature data via a weather API without collecting weather data itself.

---

## Tools used, technical terms and key vocabulary

|Term|Meaning|
|---|---|
|**Tools used**||
|HTTP protocol|Transmission protocol for communication between client and server on the web|
|JSON (JavaScript Object Notation)|Lightweight data format for data exchange between systems|
|Browser Developer Tools (F12)|Developer tools in the browser for analysing network requests and responses|
|Mermaid|Diagramming tool for visualising processes and sequences|
|**Technical terms**||
|API (Application Programming Interface)|Interface that enables communication between different software applications|
|REST (Representational State Transfer)|Architectural style for APIs that uses standard HTTP methods|
|HTTP methods (GET, POST, PUT, PATCH, DELETE)|Standardised verbs for performing operations on resources|
|Endpoint|Specific URL address via which an API resource can be accessed|
|Request|Message from the client to the server containing the URL, method, headers and, where applicable, body|
|Response|Message from the server to the client containing the status code, headers and, where applicable, body|
|HTTP status code|Three-digit number indicating the result of a request (e.g. 200, 404, 500)|
|Header|Additional information in HTTP requests/responses (e.g. Content-Type, Authorization)|
|Payload (Body)|Data section of an HTTP message, usually in JSON format|
|Statelessness|Principle whereby each request contains all necessary information, without server-side context|
|Resource|Data element in an API (e.g. user, product), identified by a URL|
|Authentication|Process for verifying a user’s identity (“Who are you?”)|
|Authorisation|Process for checking access rights (“What are you allowed to do?”)|
|API Key|Unique string used to identify a client programme|
|HTTP Basic Authentication|Authentication method using Base64-encoded username:password|
|Bearer Token|Security token transmitted in the Authorisation header|
|OAuth 2.0|Authorisation framework for controlled access to HTTP services|
|JWT (JSON Web Token)|Compact, URL-safe token format for authentication with embedded claims|
|HTTPS|Encrypted version of HTTP for secure data transmission|
|Base64|Encoding method for representing binary data as text|
|**Key terms**||
|Client|Application or system that uses an API (consumer)|
|Server|System that provides an API (provider)|
|Provider|Provider of an API or a service|
|Token|Digital proof of access with limited validity|
|Credentials|Login details (username, password) for authentication|
|Scope|Scope of the permissions granted by a token|
|Claims|Statements of information in a JWT regarding users or tokens|
|Rate Limiting|Limiting the number of API requests per unit of time|
|Revocation|Revocation/invalidation of a token or key|


