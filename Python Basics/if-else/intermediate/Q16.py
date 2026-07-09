#Temperature Advice

t=int(input("enter temperature: "))
if t<0:
    print("freezing")
elif t>=0 or t<=15:
    print("cold")
elif t>=16 or t<=25:
    print("pleasant")
elif t>=26 or t<=35:
    print("warm")
else:
    print("very hot")