n=int(input())
s=int(input())
list1=[]
if n>2:
    for i in range(n):
        list1.append(int(input()))
else:
    print('-1')

list1.sort()
for i in range(0,len(list1)-1):
    sum1= list1[i]+list1[i+1]
    if sum1<s:
        print(list1[i]*list1[i+1])
        break
    else:
        print('0')
    
