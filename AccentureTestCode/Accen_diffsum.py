n=int(input())
list1=[]
for i in range(1,n+1):
    list1.append(input())

print(list1)
list2=list1[::-1]
print(list2)
s=0
for i in range(0,len(list1)):
    n1=list1[i]
    n2=list2[i]
    s+=int(n1)-int(n2)
    print(s)   
    
