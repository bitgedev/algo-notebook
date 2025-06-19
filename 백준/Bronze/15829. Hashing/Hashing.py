l=int(input())
code=input()
result=0
mod = 1234567891
for i in range(l):
    result+=(ord(code[i])-96)*pow(31, i, mod)
    result%=mod
print(result)