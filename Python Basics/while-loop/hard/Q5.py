#Ask the user for a positive integer and calculate its factorial using a while loop (e.g. 5 -> 5 x 4 x 3 x 2 x 1 = 120). 
# If the user enters a negative number, print "Invalid input"

n=int(input("enter number: "))
if n<0:
    print("invalid input")
else:
    f=1
    i=n
    while i>0:
        f=f*i
        i=i-1
    print("factorial of",n,"=",f)