#From {15, 25, 35, 45, 55}, remove all numbers greater than 30 using a while loop. 
# Do not directly loop over the set while removing.

a={15,25,35,45,55}
print(a)
b=list(a)
i=0
while i<len(b):
    if b[i]>30:
        a.remove(b[i])
    i=i+1
print(a)