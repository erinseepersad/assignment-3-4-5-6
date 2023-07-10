"""
Erin Seepersad	2/16/23	CSCI-UA 2 - 006
Assignment #3 Problem #1

"""
print("Welcome to Haagen-Dazs online ordering system!")
print("Customize your order by answering the following question.")
# container type and price
container= input("Would you like a cup(c) or cone(n)? ")
if container == "c":
        containerprice= 1.00
elif container == "n":
        containerprice= 2.75

#number of scoops and price
scoops= float(input("How many scoops of ice cream would you like? "))
if scoops == 1:
    scoops= 2.00
elif scoops == 2:
    scoops= 2.75
elif scoops == 3:
    scoops =3.50

# number of toppings and price per topping
topping=int(input("How many toppings would you like to add? "))
if topping==0:
        top= 0.00
elif topping <= 3:
        top = 1.25
elif topping <= 6:
        top= 1.00
elif topping >= 7:
        top= 0.75
toppingcharge= topping*top
total= toppingcharge+scoops+containerprice
print()
print("Adding to cart...")
print()
print("Container Charge: ",format(containerprice,'.2f'), sep='$')
print("Scoop Charge: ", format(scoops,'.2f'), sep='$')
print("Topping Charge: ", topping," topping(s) x $", format(top,'.2f')," = ", "$",format(toppingcharge,'.2f'), sep='')
print("Total: ", total, sep='$')


