n = int(input())
count = 0
sum = 0
arr = []
for i in range(2, n + 1):
    for j in range(2, (i // 2) + 2):
        if (i % j == 0):
            break
        else:
            if (j == (i // 2) + 1):
                arr.append(i)


def is_prime(sum):
    for k in range(2, (sum // 2) + 2):
        if (sum % k == 0):
            return False
        else:
            return True


for i in range(0, len(arr)):
    sum = sum + arr[i]
    if sum <= n:
        if is_prime(sum):
            count += 1

print(count)