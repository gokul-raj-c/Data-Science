#A sentence is "red blue red green blue yellow". Count how many unique words are present using a set.

sentence="red blue red green blue yellow"
print(sentence)
a=list(sentence.split())
print(a)
s=set()
i=0
while i<len(a):
    s.add(a[i])
    i=i+1
print(s)
print(len(s))
