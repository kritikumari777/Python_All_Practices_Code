year = int(input("Enter a year :\n"))
if(year%4 == 0):
    if( year%100 == 0):
        if ( year%400 == 0):
            print(year, end = " ")
            print("is a leap year")
        else:
            print(year, end = " ")
            print("is not a leap year")
    else:
       print(year, end = " ")
       print("is a leap year")
else:
    print(year, end = " ")
    print("is not a leap year")