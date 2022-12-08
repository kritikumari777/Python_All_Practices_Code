def sot(x):
    st=''
    for i in range(len(x)):
        st+=x[i]
        st+="_"
    return st

x=['apple','bav','cata']
print(sot(x))