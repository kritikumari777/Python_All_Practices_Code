def swapposs(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list


list = [2, 4, 3, 5, 6, 8]
pos1, pos2 = 1, 2
print(swapposs(list, pos1, pos2))


def swapposs(list):
    temp = list[0]
    list[0] = list[1]
    list[1] = temp
    return list


list = [1, 3, 5, 6, 7]
print(swapposs(list))