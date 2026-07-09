#Number of Digits

a=int(input("enter positive number less than 1000: "))
if a<10:
    print("1 digit")
elif a<100:
    print("2 digit")
else:
    print("3 digit")