"""
Erin Seepersad	3/29/23	CSCI-UA 2 - 006
Assignment #6 Problem #2
"""
import analyzer

a1 = analyzer.is_even(5)
a2 = analyzer.is_even(6)
print (a1, a2) # False True

b1 = analyzer.is_odd(5)
b2 = analyzer.is_odd(6)
print (b1, b2) # True False

c1 = analyzer.is_prime(5)
c2 = analyzer.is_prime(17)
c3 = analyzer.is_prime(21)
print (c1,c2,c3) # True True False

d1 = analyzer.is_perfect(6)
d2 = analyzer.is_perfect(7)
d3 = analyzer.is_perfect(10)
print (d1,d2,d3) # True False False

e1 = analyzer.is_abundant(12)
e2 = analyzer.is_abundant(13)
e3 = analyzer.is_abundant(14)
print (e1,e2,e3) # True False False
