#Remove duplicate elements from a list without using set()

a=[2,3,4,5,3,2,8,9]
print(a)
b=[]
for i in a:
    if i not in b:
        b.append(i)
print(b)