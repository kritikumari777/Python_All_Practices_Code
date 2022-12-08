def defofsum(n,m):
    list1 =[]
    list2 =[]

    for i in range(1, m+1):
        if(i%n==0):
           list1.append(i)
        else:
            list2.append(i)

    print(list1)
    print(list2)
    list1sum = sum(list1)
    list2sum = sum(list2)
    return list1sum-list2sum
    
n=2;
m=10;

if(n>0 and m>0):
    print(defofsum(n, m))
else:
    print("INVALID INPUT")
