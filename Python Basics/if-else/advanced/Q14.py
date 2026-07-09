#Parking Fee

h=int(input("enter no of hours parked: "))
if h<=1:
    f=30
else:
    f=30+(h-1)*20
if f>150:
    f=150
print("parking fee=",f)