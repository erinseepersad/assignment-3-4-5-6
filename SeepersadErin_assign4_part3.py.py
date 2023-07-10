"""
Erin Seepersad	2/27/23	CSCI-UA 2 - 006
Assignment #4 Problem #3
I worked with Beverly Ajao
"""
#new version 
import random
turns=0
player= 1
num1=int(input('How many sticks(10-100)? '))
#invalid 
while num1>100 or num1<10:
    print("Sorry, that's too many sticks. Try again")
    num1=int(input('How many sticks(10-100)? '))
#calculations
print("Great Let's play ...")
while num1>=10 and num1<=100:
    print()
    while True:
        if turns==0:
            #even
            print('Turn: Player', player)
            print('There are', num1, 'on the table')
            num2= int(input('How many sticks do you want to take (1,2 or 3)? '))
            while num2!=3 and num2!=1 and num2!=2:
                print("Sorry, that's not a valid number")
                print()
                num2=int(input('How many sticks do you want to take (1,2 or 3)? '))
            while num2>num1:
                print('Sorry that would brng the total # of sticks below 0. Try again')
                print()
                num2= int(input('How many sticks do you want to take (1,2 or 3)? '))
            if num1>num2:
                num1-=num2
                turns+=1
                print()
            elif num2>=num1:
                print()
                print('There are no sticks left on the table!Game over.')
                if turns==0:
                    print('Player 2 wins!')
                else:
                    print('Player 1 wins!')
                break
            
            #odd
        elif turns==1:
            print('Turn: Player 2')
            print('There are', num1, 'on the table')
            num2= random.randint(1,4)
            print('Computer picked: ',num2)
            while num2>num1:
                print('Sorry, that would bring the total # of sticks below 0. Try again.')
                print()
                print('Turn: Player 2')
                print('There are', num1, 'on the table')
                print('Computer picked:', num2)
                num2= random.randint(1,4)
            if num1>num2:
                num1-=num2
                turns-=1
                print()
            elif num2>=num1:
                print()
                print('There are no sticks left on the table! Game over.')
                if turns==0:
                    print('Player 2 wins!')
                else:
                    print('Player 1 wins!')
                break
                   
""" old version -- CHECK FOR RUNNING TWO 
    print('Turn: Player', player)
    print('There are', num1, 'on the table')
    num2= int(input('How many sticks do you want to take (1,2 or 3)? '))
    if player==1:
        num2=int(input('How many sticks do you want to take (1,2 or 3)? '))
        if num2>3 or num2<1:
            print("Sorry, that's not a valid number")
            print()
        elif num2>num1:
            print('Sorry, that would bring the total # of sticks below 0. Try again.')
            print()
        else:
            break
        num1-=num2
    else:
        print()
        computer= random.randint(1,4)
        print('Computer picked: ', computer)
    if player==1:
        print('Player 2 wins')
    else:
        print('Player 1 wins')

         

    while num2>3 or num2<1:
        print("Sorry, that's not a valid number")
        print()
        print('There are', num1, 'on the table')
        num2= int(input('How many sticks do you want to take (1,2 or 3)? '))
    if num2==1 or num2==2 or  num2==3:
        print()
        print('Turn: Player',player2)
        computer= random.randint(1,4)
        print('Computer picked: ', computer)
    if num2>num1:
        print('Sorry, that would bring the total # of sticks below 0. Try again.')
        print()
        continue
    num1-=num2
    print()
    if num1==0:
        print()
        print('There are no sticks left on the table! game over.')
        break

"""
