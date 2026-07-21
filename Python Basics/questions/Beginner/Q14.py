#Ask the user for a password, giving them a maximum of 3 attempts. If the correct password ("python123") is entered, 
# print "Welcome"; after 3 wrong tries, print "Locked out".

a=input("enter password: ")
c=0
while a!="python123":
    c=c+1
    if c!=3:
        a=input("enter password: ")
    else:
        print("locked out")
if a=="python123":
            print("welcome")