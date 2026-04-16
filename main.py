def check_number(num):
    if num > 0:
        return "Positive"
    elif num == 0:
        return "Zero"
    else:
        return "Negative"


class Counter:
    def __init__(self, limit):
        self.limit = limit

    def count(self):
        for i in range(self.limit):
            print("Count:", i)


numbers = [-1, 0, 2, 5]

for n in numbers:
    print(n, "is", check_number(n))

counter = Counter(3)
counter.count()