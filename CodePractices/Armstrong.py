# amostrong number 1**3+5**3+3**3.
n= int(input("n\n"))
num=n
res=0
while(n>0):
    rem= n%10
    n=n//10
    res+=rem**3
if(res==num):
    print (str(num)+" is amostrong num")
else:
    print ("not a amostrong num")