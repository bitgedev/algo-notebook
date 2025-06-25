n=int(input())
s=list(map(int,input().split()))
newSum=0
for i in s:
    newSum+=i/max(s)*100
print(newSum/len(s))