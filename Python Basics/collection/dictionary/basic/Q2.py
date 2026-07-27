# A dictionary stores item prices: {"pen": 10, "book": 50, "bag": 300}. Find the total bill using a while loop

prices={
    "pen":10,
    "book":50, 
    "bag":300
    }
a=list(prices.keys())
i=0
s=0
while i<len(a):
    s=s+prices[a[i]]
    i=i+1
print(prices)
print("total bill:",s)