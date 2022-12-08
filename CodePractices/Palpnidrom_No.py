def rev(n, temp):
    num = temp
    if (n == 0):
        return temp

    temp = (temp * 10) + n % 10
    yield rev(n // 10, temp)


n = int(input("n\n"))
temp = 0
rev(n, temp)
if (temp != n):
    print(str(n) + " is palonidrom num")
else:
    print(str(n) + " is not a palonidrom")

# or
temp = n
rev = 0
while (n > 0):
    dig = n % 10
    rev = rev * 10 + dig
    n = n // 10
if (temp == rev):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")

