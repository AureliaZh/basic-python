def first_last_same(lst):
    if not lst:
        return False
    return lst[0] == lst[-1]    
print(first_last_same([1, 2, 3, 4, 1]))  # True
print(first_last_same([1, 2, 3, 4, 5]))
