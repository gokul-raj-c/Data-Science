# Shipping Cost by Weight

w=float(input("enter weight in kg: "))
if w<=1:
    print(50)
elif w>1 or w<=5:
    print(100)
elif w>5 or w<=10:
    print(200)
else:
    print(500)