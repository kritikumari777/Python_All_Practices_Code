def pare(list1, s):
    p=0
    mul=0
    while(len(list1)>1):
        flag=0;
        m=min(list1)
        list1.remove(m)
        m2=min(list1)
        list1.remove(m2)
        if(m*m2==s):
            mul=m*m2
            flag=1;
            break
    if(flag==1):
        return mul
    else:
        return "not such pare"
    
n=int(input())
s=8
list1=[]
if(n>2):
    for i in range(1, n+1):
        list1.append(int(input()))
else:
    print('-1')

if(len(list1)>0):
    print(pare(list1, s))
else:
    print('0')
