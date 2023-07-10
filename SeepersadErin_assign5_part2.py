"""
Erin Seepersad	3/25/23	CSCI-UA 2 - 006
Assignment #5 Problem #2

"""
month=0
average=0
totalexpenses=0
#enter a number of months
askmonth=int(input('How many months would you like to analyze? '))
while askmonth < 1 or askmonth> 12:
    print('invalid number of months, try again.')
    askmonth=int(input('How many months would you like to analyze? '))
askbudget=float(input('What is your budget for this time period? '))
while askbudget < 0:
    print('invalid budget, try again.')
    askbudget=float(input('What is your budget for this time period? '))
    
format(askbudget, '.2f')
print()
print('Here we go!')
print()

#analyze the data
#for month in range (0,askmonth):
while month<askmonth:
    month+=1
    print('**** Month #', month,'****')
    weekexpense1=float(input('Week #1 Expenses: '))
    while weekexpense1 < 0:
        print('invalid entry, try again.')
        weekexpense1=float(input('Week #1 Expenses: '))

    weekexpense2=float(input('Week #2 Expenses: '))
    while  weekexpense2 < 0:
        print('invalid entry, try again.')
        weekexpense2=float(input('Week #2 Expenses: '))
                    
    weekexpense3=float(input('Week #3 Expenses: '))
    while  weekexpense3 < 0:
        print('invalid entry, try again.')
        weekexpense3=float(input('Week #3 Expenses: '))
        
    weekexpense4=float(input('Week #4 Expenses: '))
    while  weekexpense4 < 0:
        print('invalid entry, try again.')
        weekexpense4=float(input('Week #4 Expenses: '))
        
    totalexpenses+= weekexpense1+ weekexpense2 +weekexpense3 +weekexpense4
    totalweek= (weekexpense1+weekexpense2+weekexpense3+weekexpense4)/4
    average+= totalweek
    totalaverageweek= average/askmonth
    print('Month #', month, 'average weekly expense:', format(totalweek, '.2f'))
    print()
print('average weekly expenses for all months:',format(totalaverageweek, '.2f') )
print('total expenses across', month, 'months:', format(totalexpenses, '.2f'))
print()
print('Great job! You stayed within budget!')
        
if totalexpenses>askbudget:
    differenceinbudget= totalexpenses-askbudget
    print('oh no! you went over budget by', format(differenceinbudget, '.2f'), end='!')
    

    
