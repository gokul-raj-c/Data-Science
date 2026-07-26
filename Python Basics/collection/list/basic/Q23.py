# Ask the user to enter 5 numbers one by one. Store them in a list, then print the largest and smallest number. 
# Do not use max() or min().

a=[]
i=0
while i<5:
    n=int(input("enter number: "))
    a.append(n)
    i=i+1
print(a)
large=a[0]
small=a[0]
i=0
while i<len(a):
    if a[i]>large:
        large=a[i]
    if a[i]<small:
        small=a[i]
    i=i+1
print("large:",large)
print("small:",small)