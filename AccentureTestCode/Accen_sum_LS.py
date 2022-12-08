def sum_ls(list1):
    if len(list1)>3:
        arr1=[]
        arr2=[]
        for i in range(0,len(list1)):
            if i%2==0:
                arr1.append(list1[i])
            else:
                arr2.append(list1[i])
        print(arr1)
        print(arr2)
        arr1.remove(max(arr1))
        arr2.remove(min(arr2))
        print(arr1)
        print(arr2)
        return(max(arr1)+ min(arr2))
    else:
        return 0
list1=[]
n=int(input())
for i in range(0,n):
    list1.append(int(input()))
print(sum_ls(list1))
