#Write a shopping cart program. Keep asking the user for an item name and its price, and store them in two lists. 
# Stop when the user types "done" as the item name. Finally, print all items with their prices and the total bill.

items=[]
price=[]
t_amt=0
item=""
while item!="done":
    item=input("enter item name: ")
    if item!="done":
        amt=int(input("enter price: "))
        items.append(item)
        price.append(amt)
        t_amt=t_amt+amt
i=0
while i<len(items):
    print(items[i],"->",price[i])
    i=i+1
print("total amount = ",t_amt)