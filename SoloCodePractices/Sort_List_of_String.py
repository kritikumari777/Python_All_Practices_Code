def sot(x):
    z=list(x)
    y=[]
    j=97
    while(j<=122):
        for i in range(len(z)):
            if ord(z[i][0])==j:
               y.append(z[i])
        j+=1
    return y

x={'bb','vv','aa'}
print(sot(x))