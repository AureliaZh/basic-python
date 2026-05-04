from pathlib import Path
import csv

from shop.product import Product, DiscountedProduct
from shop.cart import ShoppingCart
from shop.errors import BudgetExceededError


BUDGET = 100.0

BASE_DIR = Path(__file__).parent
PRODUCTS_CSV = BASE_DIR / "data" / "products.csv"



def load_products_from_csv(path):
    """
    Load products from a CSV file and return a dictionary:
    key   -> lowercase product name
    value -> Product or DiscountedProduct object
    """
    products = {}

    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row["name"]
            price = float(row["price"])
            discount = row["discount"].strip()

            key = name.lower()

            if discount:
                products[key] = DiscountedProduct(
                    name,
                    price,
                    float(discount)
                )
            else:
                products[key] = Product(name, price)

    return products


def main():
    # --------- Load products ---------
    products = load_products_from_csv(PRODUCTS_CSV)

    cart = ShoppingCart()

    print("Available products:")
    for p in products.values():
        print(f"- {p.name} (${p.get_price():.2f})")

    # --------- User interaction loop ---------
    while True:
        choice = input("\nEnter product name (or 'done'): ").strip().lower()

        if choice == "done":
            break

        if choice not in products:
            print("Product not found.")
            continue

        try:
            quantity = int(input("Enter quantity: "))
            if quantity <= 0:
                raise ValueError
        except ValueError:
            print("Quantity must be a positive integer.")
            continue

        cart.add_item(products[choice], quantity)
        print(f"Added {quantity} × {products[choice].name}")

    # --------- Checkout ---------
    print("\nChecking out...")

    try:
        total = cart.calculate_total()
        cart.check_budget(BUDGET)
        print(f"Total cost: ${total:.2f}")
    except BudgetExceededError as e:
        print(e)


if __name__ == "__main__":
    main()
