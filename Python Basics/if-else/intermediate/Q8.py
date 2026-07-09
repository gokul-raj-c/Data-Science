#State of Water

t=int(input("enter temperature: "))
if t<0:
    print("ice")
elif t>=0 or t<=100:
    print("water")
else:
    print("steam")