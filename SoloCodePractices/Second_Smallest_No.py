list1 = [10, 20, 4, 45, 99]
list1.sort()
print("Second smallest element is:", list1[1])
print("Second largest element is:", list1[-2])

#or
# Python prog to illustrate the following in a list

def find_len(list):
    l = len(list)
    list.sort()
    print("Largest element is:", list[l-1])
    print("Smallest element is:", list[0])
    print("Second Largest element is:", list[l-2])
    print("Second Smallest element is:", list[1])

# Driver Code
list=[12, 45, 2, 41, 31, 10, 8, 6, 4]
Largest = find_len(list)



