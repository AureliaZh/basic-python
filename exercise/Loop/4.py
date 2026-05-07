#Count occurrences of a specific element in a list
LIST1=[1, 2, 3, 4, 5, 1, 2, 1]
TARGET=1
COUNT=0
for numbers in LIST1:
    if numbers==TARGET:
        COUNT+=1
print(COUNT)
