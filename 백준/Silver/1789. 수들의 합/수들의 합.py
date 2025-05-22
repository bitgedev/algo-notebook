s=int(input())
max=0
n=0
while max + (n+1) <= s:
    n+=1
    max+=n
print(n)