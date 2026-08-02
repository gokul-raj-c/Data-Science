#A dictionary stores prices: {"pen": 10, "book": 50, "bag": 400, "scale": 20} . 
# Ask the user for an amount of money and print the items they can afford.

store={
    "pen": 10, 
    "book": 50, 
    "bag": 400, 
    "scale": 20
    }
 
amt=int(input("enter amount that can afford: "))
for i in store:
    if store[i] <= amt:
        print(i)
