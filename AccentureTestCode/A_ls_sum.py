def ls_sum(list1):
    even=[]
    odd=[]
    L=len(list1)
    for i in range(0,L):
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    even.sort()
    odd.sort()
    S=len(even)
    l=even[S-1]
    s=odd[1]
    print(l+s)
    
list1=[]
list1= input().split(" ")
print(list1)
ls_sum(list1)
    
