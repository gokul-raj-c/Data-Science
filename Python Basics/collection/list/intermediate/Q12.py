#Print the frequency of every element in the list [2,5,2,8,5,2], showing each element only once, like: 
# 2 appears 3 times 5 appears 2 times 8 appears 1 time


a=[2,5,2,8,5,2]
i=0
while i<len(a):
    j=0
    f=0
    while j<i:
        if a[i]==a[j]:
            f=1
        j=j+1
    if f==0:
        c=0
        j=0
        while j<len(a):
            if a[i]==a[j]:
                c=c+1
            j=j+1
        print(a[i],"appears",c,"times")
    i=i+1