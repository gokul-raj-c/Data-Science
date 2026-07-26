#Create a list of the squares of the numbers 1 to 10 ([1,4,9,...]) using a while loop and append().

a=[]
i=1
while i<=10:
    a.append(i**2)
    i=i+1
print(a)