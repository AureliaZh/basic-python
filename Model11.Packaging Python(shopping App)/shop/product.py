class Product:
    tax_rate = 0.10

    def __init__(self, name, base_price):
        self.name = name
        self.base_price = base_price

    def get_price(self):
        return self.base_price

    def get_price_with_tax(self):
        return self.get_price() * (1 + Product.tax_rate)


class DiscountedProduct(Product):
    def __init__(self, name, base_price, discount):
        super().__init__(name, base_price)
        self.discount = discount

    def get_price(self):
        return self.base_price * (1 - self.discount)