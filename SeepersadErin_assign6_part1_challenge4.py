"""
Erin Seepersad	3/29/23	CSCI-UA 2 - 006
Assignment #6 Problem #1
"""
#maximum and minimum
maximum=0
minimum=0 
a = 5
b = 10
c = 15
d = 20
def maximum(a,b):
    if a>b:
        return a
    else:
        return b
def minimum(c,d):
    if c<d:
        return c
    else:
        return d
ans1 = maximum(a,b)
ans2 = maximum(a,c)
ans3 = maximum(a,d)
print (ans1,ans2,ans3) # 10 15 20

ans4 = minimum(d,c)
ans5 = minimum(d,b)
ans6 = minimum(d,a)
print (ans4,ans5,ans6) # 15 10 5

ans7 = maximum( maximum(a,b), maximum(c,d) )
print ("The biggest is:", ans7)


# simpleshort version 1
simple_sort_version1=0
def simple_sort_version1(a, b):
    if a < b:
        return a, b
    else:
        return b, a
    
a,b = simple_sort_version1(10,20)
print (a,b) # 10 20

a,b = simple_sort_version1(20,10)
print (a,b) # 10 20

a,b = simple_sort_version1(30,30)
print (a,b) # 30 30

# next, write a new function called 'simple_sort_version2' that accepts three values.  you can assume
# that your three values will always be the same data type (all ints, all floats or all strings).
# sort these values in ascending order and return them. 
# you may use any function that you've written so far in this assignment if you'd like to (simple_sort_version1, maximum, minimum, etc)

# your function should work perfectly with the following lines of code
def simple_sort_version2(a,b,c):
    if a<=b and a<=c:
        if b<c:
            return a,b,c
        else:
            return a,c,b
    if b<=a and b<=c:
        if a<c:
            return b,a,c
        else:
            return b,c,a
    if c<=a and c<=b:
        if a<b:
            return c,a,b
        else:
            return c,b,a

a,b,c = simple_sort_version2(10,20,30)
print (a,b,c) # 10 20 30

a,b,c = simple_sort_version2(10,30,20)
print (a,b,c) # 10 20 30

a,b,c = simple_sort_version2(30,20,10)
print (a,b,c) # 10 20 30

a,b,c = simple_sort_version2(30,20,20)
print (a,b,c) # 20 20 30
