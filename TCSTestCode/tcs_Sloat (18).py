amt=int(input())
parent=input()
nofchild = int(input())
s=[]
comparent=0
comchild=0
if(nofchild ==0):
    comparent=amt*5*0.01
    print("TOTAL MEMBER",1+len(s))
    print("COMISSION DETAILS")
    print(parent,comparent)
else:    
    for i in range(1,nofchild+1):
        s+=(input().split(","))
    print("TOTAL MEMBER",1+len(s))
    print("COMISSION DETAILS")
    for j in range(1, nofchild+1):
        comparent+= amt*0.1
    print(parent,comparent)

    for k in s:
        comchild= amt*5*0.01
        print(k,comchild)

###or#####

parent = input()
Yes_No = input()
if Yes_No == "N":
    print("TOTAL MEMBERS:1\nCOMMISSION DETAILS\n{0}: 250 INR".format(parent))
elif Yes_No == "Y":
    child=list(map(str,input().split(",")))
    print("TOTAL MEMBERS:{}".format(len(child)+1))
    print("COMMISSION DETAILS \n{0}:{1} INR".format(parent,len(child)*500))
    for i in child:
        print("{0}:250 INR".format(i))    
'''               
Problem Statement

Chain Marketing Organization has has a scheme for income generation, through which its members generate income for themselves. The scheme is such that suppose A joins the scheme and makes R and V to join this scheme  then A is Parent Member of R and V who are child Members. When any member joins the scheme then the parent gets total commission of 10% from each of its child members.
Child members receive commission of 5% respectively. If a Parent member does not have any member joined under him, then he gets commission of 5%.
Take name of the members joining the scheme as input.
Display how many members joined the scheme including parent member.Calculate the Total commission gained by each members in the scheme. The fixed amount for joining the scheme is Rs.5000 on which commission will be generated
SchemeAmount = 5000

Example 1: When there are more than one child members 
Input : (Do not give input prompts.Accept values as follows. )
Amit                     //Enter parent Member as this
Y                           //Enter Y if  Parent member has child members otherwise enter N
Rajesh,Virat        //Enter names of child members of Amit in comma separated
Output:(Final Output must be in format given below.)
TOTAL MEMBERS:3
COMISSION DETAILS
Amit: 1000 INR
Rajesh :250 INR
Virat: 250 INR

Example 2: When there is only one child member in the hierarchy
Input :
Amit
Y
Rajesh
Output:
Total Members: 2 
Comission Details
Amit: 500 INR
Rajesh: 250 INR'''
