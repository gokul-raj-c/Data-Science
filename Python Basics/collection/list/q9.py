a=[10,20,["hello",75],6]
b=[]
b.append(a[2])  #append ['hello', 75]
a.extend(b)    # extend ['hello', 75] to a
print(a)


# [10, 20, ['hello', 75], 6, ['hello', 75]]

#append -> element
#extend -> add values to list