word=input()
reversed=""
for i in range(len(word)-1, -1, -1):
    reversed+=word[i]
print(1 if word==reversed else 0)