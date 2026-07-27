#Find the common vowels between the words "education" and "beautiful" using sets.

w1="education"
w2="beautiful"
s1=set()
s2=set()
common = set()
i=0
while i<len(w1):
    if w1[i]=="a" or w1[i]=="e" or w1[i]=="i" or w1[i]=="o" or w1[i]=="u":
        s1.add(w1[i]) 
    i=i+1
i=0
while i<len(w2):
    if w2[i]=="a" or w2[i]=="e" or w2[i]=="i" or w2[i]=="o" or w2[i]=="u":
        s2.add(w2[i]) 
    i=i+1
print(s1)
print(s2)
s1=list(s1)
s2=list(s2)
i=0
while i<len(s1):
    j=0
    while j<len(s2):
        if s1[i]==s2[j]:
            common.add(s1[i])
        j=j+1
    i=i+1
print(common)

# for x in s1:
#     if x in s2:
#         common.add(x)
# print(common)