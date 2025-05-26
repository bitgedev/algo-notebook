n, m=map(int, input().split())
matrix = [[0]*m for _ in range(n)]
for _ in range(2):
    for i in range(0,n):
        row=list(map(int,input().split()))
        for j in range(0,m):
            matrix[i][j]+=row[j]
for i in range(0,n):
    s=""
    for j in range(0,m):
        s += str(matrix[i][j])+" "
    print(s)