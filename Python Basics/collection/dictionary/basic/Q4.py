#Count the frequency of each character in the word "hello" and store the result in a dictionary.

c={}
s="hello"
i=0
while i<len(s):
    keys=list(c.keys())
    f=0
    j=0
    while j<len(keys):
        if s[i]==keys[j]:
            f=1
        j=j+1
    if f==1:
        c[s[i]]=c[s[i]]+1
    else:
        c[s[i]]=1
    i=i+1
print(c)


# while i<len(s):
#     if s[i] in c:
#         c[s[i]]=c[s[i]]+1
#     else:
#         c[s[i]]=1
#     i=i+1
# print(c)