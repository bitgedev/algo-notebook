x=list()
y=list()
for _ in range(3):
    a, b=map(int,input().split())
    x.append(a)
    y.append(b)
print(2*(max(x)+min(x))-sum(x), 2*(max(y)+min(y))-sum(y))