modList=[]
for _ in range(10):
    n=int(input())
    modList.append(n%42)
print(len(set(modList)))