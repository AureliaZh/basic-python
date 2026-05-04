
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_price(self):
        return self.price

class DiscountedProduct(Product):
    def __init__(self, name, price, discount):
        super().__init__(name, price)
        self.discount = discount

    def get_price(self):
        return self.price * (1 - self.discount)
