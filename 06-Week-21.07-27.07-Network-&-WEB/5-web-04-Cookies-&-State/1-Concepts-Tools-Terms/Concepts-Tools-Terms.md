## 📊 Summary based on the 80/20 principle

**The problem:** HTTP is stateless – each request is independent, and the server ‘forgets’ previous interactions. However, modern web applications need to remember users (login details, shopping basket, settings).

**The solution: Cookies** – The server sends small data packets (`Set-Cookie` header) to the browser, which stores them and sends them back with every subsequent request (`Cookie` header). This allows the server to recognise the user.

**Two types of cookies:**

- **Session cookies:** Temporary; deleted when the browser is closed
- **Persistent cookies:** Long-term with an expiry date; survive browser restarts

**Critical security attributes:**

- `HttpOnly` – protects against JavaScript access (XSS protection)
- `Secure` – transmitted via HTTPS only
- `SameSite` – prevents unwanted cross-site requests (CSRF protection)

**Best practice: Server-side sessions** – Instead of storing all data in the cookie, the server stores the data and sends only a session ID as a cookie. More secure and flexible.

**Main risks:** Session hijacking (stolen cookies), XSS attacks, CSRF attacks and tracking via third-party cookies.

**Practical learning:** Using Browser Developer Tools (F12 → Application/Storage tab), you can inspect all cookies on a website and view their attributes.

---

## Table 1: Tools used

|Tools used|Description|
|---|---|
|Browser Developer Tools (F12)|Developer tools for inspecting cookies and HTTP traffic|
|Application/Storage tab|Section in the Developer Tools for displaying stored data (cookies, LocalStorage, etc.)|
|Network Tab|Section for monitoring HTTP requests and responses, including cookie headers|
|Right-click → "Inspect"|Alternative method for opening the Developer Tools|

**Windows 11 adaptation:** The keyboard shortcut `F12` or `Ctrl+Shift+I` works identically in Windows 11 (instead of `Cmd+Opt+I` on macOS).

---

## Table 2: Technical Terms

|Technical Terms|Meaning|
|---|---|
|HTTP (Hypertext Transfer Protocol)|Stateless protocol for data communication on the web|
|Stateless Protocol|A protocol in which each request is handled independently – no automatic recall of previous requests|
|State Management|Management of state information across multiple requests|
|Cookie|A small amount of data stored by the server in the browser|
|Session Cookie|A temporary cookie with no expiry date; it is deleted when the browser is closed|
|Persistent Cookie|A permanent cookie with a set expiry date|
|Set-Cookie Header|An HTTP response header used by servers to set cookies in the browser|
|Cookie Header|An HTTP request header used by the browser to send cookies back to the server|
|Session ID|A unique identifier for a user session|
|Server-side sessions|Session data is stored on the server; only the session ID is transmitted in the cookie|
|Third-party cookies|Cookies from third parties (e.g. advertising networks) that track user behaviour across multiple websites|
|Session hijacking|An attack in which an attacker steals a user’s session cookie|
|XSS (Cross-Site Scripting)|Security vulnerability where attackers inject malicious code into web pages|
|CSRF (Cross-Site Request Forgery)|An attack in which users unintentionally send malicious requests to authenticated websites|

---

## Table 3: Important cookie attributes (Terminology)

|Key terms|Meaning|
|---|---|
|`Expires=<date>`|Expiry date of the cookie (date and time)|
|`Max-Age=<seconds>`|Lifetime of the cookie in seconds (takes precedence over `Expires`)|
|`Domain=<domain-name>`|Specifies the domain(s) for which the cookie is valid|
|`Path=<path>`|URL path for which the cookie is valid|
|`Secure`|Cookie is only transmitted via encrypted HTTPS connections|
|`HttpOnly`|Cookie cannot be accessed via JavaScript (protection against XSS)|
|`SameSite=Strict`|Cookie is only sent for requests from the same website|
|`SameSite=Lax`|Cookie for same-site requests and top-level navigation (default)|
|`SameSite=None`|Cookie is sent for all requests (requires `Secure`)|


