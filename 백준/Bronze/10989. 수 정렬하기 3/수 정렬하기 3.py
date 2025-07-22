import sys

n=int(sys.stdin.readline()) # sys.stdin.readline() 입력단축
num=0
count = [0] * 10001
for _ in range(n):
    num = int(sys.stdin.readline())
    count[num] += 1

for i in range(1,10001):
    if count[i] > 0:
        for _ in range(count[i]):
            sys.stdout.write(f"{i}\n") # sys.stdout.write() 출력단축