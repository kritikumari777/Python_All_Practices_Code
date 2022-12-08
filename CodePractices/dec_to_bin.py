'''n=input()
s=int(n,2)
print (s)'''

import math
def dectobin(n):
    bin=0
    i=1
    while (n!=0):
        rem= n % 2
        n=n//2
        bin= bin+ rem*i
        i=i*10
    return bin
n=int(input("enter the number"))
print (dectobin (n))    
