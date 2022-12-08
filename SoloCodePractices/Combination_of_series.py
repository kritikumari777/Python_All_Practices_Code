# 1 2 1 3 2 5 3
n = int(input("enter the number"))


def prime(n):
    for j in range(2, n + 1):

        for k in range(2, (j // 2) + 2):
            if (j % k == 0):
                break
            else:
                if (k == (j // 2) + 1):
                    print(j)


def fabonacci(n):
    for m in range(1, n + 1):
        if (m == 1 or m == 2):
            print("1")
        else:
            print((m - 1) + (m - 2))


for i in range(1, n + 1):
    if (i % 2 == 0):
        prime(n)
    else:
        fabonacci(n) 