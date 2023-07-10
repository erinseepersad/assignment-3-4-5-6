"""
Erin Seepersad	3/29/23	CSCI-UA 2 - 006
Assignment #6 Problem #1
"""
#Challenge 2
#function: you have a and b that are numbers
#input: the numbers that the variables hold
#processing: you are comparing (boolean) and returning the larger one
#output: the maximum 
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
