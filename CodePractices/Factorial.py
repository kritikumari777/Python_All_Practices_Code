def factorial(n):
    if (n == 0):
        return 1

    return (n * factorial(n - 1))


n = int(input("enter the number:"))
if (n < 0):
    print("invalid input")
else:
    print(factorial(n))