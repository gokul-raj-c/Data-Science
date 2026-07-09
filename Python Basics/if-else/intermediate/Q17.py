# Angle Type

a=int(input("enter angle in degree: "))
if a<90:
    print("acute")
elif a==90:
    print("right")
elif a>90 or a<180:
    print("obtuse")
elif a==180:
    print("straight")
else:
    print("invalid angle")