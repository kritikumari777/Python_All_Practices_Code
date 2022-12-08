def felterCount():
    arr = [5, 3, 1]
    arr.sort()
    c = 0
    L = len(arr)
    print(arr[0])
    for i in range(arr[0], arr[L - 1]):
        if i not in arr:
            c += 1
        else:
            continue
    return c


ans = felterCount()
print(ans)
