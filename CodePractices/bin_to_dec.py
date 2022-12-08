'''bin_to_dec_shot
n=input()
s=int(n,2)
print (s)'''


import math
n=int(input("enter the binary number\n"))
decimal =0
rem=0
i=0
while(n!=0):
    rem=n%10
    n=n//10
    decimal = decimal + rem*math.pow(2,i)
    i=i+1
print ("decinail number"+ str(decimal))

