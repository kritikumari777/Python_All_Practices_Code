import math


def octtodec(n):
    dec = 0
    rem = 0
    i = 0
    while (n != 0):
        rem = n % 10
        n = n // 10
        dec = dec + rem * math.pow(8, i)
        i = i + 1
    return dectobin(dec)


def dectobin(dec):
    i = 1
    bin = 0
    while (dec != 0):
        bin += (dec % 2) * i
        dec = dec // 2
        i *= 10
    return bin


n = int(input("enter the binary number\n"))
print(octtodec(n))

