n, x=map(int, input().split())
# arr=list(range(1,n+1))
# arr.append(map(int,input().split()))
arr = list(map(int, input().split()))
output=""
for i in range(n):
    if arr[i]<x:
        output+=str(arr[i])+" "
print(output)