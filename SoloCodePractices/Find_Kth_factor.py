number, k = [int(i) for i in input().split(" ")]
factor = []
count = 0
for i in range(1, number+1):
    if number % i == 0:
        count = count + 1
        factor.append(i)

if count < k:
    print("cant be determian k is out of range")
else:
    print(factor[k])

for i in factor:
    print(i)