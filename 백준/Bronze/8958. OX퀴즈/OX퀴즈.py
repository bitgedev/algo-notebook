n=int(input())
for _ in range(n):
    quiz=input()
    score=0
    consecutive=0
    for i in quiz:
        if i=="O":
            consecutive+=1
            score+=consecutive
        else:
            consecutive=0
    print(score)