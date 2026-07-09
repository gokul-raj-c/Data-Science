#Ticket Price by Age

x=int(input("enter age: "))
if x<5:
    print("free")
elif x>=5 and x<=12:
    print(100)
elif x>=13 and x<=59:
    print(250)
else:
    print(150)