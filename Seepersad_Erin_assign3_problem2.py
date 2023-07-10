"""
Erin Seepersad	2/16/23	CSCI-UA 2 - 006
Assignment #3 Problem #2

"""
import random

date = 0
x = True
m = ""

# ask the user to supply a date in yyyymmdd
num=str(input("Enter a date in YYYYMMDD format or the word RANDOM: "))

#if user input is random
if num == "RANDOM":
        #generate random number
        date = random.randint(10000000,99999999)
        print("The computer selected: ", date)
else:
        #date = user input
        date = int(num)

#get year month and date
day = int(date%100)
month = int(date/100)%100
year = int(date/10000)
        

#check if month is valid
if month == 9 or month == 4 or month == 6 or month == 11:
    if day > 30:
        print("This is NOT a valid date")
        x = False
    elif month == 9:
        m = "September "
    elif month == 4:
        m= "May "
    elif month == 6:
        m="June "
    elif month == 11:
        m= "Novemember "
elif month == 1 or month==3 or month==5 or month== 7 or month== 8 or month==10 or month==12:
    if day > 31:
        print("This is NOT a valid date")
        x = False
    elif month == 1:
        m="January "
    elif month == 3:
        m="March "
    elif month == 5:
        m="May "
    elif month == 7:
        m="July "
    elif month == 8:
        m="August "
    elif month == 10:
        m="October "
    elif month == 12:
        m="December "
elif month == 2:
    if day > 28:
        print("This is NOT a valid date")
        x = False
    elif month == 2:
        m= 'February '
elif month > 12:
    print("This is NOT a valid date")
    x = False

if x == True:
    #prints dates
    if day == 1 or day == 21 or day == 31:
        print(m, day,"st" ,sep="", end=", ")
    elif day == 2 or day== 22:
        print(m,day,'nd', sep="", end=", ")
    elif day == 3 or day== 23:
        print(m,day,'rd', sep="", end=", ")
    else:
        print(m,day,'th', sep="", end=", ")

    print(year,end=' is a valid date')
    

