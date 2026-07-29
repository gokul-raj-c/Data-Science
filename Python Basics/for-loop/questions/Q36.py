# Find the longest word in a sentence.

s=input("enter sentence: ")
w=s.split()
print(w)
long=w[0]
for i in w:
    if len(i) > len(long):
        long=i
print(long)