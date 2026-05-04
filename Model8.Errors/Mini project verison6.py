
# Custom Exceptions

class ProductNotFoundError(Exception):     
    """Raised when a product is not found"""
    pass


class BudgetExceededError(Exception):     
    """Raised when total price exceeds budget"""
    pass


# Product Classes


class Product:
    tax_rate = 0.10                       # Class attribute (static attribute)

    def __init__(self, name, base_price):
        self.name = name                  # Instance attribute
        self.base_price = base_price      # Instance attribute

    def get_price(self):
        return self.base_price

    def get_price_with_tax(self):
        return self.get_price() * (1 + Product.tax_rate)


class DiscountedProduct(Product):          # Inheritance
    def __init__(self, name, base_price, discount):
        super().__init__(name, base_price)
        self.discount = discount           # Instance attribute

    def get_price(self):                   
        return self.base_price * (1 - self.discount)


# Cart Classes

class CartItem:
    def __init__(self, product, quantity):
        self.product = product             # Object reference
        self.quantity = quantity

    def total_price(self):
        return self.product.get_price_with_tax() * self.quantity


class ShoppingCart:
    def __init__(self):
        self.items = []                    # List (stores CartItem objects)

    def add_item(self, product, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero")
            # Built-in exception (ValueError)
        self.items.append(CartItem(product, quantity))

    def calculate_total(self):
        return sum(item.total_price() for item in self.items)
        # Generator expression using a list

    def check_budget(self, budget):
        total = self.calculate_total()
        if total > budget:
            raise BudgetExceededError(     # Custom exception for business rule
                f"Total ${total:.2f} exceeds budget ${budget:.2f}"
            )

    def print_summary(self):
        print("\nOrder Summary:")

        # List comprehension
        lines = [
            f"- {item.product.name}: {item.quantity} * ${item.product.get_price():.2f}"
            for item in self.items
        ]

        for line in lines:
            print(line)

        print(f"\nTotal (with tax): ${self.calculate_total():.2f}")


class InputHelper:
    @staticmethod
    def get_quantity():                   # Static method
        while True:
            try:                           # try / except structure
                value = int(input("Enter quantity: "))
                if value <= 0:
                    raise ValueError       # Built-in exception
                return value
            except ValueError:
                print("Invalid quantity. Please enter a positive integer.")


BUDGET = 100.0                            # Constant

product_data = [                          # List of tuples
    ("Notebook", 19.99),                  # Tuple
    ("Pen", 2.50),
    ("Bag", 49.99)
]

products = {                              # Dictionary comprehension
    name.lower(): Product(name, price)
    for name, price in product_data
}

products["bag"] = DiscountedProduct("Bag", 49.99, 0.2)
# Dictionary usage + polymorphism

added_products = set()                   # Set (stores unique product names)


def get_product(products, name):
    try:
        return products[name]             # Dictionary lookup
    except KeyError:                      # Built-in exception
        raise ProductNotFoundError(       # Custom exception
            f"Product '{name}' does not exist."
        )


cart = ShoppingCart()                     # Object creation

print("Available products:")
for product in products.values():         # Iterating over dictionary values
    print(f"- {product.name} (${product.get_price():.2f})")

while True:
    choice = input("\nEnter product name (or 'done'): ").strip().lower()
