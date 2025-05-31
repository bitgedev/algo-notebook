n=int(input())
bestPrize=0
for _ in range(n):
    a, b, c=map(int,input().split())
    if a==b==c:
        prize=10000+a*1000
    elif a!=b and b!=c and a!=c:
        prize=max(a,b,c)*100
    else:
        prize=1000+a*100 if a==b or a==c else 1000+b*100
    bestPrize=max(bestPrize,prize)
print(bestPrize)