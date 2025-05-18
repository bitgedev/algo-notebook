a, b, c=map(int,input().split())
d=int(input())
sec=a*60*60+b*60+c+d
print(f"{sec//60//60%24} {sec//60%60} {sec%60}")