"""
Erin Seepersad	3/29/23	CSCI-UA 2 - 006
Assignment #6 Problem #1
"""
# these are the basic arithmetic functions you will be using for this challenge

# function:   add
# input:      two integers/floats
# processing: adds the two supplied values
# output:     returns the sum (integer/float)
def add(a,b):
    return a+b

# function:   sub
# input:      two integers/floats
# processing: subtracts the two supplied values
# output:     returns the difference (integer/float)
def sub(a,b):
    return a-b

# function:   mult
# input:      two integers/floats
# processing: multiplies the two supplied values
# output:     returns the product (integer/float)
def mult(a,b):
    return a*b

# function:   div
# input:      two integers/floats
# processing: divides the first value by the second value
# output:     returns the result (float)
def div(a,b):
    return a/b

# function:   sqrt
# input:      one integer/float
# processing: computes the square root of the supplied value
# output:     returns the square root (float)
def sqrt(a):
    return a**0.5

# function:   square
# input:      one integer/float
# processing: raises the supplied integer/float to the 2nd power
# output:     returns the square (integer/float)
def square(a):
    return a**2

#challenge 1: expression 1
#function: sub, multiply, add (here is intergers, but floats work)
#input
#processing: parentheses first then add both numbers
#output: returns the excuted answer
a=3 
b=4
c=1
d=2
y= add(sub(a,b),mult(c,d))

#challenge 1: expression 2
#function: add
#input
#processing: adds all inputs (here is intergers, but floats work)
#output: returns the sum
a=5
b=1
c=7
d=9
e=13
f=12
y=add(add(add(a,b),add(c,d)),add(e,f))

#challenge 1: expression 3
#function
#input
#processing
#output
a=5
b=1
c=7
d=2
e=3
y=div(add(a,b),add(add(c,d),add(0,3)))

#challenge 1: expression 4
#function
#input
#processing
#output
x1=0
y1=0
x2=100
y2=100
y=sqrt((add(square(sub(x2,x1)),square(sub(y2,y1)))))


