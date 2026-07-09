# Electricity Bill

a=int(input("enter units: "))
if a>=0 or a<=100:
    amt=a*5
elif a>100 or a<=200:
    amt=500+(a-100)*7
else:
    amt=1200+(a-200)*10
print(amt)