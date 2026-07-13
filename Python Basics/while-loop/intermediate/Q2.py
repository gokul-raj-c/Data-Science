# Ask the user for a password. Keep asking while the input is not equal to "open123". Once correct, print "Access granted".

p=input("enter password: ")
while p!="open123":
    p=input("enter password: ")
print("Access granted")