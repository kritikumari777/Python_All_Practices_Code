a=int(input())
b=int(input())
matric=[]
lst=[]
for i in range(a):
    c=[]
    for j in range(b):
        j=int(input(str(i)+" "+ str(j)+" "))
        c.append(j)
    print()
    matric.append(c)
for j in range(b):
    sum1=0
    for i in range(a):
        sum1+=matric[j][i]
        lst.append(sum1)
    print(sum1)
    print()
print(max(lst))
