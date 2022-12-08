def Extraction(Str):
    newst = ""
    for i in Str:
        if (i == "@"):
            break
        else:
            newst += i

    return (newst + str(len(newst)))


Str = "321kritikumari@gmail.com"
print(Extraction(Str))