st = input()
print(st)
c = 0
for i in st:
    c = st.count(i)
    if c > 1:
        for j in range(2, (c // 2) + 2):
            if c % j == 0:
                print("no")
                break
            else:
                if (j == (c // 2) + 1):
                    st.replace(i, "")
                    print(st)

if len(st) > 0:
    print(st)
else:
    print("Marry")