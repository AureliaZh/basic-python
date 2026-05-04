
students = [
    {"name": "Alice", "age": 20},
    {"name": "Bob", "age": 22},
    {"name": "Charlie", "age": 21}
]

names = []
for student in students:
    names.append(student["name"])

names = [student["name"] for student in students]
print(names)
