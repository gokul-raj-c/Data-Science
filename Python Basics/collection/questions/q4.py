#Print the list [10, 20, 30, 40, 50] in reverse order without using reverse() or slicing.

a=[10,20,30,40,50]
print(a)
for i in range(len(a)-1,-1,-1):
    print(a[i],end=" ")