a=int(input("enter number: "))
if a%5==0:
    if a%3==0:
        print("multiple of 5 and 3")
    elif a%7==0:
        print("multiple of 5 and 7")
    else:
        print("multiple of 5, but not multiple of 3 and 7")
elif a%2==0:
    if a%11==0:
        print("multiple of 2 and 11")
    elif a%3==0:
        print("multiple of 2 and 3")
    else:
        print("multiple of 2, but not multiple of 11 and 3")
else:
    print("not multiple of 5 and 2")