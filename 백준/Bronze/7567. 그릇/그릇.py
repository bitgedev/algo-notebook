plates=input()
height=10
for i in range(len(plates)-1):
    if plates[i] == plates[i+1]:
        height+=5
    else:
        height+=10
print(height)