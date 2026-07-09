#Within Budget

p=int(input("enter price: "))
a=int(input("enter amount: "))
if p<a:
    print("you can buy it")
elif p>a:
    print("too expensive")
else:
    print("same")