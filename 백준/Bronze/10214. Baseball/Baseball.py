t=int(input())
for _ in range(t):
    yw=0
    kw=0
    for _ in range(9):
        y, k=map(int,input().split())
        yw+=y
        kw+=k
    if yw>kw:
        print("Yonsei")
    elif yw<kw:
        print("Korea")
    else:
        print("Draw")