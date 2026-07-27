#Merge {"pen": 5, "book": 2} and {"pen": 3, "bag": 4} into one stock dictionary. 
# If an item appears in both dictionaries, add the quantities

d1={
    "pen":5, 
    "book":2
    } 
d2={
    "pen":3, 
    "bag":4
    }
print(d1)
print(d2)

b=list(d2.keys())
i=0
while i<len(b):
    a=list(d1.keys())
    j=0
    f=0
    while j<len(a):
        if b[i]==a[j]:
            f=1
        j=j+1
    if f==1:
        d1[b[i]]=d1[b[i]]+d2[b[i]]
    else:
        d1[b[i]]=d2[b[i]]
    i=i+1
print(d1)
