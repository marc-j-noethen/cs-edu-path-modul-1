# 🐍 Vending Machine - Object Composition

**Course:** Cyber Security Analyst - Python Basics | **Date:** 10 July 2025

---

## Task

**Objective:** To simulate a snack vending machine with stock management

**Requirements:**
- Class: `SnackItem(name, quantity)` - Represents a snack
  - `has_stock()`: Checks if stock is available
  - `sell_one()`: Sells one item (decreases quantity)
- Class: `VendingMachine()` - Manages snacks in slots
  - `add_snack(snack_object, slot_id)`: Adds a snack to a slot
  - `vend(slot_id)`: Sells an item from a slot
- Return value: Boolean (True on success, False on failure)
- Edge cases: No stock, slot does not exist

---

## Solution

```python
class SnackItem:
    """Represents a snack with a name and quantity."""
    
    def __init__(self, name, quantity):
        """Initialises a snack with a name and quantity."""
        self.name = name
        self.quantity = quantity
    
    def has_stock(self):
        """Checks if there is stock available."""
        return self.quantity > 0
    
    def sell_one(self):
        """Sells one item. Returns True on success, False if out of stock."""
        if self.has_stock():
            self.quantity -= 1
            return True
        return False


class VendingMachine:
    """Manages snacks in different slots."""
    
    def __init__(self):
        """Initialises an empty vending machine."""
        self.slots = {}
    
    def add_snack(self, snack_object, slot_id):
        """Adds a snack to a slot."""
        self.slots[slot_id] = snack_object
    
    def vend(self, slot_id):
        """Sells an item from a slot. Returns True on success, False on failure."""
        if slot_id not in self.slots:
            return False
        snack = self.slots[slot_id]
        return snack.sell_one()
```

---

## Tests

| Input | Expected | Result | ✓ |
|-------|----------|----------|---|
| `crisps = SnackItem("Crisps", 5); vm = VendingMachine(); vm.add_snack(crisps, "A1"); vm.vend("A1")` | True | True | ✅ |
| `crisps.quantity` | 4 | 4 | ✅ |
| `vm.vend("A1")` | True | True | ✅ |
| `crisps.quantity` | 3 | 3 | ✅ |
| `choc = SnackItem("Chocolate", 0); vm.add_snack(choc, "A2"); vm.vend("A2")` | False | False | ✅ |
| `vm.vend("B1")` | False | False | ✅ |

---

## Notes

- **Concept:** Object composition – VendingMachine contains SnackItem objects
- **Dictionary:** `slots` stores slot ID as the key, SnackItem as the value
- **State management:** `quantity` is managed directly within the SnackItem object
- **Delegation:** `vend()` delegates the sale to the `sell_one()` method
- **in operator:** Checks whether a key exists in the dictionary
- **Design Pattern:** Composition over Inheritance


