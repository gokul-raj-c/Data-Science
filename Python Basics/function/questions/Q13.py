# Write a function total_bill(*prices) that accepts any number of prices and returns their total. 
# Test it with total_bill(10, 50, 400) and total_bill(25, 25).

def total_bill(*prices):
    total=0
    for i in prices:
        total=total+i
    return total

res1=total_bill(10, 50, 400)
print("total_bill(10, 50, 400):",res1)
res2=total_bill(25, 25)
print("total_bill(25, 25):",res2)