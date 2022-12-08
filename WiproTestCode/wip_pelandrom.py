T = int(input())
if(1<=T<=20):
    for i in range(T):
        N = int(input())
        if(1<=N<=20000):
            i=0
            num=N
            res=0
            while(num>0):
                rem = num%10;
                res=(res*i)+rem
                num//=10
                i=10    
            if(N==res):
                print("wins")
            else:
                print("loses")
        else:
            print("Invalid")
else:
    print("Invalid")
       
#language: Python
