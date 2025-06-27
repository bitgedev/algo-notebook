import math
n, m=map(int,input().split())
cg=math.gcd(n,m)
print(cg)
print(n*m//cg)