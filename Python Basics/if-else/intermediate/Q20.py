#Grade Point (GPA)

x=int(input("enter mark: "))
if x >= 90:
    print(10)
elif x >= 80 and x < 90:
    print(9)
elif x >= 70 and x < 80:
    print(8)
elif x >= 60 and x < 70:
    print(7)
elif x >= 50 and x < 60:
    print(6)
else:
    print("fail")