#A list has repeated roll numbers: [1, 2, 2, 3, 4, 4, 5]. Use a while loop and a set to print only the unique roll numbers.

a=[1,2,2,3,4,4,5]
s=set()
i=0
while i<len(a):
    if a[i] in s:
        i=i+1
    else:
        s.add(a[i])
        i=i+1
print(a)
print(s)