
BUDGET = 100.0

PRODUCTS = [
    {"name": "Notebook", "price": 19.99},
    {"name": "Pen", "price": 2.50},
    {"name": "Bag", "price": 49.99}
]



def show_products(products):
    print("Available products:")
    for p in products:
        print(f"- {p['name']} (${p['price']:.2f})")


def find_product(products, name):
    for p in products:
        if p["name"].lower() == name.lower():
            return p
    return None


def get_quantity():
    while True:
        qty = input("Enter quantity: ")

        if not qty.isdigit():
            print("Quantity must be a number.")
            continue

        qty = int(qty)
        if qty <= 0:
            print("Quantity must be greater than 0.")
            continue

        return qty


def shopping_loop(products):
    cart = []

    while True:
        choice = input("\nEnter product name (or 'done'): ").strip()

        if choice.lower() == "done":
            break

        product = find_product(products, choice)

        if product is None:
            print("Product not found.")
            continue

        quantity = get_quantity()

        cart.append({
            "name": product["name"],
            "price": product["price"],
            "quantity": quantity
        })

        print(f"Added {quantity} × {product['name']}.")

    return cart


def print_summary(cart):
    print("\nOrder summary:")
    total = 0.0

    for item in cart:
        item_total = item["price"] * item["quantity"]
        total += item_total
        print(f"- {item['name']}: {item['quantity']} × ${item['price']:.2f}")

    print(f"\nTotal cost: ${total:.2f}")
    return total


def check_budget(total, budget):
    if total <= budget:
        print(" Order is within budget.")
    else:
        print(" Order exceeds budget.")



print("Welcome to the shop!\n")

show_products(PRODUCTS)
cart = shopping_loop(PRODUCTS)
total_cost = print_summary(cart)
check_budget(total_cost, BUDGET)