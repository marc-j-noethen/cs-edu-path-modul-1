# 🐍 Find Average Positive - Durchschnitt positiver Zahlen

**Course:** Cyber Security Analyst - Python Basics | **Date:** 01 July 2025

---

## Aufgabe

**Ziel:** Berechne den Durchschnitt nur der positiven Zahlen (> 0) in einer Liste.

**Anforderungen:**
- Funktion: `find_average_positive(numbers)`
- Rückgabe: Float (Durchschnitt) oder `0`
- Edge Cases: Leere Liste, keine positiven Zahlen → `0`

---

## Lösung

```python
def find_average_positive(numbers):
    total = 0
    count = 0
    for num in numbers:
        if num > 0:            # Fix: > statt >= (0 ist nicht positiv)
            total += num
            count += 1         # Fix: nur positive zählen
    if count == 0:             # Fix: count prüfen statt total
        return 0               # Fix: 0 statt None
    return total / count       # Fix: / statt // (Float-Division)
```

---

## Tests

| Input | Erwartet | Ergebnis | ✓ |
|-------|----------|----------|---|
| `[1, 2, 3, -1, 4]` | 2.5 | 2.5 | ✅ |
| `[]` | 0 | 0 | ✅ |
| `[-1, -2, -3]` | 0 | 0 | ✅ |

---

## Notizen

- **Fehler 1:** `>= 0` → `> 0` (0 ist nicht positiv)
- **Fehler 2:** `count += 1` war außerhalb des `if`-Blocks
- **Fehler 3:** `return None` → `return 0` laut Anforderung
- **Fehler 4:** `//` (Integer-Division) → `/` (Float-Division für 2.5)
