# Income Tax Slab

s=int(input("enter salary: "))
if s <= 250000:
    tax=0
elif s > 250000 and s <= 500000:
    tax = (s - 250000) * 0.05
elif s > 500000 and s <= 1000000:
    tax = 12500 + (s - 500000) * 0.20
else:
    tax = 112500 + (s - 1000000) * 0.30
print("tax=",tax)