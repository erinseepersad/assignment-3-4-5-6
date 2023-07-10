"""
Erin Seepersad	2/27/23	CSCI-UA 2 - 006
Assignment #4 Problem #1
I worked with Beverly Ajao
"""
column=0
#ask user to enter a number
numcol= int(input("Enter a number: "))
    
#invalid 
while numcol<=column:
    print('invalid try again')
    numcol= int(input("Enter a number: "))

#making the column
while column<numcol:
    print(' '*column+'* *')
    column+=1

while column>=0:
    print(' '*column+'* *')
    column-=1
    

    
