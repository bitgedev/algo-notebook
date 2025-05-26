arr=list(range(1,31))
attend=list()
for _ in range(28):
    attend.append(int(input()))
for num in attend:
    arr.remove(num)
arr.sort()
print(arr[0])
print(arr[1])