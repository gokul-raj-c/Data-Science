#Write a shopping cart program. Keep asking the user for an item name and its price, and store them in two lists. 
# Stop when the user types "done" as the item name. Finally, print all items with their prices and the total bill.

items=[]
price=[]
total_amt=0
item_name=""
while item_name!="done":
    item_name=input("enter item name: ")
    if item_name != "done":
        amt=int(input("enter price: "))
        items.append(item_name)
        price.append(amt)
        total_amt=total_amt+amt
i=0
while i<len(items):
    print(items[i],"->",price[i])
    i=i+1
print("total amount:",total_amt)