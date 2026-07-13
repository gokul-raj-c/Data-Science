# Keep asking the user to enter a number. Stop the loop only when they enter 0. Then print "You entered zero, goodbye!"

n=int(input("enter number: "))
while n!=0:
    n=int(input("enter number: "))
print("You entered zero, goodbye!")