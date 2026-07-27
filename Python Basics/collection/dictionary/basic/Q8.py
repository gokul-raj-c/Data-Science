#A dictionary stores prices: {"shirt": 500, "cap": 150, "shoes": 1200}. 
# Apply a 10% discount only to items costing more than 500 and print the updated dictionary

prices={
    "shirt":500, 
    "cap":150, 
    "shoes":1200
    }
items=list(prices.keys())
i=0
while i<len(items):
    if prices[items[i]]>500:
        prices[items[i]]=prices[items[i]]-(prices[items[i]]*0.1)
    i=i+1
print(prices)