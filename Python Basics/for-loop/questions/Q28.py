#Find the second largest element in a list

a=[15,16,2,3,8,20,22]
large=a[0]
for i in a:
    if i>large:
        large=i
second_large=a[0]
for i in a:
    if i>second_large and i!=large:
        second_large=i
print(a)
print(second_large)