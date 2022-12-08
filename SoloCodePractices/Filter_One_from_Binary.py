N="11101"
c=0
for i in range(0,len(N)):
    if N[i]==1:
        c=i
        print(i)
    else:
        continue
print(c)