class SnackItem:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def has_stock(self):
        return self.quantity > 0

    def sell_one(self):
        if self.has_stock():
            self.quantity -= 1
            return True
        return False


class VendingMachine:
    def __init__(self):
        self.slots = {}

    def add_snack(self, snack_object, slot_id):
        self.slots[slot_id] = snack_object

    def vend(self, slot_id):
        if slot_id not in self.slots:
            return False
        snack = self.slots[slot_id]
        return snack.sell_one()
