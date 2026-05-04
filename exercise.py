
item_name = "Notebook"
item_price = 19.99     
budget = 50.0          

first_name = "Aurelia"
last_name = "Zhang"
customer_name = first_name + " " + last_name

print("Customer:", customer_name)
print("Item:", item_name)
print("Price per item:", item_price)

user_input = input("Enter quantity: ")
quantity = int(user_input)

final_total = quantity * item_price
print("Final total:", f"{final_total:.2f}")


if final_total <= budget:
    within_budget = True
    print("Order is within budget.")
else:
    within_budget = False
    print("Order exceeds budget.")

hex_order_id = "ff"
order_id = int(hex_order_id, 16)
print("Order ID:", order_id)

confirmation_message = (
    "Order confirmed for "
    + customer_name
    + ". Quantity: "
    + str(quantity)
    + ". Total amount: "
    + str(final_total)
)


encoded_message = confirmation_message.encode("utf-8")

print("Encoded confirmation message:")
print(encoded_message)