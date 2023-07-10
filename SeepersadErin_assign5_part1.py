"""
Erin Seepersad	3/25/23	CSCI-UA 2 - 006
Assignment #5 Problem #1

"""

factor=1
step='1'

#ask user for number
usernumber=int(input("Please enter a positive integer greater than 1: "))
#invalid
while usernumber <= 1:
    print('invalid entry. try again.')
    usernumber=int(input("Please enter a positive integer greater than 1: "))
#steps
for i in range (2,usernumber+1):
    factor*=i
    step+= ' X '+ str(i)
    print(usernumber,'!', ' -> ',sep='', end='')
    print(step,'=',format(factor, ','))
   
    
    

