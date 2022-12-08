def dec_to_oct(dec):
    oct = 0
    i = 1
    while (dec != 0):
        oct = oct + (dec % 8) * i
        dec = dec // 8
        i = i * 10
    return oct


dec = int(input("enter the decmal num"))
print("\noctal num", dec_to_oct(dec))