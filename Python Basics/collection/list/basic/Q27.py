#From the list [5, -2, 0, 9, -7, 0, 3], create three lists: positive numbers, negative numbers, and zeros.

a=[5,-2,0,9,-7,0,3]
pos=[]
neg=[]
zero=[]
i=0
while i<len(a):
    if a[i]>0:
        pos.append(a[i])
    elif a[i]<0:
        neg.append(a[i])
    else:
        zero.append(a[i])
    i=i+1
print(a)
print("positive numbers:",pos)
print("negative numbers:",neg)
print("zeros:",zero)