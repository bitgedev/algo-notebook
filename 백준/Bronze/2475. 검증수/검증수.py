code=input().replace(" ", "")
rs=0
for i in code:
    rs+=int(i)**2
print(rs%10)