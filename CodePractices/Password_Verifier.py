'''Write a program that takes in a string as input and evaluates it as a valid password. The password is valid if it has at a minimum 2 numbers, 2 of the following special characters ('!', '@', '#', '$', '%', '&', '*'), and a length of at least 7 characters.
If the password passes the check, output 'Strong', else output 'Weak'.'''

l, u, d, s = 0, 0, 0, 0

a = input()

if (len(a) >= 7):
    for i in a:
        if (i.islower()):
            l += 1
        if (i.isupper()):
            u += 1
        if (i.isdigit()):
            d += 1
        if (i == "@" or i == "#" or i == "$" or i == "%" or i == "&" or i == "!" or i == "*"):
            s += 1
if (l >= 1 and u >= 1 and d >= 2 and s >= 2 and l + u + d + s == len(a)):
    print("Strong")
else:
    print("Weak")  