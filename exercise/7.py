
def merge_unique(list1, list2):
    result = []
    for num in list1 + list2:
        if num not in result:
            result.append(num)
    return result
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
merged_list = merge_unique(list1, list2)
print(merged_list)  # Output: [1, 2, 3,