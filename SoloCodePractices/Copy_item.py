list1 = [3, 5, 7, 8, 5]
list2 = list(list1)
print("original list:", list1)
print("after copying:", list2)


# or
def copy(list):
    li_copy = list[:]
    return li_copy


list = [3, 5, 7, 8, 5]
list2 = copy(list)
print("original list:", list)
print("after copying:", list2)


# or
def copying(list1):
    li_copy = [i for i in list]
    return li_copy


list1 = [3, 5, 7, 8, 5]
list2 = copying(list1)
print("original list:", list1)
print("after copying:", list2)


# or
def copying(list1):
    li_copy = list.copy()
    return li_copy


list1 = [3, 5, 7, 8, 5]
list2 = copying(list1)
print("original list:", list1)
print("after copying:", list2)


