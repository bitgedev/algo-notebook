import math
n=int(input())
shirts=list(map(int,input().split()))
t, p=map(int,input().split())
orderT=0
for i in range(6):
    orderT += math.ceil(shirts[i] / t)
print(orderT)
print(n//p,n%p)