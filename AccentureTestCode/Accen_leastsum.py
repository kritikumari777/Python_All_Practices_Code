def lestsum(s,lst1):
    l1=0
    l2=0
    m=0
    f=0
    while(len(lst1)>0):
        l1=min(lst1)
        lst1.remove(l1)
        l2=min(lst1)
        lst1.remove(l2)
        if l2+l1<s :
            m=(l1*l2)
            f=1
            break
    if f>0:
        print(m)
    else:
        print("such a pare not found")        
s=int(input())
n=int(input())
lst1=[]
if n>2:
    for i in range(1,n+1):
        lst1.append(int(input()))
else:
    print('-1')
    
if len(lst1)>0:
    lestsum(s,lst1)
else:
    print('0')
        
