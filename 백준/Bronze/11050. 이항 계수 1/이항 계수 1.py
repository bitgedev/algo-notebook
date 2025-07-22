n, k = map(int,input().split())
m=1
s=1
z=1
for i in range(1,n+1):
    m*=i
for i in range(1,k+1):
    s*=i
for i in range(1,n-k+1):
    z*=i
print(int(m//(s*z)))