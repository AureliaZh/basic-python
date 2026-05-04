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

    def print_summary(self):
        print("\nOrder Summary:")

        summaries = [
            f"- {item.product.name}: {item.quantity} × ${item.product.get_price():.2f}"
            for item in self.items
        ]

        for line in summaries:
            print(line)

        print(f"\nTotal (with tax): ${self.calculate_total():.2f}")


class InputHelper:
    @staticmethod
    def get_quantity():
        while True:
            value = input("Enter quantity: ")
            if value.isdigit() and int(value) > 0:
                return int(value)
            print("Invalid quantity.")


BUDGET = 100.0

product_data = [
    ("Notebook", 19.99),
    ("Pen", 2.50),
    ("Bag", 49.99)
]

products = {
    name.lower(): Product(name, price)
    for name, price in product_data
}

products["bag"] = DiscountedProduct("Bag", 49.99, 0.2)

added_products = set()

cart = ShoppingCart()

print("Available products:")
for product in products.values():
    print(f"- {product.name} (${product.get_price():.2f})")

while True:
    choice = input("\nEnter product name (or 'done'): ").strip().lower()
    if choice == "done":
        break

    product = products.get(choice)
    if product is None:
        print("Product not found.")
        continue

    quantity = InputHelper.get_quantity()
    cart.add_item(product, quantity)

    added_products.add(product.name)  
    print("Item added!")

cart.print_summary()

total = cart.calculate_total()
if total <= BUDGET:
    print("Within budget.")
else:
    print("Over budget.")

print("\nUnique products purchased:", added_products)