#Valid Date Check

d=int(input("enter day number: "))
m=int(input("enter month number: "))
y=int(input("enter year: "))
if m>=1 and m<=12:
    if m==2:
        if (y%400==0) or (y%4==0 and y%100!=0):
            days=29
        else:
            days=28
    elif m==4 or m==6 or m==9 or m==11:
        days=30
    else:
        days=31
    if d>=1 and d<=days:
        print("valid date")
    else:
        print("invalid date")
else:
    print("invalid date")