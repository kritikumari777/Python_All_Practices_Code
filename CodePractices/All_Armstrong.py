# 1**3+5**3+3**3=153
#  1,153,370,371..
n = int(input("n\n"))
for i in range(1, n + 1):
    num = i
    sum = 0
    while (i > 0):
        rem = i % 10
        sum += rem ** 3
        i = i // 10
    if (num == sum):
        print(sum)


