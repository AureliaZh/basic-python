budget = 100.00

products = [
    {"name": "Notebook", "price": 19.99},
    {"name": "Pen", "price": 2.50}
]

print("Available products:")
for p in products:
    print(f"- {p['name']} (${p['price']:.2f})")

print("\nEnter quantity for each product:")

products_with_quantity = [
    {
        **product,
        "quantity": int(input(f"{product['name']} quantity: "))
    }
    for product in products
]

item_totals = [
    p["price"] * p["quantity"]
    for p in products_with_quantity
]

total_cost = sum(item_totals)

within_budget = total_cost <= budget


print("\nOrder summary:")
for p in products_with_quantity:
    print(
        f"- {p['name']}: "
        f"{p['quantity']} × ${p['price']:.2f}"
    )

print(f"\nTotal cost: ${total_cost:.2f}")
print(f"Within budget: {within_budget}")
