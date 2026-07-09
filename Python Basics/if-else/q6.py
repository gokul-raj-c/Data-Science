#Password Length Check

x=input("enter password: ")
if len(x) >= 8:
    print("Strong length")
else:
    print("Too short")