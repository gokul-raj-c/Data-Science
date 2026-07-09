p1=input("enter first password:")
p2=input("enter second password:")
if len(p1) >= 5 and len(p2) >= 5:
    if p1==p2:
        print("password match")
    else:
        print("password not match")
else:
    print("invalid password")