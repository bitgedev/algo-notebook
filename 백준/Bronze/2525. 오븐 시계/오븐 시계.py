a, b=map(int,input().split())
c=int(input())
min=a*60+b+c
print(f"{min//60%24} {min%60}")