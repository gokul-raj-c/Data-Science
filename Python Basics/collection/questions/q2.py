#In [4, 7, 2, 9, 6, 3] , count how many numbers are bigger than the number just before them. Print the count.

a=[4,7,2,9,6,3]
c=0
for i in range(1,len(a)):
    if a[i]<a[i-1]:
        c=c+1
print(c)