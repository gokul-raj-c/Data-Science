a=(4,5,6,7,8)
print(a)
#a[0]=77    #TypeError: 'tuple' object does not support item assignment

#to change a value in tuple we need to convert it into list and change the value
b=list(a)
print(b)
b[0]=77
a=tuple(b)
print(a)