# Count how many times each word appears in ["apple", "banana", "apple", "orange", "banana","apple"] using a dictionary.

words=["apple", "banana", "apple", "orange", "banana","apple"]
print(words)
count={}
i=0
while i<len(words):
    k=list(count.keys())
    f=0
    j=0
    while j<len(k):
        if words[i]==k[j]:
            f=1
        j=j+1
    if f==1:
        count[words[i]]=count[words[i]]+1
    else:
        count[words[i]]=1
    i=i+1
print(count)