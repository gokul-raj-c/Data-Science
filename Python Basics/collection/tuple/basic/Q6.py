# Build a list of squares from 1 to 5 using a while loop, convert it into a tuple, and print it.

a=[]
i=1
while i<=5:
    a.append(i**2)
    i=i+1
print(a)
print(tuple(a))