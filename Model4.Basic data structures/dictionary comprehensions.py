
numbers = [1, 2, 3, 4, 5, 6]

even_squares = {}
for n in numbers:
    if n % 2 == 0:
        even_squares[n] = n * n
print(even_squares)
even_squares = {n: n * n for n in numbers if n % 2 == 0}
print(even_squares)