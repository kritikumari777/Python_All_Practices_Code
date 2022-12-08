# filter repated number from both the string and murge them.

X="kriti"
Y="printi"
sorted (X)
sorted (Y)
s=""
for i in X:
    if i not in Y:
        s+=i
for j in Y:
    if j not in X:
        s+=j
print(s)