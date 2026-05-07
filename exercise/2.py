numbers=[]
for i in range(1,6):
    numbers.append(i)
print(numbers)

person=("Alice","20","New York")

name,age,city=person
print(person)

student={"name":"Tom","age":20,"score":85}
print(student["score"])
student["score"]=90
print(student["score"])

numbers=[1,2,3,4,5,6]
evens=[n for n in numbers if n%2==0]
print(evens)

score=72
if score>=60:
    print("pass")
else:
    print("fail")

numbers=[1,2,3,4,5,6,7,8,9,10]
odd=[n for n in numbers if n%2 !=0]
print(odd)

count=1
while count<=5:
    print(count)
    count+=1


n = 7
is_prime = True

for i in range(2, n):
    if n % i == 0:
        is_prime = False
        break

if is_prime and n > 1:
    print("Prime")
else:
    print("Not Prime")

