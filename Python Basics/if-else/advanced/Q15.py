#Shipping Zone + Weight

z=input("enter zone 'local, national, international: ") 
w=int(input("enter weight in kg: "))
if z=="local":
    c=w*20
elif z=="national":
    c=w*50
elif z=="international":
    c=w*120
else:
    print("invalid input")
if w>20:
    c=c+100
print("cost:",c)