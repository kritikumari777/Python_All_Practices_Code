s = input()
count = 0
for i in range(1, len(s) + 1):
    count += 1
print(count - (len(s.split())))

# or
c = len(s) - s.count(" ")
print(c)

# or
con = 0
for j in s:
    if (j == " "):
        continue  # cant be j+1, str & int
        # not concatinet
    else:
        con += 1
print(con)
# if(k.space()): str obj has not space attribute
