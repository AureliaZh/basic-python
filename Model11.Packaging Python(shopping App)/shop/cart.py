from shop.errors import BudgetExceededError

class CartItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def total_price(self):
        return self.product.get_price_with_tax() * self.quantity


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity):
        self.items.append(CartItem(product, quantity))

    def calculate_total(self):
        return sum(item.total_price() for item in self.items)

    def check_budget(self, budget):
        if self.calculate_total() > budget:
            raise BudgetExceededError("Budget exceeded")