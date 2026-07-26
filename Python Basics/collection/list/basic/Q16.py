#Count how many times the number 7 appears in the list [7,3,7,9,7,1]usinga loop. (Do not use count().)

a=[7,3,7,9,7,1]
c=0
i=0
while i<len(a):
    if a[i]==7:
        c=c+1
    i=i+1
print(c)