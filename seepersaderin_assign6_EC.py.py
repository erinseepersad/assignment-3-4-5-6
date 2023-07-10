#what you start with
points=0

#introduction
print('Welcome to: ESCAPE ROOM 101!') 
print('There are five rooms with different themes. Do not worry about getting stuck in one, however, do worry about collecting enough points to save your family.')
print()
startgame= input('You might be wondering what do I mean save your family? Well, as soon as you started this game, your family was kidnapped and now is held captive, it is up to you to collect enough points to set them free! Can you defy the odds?(yes or no) ')
if startgame.lower() == 'no':
    print('not up for a challenge eh? well whatever, here is your family. have a great day!')
if startgame.lower()== 'yes':
    print()
    print('ahh so you have accepted the challenge... well let us begin!')
    print()
    print('listen closely:')
    print()
    print('as stated before, there are five rooms with different themes, but you will not get stuck in one. ')
    print('As you enter a themed room, you have 0 points. There are four objects to choose from that will reveal a key to move on to the next themed room. the trick here is that you only have 3 tries to get the key, if you fail, you will still move to the next room, but deducted 350 points. If you get more than 6000 points then your family will be set free, if not you lost :( and would have to try again.')
    print()
    understandinstructions= input('got it? ')
    if understandinstructions.lower()== 'no':
        print('listen closely:')
        print('as stated before, there are five rooms with different themes, but you will not get stuck in one. As you enter a themed room, you have 0 points. There are four objects to choose from that will reveal a key to move on to the next themed room. the trick here is that you only have 3 tries to get the key, if you fail, you will still move to the next room, but deducted 350 points. If you get more than 6000 points then your family will be set free, if not you lost :( and would have to try again.')
        understandinstructions= input('got it? ')
    if understandinstructions.lower()== 'yes':
        
    #room 1
        print()
        print('Welcome to room 1! This is a classroom theme. Good luck!')
        print()
        print('WARNING!! NEW RULE ALERT!')
        print('if you choose not to enter an object listed, you will not be asked to enter a valid one. it will count as one turn!')
        print()
        print('There are four objects and under one is a key. You have three chances to pick the correct one before points are deducted as you continue.')
        print()
        print('the objects are: ')
        def classroom():
            print('1. rug 2. bookstand 3. waterbottle 4. keyboard', sep='\n')#n is not working 
            attempts = 0
            while attempts < 3:
                room1guess = input('what do you think the key is under? ')
                attempts += 1
                if room1guess.lower() == 'bookstand':
                    print("wow! you're correct. time to go to room 2.")
                    room1total = points + 1100
                    print('your total points has updated to', room1total)
                    break # Exit the loop 
                else:
                    print('wrong. try again!')
            else:
                print('Sorry, you have used up all your chances!Lets head to Room 2')
                room1total= points-350
                print('your total points has updated to', room1total)
            return room1total
        points = classroom()
        #ROOM 2
        print()
        print('Welcome to room 2! This is a playground theme. remember all the rules and Good luck!')
        print()
        print('There are four objects and under one is a key. You have three chances to pick the correct one before points are deducted as you continue.')
        print()
        print('the objects are:')
        def playground():
            print('1.tireswing 2. slide 3. sandbox 4. seasaw', sep='\n')
            attempts = 0
            while attempts < 3:
                room2guess = input('what do you think the key is under? ')
                attempts += 1
                if room2guess.lower() == 'sandbox':
                    print("wow! you're correct. time to go to room 3.")
                    room2total = points + 1050
                    print('your total points has updated to', room2total)
                    break # Exit the loop 
                else:
                    print('wrong. try again!')
            else:
                print('Sorry, you have used up all your chances!Lets head to Room 3')
                room2total= points-350
                print('your total points has updated to', room2total)
            return room2total
        points = playground()+classroom()
        #room3
        print()
        print('Welcome to room 3! This is a museum theme. remember all the rules and Good luck!')
        print()
        print('There are four objects and under one is a key.You have three chances to pick the correct one before points are deducted as you continue.')
        print(' the objects are: ')
        def museum():
            print('1. painting 2. bench 3. sculpture 4. portrait', sep='\n')
            attempts = 0
            while attempts < 3:
                room3guess = input('what do you think the key is under? ')
                attempts += 1
                if room3guess.lower() == 'sandbox':
                    print("wow! you're correct. time to go to room 4.")
                    room3total = points + 1050
                    print('your total points has updated to', room3total)
                    break # Exit the loop 
                else:
                    print('wrong. try again!')
            else:
                print('Sorry, you have used up all your chances!Lets head to Room 4')
                room3total= points-350
                print('your total points has updated to', room3total)
            return room3total
        points = museum()+playground()+ classroom()
        #room 4
        print()
        print('Welcome to room 4! This is a cafe theme. Good luck!')
        print('There are four objects and under one is a key.You have three chances to pick the correct one before points are deducted as you continue.')
        print(' the objects are: ')
        def cafe():
            print('1. coffee cup 2. stool 3. pastry 4. laptop', sep='\n')
            attempts = 0
            while attempts < 3:
                room4guess = input('what do you think the key is under? ')
                attempts += 1
                if room4guess.lower() == 'laptop':
                    print("wow! you're correct. time to go to room 5.")
                    room4total = points + 1050
                    print('your total points has updated to', room4total)
                    break # Exit the loop 
                else:
                    print('wrong. try again!')
            else:
                print('Sorry, you have used up all your chances! Lets head to Room 5')
                room4total= points-350
                print('your total points has updated to', room4total)
            return room4total
        points = cafe()+playground()+ museum()+ classroom()
        
        #room 5 
        print('Welcome to room 5! This is a haunted house theme. Good luck!')
        print('There are four objects and under one is a key.You have three chances to pick the correct one before points are deducted as you continue.')
        print(' the objects are: ')
        def hauntedhouse():
            print('1. clown 2. blood 3. spiderwebs 4. doll', sep='\n')
            attempts = 0
            while attempts < 3:
                room5guess = input('what do you think the key is under? ')
                attempts += 1
                if room5guess.lower() == 'spiderwebs':
                    print("wow! you're correct.time to calculate the total to see if you get your family back...")
                    room5total = points + 1050
                    print('your total points has updated to', room5total)
                    break # Exit the loop 
                else:
                    print('wrong. try again!')
            else:
                print('Sorry, you have used up all your chances! The End')
                room5total= points-350
                print('your total points has updated to', room5total)
            return room5total
        points = hauntedhouse()+playground()+ museum()+ cafe()+ classroom()
        if points < 6000:
            print('I am sorry you lost but your family is stuck with us.')
            print()
            print('farewell! Thank you for joining.')
        else:
            print('Congratulations! here is your family back tehehe')
else:
    print('invalid phrase. try again with yes or no.')
    understandinstructions= input('got it? ')
"""

if startgame.lower() != 'yes' and startgame.lower() != 'no':
    print('invalid phrase. try again using yes or no.')
    print('ahh so you have accepted the challenge... well let us begin!')
    print('listen closely:')
    print('as stated before, there are five rooms with different themes, but you will not get stuck in one. As you enter a themed room, you have 0 points. There are four objects to choose from that will reveal a key to move on to the next themed room. the trick here is that you only have 3 tries to get the key, if you fail, you will still move to the next room, but deducted 350 points. If you get more than 6000 points then your family will be set free, if not you lost :( and would have to try again.')
    understandinstructions= input('got it? ')
  """


