#Take the list [1,2,3,4,5] and remove one item at a time using pop() inside a while loop until the list becomes empty. 
# Print the list after every removal.

a=[1,2,3,4,5]
print(a)
while len(a)>0:
    a.pop(0)
    print(a)