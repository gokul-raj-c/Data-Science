#Create a new list containing only even numbers from another list

a=[1,2,3,4,5,6,7,8]
b=[]
print(a)
for i in a:
    if i%2==0:
        b.append(i)
print(b)