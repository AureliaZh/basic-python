data=[1,2,3,4,5]
group={}
for n in data:
    if n%2==0:
        group.setdefault('even',[]).append(n)
    else:
        group.setdefault('odd',[]).append(n)
print(group)