s=input()
indexList=list()
for i in range(97,123):
    indexList.append(s.find(chr(i)))
print(*indexList)