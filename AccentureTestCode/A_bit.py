def bit(str1):
    str1.split()
    res=0
    i=0
    
    while(i>len(str1)):
        if str1[i+1]=='A':
            res=str1[i] and str1[i+2]
            str1[i+2]=res
            i+=2
        elif str1[i+1]=='B':
            res= str1[i] or str1[i+2]
            str1[i+2]=res
            i+=2
        #elif: str1[i]=='C':
            #if str1[i] 
        else:
            i+=1
    print(res)    
            
str1=input()
if len(str1)%2!=0:
    bit(str1)
