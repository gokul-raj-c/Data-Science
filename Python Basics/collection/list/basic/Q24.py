# Reverse the list [10, 20, 30, 40, 50] into a new list using a while loop. Do not use slicing or reverse().

a=[10,20,30,40,50]
rev=[]
i=len(a)-1
while i>=0:
    rev.append(a[i])
    i=i-1
print(a)
print(rev)