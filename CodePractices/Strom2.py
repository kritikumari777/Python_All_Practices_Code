# 145 is a strom number 1!+4!+5!=145
n = int(input("n\n"))
sum = 0
temp = n
while (n >= 1):
    i = 1
    f = 1
    r = n % 10
    while (i <= r):
        f = f * i
        i = i + 1
    n = n // 10
    sum = sum + f
if (sum == temp):
    print(str(sum) + " is a strom num")
else:
    print(str(sum) + " not a strong num")


