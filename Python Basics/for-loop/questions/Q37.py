#Count the number of words in a sentence without using split().

s=input("enter sentence: ")
print(s)
c=1
for i in s:
    if i==" ":
        c=c+1
print(c)