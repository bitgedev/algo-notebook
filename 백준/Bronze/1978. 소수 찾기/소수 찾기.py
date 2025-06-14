n=int(input())
x=list(map(int,input().split()))
primeCount=0
for i in range(0, n):
    isPrime=True
    if x[i]==1:
        isPrime=False
    else:
        for j in range(2,x[i]):
            if x[i]%j==0:
                isPrime=False
                break
    if isPrime:
        primeCount+=1
print(primeCount)