n=int(input("enter n\n"))
def onion_peel_count(n):
    if(n==0):
        return 0
    else:
        return (1+(onion_peel_count(n-1)))
print ("total no of onion peel is:" +str(onion_peel_count (n)))