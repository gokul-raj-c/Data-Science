# Point Quadrant

x=float(input("enter x coordinate: "))
y=float(input("enter y coordinate: "))
if x>0 and y>0:
    print("Quadrant 1")
elif x<0 and y>0:
    print("Quadrant 2")
elif x<0 and y<0:
    print("Quadrant 3")
elif x>0 and y<0:
    print("Quadrant 4")
elif x==0 or y==0:
    print("On an axis")
elif x==0 and y==0:
    print("Origin")
