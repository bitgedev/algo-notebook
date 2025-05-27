word=input()
rs=""
for i in word:
    aci=ord(i)
    if aci>=97:
        rs+=chr(aci-32)
    if aci<=90:
        rs+=chr(aci+32)
print(rs)
