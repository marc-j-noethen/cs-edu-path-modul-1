## 📊 Summary based on the 80/20 principle

**What is HTTP?** HTTP (Hypertext Transfer Protocol) is the fundamental communication protocol of the internet. It defines how web browsers (clients) request web pages from servers and how servers respond to them.

**Basic principles:**

1. **Client-server model**: Your browser sends a request, the server responds
2. **Statelessness**: Each request is independent – the server does not ‘remember’ previous requests
3. **Resources & URLs**: Everything on the web (webpages, images, data) can be identified via URLs

**The most important HTTP methods:**

- **GET**: Retrieve a webpage or data (read-only)
- **POST**: Send data (e.g. submit forms)

**The most important status codes:**

- **200 OK**: Everything worked
- **404 Not Found**: Page does not exist
- **500 Internal Server Error**: Server problem

**HTTP vs. HTTPS:**

- **HTTP**: Unencrypted transmission – insecure
- **HTTPS**: Encrypted transmission using TLS/SSL – secure and now the standard

**Practical use:** Using the browser developer tools (F12 or right-click → "Inspect" → Network tab), you can observe and analyse all HTTP requests in real time – perfect for learning and debugging.

**Key takeaway:** HTTP is text-based and follows a simple request-response pattern. Every web interaction follows this cycle: browser requests → server responds → browser displays the result.

---

## Categorisation

|Category|Term|Meaning|
|---|---|---|
|**Tools used**|Browser Developer Tools|Developer tools in modern browsers (Chrome, Firefox) for inspecting network traffic|
||Network Tab|Tab in the Developer Tools for displaying all HTTP requests|
||curl|Command-line tool for sending HTTP requests|
||Apache / Nginx / IIS|Web server software for hosting and serving web resources|
|**Technical Terms**|HTTP (Hypertext Transfer Protocol)|Set of rules for communication between web browsers and web servers|
||HTTPS (HTTP Secure)|Encrypted version of HTTP using TLS/SSL encryption|
||Client-server model|Architecture in which the client makes requests and the server responds|
||Request-response cycle|The sequence of request and response in HTTP|
||Statelessness|Each HTTP request is handled independently, without storing previous requests|
||URL (Uniform Resource Locator)|Address used to identify a web resource (e.g. web page, image)|
||DNS (Domain Name System)|System for resolving domain names into IP addresses|
||TCP|Transport protocol on which HTTP is based (port 80 for HTTP, port 443 for HTTPS)|
||Application Layer|Topmost layer in the 5-layer network model|
||Headers|Metadata in HTTP messages (name-value pairs)|
||Message Body|Actual data content of an HTTP message|
||TLS/SSL|Encryption protocols for secure data transmission|
||Idempotent|Property of an operation that returns the same result when executed multiple times|
||CRLF|Carriage Return Line Feed – line break in HTTP messages|
|**HTTP Methods**|GET|Retrieving a resource (read-only, no state change)|
||POST|Sending data for processing (e.g. form submission)|
||PUT|Replacing a resource with new data|
||DELETE|Deleting a specified resource|
||HEAD|Retrieving only the headers without the body (for metadata checking)|
||OPTIONS|Querying available communication options|
||PATCH|Partial modification of a resource|
|**HTTP status codes**|1xx|Informational – request received, processing in progress|
||2xx|Success (e.g. 200 OK, 201 Created, 204 No Content)|
||3xx|Redirection (e.g. 301 Moved Permanently, 302 Found)|
||4xx|Client error (e.g. 400 Bad Request, 401 Unauthorised, 403 Forbidden, 404 Not Found)|
||5xx|Server error (e.g. 500 Internal Server Error, 503 Service Unavailable)|
|**URL components**|Scheme|Protocol designation (http:// or https://)|
||Host|Domain name or IP address of the server|
||Path|Location of the resource on the server|
||Query string|Parameters for data transfer (begins with ?)|
||Fragment|Section identifier within the resource (begins with #)|
|**Important Headers**|Host|Target domain of the server (required in HTTP/1.1)|
||User-Agent|Identification of the client software|
||Accept|Content types preferred by the client|
||Content-Type|Type of content being transferred|
||Content-Length|Size of the message body in bytes|
||Location|New URL for redirects|
|**Security concepts**|Confidentiality|Protection against unauthorised eavesdropping through encryption|
||Integrity|Ensuring that data has not been tampered with|
||Authentication|Verification of the server’s identity using certificates|
||Man-in-the-middle attack|Attack involving the interception and manipulation of communication|


