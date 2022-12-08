T=int(input())
n=int(input())
sum=0
for i in range(n):
    b=bin(i)
    sum+=int(b[2::])
print(sum)
