# 🐍 Text Processing Pipeline - Chain of Responsibility

**Course:** Cyber Security Analyst - Python Basics | **Date:** 10 July 2025

---

## Task

**Objective:** To implement a pipeline for sequential text processing

**Requirements:**
- Base class: `TextProcessor` with abstract `process(text)` method
- Subclass: `UpperCaseProcessor` - Converts text to uppercase
- Subclass: `RemovePunctuationProcessor` - Removes punctuation marks (.,!?)
- Class: `Pipeline` – Chains multiple processors
  - `add_processor(processor_object)`: Adds a processor
  - `run(initial_text)`: Executes all processors sequentially
- Return value: String (processed text)
- Edge cases: Base method raises NotImplementedError

---

## Solution

```python
class TextProcessor:
    """Base class for text processing processors."""
    
    def __init__(self):
        """Initialisation (optional)."""
        pass
    
    def process(self, text):
        """Must be implemented by subclasses."" "
        raise NotImplementedError("Subclass must implement this method")


class UpperCaseProcessor(TextProcessor):
    """Converts text to uppercase."""
    
    def process(self, text):
        """Returns text in uppercase."""
        return text.upper()


class RemovePunctuationProcessor(TextProcessor):
    """Removes common punctuation marks from text."""
    
    def process(self, text):
        """Removes punctuation marks (.,!?) from the text."""
        translator = str.maketrans('', '', '.,!?'),
        return text.translate(translator)


class Pipeline:
    """Chains multiple TextProcessor objects into a pipeline."""
    
    def __init__(self):
        """Initialises an empty list of processors."""
        self.processors = []
    
    def add_processor(self, processor_object):
        """Adds a TextProcessor to the pipeline."""
        self.processors.append(processor_object)
    
    def run(self, initial_text):
        """Executes all processors sequentially and returns the result."""
        current_text = initial_text
        for processor in self.processors:
            current_text = processor.process(current_text)
        return current_text
```

---

## Tests

| Input | Expected | Result | ✓ |
|-------|----------|----------|---|
| `pipeline = Pipeline(); pipeline.add_processor(UpperCaseProcessor()); pipeline.add_processor(RemovePunctuationProcessor()); pipeline.run("Hello, World! How are you?")` | "HELLO WORLD HOW ARE YOU" | HELLO WORLD HOW ARE YOU | ✅ |
| `pipeline2 = Pipeline(); pipeline2.add_processor(RemovePunctuationProcessor()); pipeline2.run("Test!")` | "Test" | Test | ✅ |

---

## Notes

- **Concept:** Chain of Responsibility Pattern & Strategy Pattern
- **str.maketrans():** Creates a translation table for `translate()`
- **translate():** Efficient method for removing/replacing characters
- **Sequential Processing:** The output of one processor is the input of the next
- **Polymorphism:** Pipeline works with any TextProcessor subclasses
- **Alternative:** `text.replace('.', '').replace(',', '')...` for punctuation removal
- **Extensibility:** New processors can be easily added



