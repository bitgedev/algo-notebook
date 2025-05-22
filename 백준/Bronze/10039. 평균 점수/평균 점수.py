def check(score):
    if score < 40:
        score = 40
    return score
a=check(int(input()))
b=check(int(input()))
c=check(int(input()))
d=check(int(input()))
e=check(int(input()))
print((a+b+c+d+e)//5)