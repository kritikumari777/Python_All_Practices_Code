test_list = [1,3,5,6,3,5,6,1]
test_list =list(set(test_list ))
print ("the list after removing duplicates:" + str(test_list ))

test_list = [1, 3, 5, 6, 3, 5, 6, 1]
res = []
for i in test_list:
    if i not in res:
        res.append(i)
print ("the list after removing duplicates:"+str(res))
