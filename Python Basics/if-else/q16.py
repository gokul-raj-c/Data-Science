# Point Quadrant

x=float(input("enter x coordinate: "))
y=float(input("enter y coordinate: "))
if x>0 and y>0:
    print("Quadrant 1")
elif x<0 and y>0:
    print("Quadrant 2")
elif x<0 and y<0:
    print("Quadrant 3")
else:
    print("Quadrant 4")