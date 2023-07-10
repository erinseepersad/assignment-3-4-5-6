"""
Erin Seepersad 3/7/2023 CSCI-US 2 -006
Assignment #5 Problem3C
"""
#start number
#end number
    #start and end number must be positive
    #end number must be greater than start number

startnumber=int(input('Start Number: '))
#format(startnumber, 'underline')
endnumber= int(input('End Number: '))
if startnumber<0 or endnumber<0:
    print('Start and end must be positive')
    print()
    startnumber=int(input('Start Number: '))
    endnumber= int(input('End Number: '))
if endnumber<startnumber:
    print('End number must be greater than start number')
    print()
    startnumber=int(input('Start Number: '))
    endnumber= int(input('End Number: '))
print()    
while startnumber<=endnumber:
    for i in range(startnumber):
        if i==0 or i==1:
            continue
        elif startnumber%i==0:
            break
        if i == startnumber-1:
            print(startnumber)
    startnumber+=1

    
