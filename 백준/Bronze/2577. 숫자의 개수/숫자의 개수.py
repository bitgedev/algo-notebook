a=int(input())
b=int(input())
c=int(input())
numbers=[0]*10
for i in str(a*b*c):
    for j in range(0,10):
        if int(i)==j:
            numbers[j]+=1
for i in numbers:
    print(i)