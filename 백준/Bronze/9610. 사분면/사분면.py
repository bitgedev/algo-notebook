n=int(input())
dots={
    "Q1":0,
    "Q2":0,
    "Q3":0,
    "Q4":0,
    "AXIS":0
}
for _ in range(n):
    x, y=map(int,input().split())
    if x==0 or y==0:
        dots["AXIS"]+=1
        continue    
    if x>0 and y>0:
        dots["Q1"]+=1
    elif x>0 and y<0:
        dots["Q4"]+=1
    elif x<0 and y>0:
        dots["Q2"]+=1
    else:
        dots["Q3"]+=1
for key in dots:
    print(f"{key}: {dots[key]}")