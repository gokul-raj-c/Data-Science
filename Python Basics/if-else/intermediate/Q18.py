#Bill Discount

a=int(input("enter amount: "))
if a<1000:
    print("no discount")
    p=0
elif a>=1000 or a<=4999:
    p=a-(a*0.10)
else:
    p=a-(a*0.20)
print(p)