l=int(input())
code=input()
result=0
for i in range(l):
    result+=(ord(code[i])-96)*31**i
print(result)