#sum of all even number
n=int(input())
lst=[int(i) for i in input().split()]
sum=0
for i in lst:
    if i%2==0:
        sum+=i
print(sum)