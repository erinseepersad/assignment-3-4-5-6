"""
Erin Seepersad	3/7/23	CSCI-UA 2 - 006
Assignment #5 Problem #3B
""""""
#ask for a number
asknumber=int(input('Enter a positive number to test: '))
print()
#invalid
while asknumber < 0:
    print('invalid number. please try again')
    asknumber=int(input('Enter a positive number to test: '))
 """
#accumulator 
targetnumber=1000
currentnumber=2

#invalid
print('1 is technically a prime number.')


#output
while currentnumber!=targetnumber:
    isPrime = True
    for i in range(3, currentnumber):
        if currentnumber%i==0:
            isPrime = False
    if isPrime:
            print(currentnumber, 'is a prime number!')
    currentnumber+=1
    
        
"""    
#is it a prime?
for asknumber in range (2,1000+1):
    if asknumber%asknumber!=0:
        print(str(asknumber),'is NOT a divisor of',asknumber,'... continuing')
        break
    else:
        if asknumber== asknumber:
            print()
            print(str(asknumber), 'is a prime number!')
        else:
            print()
            print(asknumber, 'is not a prime number.')
    if asknumber == asknumber:
        print(asknumber, 'is a prime number!')
        """
    
    

   
                      



    
