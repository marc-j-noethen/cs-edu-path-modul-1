# Cookie Choices (Cookies & State)

**Course:** Cyber Security Analyst – Web Technology | **Date:** 25 July 2025

---

## Task

**Objective:**  
Observe how cookies change before consent is given, after they are rejected, and after `Accept all` is selected.

**Requirements:**

- Examine `dw.com` in private mode.
- Compare cookies before consent, after rejection and after full consent.
- Explain categories and purpose.

---

## Solution

```text
Pattern observation:
- Before consent: usually only a few technically necessary or consent-related cookies.
- After rejecting optional cookies: still only necessary cookies, e.g. consent status, session or language.
- After `Accept all`: additional analytics, personalisation and advertising cookies.

Typical example categories:
- Analytics: e.g. `_ga`, `_gid`
- Advertising/Tracking: e.g. `IDE`, DoubleClick or AdTech cookies
- Personalisation: e.g. user preferences or A/B testing cookies

Why websites do this:
- Legal requirement for consent
- Transparency regarding tracking and personalisation
- Separation between necessary and optional data processing
```

**Alternative (compact):**

```text
The more consent is given, the more non-essential cookies may be set.
```

---

## Tests

|State|Expected|✓|
|---|---|---|
|Before consent|few cookies|✅|
|After refusal|mainly necessary cookies|✅|
|After ‘Accept all’|more tracking/analytics cookies|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|Essential Cookies|Required for basic functionality and session management.|
|Analytics Cookies|Measure usage and behaviour.|
|Advertising Cookies|Support profiling, campaigns and retargeting.|

---

## Rules / Logic

```text
Without consent -> only necessary categories.
With full consent -> additional optional categories.
Consent cookie stores the user’s selection.
```

---

## Notes

- **Important:** Exact cookie names may change on `dw.com` at any time.
- **Tip:** In the submission, enter the names actually observed from your own session.

---

## Optional: Extensions

- Compare network requests with and without consent.
- Examine third-party domains in the browser.

