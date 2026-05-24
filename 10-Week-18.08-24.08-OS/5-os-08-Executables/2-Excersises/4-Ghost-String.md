# 🐍 Ghost String (Executable Strings)

**Course:** Cyber Security Analyst - OS Technology | **Date:** 22 August 2025

---

## Task

**Objective:**  
Compare two C programmes and explain why an unused string may appear in one binary but not in the other.

**Requirements:**

- Compile Programme A and Programme B.
- Search for the string `ProjectChimera_Payload_Alpha_7_Variant_Echo` in both EXEs.
- Explain the consequences of unreferenced data in the binary.
- Describe the forensic value of embedded strings.

- Output:

    - String in Program A: found
    - String in Program B: not found
    - Analysis of why this is relevant from an analyst’s perspective

---

## Solution

```text
Result:
- `program_A.exe`: The string `ProjectChimera_Payload_Alpha_7_Variant_Echo` was found.
- `program_B.exe`: The string was not found.

Search method:
- Searched for the exact plaintext using `strings.exe`, a hex editor or CFF Explorer.
- For the architecture verification in the task, the machine type in the PE headers would also be shown.

Why is the string still present in Program A despite the lack of output?
The compiler and linker may leave data objects in the binary even if `main()` does not explicitly use them,
particularly if optimisation/dead-data elimination does not remove the constant.

What does Program B show?
If the data has genuinely been removed or commented out from the source code, there is no longer any reason
to carry it over into the final binary – so the trace also disappears during the search.

Why is string searching valuable for analysts?
Embedded strings can indicate C2 servers, filenames, function names, internal project names,
error messages, PDB paths, cryptographic material or malware family references.
Even if the programme appears harmless in its normal output, the binary often reveals more about its purpose and origin.
```

**Alternative (compact):**

```text
Unprinted plain text can still end up in the binary – and that is precisely why strings are so valuable to analysts.
```

---

## Tests

|Input 1|Input 2|Input 3|Expected|Result|✓|
|---|---|---|---|---|---|
|`program_A.exe`|`string search`|`ProjectChimera`|`found`|`expected`|✅|
|`program_B.exe`|`string search`|`ProjectChimera`|`not found`|`expected`|✅|
|`analyst view`|`embedded strings`|`unknown exe`|`useful clues`|`yes`|✅|

---

## Explanation / Concepts

|Concept|Description|
|---|---|
|Unreferenced Data|Data may remain in the binary despite not being used at runtime.|
|Dead-Data Elimination|Optimisation mechanism that can remove unused data from the final artefact.|
|Static Analysis|Analysis of a programme without executing it, e.g. via headers, imports and strings.|

---

## Rules / Logic

```text
What does not appear in the GUI output may still be present in the binary.
A negative search result in version B is just as meaningful as a positive result in version A.
Strings provide context, but do not replace a comprehensive analysis.
```

---

## Notes

- **Important:** The exact ARM64 build is environment-dependent; the key point regarding string behaviour remains the same.
- **Tip:** Use multiple tools – `strings`, a hex editor and a PE viewer complement each other well.
- **Observation:** Harmless demo binaries in particular demonstrate very clearly why string searching is standard practice in malware analysis.

---

## Optional: Extensions

- Compare the same behaviour with different optimisation levels (`-O0`, `-O2`).
- Additionally, examine PDB/debug paths or import tables for origin clues.


