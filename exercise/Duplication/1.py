data=[1,2,2,3,4,3,1]
unique_data=[]
for n in data:
    if n not in unique_data:
        unique_data.append(n)
print(f"unique_data: {unique_data}")