#A dictionary stores product prices: {"pen": 10, "book": 50, "bag": 400, "scale": 20}. Print the cheapest and costliest item

prices={
    "pen":10, 
    "book":50, 
    "bag":400, 
    "scale":20
    }
a=list(prices.keys())
i=0
cheap=prices[a[0]]
cost=prices[a[0]]
while i<len(a):
    if prices[a[i]] > cost:
        cost=prices[a[i]]
    if prices[a[i]] < cheap:
        cheap=prices[a[i]]
    i=i+1
print(prices)
i=0
while i<len(a):
    if prices[a[i]]==cheap:
        print("cheapest item:",a[i])
    if prices[a[i]]==cost:
            print("costliest item:",a[i])
    i=i+1
