import math


def bintodes(n):
    dec = 0
    rem = 0
    i = 0
    while (n != 0):
        rem = n % 10
        n = n // 10
        dec = dec + rem * math.pow(2, i)
        i = i + 1
    return dectooct(dec)


def dectooct(dec):
    i = 1
    oct = 0
    while (dec != 0):
        oct += (dec % 8) * i
        dec = dec // 8
        i *= 10
    return oct


n = int(input("enter the binary number"))
print(bintodes(n))
