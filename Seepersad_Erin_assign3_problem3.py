"""
Erin Seepersad	2/16/23	CSCI-UA 2 - 006
Assignment #3 Problem #3

"""
print("        Conifer Identifier        ")
print()
print("-----------------------------------")

print()
tree= input("Is the foilage waxy(W) or has needles?(N) ")
if tree.upper()=='W':
        cone=input("Are the cones spherical(Y/N): ")
        if cone.upper() == "Y":
            print('This is a CYPRESS tree.')
        else:
            if cone.upper() == "N":
                print('This is a WESTERN RED CEDAR tree.')
elif tree.upper()=='N':
        needles=input("are the needles growing in clusters of 10+? " )
        if needles.upper()=="Y":
            next=(input("Is it an evergreen tree, are the cones dense or are the needles dark/green/prickly? "))
            if next.upper()== 'Y':
                print("This is a CEDAR (TRUE CEDAR) tree.")
            if next.upper()== 'N':
                print("This is a LARCH tree.")                                                             
        else:
             if needles.upper()=='N':
                isol=(input("Are the needles growing in isolation? "))
                if isol.upper()=="Y":
                    print("Too many possibilites! More information is needed to identify this tree.")
                else:
                    another=(input("Are the needles growing in groups of 3 and radiate around the stem like helicopter blades? "))
                    if another.upper()=="Y":
                        print("This is a JUNIPER tree.")
                    else: 
                        print("This is a PINE tree.")
else:
    print("Invalid answer. Please try again.")
