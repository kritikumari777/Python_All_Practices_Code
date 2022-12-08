st=input()
print(st)
sum= 0
for i in st:
    if i.isdigit():
        sum+=int(i)
print(sum)