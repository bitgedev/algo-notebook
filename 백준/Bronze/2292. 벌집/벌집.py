n=int(input())

cnt = 1
range_max = 1

while n > range_max:
    range_max+=6*cnt
    cnt+=1

print(cnt)