# Formidable POST (HTTP)

**Course:** Cyber Security Analyst – Network Technology | **Date:** 22 July 2025

---

## Task

**Objective:**  
Analyse a form POST and understand how an additional field appears in the request body.

**Requirements:**

- Observe the POST request to `http://httpbin.org/forms/post`.
- Identify the body format in Wireshark and DevTools.
- Describe the change caused by the `Delivery Tip` field.

---

## Solution

```text
Typical body format:
application/x-www-form-urlencoded

Example body:
custname=Alice&custtel=123456&custemail=alice%40example.com&size=medium&delivery=13%3A00&comments=Test

Answer to the question:
If there were an additional field called `Delivery Tip`, another key-value pair would simply be added,
e.g. `&delivery_tip=5` or `&tip=5.00` – depending on the field name in the HTML form.
```

**Alternative (compact):**

```text
Each new form field adds another parameter to the URL-encoded body.
```

---

## Tests

|Item|Expected|Result|✓|
|---|---|---|---|
|Body visible|Form data readable|Yes|✅|
|Encoding recognised|`application/x-www-form-urlencoded`|Yes|✅|
|Additional field understood|further `key=value` pair|Yes|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|POST|Sends data in the request body to the server.|
|Form encoding|Special characters are URL-encoded, e.g. `%40` for `@`.|
|DevTools vs. Wireshark|DevTools displays browser-level data, Wireshark displays packet-level data.|

---

## Rules / Logic

```text
HTML form -> Name/value pairs.
POST body -> connected with `&`.
New field -> new parameter in the body.
```

---

## Notes

- **Concept:** The field name in the HTML determines the key in the body.
- **Tip:** In DevTools, the body is often easier to read than in the raw packet.

---

## Optional: Extensions

- Send the same form using JSON instead of form encoding.
- Compare the difference between a GET query and a POST body.

