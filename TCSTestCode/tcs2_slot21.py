n= int(input())
m=int(input())
p=int(input())
k=int(input())
j=int(input())
count1=0
count2=0
if(n>0 and m>0 and p>0 and k>0 and j>0):
    
    for x in range(1,m+1):
        if(x%k==0):
            count1+=1

    for y in range(1,p+1):
        if(y%j==0):
            count2+=1
    print('Number of  Monkeys left on the tree:',n-(count1+count2))
else:
    print("invalid input")
###or####
n= int(input())
m=int(input())
p=int(input())
k=int(input())
j=int(input())
atebanana=0
atepeanut=0
if(n>0 and m>0 and p>0 and k>0 and j>0):
    
    if(k>0):
        atebanana=m//k
    if(j>0):
        atepeanut=p//j

    print('Number of  Monkeys left on the tree:',n-(atebanana+atepeanut))
else:
    print("invalid input")
    
'''
There are total n number of Monkeys sitting on the branches of a huge Tree.
As travelers offer Bananas and Peanuts, the Monkeys jump down the Tree.
If every Monkey can eat k Bananas and j Peanuts.
If total m number of Bananas and p number of Peanuts are offered by travelers,
calculate how many Monkeys remain on the Tree after some of them jumped down toeat.
At a time one Monkeys gets down and finishes eating and go to the other side ofthe road.
The Monkey who climbed down does not climb up again after eating untilthe other Monkeys finish eating.
Monkey can either eat k Bananas or j Peanuts. If for last Monkey there are less
than k Bananas left on the ground or less than j Peanuts left on the ground,
only that Monkey can eat Bananas(<k) along with the Peanuts(<j).
Write code to take inputs as n, m, p, k, j and return  the number of Monkeysleft on the Tree.
    Where, n= Total no of Monkeys
        k= Number of eatable Bananas by Single Monkey
        (Monkey that jumped down last may get less than k Bananas)
        j = Number of eatable Peanuts by single Monkey
        (Monkey that jumped down last may get less than j Peanuts)
        m = Total number of Bananas
        p  = Total number of Peanuts
Remember that the Monkeys always eat Bananas and Peanuts,
so there is no possibility of k and j having a value zero

Example 1:
Input Values    
20
2
3
12
12

Output Values
Number of  Monkeys left on the tree:10

Note: Kindly follow  the order of inputs as n,k,j,m,p as given in the above example.
And output must include  the same format  as in above example
(Number of Monkeys left on the Tree:)
For any wrong input display INVALID INPUT'''
