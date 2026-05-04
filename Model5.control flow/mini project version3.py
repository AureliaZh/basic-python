budget = 100.0

products = [
    {"name": "Notebook", "price": 19.99},
    {"name": "Pen", "price": 2.50},
    {"name": "Bag", "price": 49.99}
]

cart = []

print("Welcome to the shop!\n")


print("Available products:")
for p in products:
    print(f"- {p['name']} (${p['price']:.2f})")


while True:
    choice = input("\nEnter product name (or 'done' to finish): ").strip()

    if choice.lower() == "done":
        break

    for p in products:
        if p["name"].lower() == choice.lower():
            product = p
            break
    else:
        print("Product not found.")
        continue   

    quantity_input = input("Enter quantity: ")

    if not quantity_input.isdigit():
        print("Invalid quantity.")
        continue

    quantity = int(quantity_input)

    if quantity <= 0:
        print("Quantity must be greater than zero.")
        continue

    cart.append({
        "name": product["name"],
        "price": product["price"],
        "quantity": quantity
    })

    print(f"Added {quantity} × {product['name']} to cart.")

print("\nOrder summary:")
total_cost = 0.0

for item in cart:
    item_total = item["price"] * item["quantity"]
    total_cost += item_total
    print(f"- {item['name']}: {item['quantity']} × ${item['price']:.2f}")

pass

print(f"\nTotal cost: ${total_cost:.2f}")

if total_cost <= budget:
    print("Order is within budget.")
else:
    print(" Order exceeds budget.")
