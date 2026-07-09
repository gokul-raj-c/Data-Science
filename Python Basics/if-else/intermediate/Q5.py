#BMI Category

w=float(input("enter weight: "))
h=float(input("enter height: "))
bmi=w/(h*h)
if bmi < 18.5:
    print(" Underweight")
elif bmi >= 18.5 and bmi < 24.9:
    print(" Normal")
elif bmi >= 25 and bmi < 29.9:
    print("Overweight")
else:
    print("Obese")