n=int(input())
ct=0
nct=0
for _ in range(n):
    vote=int(input())
    if vote==1:
        ct+=1
    else:
        nct+=1
print("Junhee is not cute!" if nct>ct else "Junhee is cute!")