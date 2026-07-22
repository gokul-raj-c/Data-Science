a=[10,20,["hello",75],6]
a.append(75)
a.pop(2)
b=[7]
a.append(b)
a.pop(0)
c=a[0]+a[1]
print(a)
print(c)




# [20, 6, 75, [7]]
# 26