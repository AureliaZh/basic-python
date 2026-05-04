
orders = [
    {
        "id": 1,
        "item": "Notebook",
        "price": 19.99,
        "quantity": 2
    },
    {
        "id": 2,
        "item": "Pen",
        "price": 2.5,
        "quantity": 5
    }
]

for order in orders:
    total = order["price"] * order["quantity"]
    print("Order", order["id"], "total:", total)
