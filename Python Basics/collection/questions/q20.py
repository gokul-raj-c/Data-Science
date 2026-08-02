#A dictionary stores stock: {"pen": 12, "book": 4, "bag": 7} . Ask the user for an item name. 
# If the item exists, print its quantity and then increase it by 5 . 
# If it does not exist, add it to the dictionary with a quantity of 1 . Print the final dictionary.

stock={
    "pen": 12, 
    "book": 4, 
    "bag": 7
    }

print(stock)
item=input("enter item name: ")
f=0
for i in stock:
    if i==item:
        stock[i]=stock[i]+5
        f=1
if f==0:
    stock[item]=1
print(stock)