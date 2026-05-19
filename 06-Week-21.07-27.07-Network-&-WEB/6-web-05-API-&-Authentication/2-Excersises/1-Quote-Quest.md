# Quote Quest (API & Authentication)

**Course:** Cyber Security Analyst – Web Technology | **Date:** 26 July 2025

---

## Task

**Objective:**  
Call a token-protected API using `curl` and read the JSON response.

**Requirements:**

- Use your own NewsAPI key.
- Retrieve `top-headlines` using `curl`.
- Save the JSON in the terminal or in `news.json`.

---

## Solution

```bash
curl "https://newsapi.org/v2/top-headlines?country=us&apiKey=YOUR_API_KEY"
```

```bash
curl "https://newsapi.org/v2/top-headlines?country=us&apiKey=YOUR_API_KEY" -o news.json
```

```json
{
  "status": "ok",
  "totalResults": 38,
  "articles": [
    {
      "source": {"id": "techcrunch", "name": "TechCrunch"},
      "title": "AI is reshaping cybersecurity"
    }
  ]
}
```

**Alternative (compact):**

```text
API key in the URL = authentication against the service.
```

---

## Tests

|Item|Expected|✓|
|---|---|---|
|Request with key|JSON response|✅|
|Read `status`|`ok` if key is valid|✅|
|Save file|`news.json` present|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|API key|Simple authentication token for the service.|
|JSON|Structured response format for APIs.|
|`curl -o`|Saves the response directly to a file.|

---

## Rules / Logic

```text
Without a valid API key -> Error response.
With a valid API key -> JSON containing articles.
Response content is time- and account-dependent.
```

---

## Notes

- **Important:** Never share your own key publicly.
- **Tip:** For submission, include the actual terminal output or `news.json` from your own run.

---

## Optional: Extensions

- Extract titles only using `jq`.
- Filter by keyword instead of country.


