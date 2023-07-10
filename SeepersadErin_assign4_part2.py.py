"""
Erin Seepersad	2/27/23	CSCI-UA 2 - 006
Assignment #4 Problem #2
I worked with Beverly Ajao
"""
ognumberstep=0
average=0
evennumber=0
oddnumber=0
increase=0
factors=0
counting=0
hasincreased= False
num1=int(input('Enter a positive number: '))

#invalid
while num1<=ognumberstep:
    print('invalid entry. try again.')
    num1=int(input('Enter a positive number: '))
starting_number= num1 #assign value of num1 to num2 (still has the orginial number despite us changing it throughout the loop   
#calculations
print()
print('Calculating.....')
print()
while num1>=1:
    if num1==1:
        factors+=1
        ognumberstep+=1
        average+=num1
        oddnumber+=1
        counting+=1
        print(counting, num1 ,sep='. ', end='')
        print('-> Odd')
        break
    if num1%2==0:
        evennumber+=1
        ognumberstep+=1
        average+=num1
        counting+=1
        print(counting , num1 ,sep='. ', end='')
        print('-> Even!', end='')
        if hasincreased== True:
            print('Increased!', end='')
            hasincreased= False
        if starting_number%num1==0 and num1!=starting_number:
            print('Factor of',starting_number)
            factors+=1
        else:
            print()
        num1//= 2
    
    else:
        oddnumber+=1
        ognumberstep+=1
        average+=num1
        counting+=1
        print(counting , num1 ,sep='. ', end='')
        print('-> Odd!')
        num1=(num1*3)+1
        increase+=1
        hasincreased= True


#steps
print('It took a total of',ognumberstep, 'steps to reach the Collatz conjecture!')
print('Along the way, there were:')
print('-->', evennumber,"even number(s)")
print("-->", oddnumber,"odd number(s)")
print('-->', increase, 'increase(s)')
print('-->', factors, 'factor(s) of', starting_number)
print('The average number in the sequence is',format(average/ognumberstep, '.2f'))
      
#format is messed up 
