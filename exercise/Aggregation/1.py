data = [10, 20, 30, 40]

avg = sum(data) / len(data)
count = sum(1 for n in data if n > avg)

print(count)