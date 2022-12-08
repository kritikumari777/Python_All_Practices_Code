input1=input()
input2=int(input())
s1=""
c=""
i=0
while(i<len(input1)):
    if input1[i].isdigit():
        for j in range(i):
            s1+=c
            i+=1
    else:
        s1+=input1[i]
        c=input1[i]
        i+=1
print(s1)
print(s1[input2])