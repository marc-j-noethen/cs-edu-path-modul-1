# 🐍 Shape Inheritance - Inheritance and Polymorphism

**Course:** Cyber Security Analyst - Python Basics | **Date:** 10 July 2025

---

## Task

**Objective:** Implement an inheritance hierarchy for geometric shapes

**Requirements:**
- Base class: `Shape` with abstract method `calculate_area()`
- Subclass: `Rectangle(width, height)` - Calculates the area of a rectangle
- Subclass: `Circle(radius)` - Calculates the area of a circle (rounded to 4 decimal places)
- Return type: Float (area)
- Edge cases: Base method raises NotImplementedError

---

## Solution

```python
import math

class Shape:
    """Base class for geometric shapes."""
    
    def calculate_area(self):
        """Must be implemented by subclasses."""
        raise NotImplementedError("Subclass must implement this method")


class Rectangle(Shape):
    """Rectangle with width and height."""
    
    def __init__(self, width, height):
        """Initialises a rectangle with width and height."""
        self.width = width
        self.height = height
    
    def calculate_area(self):
        """Calculates the area of the rectangle."""
        return self.width * self.height


class Circle(Shape):
    """Circle with radius."""
    
    def __init__(self, radius):
        """Initialises a circle with a radius."""
        self.radius = radius
    
    def calculate_area(self):
        """Calculates the area of the circle (rounded to 4 decimal places)."""
        return round(math.pi * self.radius ** 2, 4)
```

---

## Tests

| Input | Expected | Result | ✓ |
|-------|----------|----------|---|
| `Rectangle(5, 10).calculate_area()` | 50 | 50 | ✅ |
| `Circle(8).calculate_area()` | 201.0619 | 201.0619 | ✅ |
| `Rectangle(3, 7).calculate_area()` | 21 | 21 | ✅ |
| `Circle(5).calculate_area()` | 78.5398 | 78.5398 | ✅ |

---

## Notes

- **Concept:** Inheritance and method overriding (Override)
- **NotImplementedError:** Enforces implementation in subclasses (Abstract Method Pattern)
- **math.pi:** Constant for π (≈ 3.14159...)
- **round(x, 4):** Rounds to 4 decimal places
- **Polymorphism:** Different forms implement the same interface differently
- **Alternative:** Abstract Base Classes (ABC) with the `@abstractmethod` decorator

