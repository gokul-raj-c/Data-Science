#From the set {15, 40, 60, 75, 20}, create a new set containing only numbers greater than 30.

a={15,40,60,75,20}
b=set()
x=list(a)
i=0
while i<len(x):
    if x[i]>30:
        b.add(x[i])
    i=i+1
print(a)
print(b)