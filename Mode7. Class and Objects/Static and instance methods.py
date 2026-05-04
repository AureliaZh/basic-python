
class CartItem:
    def __init__(self, name, price, quantity):
        self.name = name          # instance attribute
        self.price = price
        self.quantity = quantity

    def total_price(self):        # instance method
        return self.price * self.quantity


class Store:
    tax_rate = 0.1   # static / class attribute

    def __init__(self, name):
        self.name = name
