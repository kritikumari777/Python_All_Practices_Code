str1=input()
list1=[]
mul=1
for i in str1:
    if i not in list1:
        list1.append(i)
        num=str1.count(i)
        if num>1:
            f1=1
            for i in range(1,num+1):
                f1*=i
            mul*=f1
            
f2=1
for i in range(1,len(str1)+1):
    f2*=i
print(f2//mul)
