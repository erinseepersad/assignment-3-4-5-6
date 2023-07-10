"""
Erin Seepersad	3/7/23	CSCI-UA 2 - 006
Assignment #5 Problem #3A
"""
#ask for a number
asknumber=int(input('Enter a positive number to test: '))
print()
#invalid
while asknumber < 0:
    print('invalid number. please try again')
    asknumber=int(input('Enter a positive number to test: '))
    
#is it a prime?
    
for i in range (2,asknumber+1):
    if asknumber%i!=0:
        print(str(i),'is NOT a divisor of', asknumber,'... continuing')
    else:
        if i== asknumber:
            print()
            print(str(i), 'is a prime number!')
            break
            print(str(i),'is a divisor of', asknumber,'... stopping')
            break
        else:

            print(str(i),'is a divisor of', asknumber,'... stopping')
            print()
            print(asknumber, 'is not a prime number.')
            break
    if i == asknumber:

        print(asknumber, 'is a prime number!')
        break
    

   
                      



    
