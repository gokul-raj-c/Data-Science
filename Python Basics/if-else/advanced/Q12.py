#Grade with Plus / Minus

x=int(input("enter mark: "))
if x >= 95:
    print("A+")
elif x >= 90 and x < 95:
    print("A")
elif x >= 85 and x < 90:
    print("B+")
elif x >= 80 and x < 85:
    print("B")
elif x >= 70 and x < 80:
    print("C")
elif x >= 60 and x < 70:
    print("D")
else:
    print("F")