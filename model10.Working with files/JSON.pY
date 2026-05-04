import csv
import json

products = []

with open("product.csv", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        products.append(row)

print("From CSV:")
print(products)
print()

with open("product.json", "w") as f:
    json.dump(products, f, indent=2)

print("Written to product.json")
print()


with open("product.json") as f:
    loaded_products = json.load(f)

print("From JSON:")
for item in loaded_products:
    print(item["name"], item["price"])