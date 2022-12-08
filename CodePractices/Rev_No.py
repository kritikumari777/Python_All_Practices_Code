n=int(input("enter the num"))
rev=0
rem=0
while (n!=0):
    rem=n%10
    n=n//10
    rev=rev*10+rem
print ("reverse the num"+ str(rev))

#or
rev_nun =0
base=1
def rev_digits(num):
    global rev_nun
    global base
    if(num > 0):
        rev_digits(num//10)
        rev_nun+=(num%10)*base
        base*=10
    return rev_nun
num=110
print ("reverse",rev_digits(num))