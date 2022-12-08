n=int(input("n\n"))
def fibonacci(i):
    if(i==1 or i==2):
        return 1
    else:
        return(fibonacci(i-1)+fibonacci(i-2))
for i in range(1, n+1):
    print (fibonacci(i))