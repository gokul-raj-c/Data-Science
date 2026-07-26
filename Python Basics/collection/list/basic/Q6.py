#Print the list ["a","b","c","d","e"] in reverse order using a while loop that starts from the last index.

a=["a","b","c","d","e"]
i=len(a)-1
while i>=0:
    print(a[i],end=" ")
    i=i-1