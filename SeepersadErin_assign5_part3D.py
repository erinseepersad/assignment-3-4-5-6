"""
Erin Seepersad 3/7/2023 CSCI-UA 2 - 006
Assignment #5 Problem#3D
"""


#start number
#end number
    #start and end number must be positive
    #end number must be greater than start number
counter=0
startnumber=int(input('Start Number: '))
#format(startnumber, 'underline')
endnumber= int(input('End Number: '))

if startnumber<0 or endnumber<0:
    print('Start and end must be positive')
    print()
    startnumber=int(input('Start Number: '))
    endnumber= int(input('End Number: '))
elif endnumber<startnumber:
    print('End number must be greater than start number')
    print()
    startnumber=int(input('Start Number: '))
    endnumber= int(input('End Number: '))
else:
    length=len(str(endnumber))+1
    #iterates from start -> end number
    for i in range(startnumber, endnumber):
        #0 and 1 base case, ignore
        if i == 0 or i == 1:
            continue
        #checks if current number i is prime
        isPrime = True
        for j in range(2, i):
            #if there is a number between 2 and i that divides i, it is not prime
            if i%j == 0:
                isPrime = False
        #if i is prime, print        
        if isPrime:
            print(format(str(i), '>' + str(length) + 's'), end='')
            counter+=1
        #if counter is 10, new line
        if counter == 10:
            print(' ')
            counter = 0
            continue
