#This is the analysis.py code, it will be used for very in-depth analysis.

#OLD CODE (WORKS)
a = 1/2

#I'm adding this code after the initial commit of this file,
#Solving for b is very important for our analysis

#BUGFIX: Added fix to an error I was getting when I was trying
#to divide by zero, handled by a try/except for now. Will have
#to rethink my analysis in the future.
try:
    b = 1/0
except:
    print("You can't divide by zero!!!")
    b = 1/100


#OLD CODE (WORKS)
print(a)

#Added a new print statement to print b for analytics purposes
print(b)
