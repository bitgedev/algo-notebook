t=int(input())
rs=[0,0,0]
a=60*5
b=60
c=10
noAnswer=False
if t>=a:
    rs[0]=t//a
    t%=a
if t>=b:
    rs[1]=t//b
    t%=b
if t>=c:
    rs[2]=t//c
    t%=c
if t!=0:
    noAnswer=True
if noAnswer:
    print(-1)
else:
    print(rs[0], rs[1], rs[2])