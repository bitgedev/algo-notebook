t=int(input())
for _ in range(t):
    n=int(input())
    univ=[0]*n
    drink=[0]*n
    for i in range(n):
        s, l=input().split()
        univ[i]=s
        drink[i]=int(l)
    print(univ[drink.index(max(drink))])