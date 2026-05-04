import threading
import multiprocessing


# ===============================
# Custom Exceptions
# ===============================

class ProductNotFoundError(Exception):
    pass


class BudgetExceededError(Exception):
    pass


# ===============================
# Product Classes
# ===============================

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


# ===============================
# Cart Classes
# ===============================

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
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero")
        self.items.append(CartItem(product, quantity))

    def calculate_total(self):
        return sum(item.total_price() for item in self.items)

    def check_budget(self, budget):
        total = self.calculate_total()
        if total > budget:
            raise BudgetExceededError(
                f"Total ${total:.2f} exceeds budget ${budget:.2f}"
            )


# ===============================
# Process Task
# ===============================

def checkout_process(user_name, cart, budget):
    print(f"[Process] {user_name} checking out...")

    try:
        total = cart.calculate_total()
        cart.check_budget(budget)
        print(f"[Process] {user_name} total: ${total:.2f}")
    except BudgetExceededError as e:
        print(f"[Process] {user_name} error: {e}")


# ===============================
# Thread Task
# ===============================

def user_thread(user_name, cart, budget):
    print(f"[Thread] {user_name} started")

    p = multiprocessing.Process(
        target=checkout_process,
        args=(user_name, cart, budget)
    )

    p.start()
    p.join()

    print(f"[Thread] {user_name} finished")


# ===============================
# Main Program
# ===============================

if __name__ == "__main__":

    BUDGET = 100.0

    products = {
        "notebook": Product("Notebook", 19.99),
        "pen": Product("Pen", 2.50),
        "bag": DiscountedProduct("Bag", 49.99, 0.2)
    }

    cart1 = ShoppingCart()
    cart1.add_item(products["notebook"], 2)
    cart1.add_item(products["pen"], 3)

    cart2 = ShoppingCart()
    cart2.add_item(products["bag"], 1)

    t1 = threading.Thread(target=user_thread, args=("User A", cart1, BUDGET))
    t2 = threading.Thread(target=user_thread, args=("User B", cart2, BUDGET))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("\nAll users finished.")