# Calculate the power of a number without using the power operator (e.g., 2^5 = 32).

a=int(input("enter number: "))
p=int(input("enter power: "))
#print(a**p)
i=1
r=1
while i<=p:
    r=r*a
    i=i+1
print(r)