word = input()
str = word.lower()

for i in range(len(str)):
    if (i != " "):
        ch = chr(ord('z') - ord(str[i]) + ord('a'))
        print(ch, end='')

    else:
        i += 1
