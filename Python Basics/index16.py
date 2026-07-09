a=input("enter number: ")
if len(a)==3:
    if a[0]==a[1]==a[2]:
        print("Valid")
    else:
        print("invalid")
else:
    print("invalid")