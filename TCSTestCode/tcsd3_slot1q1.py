c={1:'esspresso Coffee',2:'cappuccino coffee',3:'latte coffee'}
t={1:'plain tea',2:'assam tea',3:'Ginger tea',4:'cardamom tea',5:'masala tea',
   6:'lemon Tea',7:'Green tea',8:'organic darjeeling tea'}
s={1:'Hot and sour soup',2:'veg corn soup',3:'tomato soup',4:'spicy tomato soup'}
b={1:'hot chocolate drink',2:'badam drink',3:'badam-pista drink'}

M_m=input()
S_m=int(input())
if(M_m=='c'):
    if S_m in c:
        print("enjoy your",c[S_m])
    else:
        print("INVALID INPUT")           
elif(M_m=='t'):
    if S_m in t:
       print("enjoy your",t[S_m])
    else:
        print("INVALLD INPUT")
elif(M_m=='s'):
    if S_m in s:
        print("enjoy your",s[S_m])
    else:
        print("INVALID INPUT")
elif(M_m=='b'):
    if S_m in b:
        print("enjoy your",b[S_m])
    else:
        print("INVALID INPUT")
            

####or####

menu = [['Espresso Coffee','Cappuucino Coffee','Latte Coffee'], ['Plain Tea',

'Assam Tea','Ginger Tea','Cardamom Tea','Masala Tea','Lemon Tea','Green Tea',

'Organic Darjeeling Tea'], ['Hot and Sour Soup','Veg Corn Soup','Tomato Soup',

'Spicy Tomato Soup'], ['Hot Chocolate Drink', 'Badam Drink',

'Badam-Pista Drink']]

m = input()

if m=='c' or m=='t' or m=='s' or m=='b':

    if m=='c':

        submenu = int(input())

        if submenu in range(3):

            print('Welcome to CCD!\nEnjoy your {}!'.format(menu[0][submenu-1]))

        else:

            print("INVALID INPUT")

    if m=='t':

        submenu = int(input())

        if submenu in range(8):

            print('Welcome to CCD!\nEnjoy your {}!'.format(menu[1][submenu-1]))

        else:

            print("INVALID INPUT")

    if m=='s':

        submenu = int(input())

        if submenu in range(4):

            print('Welcome to CCD!\nEnjoy your {}!'.format(menu[2][submenu-1]))

        else:

            print("INVALID INPUT")

    if m=='b':

        submenu = int(input())

        if submenu in range(3):

            print('Welcome to CCD!\nEnjoy your {}!'.format(menu[3][submenu-1]))

        else:

            print("INVALID INPUT")

else:

    print("INVALID INPUT!")        

'''FULLY AUTOMATIC VENDING MACHINE – dispenses your cuppa on just press of button. A vending machine can serve range of products as follows:

Coffee

Espresso Coffee
Cappuccino Coffee
Latte Coffee
Tea

Plain Tea
Assam Tea
Ginger Tea
Cardamom Tea
Masala Tea
Lemon Tea
Green Tea
Organic Darjeeling Tea
Soups 

Hot and Sour Soup
Veg Corn Soup
Tomato Soup
Spicy Tomato Soup
Beverages

Hot Chocolate Drink
Badam Drink
Badam-Pista Drink
Write a program to take input for main menu & sub menu and display the name of sub menu selected in the following format (enter the first letter to select main menu):

Welcome to CCD 

Enjoy your

Example 1:

Input:
c
1
Output
Welcome to CCD!
Enjoy your Espresso Coffee!
Example 2:

Input
t
9
Output
INVALID OUTPUT!'''

