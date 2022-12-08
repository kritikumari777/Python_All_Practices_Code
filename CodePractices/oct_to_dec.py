import math
n=int(input("enter the binary number"))
decimal =0
rem=0
i=0
while(n!=0):
    rem=n%10
    n=n//10
    decimal = decimal + rem*math.pow(8,i)
    i=i+1
print ("\ndecinail number"+ str(decimal))

