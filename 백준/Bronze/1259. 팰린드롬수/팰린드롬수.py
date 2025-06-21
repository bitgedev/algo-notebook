while True:
    n=input()
    if n=="0":
        break
    pel="yes"
    for i in range(len(n)):
        if n[i]==n[len(n)-1-i]:
            continue
        else:
            pel="no"
    print(pel)