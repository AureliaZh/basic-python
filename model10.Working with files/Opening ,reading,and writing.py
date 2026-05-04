
import csv

with open("product.csv", newline="") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)


with open("notes.txt") as f:
    for line in f:
        print(line.strip())
        
with open("notes.txt", "a") as f:
    f.write("- Buy bag\n")


import csv

with open("product.csv", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["name"], row["price"])

import csv

with open("product.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "price"])
    writer.writerow(["Notebook", 19.99])
    writer.writerow(["Pen", 2.5])

import csv

with open("product.csv", newline="") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
