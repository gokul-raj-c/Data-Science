#Split the list [10,20, 30,40,50, 60] into two halves and print both. If the list has an odd number of items, 
# put the extra item in the first half.

a=[10,20,30,40,50,60,70]
print(a)
first=[]
second=[]
mid=(len(a)+1)//2
i = 0
while i<mid:
    first.append(a[i])
    i=i+1
while i<len(a):
    second.append(a[i])
    i=i+1
print("first half:",first)
print("second half:",second)