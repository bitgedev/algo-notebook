sc=input()
op=0
if "A" in sc:
    op+=4
elif "B" in sc:
    op+=3
elif "C" in sc:
    op+=2
elif "D" in sc:
    op+=1

if "+" in sc:
    op+=0.3
elif "-" in sc:
    op+=-0.3
else:
    op=float(op)
print(op)