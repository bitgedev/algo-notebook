n=int(input())
m=1
while True:
    if m==n:
        print(0)
        break
    if n-m==sum([int(ch) for ch in str(m)]):
        print(m)
        break
    m+=1