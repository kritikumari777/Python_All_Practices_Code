def diffofsum(n,m):
    list1=[]
    list2=[]
    for i in range(1,m+1):
        if i%n==0:
            list1.append(i)
        else:
            list2.append(i)
    print(list1)
    print(list2)
    s1=sum(list1)
    s2=sum(list2)
    print(s1,s2)
    if s1>s2:
        return s1-s2
    else:
        return s2-s1

n=int(input())
m=int(input())
if n>0 and m>0:
    print(diffofsum(n,m))
else:
    print("invalid input")
