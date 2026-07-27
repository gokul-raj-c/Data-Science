# A dictionary stores stock: {"pen": 5, "pencil": 0, "eraser": 3, "book": 0}. 
# Create a new dictionary containing only items that are in stock.

stock={
    "pen":5,
    "pencil":0,
    "eraser":3,
    "book":0
}
items={}
a=list(stock.keys())
i=0
while i<len(a):
    if stock[a[i]]>0:
        items[a[i]]=stock[a[i]]
    i=i+1
print(stock)
print(items)