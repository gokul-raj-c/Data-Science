#Body Temperature Diagnosis

t=float(input("enter body temperature: "))
if t<95:
    print("Low (hypothermia)")
elif t>=95 and t<=99.5:
    print("Normal")
elif t>=99.6 and t<=100.9:
    print("Mild fever")
else:
    print("High fever")