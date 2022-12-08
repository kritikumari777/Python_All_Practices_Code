str1=input().split()
list1=[]
for i in str1:
    list1.append(len(i))
print(list1)
m=max(list1)
if m%2!=0:
    for i in str1:
        if m==len(i):
            print(i)
            break
    
else:
    print('better luck for next time')

#or
str1=input().split()
list1=[]
for i in str1:
    if len(i)%2!=0:
        list1.append(len(i))
if max(list1)==0:
    print("better luck for nexxt time")
else:
    for i in str1:
        if len(i)==max(list1):
            print(i)
        
