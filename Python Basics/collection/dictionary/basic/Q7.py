#Ask the user to enter 3 item names and prices. Store them in a dictionary, then print the total bill.

store={}
i=0
total=0
while i<3:
    item=input("enter item name: ")
    price=int(input("enter price: "))
    total=total+price
    store[item]=price
    i=i+1
print(store)
print("total amount:",total)