a=[10,20,["hello",75],6]
b=[]
b.extend(a[2])
c=a[0]+b[1]
a.append(c)
print(a)



# [10, 20, ['hello', 75], 6, 85]